#!/usr/local/bin/python3
# _*_ coding: utf8 _*_

import requests
from bs4 import BeautifulSoup

url = "https://jam620.wordpress.com/"
headers = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686; en-US;rv:1.9.2.3)"
                         "Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3"}
peticion = requests.request('get', url=url, headers=headers)
#print(peticion.text)

soup = BeautifulSoup(peticion.text, 'html.parser')
for v in soup.find_all('meta'):
    if v.get('name') == 'generator':
        version = v.get('content')
        print(version)

