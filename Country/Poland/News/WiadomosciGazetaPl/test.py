from Country.Poland.News.WiadomosciGazetaPl.CategoriesScraper import NewsScraper
from LanguageProcessing.Translation.GoogleTranslator import GoogleTranslator
from Scraper.Writers.FileWriter import FileWriter
from Scraper.Writers.ElasticSearchWritter import ElasticSearchWriter
from Requests.Requester import Requester
from threading import Thread
from datetime import datetime

translator = GoogleTranslator()
# today news http://wiadomosci.gazeta.pl/wiadomosci/0,114871.html

categories = {
    "Polska":"http://wiadomosci.gazeta.pl/wiadomosci/0,114883.html",
    "Polityka":"http://wiadomosci.gazeta.pl/wiadomosci/0,114884.html",
    "Swiat":"http://wiadomosci.gazeta.pl/wiadomosci/0,114881.html",
    "Opinie":"http://wiadomosci.gazeta.pl/wiadomosci/0,161770.html",
    "Nauka":"http://wiadomosci.gazeta.pl/wiadomosci/0,114885.html",
    "Edukacja":"http://wiadomosci.gazeta.pl/wiadomosci/0,156046.html"
}


def getArticle(url, dataset):
    requester = Requester(url=url, retries=5, sleep_time=3)
    response = requester.make_get_request()
    html = response.get_data()
    #try:
    dataset[url]["subtitle"] = (NewsScraper.parse_article_subtitle(html=html))
    dataset[url]["date"] = (NewsScraper.parse_article_datetime(html=html))
    dataset[url]["html"],dataset[url]["text"] = (NewsScraper.parse_article_text(html=html))
    try:
        translation_result = translator.get_translation(dataset[url]["text"])
        dataset[url]["translation_en"] = translation_result['translation']
    except Exception:
        print("Translation error with url {0} and text {1}".format(url, dataset[url]["text"]))
    #except Exception:
    #    print("Something went wrong in "+url)


def getNewsDataset(category,date):
    dataset = dict()
    for page in range(5):
        url = categories[category]+"?str="+str(page+1)

        requester = Requester(url=url, retries=5, sleep_time=3)
        response = requester.make_get_request()
        html = response.get_data()

        dataset.update(NewsScraper.parse_articles_list(url_root=requester.get_url_root(),html=html,date=date))

    threads=[]

    for article in dataset:
        url = article
        threads.append(Thread(target=getArticle, args=(url, dataset)))
        threads[-1].start()

    for thread in threads:
        thread.join()

    return dataset



category="Polska"
date = datetime.today()
dataset=getNewsDataset(category,date)
writer = FileWriter("data/{}.csv".format(category))
writer.write(dataset)
#writers = [FileWriter("data/news.csv"),ElasticSearchWriter(index_name="test_poland")]
#writers[1].delete_index()
#for writer in writers:
#    writer.write(dataset)


