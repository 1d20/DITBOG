import urllib, urllib2, simplejson, threading, time, os, shutil, sys
from zipfile import ZipFile, ZIP_DEFLATED
from contextlib import closing
	

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
    os.makedirs(out_folder_path+engineID+'/')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
zipdir(out_folder_path+engineID+'/', out_folder_path+theme_name.lower()+engineID+'.zip')
shutil.rmtree(out_folder_path+engineID)