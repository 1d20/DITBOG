from PIL import Image
import json
from StringIO import StringIO
from urllib2 import Request, urlopen
import requests


def query(q, size, path):
	for url in find_images(q):
		if check_if_image(url):
			return save_image(url, size, path)
			break


def check_if_image(url):
    request = Request(url)
    request.get_method = lambda : 'HEAD'
    try:
        response = urlopen(request)
        maintype = response.info().maintype
    except:
        return False
    return maintype == 'image'


def find_images(q):
    q = q.replace(' ', '%20').replace('-', '%20').lower()
    start = 0
    while start < 10:
	    url = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' + q + '&start=' + str(start)
	    request = Request(url, None, {'Referer': ''})
	    result = json.load(urlopen(request))

	    for res in result['responseData']['results']: 
	        yield res['url']

		start + 4
        

def save_image(url, size, path):
    r = requests.get(url)
    im = Image.open(StringIO(r.content))
    im.resize(size, Image.ANTIALIAS)
    return im #im.save(path)