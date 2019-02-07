from Requests.Requester import Requester
from Country.Ukraine.News.PravdaUa.NewsScraper import NewsScraper
from bs4 import BeautifulSoup
from LanguageProcessing.Translation.GoogleTranslator import GoogleTranslator
from Scraper.Writers.ElasticSearchWritter import ElasticSearchWriter
from Scraper.Writers.FileWriter import FileWriter

translator = GoogleTranslator()

# today news https://www.pravda.com.ua/news/
url = "https://www.pravda.com.ua/news/"

# step 1. Read all page with taday's news
requester = Requester(url=url, retries=5, sleep_time=3)
response = requester.make_get_request()
html = response.get_data()

# step 2. Create half empty dataset with parsed urls of articles
dataset = NewsScraper.parse_articles_list(url_root=requester.get_url_root(),html=html)

# step 3. Loop over all urls and scrape article data
for url in list(dataset):

    print("parse", url)
    try:

        # make new request to upload article data
        requester = Requester(url=url, retries=5)
        response = requester.make_get_request()
        html = response.get_data()

        # load html into soup
        soup = BeautifulSoup(html, 'html.parser')

        subtitle = NewsScraper.parse_article_subtitle(html=html, soup=soup)

        date = NewsScraper.parse_article_datetime(html=html, soup=soup, year=2019, month=1, day=22, hours=11, minutes=11)

        dataset[url]["html"], dataset[url]["text"] = NewsScraper.parse_article_text(html=html, soup=soup)

        dataset[url]['date'] = date
        dataset[url]['subtitle'] = subtitle


    except Exception:
        pass
    # translation_result = translator.get_translation(dataset[url]["text"])
    # dataset[url]["translation_en"] = translation_result['translation']


# step 4. Save dataset to folder

writers = [FileWriter("data/news.csv"), ElasticSearchWriter(index_name='test_ukraine')]

for writer in writers:
    writer.write(dataset)




