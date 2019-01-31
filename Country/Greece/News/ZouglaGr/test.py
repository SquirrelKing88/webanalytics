from datetime import datetime

import queue
import threading
from Requests.Requester import Requester
from Country.Greece.News.ZouglaGr.NewsScraper import NewsScraper
from bs4 import BeautifulSoup
from Translation.GoogleTranslator import GoogleTranslator
from Scraper.Writters.FileWritter import FileWriter


def parse_one_article(source_queue, dataset):
    while not source_queue.empty():
        url = source_queue.get()
        requester = Requester(url=url, retries=5, sleep_time=3)
        response = requester.make_get_request()
        html_text, text = NewsScraper.parse_article_text(html=response.data)
        title = NewsScraper.parse_article_title(html=response.data)
        article_datetime = NewsScraper.parse_article_datetime(html=response.data)

        dataset[url] = {
                    "url": url,
                    "date": article_datetime,
                    "title": title,
                    "subtitle": None,
                    "html": html_text,
                    "text": text,
                    "translation_en": None
                }

        #translation_result = translator.get_translation(text)
        #dataset[url]["translation_en"] = translation_result['translation']
                                   #translator still doesn't work


url = "https://www.zougla.gr/ola"

translator = GoogleTranslator()

# step 1. Read all page with today's news
requester = Requester(url=url, retries=5, sleep_time=3)
response = requester.make_get_request()
html = response.data
articles_generator = NewsScraper.parse_articles_list(html=html, url_root=url)

urls_queue = queue.Queue(maxsize=0)
[urls_queue.put(one_url) for one_url in articles_generator]

number_of_threads_wanted = 8
dataset = dict()

thread_list = []
for num in range(0, number_of_threads_wanted):
    thread_list.append(threading.Thread(target=parse_one_article,
                                        name='scraper_thread{0}'.format(num),
                                        args=(urls_queue, dataset)))
    thread_list[-1].start()

for t in thread_list:
    t.join()

writer = FileWriter("data/news.csv")
writer.write(dataset)
