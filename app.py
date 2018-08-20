import urllib2
#import requests as req #windows py3
#import urllib.request #windows
from bs4 import BeautifulSoup

#1 getting web page:
web_page = 'https://finance.yahoo.com/quote/FB?p=FB'

#query the website and return the html to the variable page:
page = urllib2.urlopen(web_page)
#page = req.get(web_page)
#urllib.request.Request(web_page) #windows
print(page)

soup = BeautifulSoup(page, 'html.parser')
#soup = BeautifulSoup(page.text, 'html.parser')
# print(soup)


name_box = soup.find('h1', attrs={'class': 'D(ib)'})
print(name_box)
name = name_box.text
print(name)

price_box = soup.find('span', attrs={'class': 'Fw(b)'})
print(price_box)
price = price_box.text
print(price)

import csv
from datetime import datetime

with open('index.csv', 'a') as csv_file: 
      writer = csv.writer(csv_file) 
      writer.writerow([name, price, datetime.now()]) 


web_page = ['https://finance.yahoo.com/quote/FB?p=FB', 'https://finance.yahoo.com/quote/AAPL?p=AAPL']

#for loop
data = []
for page in web_page:
    co_pg = urllib2.urlopen(page)
    soup = BeautifulSoup(co_pg, 'html.parser')
    name_box = soup.find('h1', attrs={'class': 'D(ib)'})
    name = name_box.text.strip()
    print(name)
    price_box = soup.find('span', attrs={'class': 'Fw(b)'})
    price = price_box.text
    print(price)
    data.append(((name, price)))

with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for name, price in data:
      writer.writerow([name, price, datetime.now()])



     