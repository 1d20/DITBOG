import urllib, urllib2, simplejson, threading, time, os, shutil, sys
from zipfile import ZipFile, ZIP_DEFLATED
from contextlib import closing

thread_count = 5
engineID = 'ditbog_engine'
# theme_name = 'Health'
# out_folder_path = '/Users/Detonavomek/Documents/Python_projects/Django/ditbog/support_scripts/'
# out_folder_name = 'out_folder'

def downloadFromUrl(url, out_folder, i):
	urllib.urlretrieve(url, out_folder+str(i)+'.png')

def downloadTheme(theme_name, out_folder):
	theme_name = theme_name.replace(' ','%20').replace('-','%20').lower()
	pages, i, res = range(1,10), 0, []
	for page in pages:
		url = ('https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q='+theme_name+'&start='+str(page*4))
		request = urllib2.Request(url, None, {'Referer': ''})
		response = urllib2.urlopen(request)
		results = simplejson.load(response)
		for result in results['responseData']['results']:
			res.append(result['url'])
			t = threading.Thread(target=downloadFromUrl, args=(result['url'], out_folder, i))
			while 1:
				if threading.active_count()>thread_count: time.sleep(1)
				else: break
			t.start()
			i+=1
	return res

def zipdir(basedir, archivename):
    assert os.path.isdir(basedir)
    with closing(ZipFile(archivename, "w", ZIP_DEFLATED)) as z:
    	for root, dirs, files in os.walk(basedir):
	        for fn in files:
				print fn
				absfn = os.path.join(root, fn)
				zfn = absfn[len(basedir)+len(os.sep)-1:]
				z.write(absfn, zfn)

out_folder_path = sys.argv[1]+'/'
theme_name = sys.argv[2]
engineID = sys.argv[3]
out_folder_name = theme_name.lower()

if not os.path.exists(out_folder_path+out_folder_name+engineID+'/'): os.makedirs(out_folder_path+out_folder_name+engineID+'/')

downloadTheme(theme_name, out_folder_path+out_folder_name+engineID+'/')
zipdir(out_folder_path+out_folder_name+engineID+'/', out_folder_path+theme_name.lower()+engineID+'.zip')
shutil.rmtree(out_folder_path+out_folder_name+engineID+'/')