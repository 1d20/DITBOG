from fabric.api import local


def help():
	print ("""
		Commands:
			'updatedb'  - create/update db and do all migrations
			'startdata'  - filling db start data
			'testengine' - add test engine to db and media folder
		""")

def updatedb():
	local('./manage.py syncdb')
	local('./manage.py migrate')

def startdata():
	local('./manage.py loaddata ../support_materials/fixtures/start_data.json')
	local('mkdir -p media/res')
	local('mkdir -p media/asset')
	local('mkdir -p media/apk')
	local('mkdir -p media/short_description')
	local('mkdir -p media/full_description')
	local('mkdir -p media/app_icon')
	local('mkdir -p media/large_promo')
	local('mkdir -p media/screens_folder')
	local('mkdir -p media/market')
	local('mkdir -p media/sertificate')
	local('mkdir -p media/source')
	local('mkdir -p media/info_appdf')
	local('mkdir -p media/script_screen')
	local('mkdir -p media/script_res')
	local('mkdir -p media/script_asset')
	local('mkdir -p media/script_ads')

def testengine():
	local('./manage.py loaddata ../support_materials/fixtures/test_engine.json')
	local('cp -r ../support_materials/media/test_engine/ media/')


