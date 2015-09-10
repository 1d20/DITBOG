from os import rename, remove
from urllib2 import Request, urlopen
import urllib
import urllib2
import json
from PIL import Image


def tuple2str(in_tuple, seperator):
    return str(seperator.join([item.encode("UTF-8") for item in in_tuple]))


def translate(text, trg):
    key = 'trnsl.1.1.20140221T230545Z.7af0b48859d16fe5.bd34ecc5117967b749e024cd9d8fb1f4d34a2967'
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?%s'
    list_of_params = {'key': key, 'text': text, 'lang': trg, 'format': 'plain'}
    request = urllib2.Request(url % urllib.urlencode(list_of_params),
                              headers={'User-Agent': 'Mozilla/5.0', 'Accept-Charset': 'utf-8'})
    response = urllib2.urlopen(request).read()

    data = json.loads(response)

    if data['code'] == 200:
        return data['text'][0]
    else:
        return text


def associate(word):
    key = 'c641aba304160d2b5ced42ce8e74519b'
    url = 'http://words.bighugelabs.com/api/2/' + key + '/' + word.replace(' ', '%20').replace('-', '%20') + '/json'
    request = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Accept-Charset': 'utf-8'})
   
    try:
        response = urllib2.urlopen(request).read()
    except:
        return [word]

    data = json.loads(response)

    if data.get('noun'):
        root = 'noun'
    elif data.get('adjective'):
        root = 'adjective'
    else:
        return [words]

    return [word] + data[root]['syn'][1:4]


def check_if_image(url):
    request = Request(url)
    request.get_method = lambda : 'HEAD'
    try:
        response = urlopen(request)
        maintype = response.info().maintype
    except:
        return False
    print 'check_if_image: maintype =', maintype, maintype == 'image'
    return maintype == 'image'


def __downloadImage(theme_name, out_file_path, start=0):
    theme_name = theme_name.replace(' ', '%20').replace('-', '%20').lower()
    url = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' + theme_name + '&start=' + str(start)
    request = urllib2.Request(url, None, {'Referer': ''})
    result = json.load(urllib2.urlopen(request))

    for res in result['responseData']['results']: 
        url = res['url']
        print '__downloadImage url:', url
        if check_if_image(url):
            print 'downloading...'
            urllib.urlretrieve(url, out_file_path)
            return
    __downloadImage(theme_name, out_file_path, start + 4)


def resizeImg(src, trg, size):
    try:
        img = Image.open(src)
        img = img.resize(size, Image.BILINEAR)#ANTIALIAS
        img.save(trg)
        if src != trg:
            remove(src)
    except:
        if src != trg:
            rename(src, str(src)+'.jpg')
            resizeImg(src, trg, size)


def downloadIcon(theme_name, out_file_path):
    width = height = 512
    __downloadImage(theme_name, out_file_path)
    resizeImg(out_file_path, out_file_path, (width, height))


def downloadPromo(theme_name, out_file_path):
    width = 1024
    height = 512
    __downloadImage(theme_name, out_file_path)
    resizeImg(out_file_path, out_file_path, (width, height))


