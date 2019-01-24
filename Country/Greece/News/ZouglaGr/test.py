from datetime import datetime

from Requests.Requester import Requester
from Country.Greece.News.ZouglaGr.NewsScraper import NewsScraper
from bs4 import BeautifulSoup
from Translation.GoogleTranslator import  GoogleTranslator
from Scraper.Writters.FileWritter import FileWriter


url = "https://www.zougla.gr/ola"

# step 1. Read all page with today's news
requester = Requester(url=url, retries=5, sleep_time=3)
response = requester.make_get_request()
html = response.data
dataset = NewsScraper.parse_articles_list(html=html, url_root=url)

for link in dataset:

    requester = Requester(url=link, retries=5, sleep_time=3)
    response = requester.make_get_request()
    text = NewsScraper.parse_article_text(response.data)
    url = link

    article_datetime = NewsScraper.parse_article_datetime(html=html)

    dataset[url]['text'] = text
    dataset[url]['url'] = url
    dataset[url]['date'] = article_datetime

writer = FileWriter("data/news.csv")
writer.write(dataset)