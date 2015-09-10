#-*- coding:utf-8 -*-
import zipfile
import os.path
import shutil
from subprocess import call

from apps.theme.models import Description
import apps.image_processor as image
from apps.utils.config.template_folders import *


__sdkdir = "/usr/local/lib/android-sdk-linux";

def replace_in_file(root, file, old, new):
	fout = os.path.join(root, file)
	with open(fout,'r') as f:
		newlines = f.readlines()
	with open(fout, 'w') as f:
		for line in newlines:
			f.write(line.replace(old, new))

def generate_sources(theme_object, tmp_dir):
	ziptemplate = theme_object.engine.path_source

	print 'tmp_dir', tmp_dir

	#template
	with zipfile.ZipFile(ziptemplate, "r") as z:
		z.extractall(tmp_dir)

	#res
	for item in theme_object.themedownloaditems_set.all():
		shutil.copyfile(item.path.path, tmp_dir + "/res/drawable/"+ str(item.engine_item.template_name))

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
	replace_in_file(tmp_dir, 'AndroidManifest.xml', tpn, opn)

	#src package
	for root, dirs, files in os.walk(tmp_dir + '/src'):
		for file in files:
			if file.endswith(".java"):
				replace_in_file(root, file, tpn, opn)


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
				replace_in_file(root, file, tpn, opn)

	#application name
	#doto
	old = '<string name="app_name">aoktest</string>'

	for desc in Description.objects.filter(theme=theme_object):
		lang = desc.language.name_short
		if lang == "en":
			strf = 'res/values/strings.xml'	
			image.resize(desc.path_app_icon, tmp_dir + '/res/drawable/ic_launcher.png', (72, 72))
		else:
			strf = 'res/values-' + lang + '/strings.xml'

		if os.path.isfile(strf):
			new = '<string name="app_name">' + desc.title + '</string>'
			replace_in_file(tmp_dir, strf, old, new)
	return


def build_unsigned_apk(tmp_dir):
	sdir = os.path.dirname(os.path.abspath(__file__))

	os.chdir(tmp_dir)
	call(["ant", "debug"])


	os.chdir(sdir)

def generate_apk(theme_object):
	#theme_object = Theme.objects.all()[0]
	
	tmp_dir = os.path.join(APK_FOLDER, theme_object.engine.name + theme_object.title)
	
	generate_sources(theme_object, tmp_dir)

	build_unsigned_apk(tmp_dir)

	apk_file = APK_FOLDER + '/' + theme_object.package_name + '.apk'
	for root, dirs, files in os.walk(tmp_dir + '/bin'):
		for file in files:
			print file
			if file.endswith(".apk"):
				os.rename(os.path.join(root, file), apk_file)
				break
				
	theme_object.path_to_apk = apk_file
	theme_object.save()
	
	shutil.rmtree(tmp_dir)

	return theme_object.package_name + '.apk'
