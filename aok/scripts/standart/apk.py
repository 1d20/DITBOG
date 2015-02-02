#-*- coding:utf-8 -*-
import zipfile
import os.path
import shutil
from subprocess import call

from apps.theme.models import Theme
from apps.theme.models import Description
from utils import utils
from utils import template_folders

__sdkdir = "/usr/local/lib/AndroidSDK";

def generate_sources(theme_object, tmp_dir):
	ziptemplate = theme_object.engine.path_source

	#template
	with zipfile.ZipFile(ziptemplate, "r") as z:
		z.extractall(tmp_dir)
	#res
	with zipfile.ZipFile(theme_object.path_res_folder, "r") as z:
		z.extractall(tmp_dir + "/res")
	#asset
	with zipfile.ZipFile(theme_object.path_asset_folder, "r") as z:
		z.extractall(tmp_dir + "/asset")
	
	#--------------------------------------------------------------
	#template package name
	tpn = theme_object.engine.package_template_name
	#out package name
	opn = theme_object.package_name
	
	#local.properties
	lp = tmp_dir + '/local.properties'
	if os.path.isfile(lp):
		with open(lp, 'w') as f:
			f.write('sdk.dir=' + __sdkdir)

	#AndroidManifest.xml
	am = tmp_dir + '/AndroidManifest.xml'
	if os.path.isfile(am):
		with open(am, 'r+') as f:
			content = f.read().decode('utf-8')
			content = content.replace(tpn, opn).encode('utf-8')
			f.seek(0)
			f.write(content)

	#src package
	for root, dirs, files in os.walk(tmp_dir + '/src'):
		for file in files:
			if file.endswith(".java"):
				with open(os.path.join(root, file), 'r+') as f:
					content = f.read().decode('utf-8')
					content = content.replace(tpn, opn).encode('utf-8')
					f.seek(0)
					f.write(content)

	#src dir
	curdir = tmp_dir + '/src'
	tpna = tpn.split('.')
	opna = opn.split('.')
	for i in range(len(tpna)):
		if tpna[i] != opna[i]:
			os.rename(curdir + '/' + tpna[i], curdir + '/' + opna[i])
		curdir +=  '/' + opna[i]

	#res package
	for root, dirs, files in os.walk(tmp_dir + '/res'):
		for file in files:
			if file.endswith(".xml"):
				with open(os.path.join(root, file), 'r+') as f:
					content = f.read().decode('utf-8')
					content = content.replace(tpn, opn).encode('utf-8')
					f.seek(0)
					f.write(content)

	#application name
	#doto
	old = '<string name="app_name">aoktest</string>'
	descriptions = Description.objects.filter(theme=theme_object)
	for desc in descriptions:
		lang = desc.language.name_short
		strf = tmp_dir
		if lang == "en":
			strf += '/res/values/strings.xml'
			
			#icon
			utils.resizeImg(desc.path_app_icon, tmp_dir + '/res/drawable/ic_launcher.png', (72, 72))
		else:
			strf += '/res/values-' + lang + '/strings.xml'

		if os.path.isfile(strf):
			new = '<string name="app_name">' + desc.title + '</string>'
			with open(strf, 'r+') as f:
					content = f.read().decode('utf-8')
					content = content.replace(old, new).encode('utf-8')
					f.seek(0)
					f.write(content)

	return

def build_unsigned_apk(tmp_dir):
	sdir = os.path.dirname(os.path.abspath(__file__))

	os.chdir(tmp_dir)
	call(["ant", "release"])


	os.chdir(sdir)

def generate_apk(theme_object):
	#theme_object = Theme.objects.all()[0]
	
	tmp_dir = template_folders.PATH_TO_MEDIA_FOLDER + "/" + template_folders.UPLOAD_APK_FOLDER + "/inProgress/" + theme_object.engine.name + theme_object.title
	
	generate_sources(theme_object, tmp_dir)

	build_unsigned_apk(tmp_dir)

	apk_file = template_folders.PATH_TO_MEDIA_FOLDER + "/" + template_folders.UPLOAD_APK_FOLDER + '/' + theme_object.package_name + '.apk'
	for root, dirs, files in os.walk(tmp_dir + '/bin'):
		for file in files:
			print file
			if file.endswith(".apk"):
				os.rename(os.path.join(root, file), apk_file)
				
	theme_object.path_to_apk = apk_file
	theme_object.save()
	
	shutil.rmtree(template_folders.PATH_TO_MEDIA_FOLDER + "/" + template_folders.UPLOAD_APK_FOLDER + "/inProgress")

	return None