# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:02:36 2021

@author: user
"""

from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request, urlretrieve
import urllib
from datetime import date
import pandas as pd

imgLink=[]
imgName=[]
imgStatus=[]

driver = webdriver.Chrome(executable_path=r'C:\Users\user\Documents\chromedriver.exe')
driver.get("https://knowyourmeme.com/memes/popular/page/2")
page = driver.page_source
data = bs(page, "html.parser")

table=data.find('table',class_='entry_list')
print(table)
for row in table.find_all('a', {'class': 'photo'}):
    link=row.find('img')
    imgLink.append(link['data-src'])
    imgName.append(link['alt'])
    
for i in range(len(imgLink)):
    imgNames = imgName[i] + '.jpg'
    try:
        urllib.request.urlretrieve(imgLink[i], 'C:/Users/user/Documents/'+imgNames)
        imgStatus.append('Found')
    except:
        print('Image Not Found')
        imgStatus.append('Image Not Found')
        

dataframe = pd.DataFrame({
  'Title': imgName,
  'Url': imgLink,
  'Timestamp': date.today().strftime("%d/%m/%Y"),
  'status': imgStatus
})
csv = dataframe.to_csv('C:/Users/user/Documents/meme.csv', index=True, header=True) 
