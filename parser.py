import requests
import lxml
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


ua = UserAgent()
headers = {'user-agent': ua.random}


news = []


def get_news(req):
    req = requests.get(req, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    newses = soup.find('ul', class_="nav nav-pills nav-stacked remember_history")

    for link in newses:
        link = link.find('a').get('href')
        site = 'https://fanat1k.ru/'
        news.append(site + link)
    
    return news[0]


def get_last_3_news(req):
    req = requests.get(req, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    newses = soup.find('ul', class_="nav nav-pills nav-stacked remember_history")

    for link in newses:
        link = link.find('a').get('href')
        site = 'https://fanat1k.ru/'
        news.append(site + link)
    
    return news[:3]

