import urllib, urllib2, simplejson, Image

def downloadIcon(theme_name, out_file_path, width, height):
	# out_file_path = '/path/to/file/icon_theme_engine.png'
	theme_name = theme_name.replace(' ','%20').replace('-','%20').lower()
	url = ('https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q='+theme_name)
	request = urllib2.Request(url, None, {'Referer': ''})
	result = simplejson.load(urllib2.urlopen(request))
	url = result['responseData']['results'][0]['url']
	urllib.urlretrieve(url, out_file_path)
	Image.open(out_file_path).resize((int(width),int(height)), Image.ANTIALIAS).save(out_file_path)

# downloadIcon(theme_name, out_folder_path+out_folder_name+theme_name.lower()+engineID+'.png')