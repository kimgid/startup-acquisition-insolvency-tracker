#!/home/kimgid/.virtualenvs/myproject/bin/python
from companies_house.api import CompaniesHouseAPI
ch = CompaniesHouseAPI('HwcI7GpyQ7KzwZjE9lf0cqXIlDU1M6dy0CyzgCvQ')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fuzzywuzzy import fuzz
import time

allcompanies2010 = pd.read_csv('data2010.csv').to_dict(orient='records')

company_names1 = []
for i in allcompanies2010:
    company_names1.append(i['0'])

companydata = []
for i in company_names1:
    d = {}
    time.sleep(0.55)
    d['search'] = i
    d['companiesinsearch'] = ch.search_companies(q = i)
    d['numbercompanies'] = len(d['companiesinsearch']['items'])
    companydata.append(d)
    print(d)

companydata2 = []
for i in companydata:
    for j in i['companiesinsearch']['items']:
        score = fuzz.token_sort_ratio(j['title'],i['search'])
        m = {}
        m['search'] = i['search']
        m['officialname'] = j['title']
        m['chnumber'] = j['company_number']
        if score >= 55:
            print(j['title'])
            print(i['search'])
            print(m)
            companydata2.append(m)

df = pd.DataFrame(companydata2)
df.to_csv(r'companydata3.csv', index = False)


