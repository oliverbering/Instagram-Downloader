import requests
import re

def get_response(url):
    r = requests.get(url)
    while r.status_code != 200:
        r = requests.get(url)
    return r.text

def prepare_urls(matches):
    return list({match.replace ("\\u0026", "&") for match in matches})

url = input('Enter Instagram URL: ')
response = get_response(url)

pic_matches re.findall('"display_url":"([^"]+)"', response)

pic_urls = prepare_urls(pic_matches)

if pic_urls:
    print('Detected Pictures: \n{0}'.format('\n'.join(pic_urls)))

if not (pic_urls):
    print ('Could not find recognize the media in the provided URL.')