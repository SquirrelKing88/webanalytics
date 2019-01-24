from Requests.Requester import Requester
from Country.Poland.News.wiadomosciGazetaPl.NewsScraper import NewsScraper
from Translation.GoogleTranslator import  GoogleTranslator
from Scraper.Writters.FileWritter import FileWriter

translator = GoogleTranslator()
# today news http://wiadomosci.gazeta.pl/wiadomosci/0,114871.html


def getNewsDataset():
    dataset = dict()
    for page in range(1):
        url = "http://wiadomosci.gazeta.pl/wiadomosci/0,114871.html?str="+str(page+1)

        requester = Requester(url=url, retries=5, sleep_time=3)
        response = requester.make_get_request()
        html = response.data

        dataset.update(NewsScraper.parse_articles_list(url_root=requester.get_url_root(),html=html))

        for article in dataset:
            url = article

            requester = Requester(url=url, retries=5, sleep_time=3)
            response = requester.make_get_request()
            html = response.data

            dataset[url]["subtitle"]=(NewsScraper.parse_article_subtitle(html=html))
            dataset[url]["date"]=(NewsScraper.parse_article_time(html=html))
            dataset[url]["text"],dataset[url]["html"]=(NewsScraper.parse_article_text(html=html))
            try:
                translation_result = translator.get_translation(dataset[url]["text"])
                dataset[url]["translation_en"] = translation_result['translation']
            except Exception:
                print("Translation error with url {0} and text {1}".format(url, dataset[url]["text"]))

    return dataset


writer = FileWriter("data/news.csv")
writer.write(getNewsDataset())

