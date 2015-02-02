import urllib, urllib2, simplejson, threading, time, os, shutil, sys
from zipfile import ZipFile, ZIP_DEFLATED
from contextlib import closing
import Image

thread_count = 10

def downloadFromUrl(url, out_folder):
	response = urllib2.urlopen(url)
	if 'image/svg+xml' not in response.info().getheader('Content-Type'):
		urllib.urlretrieve(url, out_folder + "/img.png")

def downloadTheme(theme_name, out_folder):
	theme_name = theme_name.replace(' ','%20').replace('-','%20').lower()
	res = []

	url = ('https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q='+theme_name+'&start='+str(1))
	request = urllib2.Request(url, None, {'Referer': ''})
	response = urllib2.urlopen(request)
	results = simplejson.load(response)
	for result in results['responseData']['results']:
		res.append(result['url'])
		t = threading.Thread(target=downloadFromUrl, args=(result['url'], out_folder))
		while 1:
			if threading.active_count()>thread_count: 
				time.sleep(1)
			else: 
				break
		t.start()

	while t.is_alive():
		time.sleep(1)

	try:
		im=Image.open(out_folder + "/img.png")
		return res
	except IOError:
		# filename not an image file
		os.remove(out_folder + "/img.png")
		downloadTheme(theme_name, out_folder)
	

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

try:
    os.makedirs(out_folder_path+engineID+'/drawable/')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

downloadTheme(theme_name, out_folder_path+engineID+'/drawable')
zipdir(out_folder_path+engineID+'/', out_folder_path+theme_name.lower()+engineID+'.zip')
shutil.rmtree(out_folder_path+engineID)