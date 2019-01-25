from datetime import datetime

from Requests.Requester import Requester
from Country.Czech.News.CeskeNoviny.NewsScraper import NewsScraper
from bs4 import BeautifulSoup
from Translation.GoogleTranslator import  GoogleTranslator
from Scraper.Writters.FileWritter import FileWriter

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
for url in list(dataset):

    # make new request to upload article data
    requester = Requester(url=url, retries=5)
    response = requester.make_get_request()
    html = response.data

    # load html into soup
    soup = BeautifulSoup(html, 'html.parser')

    subtitle = NewsScraper.parse_article_subtitle(html=html, soup=soup)

    hours, minutes = NewsScraper.parse_article_datetime(html=html, soup=soup)

    html, text = NewsScraper.parse_article_text(html=html, soup=soup)

    # TODO scrape year month and day
    date = datetime(year=2019, month=1, day=25)
    if hours:
        date = date.replace(hour=hours)
    if minutes:
        date = date.replace(minute=minutes)

    dataset[url]['date'] = date
    dataset[url]['subtitle'] = subtitle
    dataset[url]["text"] = text
    dataset[url]["html"] = html

    translation_result = translator.get_translation(text)
    dataset[url]["translation_en"] = translation_result['translation']



# step 4. Save dataset to folder
writer = FileWriter("data/news.csv")
writer.write(dataset)
