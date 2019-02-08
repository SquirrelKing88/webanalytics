from datetime import datetime

from LanguageProcessing.Translation.GoogleTranslator import GoogleTranslator
from Requests.Requester import Requester
from Country.Greece.News.ZouglaGr.NewsScraper import NewsScraper
from bs4 import BeautifulSoup
from Scraper.Writers.FileWriter import FileWriter


def process_articles_singlethread(source_dataset, target_dataset):
    for url in source_dataset:
        requester = Requester(url=url, retries=5, sleep_time=3)
        response = requester.make_get_request()
        html_text, text = NewsScraper.parse_article_text(html=response.get_data())
        article_datetime = NewsScraper.parse_article_datetime(html=response.get_data())

        target_dataset[url]['text'] = text
        target_dataset[url]['url'] = url
        target_dataset[url]['date'] = article_datetime
        target_dataset[url]['html'] = html_text

        translation_result = translator.get_translation(text)
        target_dataset[url]["translation_en"] = translation_result['translation']


url = "https://www.zougla.gr/ola"

translator = GoogleTranslator()

# step 1. Read all page with today's news
requester = Requester(url=url, retries=5, sleep_time=3)
response = requester.make_get_request()
html = response.get_data()
dataset = NewsScraper.parse_articles_list(html=html, url_root=url)

if 'https://www.zougla.gr/politiki/article/' in dataset:
    # Code to avoid attempt of scrapping missing page
    del dataset['https://www.zougla.gr/politiki/article/']

process_articles_singlethread(source_dataset=dataset.copy(), target_dataset=dataset)

writer = FileWriter("data/news.csv")
writer.write(dataset)
