#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import time


# In[31]:


url = 'https://mars.nasa.gov/news/'
response = requests.get(url)


# In[32]:


headlines_soup = bs(response.text, 'lxml')


# In[33]:


headline = headlines_soup.find('div', class_ = 'content_title').text.strip()


# In[34]:


print(headline)


# In[35]:


news = headlines_soup.find('div', class_ = 'rollover_description_inner').text.strip()


# In[36]:


print(news)


# In[42]:



url = ('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[43]:


images = soup.find_all('a', class_="fancybox")
print(images)


# In[44]:


pic_src = []
for image in images:
    pic = image['data-fancybox-href']
    pic_src.append(pic)

featured_image_url = 'https://www.jpl.nasa.gov' + pic
featured_image_url


# In[45]:


url = ('https://twitter.com/marswxreport?lang=en')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[46]:


print(soup.prettify())


# In[49]:


contents = soup.find_all("div",class_="content")
print(contents)


# In[50]:


weather_mars = []
for content in contents:
    tweet = content.find("div", class_="js-tweet-text-container").text
    weather_mars.append(tweet)
#print(weather_mars)

mars_weather = weather_mars[8]
print(mars_weather)


# In[51]:


mars_facts_url = "https://space-facts.com/mars/"
table = pd.read_html(mars_facts_url)
table[0]


# In[53]:



facts_html = df.to_html()
facts_html = facts_html.replace("\n","")
facts_html


# In[54]:


hemisphere_image_urls = []


# In[56]:


url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[57]:



cerberus_img = soup.find_all('div', class_="wide-image-wrapper")
print(cerberus_img)


# In[58]:


for img in cerberus_img:
    pic = img.find('li')
    full_img = pic.find('a')['href']
    print(full_img)
cerberus_title = soup.find('h2', class_='title').text
print(cerberus_title)
cerberus_hem = {"Title": cerberus_title, "url": full_img}
print(cerberus_hem)


# In[ ]:




