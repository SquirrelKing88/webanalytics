from datetime import datetime

from Requests.Requester import Requester
from Country.Czech.News.CeskeNoviny.NewsScraper import NewsScraper
from bs4 import BeautifulSoup
from Translation.GoogleTranslator import  GoogleTranslator
from Scraper.Writters.FileWritter import FileWriter
from threading import Thread

translator = GoogleTranslator()

# today news https://www.pravda.com.ua/news/
url = "https://www.ceskenoviny.cz/prehled-zprav/"


# step 1. Read all page with tоday's news
requester = Requester(url=url, retries=5, sleep_time=3)
response = requester.make_get_request()
html = response.data


# step 2. Create half empty dataset with parsed urls of articles
dataset = NewsScraper.parse_articles_list(url_root=requester.get_url_root(), html=html)


# step 3. Loop over all urls and scrape article data
def scrape_url(url):
    print('thread {} started scrapping'.format(i))

    # make new request to upload article data
    requester = Requester(url=url, retries=5)
    response = requester.make_get_request()
    html = response.data

    # load html into soup
    soup = BeautifulSoup(html, 'html.parser')

    subtitle = NewsScraper.parse_article_subtitle(html=html, soup=soup)

    date = NewsScraper.parse_article_datetime(html=html, soup=soup)

    html, text = NewsScraper.parse_article_text(html=html, soup=soup)


    dataset[url]['date'] = date
    dataset[url]['subtitle'] = subtitle
    dataset[url]["text"] = text
    dataset[url]["html"] = html

    translation_result = translator.get_translation(text)
    dataset[url]["translation_en"] = translation_result['translation']
    print('thread {} finished scrapping'.format(i))


for i in range(len(list(dataset))):
    url = list(dataset)[i]
    th = Thread(target=scrape_url, args=(url, ))
    th.start()

th.join()

# step 4. Save dataset to folder
writer = FileWriter("data/news.csv")
writer.write(dataset)
