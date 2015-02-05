#-*- coding:utf-8 -*-
from django.db import models

from apps.utils.config import template_folders as tf
from apps.utils.config.download_item_types import ITEM_TYPES, FOLDER_TYPES
from apps.utils.apk import downloader
from django.core.files import File


class Market(models.Model):
    title = models.CharField(max_length=255)
    path_script = models.FileField(upload_to=tf.UPLOAD_MARKET_FOLDER)

    def __unicode__(self):
        return u'%s' % (self.title)


class Engine(models.Model):
    name = models.CharField(max_length=255)
    package_template_name = models.CharField(max_length=255)
    path_sertificate = models.FileField(upload_to=tf.UPLOAD_SERTIFICATE_FOLDER)
    pass_sertificate = models.CharField(max_length=255)
    path_source = models.FileField(upload_to=tf.UPLOAD_SOURCE_FOLDER)
    path_info_appdf = models.FileField(upload_to=tf.UPLOAD_APPDF_FOLDER)
    path_script_screen = models.FileField(upload_to=tf.UPLOAD_SCREENS_SCRIPT_FOLDER)

    def __unicode__(self):
        return u'%s' % (self.name)


class EngineDownloadItems(models.Model):
    engine = models.ForeignKey(Engine)
    item_type = models.IntegerField(choices=ITEM_TYPES, default=1)
    folder_type = models.IntegerField(choices=FOLDER_TYPES, default=1)
    count = models.IntegerField(default=1)
    required_count = models.BooleanField(default=True) # Is required max count
    value = models.CharField(max_length=255, default='')
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    template_name = models.CharField(max_length=255, default='{0}')

    def generate(self, theme):
        for generated_file_name, generated_file_tmp_path in downloader.query(theme, self):
            t_item = ThemeDownloadItems(theme=theme, engine_item = self)
            if generated_file_tmp_path:
                t_item.path.save(generated_file_name, File(open(generated_file_tmp_path)))

    def __unicode__(self):
        return '%s: %s(%s)' % (self.engine.name, self.get_item_type_display(), str(self.count))


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
    ad_code = models.CharField(max_length=255, default='')
    path_to_apk = models.FileField(upload_to=tf.UPLOAD_APK_FOLDER, default=None)
    date_add = models.DateTimeField(verbose_name=u'Date', auto_now_add=True)

    def generate_res(self):
        for e_item in self.engine.enginedownloaditems_set.all():
            e_item.generate(self)

    def __unicode__(self):
        return u'%s( %s )' % (self.title, self.engine)


class ThemeDownloadItems(models.Model):
    theme = models.ForeignKey(Theme)
    engine_item = models.ForeignKey(EngineDownloadItems)
    path = models.FileField(upload_to=tf.UPLOAD_THEME_ITEMS_FOLDER)

    def __unicode__(self):
        return '%s: %s $s' % (self.engine.name, str(self.type), str(self.count))


class Description(models.Model):
    language = models.ForeignKey('theme.language', related_name='description_language')
    theme = models.ForeignKey('theme.theme', related_name='description_theme')
    title = models.CharField(max_length=255)
    keywords = models.TextField(default=None)
    short_description = models.TextField(default='')
    full_description = models.TextField(default='')
    features = models.TextField(default='-</feature><feature>-</feature><feature>-')
    path_app_icon = models.FileField(upload_to=tf.UPLOAD_APP_ICON_FOLDER, default=None)
    path_large_promo = models.FileField(upload_to=tf.UPLOAD_LARGE_PROMO_FOLDER, default=None)
    path_screens_folder = models.FileField(upload_to=tf.UPLOAD_SCREENS_FOLDER, default=None)

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
    gen_script = models.FileField(upload_to=tf.UPLOAD_ADS_SCRIPT_FOLDER)

    def __unicode__(self):
        return self.title

class ThemeAd(models.Model):
    theme = models.ForeignKey('theme.theme', related_name='themead_theme')
    ad = models.ForeignKey('theme.ads', related_name='themead_ad')
    value = models.CharField(max_length=255)

    def __unicode__(self):
        return self.value+' - '+str(self.theme)+str(self.ad)
