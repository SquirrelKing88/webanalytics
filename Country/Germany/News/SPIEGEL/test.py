from Requests.Requester import Requester
from Country.Germany.News.SPIEGEL.NewsScraper import NewsScraper
from bs4 import BeautifulSoup
from LanguageProcessing.Translation.GoogleTranslator import GoogleTranslator
from Scraper.Writers.FileWriter import FileWriter

translator = GoogleTranslator()

url = "http://www.spiegel.de/"

requester = Requester(url=url, retries=5, sleep_time=3)
response = requester.make_get_request()
html = response.data


dataset = NewsScraper.parse_articles_list(url_root=url,html=html)

for url in list(dataset):

    requester = Requester(url=url, retries=5)
    response = requester.make_get_request()
    html = response.data

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

writer = FileWriter("data/news.csv")
writer.write(dataset) #ERROR: File "C:/Users/Саша/Desktop/PyCh/webanalytics/Country/Germany/News/SPIEGEL/test.py", line 43, in <module>
                            #writer.write(dataset)
                            #File "C:\Users\Саша\Desktop\PyCh\webanalytics\Scraper\Writters\FileWritter.py", line 32, in write
                            #data['date'] = data['date'].strftime("%d/%m/%Y %H:%M:%S")
                            #AttributeError: 'NoneType' object has no attribute 'strftime'