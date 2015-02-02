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

def testengine():
	local('./manage.py loaddata ../support_materials/fixtures/test_engine.json')
	local('cp -r ../support_materials/media/test_engine/ media/')


