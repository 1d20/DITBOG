from urllib import quote_plus, urlretrieve
from urllib2 import Request, urlopen
import json
from PIL import Image

def __search_img(query, count = 1):
    query = quote_plus(query)
    url = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' + query
    request = Request(url, None, {'Referer': ''})
    result = json.load(urlopen(request))

    img_urls = [x['url'] for x in result['responseData']['results'][:count]]

    return img_urls


def __download_img(img_url, out_file_path):    
    urlretrieve(img_url, out_file_path)

def img_query(q, count, size, out_dir, file_name_mask):
    urls = __search_img(q, count)

    if len(urls) < count:
        urls += __search_img('placeholder', count - len(urls))

    answer = []

    for i, url in enumerate(urls):
        answer.append(file_name_mask.format(i))
        img_path = out_dir + file_name_mask.format(i)
        __download_img(url, img_path)
        Image.open(img_path).resize(size), Image.ANTIALIAS).save(img_path)

    return answer