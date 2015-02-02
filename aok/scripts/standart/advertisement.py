__author__ = 'Detonavomek'
#-*- coding:utf-8 -*-
import subprocess, os
from apps.theme.models import Ads, ThemeAd

def generate_advertisement(theme_object, package_name, parent_path, path_info_appdf):
    themeTitle = theme_object.title
    theme_name = themeTitle
    ads = Ads.objects.all()
    for ad in ads:
        full_path_to_script = parent_path+'/'+str(ad.gen_script)
        command = 'python '+full_path_to_script+' \''+theme_name+'\''
        result = subprocess.check_output(command, shell=True)
        result = result[:-1]
        theme_ad = ThemeAd()
        theme_ad.theme = theme_object
        theme_ad.ad = ad
        theme_ad.value = result
        theme_ad.save()
    return True