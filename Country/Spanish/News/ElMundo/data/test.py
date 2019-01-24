from Country.Spanish.News.ElMundo.data.NewsScraper import NewsScraper
from Requests.Requester import Requester
from datetime import datetime
from bs4 import BeautifulSoup
from Translation.GoogleTranslator import  GoogleTranslator
from Scraper.Writters.FileWritter import FileWriter

url = 'https://www.efe.com/efe/espana/'

html = NewsScraper.get_page_data(root_url='https://www.efe.com/efe/espana/', page=1)
requester = Requester(url=url, retries=5, sleep_time=3)
response = requester.make_get_request()



dataset = NewsScraper.parse_articles_list(url_root=requester.get_url_root(),html=html)
if dataset is not None:
    for url in list(dataset):


       """ dataset[url]['subtitle'] = subtitle
        dataset[url]["text"] = text
        dataset[url]["html"] = html"""


    writer = FileWriter("data/news.csv")
    writer.write(dataset)
