#!/home/kimgid/.virtualenvs/myproject/bin/python
from companies_house.api import CompaniesHouseAPI
ch = CompaniesHouseAPI('HwcI7GpyQ7KzwZjE9lf0cqXIlDU1M6dy0CyzgCvQ')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fuzzywuzzy import fuzz
import time
import datetime
import requests
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import json
import os
import re


"""url = "https://beta.companieshouse.gov.uk//company/05396788/filing-history/MzI2MDEzNTAwMmFkaXF6a2N4/document?format=pdf"

r = requests.get(url)
with open('test1.pdf', 'wb') as fp:
    fp.write(r.content)"""

# Load today's links
with open('todays_links.json', 'r') as fp:
    data = json.load(fp)

matches = []

# Create test tech giants to check

tech_giants = [
    {'name': 'Apple',
    'address': 'One Apple Park Way, Cupertino, California, United States, 95014'},
    {'name': 'Facebook',
    'address': 'Menlo Park, California, United States'},
    {'name': 'Google',
    'name': 'Mountain View, California, United States'}
    ]

for t in tech_giants:
    t['words'] = [a.strip() for a in t['address'].split(',')]

for d in data[:1]:
    # Make temporary directory for saving company's pdf and converted images
    file_dir = re.sub(' ', '_', d['company_name'])
    try:
        os.mkdir(file_dir)
    except:
        pass


    # Get pdf and save
    pdf = requests.get(d['pdf'])
    with open(file_dir + '/' + file_dir + '.pdf', 'wb') as fp:
        fp.write(pdf.content)

    # Covert pdf pages images and save to directory
    images = convert_from_path(file_dir + '/' + file_dir + '.pdf')
    for i,image in enumerate(images):
        image.save(file_dir + '/' + file_dir + '.jpg', 'JPEG')

    # For each image, extract text and check for any of the tech giant's names or addresses

    d['extracted_text'] = []
    for i, image in enumerate([file for file in os.listdir(file_dir) if file.split('.')[-1] == 'jpg']):
        d['extracted_text'].append(pytesseract.image_to_string(Image.open(file_dir + '/' + image)))
    d['joined_text'] = " ".join(d['extracted_text'])
    d['words'] = d['joined_text'].split(" ")

    for word in d['words']
        for t in tech_giants:
            # First check names of tech giants
            if t['name'].lower() == word.lower():
                print('Match! The following tech giant has been detected in the document:', t['name'])
            for t_word in t['words']:
                if t_word.lower() == word:
                    print('Match! The following tech giant has been detected in the document:', t['name'])
