# startup-acquisition-insolvency-tracker
This repo firstly contains Python scripts for detecting if a UK startup has been acquired by a tech giant - or gone insolvent. When used together these scripts searche a pre-gathered list of names of UK startups on Companies House, monitors for any new filings and, when one is found, looks for evidence of a tech giant - either through outright finding a tech giant's name or instead finding their HQ address. These scripts would enable a newsroom to quickly detect a tech giant acquisition potentially before its announced.

It also includes a script that scrapes the Gazette insolvency register to check if any of the UK startups have gone out of business.

The scripts use the following Python modules:
- ```companies-house``` A wrapper for the Companies House API. It's used to search for listings of UK startups on Companies House and then regularly checking filing histories for any new document that may indicate an acquisition by a tech giant
- ```fuzzywuzzy``` A fuzzy matching module. Because names on Companies House do not perfectly match my pre-gathered list of UK startup name, this is used to gather a rough set of companies that may include the one of interest.
- ```pdf2image``` A converter from pdf to image files. Unfortunately the pdfs of filings on Companies House are actually just scanned images, which stops straightforward text extraction using modules like '''pdfminer'''. So instead this module is used to convert the pages of pdfs to images for later text extraction
- ```pytesseract``` An optical character recognition tool for Python. It's used to extract text from Company House filings which is then searched for evidence of tech giants  
- ```BeautifulSoup``` A web-scraping module. This is used to detect insolvencies on the Gazette - this web page is used instead of the Companies House API because insolvencies appear much later on the latter
