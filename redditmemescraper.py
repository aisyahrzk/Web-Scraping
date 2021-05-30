# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 12:59:01 2021

@author: user
"""

import praw
from urllib.request import urlopen, Request, urlretrieve
import urllib
from datetime import date
import pandas as pd

reddit = praw.Reddit(client_id = '', client_secret = '', user_agent = '')


imgLink=[]
imgName=[]
imgStatus=[]
#image_timestamps=[]

#limit=how many image from post we want
subreddit =reddit.subreddit('meme')
posts = subreddit.hot(limit=30)

for post in posts:
    imgLink.append(post.url)
    imgName.append(post.title)



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
csv = dataframe.to_csv('C:/Users/user/Documents/memereddit.csv', index=True, header=True) 








































