from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import json
import requests
from urllib.request import urlopen
from datetime import datetime
from datetime import timedelta
import numpy as np

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from time import sleep


from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request, urlretrieve
import urllib
from datetime import date
import pandas as pd

imgName=[]
productTitle=[]
imgStatus=[]
imgLink = []
link=[]
imgID = []

driver = webdriver.Chrome(executable_path=r'C:\Users\user\Documents\chromedriver.exe')

mok = ['A','B']
for x in range(2):
    
    driver.get("https://shopee.com.my/shop/41985388/search?page="+str(x)+"&sortBy=pop")

    for i in range(10):
        driver.execute_script("window.scrollBy(0, 350)")
        sleep(1)
    page = driver.page_source
    delay = 5 #secods
    data = bs(page, "html.parser")


    

    while True:
        try:
            
            WebDriverWait(driver, delay)
            print ("Page is ready")
            sleep(5)
            html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
            
            soup = BeautifulSoup(html, "html.parser")
            
            
            #name
            for item_n in soup.find_all('div', class_='_10Wbs- _5SSWfi UjjMrh'):
                mek = item_n.get_text()
                imgName.append(mek)
                print(mek)
            #link
            for item in soup.find_all('div', class_='shop-search-result-view__item col-xs-2-4'):
                ok = item.find('a')
                link.append('shopee.com.my' +ok['href'])
            
            #image source
            for me in soup.find_all('div', class_='_25_r8I ggJllv'):
                mok = me.find('img')
                sleep(5)
                imgLink.append(mok['src'])
                print(mok['src'])
            

  

            break # it will break from the loop once the specific element will be present. 
        except TimeoutException:
            print ("Loading took too much time!-Try again")

#download images
for i in range(len(imgLink)):
                
    imgIDs = str(i)
    imgID.append(str(i))
                
                
            
    try:
        urllib.request.urlretrieve(imgLink[i], 'C:/Users/user/Documents/shopee/'+imgIDs)
        imgStatus.append('Found')
                    
    except:
        print('Image Not Found')
        imgStatus.append('Image Not Found')
       

dataframe = pd.DataFrame({
    'ID':imgID,
  'Title': imgName
,'link':link,
'imgStatus':imgStatus})

csv = dataframe.to_csv('C:/Users/user/Documents/shopee.csv', index=True, header=True) 
