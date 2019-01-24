from datetime import datetime

from Requests.Requester import Requester
from Country.Greece.News.ZouglaGr.NewsScraper import NewsScraper
from bs4 import BeautifulSoup
from Translation.GoogleTranslator import GoogleTranslator
from Scraper.Writters.FileWritter import FileWriter


url = "https://www.zougla.gr/ola"

translator = GoogleTranslator()

# step 1. Read all page with today's news
requester = Requester(url=url, retries=5, sleep_time=3)
response = requester.make_get_request()
html = response.data
dataset = NewsScraper.parse_articles_list(html=html, url_root=url)

for link in dataset:

    requester = Requester(url=link, retries=5, sleep_time=3)
    response = requester.make_get_request()
    text = NewsScraper.parse_article_text(html=response.data)[1]
    url = link

    article_datetime = NewsScraper.parse_article_datetime(html=response.data)

    dataset[url]['text'] = text
    dataset[url]['url'] = url
    dataset[url]['date'] = article_datetime

    #translation_result = translator.get_translation(text)
    #dataset[url]["translation_en"] = translation_result['translation']
                                                                  #translator claims that it can't translate greek(?)

writer = FileWriter("data/news.csv")
writer.write(dataset)