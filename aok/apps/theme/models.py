#-*- coding:utf-8 -*-
from django.db import models
from utils import template_folders


class Market(models.Model):
    title = models.CharField(max_length=255)
    path_script = models.FileField(upload_to=template_folders.UPLOAD_MARKET_FOLDER)

    def __unicode__(self):
        return u'%s' % (self.title)


class Engine(models.Model):
    name = models.CharField(max_length=255)
    package_template_name = models.CharField(max_length=255)
    path_sertificate = models.FileField(upload_to=template_folders.UPLOAD_SERTIFICATE_FOLDER)
    pass_sertificate = models.CharField(max_length=255)
    path_source = models.FileField(upload_to=template_folders.UPLOAD_SOURCE_FOLDER)
    path_info_appdf = models.FileField(upload_to=template_folders.UPLOAD_APPDF_FOLDER)
    path_script_screen = models.FileField(upload_to=template_folders.UPLOAD_SCREENS_SCRIPT_FOLDER)
    path_script_res = models.FileField(upload_to=template_folders.UPLOAD_RES_SCRIPT_FOLDER)
    path_script_asset = models.FileField(upload_to=template_folders.UPLOAD_ASSET_SCRIPT_FOLDER)

    def __unicode__(self):
        return u'%s' % (self.name)


class Language(models.Model):
    name_long = models.CharField(max_length=255)
    name_short = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % (self.name_long)


class TemplateDescription(models.Model):
    language = models.ForeignKey('theme.language', related_name='templatedescription_language')
    engine = models.ForeignKey('theme.engine', related_name='templatedescription_engine')
    template_description = models.TextField()

    def __unicode__(self):
        return u'%s %s' % (self.language, self.engine)


class Theme(models.Model):
    engine = models.ForeignKey('theme.engine', related_name='theme_engine')
    version = models.CharField(max_length=10, default='1.0')
    title = models.CharField(max_length=25)
    package_name = models.CharField(max_length=255)
    path_res_folder = models.FileField(upload_to=template_folders.UPLOAD_RES_FOLDER, default=None)
    path_asset_folder = models.FileField(upload_to=template_folders.UPLOAD_ASSET_FOLDER, default=None)
    ad_code = models.CharField(max_length=255, default='')
    path_to_apk = models.FileField(upload_to=template_folders.UPLOAD_APK_FOLDER, default=None)
    date_add = models.DateTimeField(verbose_name=u'Date', auto_now_add=True)

    def __unicode__(self):
        return u'%s( %s )' % (self.title, self.engine)


class Description(models.Model):
    language = models.ForeignKey('theme.language', related_name='description_language')
    theme = models.ForeignKey('theme.theme', related_name='description_theme')
    title = models.CharField(max_length=255)
    keywords = models.TextField(default=None)
    path_short_description = models.FileField(upload_to=template_folders.UPLOAD_SHORT_DESC_FOLDER)
    path_full_description = models.FileField(upload_to=template_folders.UPLOAD_FULL_DESC_FOLDER)
    feathures = models.TextField(default='-</feathure><feathure>-</feathure><feathure>-')
    path_app_icon = models.FileField(upload_to=template_folders.UPLOAD_APP_ICON_FOLDER, default=None)
    path_large_promo = models.FileField(upload_to=template_folders.UPLOAD_LARGE_PROMO_FOLDER, default=None)
    path_screens_folder = models.FileField(upload_to=template_folders.UPLOAD_SCREENS_FOLDER, default=None)

    def __unicode__(self):
        return u'%s : %s' % (self.title, self.theme)


class ThemeMarket(models.Model):
    theme = models.ForeignKey('theme.theme', related_name='thememarket_theme')
    market = models.ForeignKey('theme.market', related_name='thememarket_market')
    info = models.CharField(max_length=255)
    date_add = models.DateTimeField(verbose_name=u'Date', auto_now_add=True)

    def __unicode__(self):
        return u'%s %s' % (self.theme, self.market)


class Ads(models.Model):
    title = models.CharField(max_length=255)
    gen_script = models.FileField(upload_to=template_folders.UPLOAD_ADS_SCRIPT_FOLDER)

    def __unicode__(self):
        return self.title

class ThemeAd(models.Model):
    theme = models.ForeignKey('theme.theme', related_name='themead_theme')
    ad = models.ForeignKey('theme.ads', related_name='themead_ad')
    value = models.CharField(max_length=255)

    def __unicode__(self):
        return self.value+' - '+str(self.theme)+str(self.ad)