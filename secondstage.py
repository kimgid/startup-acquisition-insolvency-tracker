#!/home/kimgid/.virtualenvs/myproject/bin/python
from companies_house.api import CompaniesHouseAPI
ch = CompaniesHouseAPI('HwcI7GpyQ7KzwZjE9lf0cqXIlDU1M6dy0CyzgCvQ')
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
from fuzzywuzzy import fuzz
import time
import datetime

# Read the pre-gathered list of UK startup names

allcompanies2010 = pd.read_csv('companydata3.csv').to_dict(orient='records')


# Call API for filing history

todayslinks = []
df2010 = []
for j, i in enumerate(allcompanies2010):
    f = {}
    f['chnumber'] = i['chnumber']
    f['company_name'] = i['officialname']
    f['search'] = i['search']
    print('checking:')
    print(f['company_name'])
    try:
        f['filhis'] = ch.list_company_filing_history(company_number=f['chnumber'],items_per_page='10')['items']
        for d in f['filhis']:
            b = {}
            b['search'] = f['search']
            b['company_name'] = f['company_name']
            b['date'] = d['date']
            if b['date'] == datetime.datetime.today().strftime('%Y-%m-%d'):
                try:
                    b['pdf'] = 'https://beta.companieshouse.gov.uk/' + d['links']['self'] + '/document?format=pdf'
                    print(b)
                    todayslinks.append(b)
                except:
                    pass
    except:
        pass

    if j % 50 == 0 and len(todayslinks) > 0:
        with open('todays_links.json', 'w') as fp:
            json.dump(todayslinks, fp)

    df2010.append(f)


