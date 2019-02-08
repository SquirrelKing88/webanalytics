from datetime import datetime

from Requests.Requester import Requester
from Country.Italy.News.ANSA.NewsScraper import NewsScraper
from bs4 import BeautifulSoup

from Scraper.Writers.FileWriter import FileWriter



# today news https://www.pravda.com.ua/news/
url = "http://www.ansa.it/sito/notizie/topnews/index.shtml"

# step 1. Read all page with taday's news
requester = Requester(url=url, retries=5, sleep_time=3)
response = requester.make_get_request()
html = response.data

# step 2. Create half empty dataset with parsed urls of articles
dataset = NewsScraper.parse_articles_list(url_root=requester.get_url_root(),html=html)

# step 3. Loop over all urls and scrape article data
for url in  list(dataset):

    # make new request to upload article data
    requester = Requester(url=url, retries=5)
    response = requester.make_get_request()
    html = response.data

    # load html into soup
    soup = BeautifulSoup(html, 'html.parser')

    subtitle = NewsScraper.parse_article_subtitle(html=html, soup=soup)

    hours, minutes, seconds = NewsScraper.parse_article_time(html=html, soup=soup)

    html, text = NewsScraper.parse_article_text(html=html, soup=soup)


    date = datetime(year=2019, month=1, day=23)


    dataset[url]['date']=date
    dataset[url]['subtitle']=subtitle
    dataset[url]['text'] = text
    dataset[url]['html'] = html






# step 4. Save dataset to folder
writer = FileWriter("data/news.csv")
writer.write(dataset)



