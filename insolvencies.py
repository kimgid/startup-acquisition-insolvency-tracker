#!/home/kimgid/.virtualenvs/myproject/bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
import requests
from bs4 import BeautifulSoup

def GetSoupHdr(url):
    print('Loading url...')
    hdr = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers = hdr).text
    return BeautifulSoup(page, 'lxml')

t = range(1,10)
g = []
for i in t:
    h = str(i)
    g.append(h)
    
insolvencies = []
base = 'https://www.thegazette.co.uk'
for t in g:

    url = 'https://www.thegazette.co.uk/insolvency/notice?results-page-size=10&numberOfLocationSearches=1&location-distance-1=1&categorycode=G405010102+-2&service=insolvency&results-page=' + t
    soup = GetSoupHdr(url)
    companies = soup.find('div',{'class':'main-pane'}).findAll('div',{'class','feed-item'})
    for i in companies:
        d = {}
        d['date'] = i.find('dd').text.strip()
        d['company'] = i.find('h3',{'class':'title'}).text.strip()
        d['link'] = base + i.find('h3',{'class':'title'}).find('a').get('href')
        soup1 = GetSoupHdr(d['link'])
        d['chnumber'] = soup1.find('div',{'class':'notice-summary'}).find('a').text.strip().replace('Notice timeline for company number ','')
        insolvencies.append(d)
        print(d)

