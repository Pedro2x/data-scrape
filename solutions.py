# #import libraries/modules
import urllib2
#import requests as req #windows for py3
#import urllib.request #windows
from bs4 import BeautifulSoup #from keyword used to import specific attributes or functions

# #1 getting the data

# #get the URL
web_page = 'https://finance.yahoo.com/quote/FB?p=FB'

# #query the website and return the html to the variable page:
page = urllib2.urlopen(web_page)
#page = req.get(web_page)
#urllib.request.Request(web_page) #windows
print(page)

# #parse the html page using Beautiful Soup and store in variable soup:
soup = BeautifulSoup(page, 'html.parser')

# #remove div element and get its innerHTML content
name_box = soup.find('h1', attrs={'class': 'D(ib)'})
print(name_box)
name = name_box.text
print(name)

price_box = soup.find('span', attrs={'class': 'Fw(b)'})
price = price_box.text
print(price)

# #2 Exporting the data
import csv
from datetime import datetime

#open csv file with append, so that old data will not be erased
#open () function - in python you need to give access to a file by opening it
#with statement provides a way to close that file (ensuring that a clean-up is always used)

#mode:
# 'r' read mode, file is only being read
# 'w' write mode, used to edit and write new information to the file (any existing files with the same name will be erased when this mode is used)
# 'a' append mode, used to add new data to the end of the file
# 'r+' special read and write mode, used to handle both actions 

with open('index.csv', 'w') as csv_file: #as is an alias, i.e. variable 
    writer = csv.writer(csv_file) #csv.writer() function from csv module
    writer.writerow([name, price, datetime.now()]) #csv.writerow() function from csv module

#3 Scrapping mutiple stock prices
#import libraries
# import urllib2
# from bs4 import BeautifulSoup
# import csv
# from datetime import datetime

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
    data.append(((name, price))

with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for name, price in data:
      writer.writerow([name, price, datetime.now()])

