from Country.Poland.News.wiadomosciGazetaPl.NewsScraper import NewsScraper
from LanguageProcessing.Translation.GoogleTranslator import GoogleTranslator
from Scraper.Writers.FileWriter import FileWriter
from Scraper.Writers.ElasticSearchWritter import ElasticSearchWriter
from Requests.Requester import Requester
from threading import Thread

translator = GoogleTranslator()
# today news http://wiadomosci.gazeta.pl/wiadomosci/0,114871.html


def getArticle(url, dataset):
    requester = Requester(url=url, retries=5, sleep_time=3)
    response = requester.make_get_request()
    html = response.get_data()

    dataset[url]["subtitle"] = (NewsScraper.parse_article_subtitle(html=html))
    dataset[url]["date"] = (NewsScraper.parse_article_datetime(html=html))
    dataset[url]["text"], dataset[url]["html"] = (NewsScraper.parse_article_text(html=html))
    try:
        translation_result = translator.get_translation(dataset[url]["text"])
        dataset[url]["translation_en"] = translation_result['translation']
    except Exception:
        print("Translation error with url {0} and text {1}".format(url, dataset[url]["text"]))


def getNewsDataset(pages):
    dataset = dict()
    for page in range(pages):
        url = "http://wiadomosci.gazeta.pl/wiadomosci/0,114871.html?str="+str(page+1)

        requester = Requester(url=url, retries=5, sleep_time=3)
        response = requester.make_get_request()
        html = response.get_data()

        dataset.update(NewsScraper.parse_articles_list(url_root=requester.get_url_root(),html=html))

        threads=[]

        for article in dataset:
            url = article
            threads.append(Thread(target=getArticle, args=(url, dataset)))
            threads[-1].start()

        for thread in threads:
            thread.join()

    return dataset

dataset=getNewsDataset(1)
writers = [FileWriter("data/news.csv"),ElasticSearchWriter(index_name="test_poland")]
for writer in writers:
    writer.write(dataset)


