import zipfile
from shutil import copyfile
from datamaster import *
from apps.theme.models import Description
from apps.utils.config.template_folders import APPDF_FOLDER
from apps.utils.apk import apk

def descr(theme):
	theme_desc = None
	for desc in Description.objects.filter(theme=theme):
		if desc.language.name_short == "en":
			theme_desc = desc


	d = DataMaster()
	d.package = theme.package_name
	d.categorization.type = "game"
	d.categorization.category = "educational"

	d.description.texts.title = theme.title
	d.description.texts.keywords = theme_desc.keywords
	d.description.texts.short_description = theme_desc.short_description
	d.description.texts.full_description = theme_desc.full_description
	
	copyfile(str(theme_desc.path_app_icon.file), "icon.png")
	copyfile(str(theme_desc.path_large_promo.file), "promo.png")
	
	d.description.images.icon = "icon.png"
	d.description.images.promo = "promo.png"

	if not theme.path_to_apk.file:
		apk.generate_apk(theme)
	copyfile(str(theme.path_to_apk.file), "app.apk")
	
	d.apk_files.apk_file = "app.apk"

	with open("description.xml", 'w') as des:
		des.write(d.ToXML())

	return "description.xml"

def build(theme):
	appdf = zipfile.ZipFile(APPDF_FOLDER + "/appdf.zip", "w" )
	appdf.write(descr(theme), "description.xml")

	appdf.write("icon.png", "icon.png")
	appdf.write("promo.png", "promo.png")
	appdf.write("app.apk", "app.apk")



	return "appdf.zip"