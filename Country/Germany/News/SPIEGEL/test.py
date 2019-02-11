from Requests.Requester import Requester
from Country.Germany.News.SPIEGEL.NewsScraper import NewsScraper
from bs4 import BeautifulSoup
from LanguageProcessing.Translation.GoogleTranslator import GoogleTranslator
from Scraper.Writers.ElasticSearchWritter import ElasticSearchWriter
from Scraper.Writers.FileWriter import FileWriter

translator = GoogleTranslator()

url = "http://www.spiegel.de/"

requester = Requester(url=url, retries=5, sleep_time=3)
response = requester.make_get_request()
html = response.get_data()

dataset = NewsScraper.parse_articles_list(url_root=url,html=html)

for url in list(dataset):
    print('parsing', url)
    requester = Requester(url=url, retries=5)
    response = requester.make_get_request()
    html = response.get_data()

    soup = BeautifulSoup(html, 'html.parser')

    subtitle = NewsScraper.parse_article_subtitle(html=html, soup=soup)

    date = NewsScraper.parse_article_datetime(html=html, soup=soup)

    html, text = NewsScraper.parse_article_text(html=html, soup=soup)

    dataset[url]['date']=date
    dataset[url]['subtitle']=subtitle
    dataset[url]["text"] = text
    dataset[url]["html"] = html

    translation_result = translator.get_translation(dataset[url]["text"])
    dataset[url]["translation_en"] = translation_result['translation']
    print(dataset[url])

es = ElasticSearchWriter(index_name='test_germany')
writers = [FileWriter("data/news.csv"), es]

for writer in writers:
    writer.write(dataset)