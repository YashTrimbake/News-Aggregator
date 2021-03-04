from django.shortcuts import render

# Create your views here.
import requests
from bs4 import BeautifulSoup

# Getting news from Times of India

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[2:17] # removing footer links

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)

# Getting news from NDTV

ndtv_r = requests.get("https://www.ndtv.com/india?pfrom=home-ndtv_mainnavgation")
ndtv_soup = BeautifulSoup(ndtv_r.content, 'html5lib')

ndtv_headings = ndtv_soup.find_all('h2')

ndtv_headings = ndtv_headings[0:15]
ndtv_news = []
for ndtvh in ndtv_headings:
    ndtv_news.append(ndtvh.text)

# Getting news from BBC

bbc_r = requests.get("https://www.bbc.com/news/world/asia/india")
bbc_soup = BeautifulSoup(bbc_r.content, 'html5lib')

bbc_headings = bbc_soup.find_all('h3')

bbc_headings = bbc_headings[2:17] # removing footer links

bbc_news = []
for th in bbc_headings:
    bbc_news.append(th.text)

# Getting news from NEWS18

news18_r = requests.get("https://www.news18.com/india/")
news18_soup = BeautifulSoup(news18_r.content, 'html5lib')

news18_headings = news18_soup.find_all('h4')

news18_headings = news18_headings[0:15] # removing footer links

news18_news = []
for th in news18_headings:
    news18_news.append(th.text)

def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news, 'ndtv_news':ndtv_news, 'bbc_news':bbc_news, 'news18_news':news18_news})
