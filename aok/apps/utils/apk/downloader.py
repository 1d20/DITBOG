from __future__ import division #3/2=1.5 insted of 1
from math import ceil #UP round, f.e. ceil(2.3) = 3 insted of round(2.3)=2

from urllib import quote_plus, urlretrieve, ContentTooShortError
from urllib2 import Request, urlopen
from PIL import Image
from django.core.files import File
import tempfile 
import json

from apps.utils.config import template_folders as tf
from apps.utils.config.download_item_types import ITEM_TYPES


def check_if_image(url):
    request = Request(url)
    request.get_method = lambda : 'HEAD'
    response = urlopen(request)
    return 'image' in response.info().gettype()

def search_img(query, count = 1):
    query = quote_plus(query)
    url = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' + query
    request = Request(url, None, {'Referer': ''})
    result = json.load(urlopen(request))
    result = [x['url'] for x in result['responseData']['results']]

    img_urls = []
    for url in result:
        if check_if_image(url):
            img_urls.append(url)  
        if len(img_urls) == count:
            break       

    img_urls = (img_urls * int(ceil(count / len(img_urls))))[:count]
    #todo
    #use plaseholder
        

    return img_urls


def download_img(img_url, size):    
    tmpfile = tempfile.NamedTemporaryFile(suffix='.png', delete=False)

    try:
        urlretrieve(img_url, tmpfile.name) ##
    except ContentTooShortError:
        #todo
        #use plaseholder
        print "error"
        return None
        pass

    Image.open(tmpfile.name).resize(size, Image.ANTIALIAS).save(tmpfile.name)
    
    return tmpfile.name

def img_query(q, count, size, mask):
    urls = search_img(q, count)

    if len(urls) < count:
        urls += search_img('placeholder', count - len(urls))

    answer = [(mask.format(i), download_img(url, size)) for i, url in enumerate(urls)]
               
    return answer


def query(theme, e_item):
    if e_item.item_type == 1: #Image
        return img_query(theme.title, e_item.count, (e_item.width, e_item.height), e_item.template_name)
    else:
        print ":O"



#download to buffer
# from PIL import Image
# import urllib2 as urllib
# fd = urllib.urlopen("http://a/b/c")

# import io
# image_file = io.BytesIO(fd.read())
# im = Image.open(image_file)

# from StringIO import StringIO
# im = Image.open(StringIO(fd.read()))




#open image to resize
#from cStringIO import StringIO
#file_jpgdata = StringIO(jpgdata)
#dt = Image.open(file_jpgdata)

#save to memory
#output = StringIO.StringIO()
#base.save(output, format='PNG')
#return [output.getvalue()]

#save to db
# >>> from django.core.files.uploadedfile import InMemoryUploadedFile
# >>> from cStringIO import StringIO
# >>> buf = StringIO(data)  # `data` is your stream of bytes
# >>> buf.seek(0, 2)  # Seek to the end of the stream, so we can get its length with `buf.tell()`
# >>> file = InMemoryUploadedFile(buf, "image", "some_filename.png", None, buf.tell(), None)
# >>> photo.image.save(file.name, file)  # `photo` is an instance of `MyModel`
# >>> photo.image
# <ImageFieldFile: ...>