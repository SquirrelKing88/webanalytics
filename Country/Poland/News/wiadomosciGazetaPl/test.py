from threading import Thread
from Requests.Requester import Requester
from Country.Poland.News.WiadomosciGazetaPl.NewsScraper import NewsScraper
from Translation.GoogleTranslator import  GoogleTranslator
from Scraper.Writters.FileWritter import FileWriter

import time

translator = GoogleTranslator()
# today news http://wiadomosci.gazeta.pl/wiadomosci/0,114871.html


def getArticles(url_list, dataset):
    for url in url_list:
        requester = Requester(url=url, retries=5, sleep_time=3)
        response = requester.make_get_request()
        html = response.data

        dataset[url]["subtitle"] = (NewsScraper.parse_article_subtitle(html=html))
        dataset[url]["date"] = (NewsScraper.parse_article_datetime(html=html))
        dataset[url]["text"], dataset[url]["html"] = (NewsScraper.parse_article_text(html=html))
        try:
            translation_result = translator.get_translation(dataset[url]["text"])
            dataset[url]["translation_en"] = translation_result['translation']
        except Exception:
            print("Translation error with url {0} and text {1}".format(url, dataset[url]["text"]))

def getNewsDataset(pages=1,processors=1):
    dataset = dict()
    for page in range(pages):
        url = "http://wiadomosci.gazeta.pl/wiadomosci/0,114871.html?str="+str(page+1)

        requester = Requester(url=url, retries=5, sleep_time=3)
        response = requester.make_get_request()
        html = response.data

        dataset.update(NewsScraper.parse_articles_list(url_root=requester.get_url_root(),html=html))

        threads=[]

        batch_size=len(dataset)//processors
        if(len(dataset)%processors):
            batch_size+=1


        url_list=[]
        counter=0
        for article in dataset:
            url_list.append(article)
            counter+=1
            if(counter==batch_size):
                threads.append(Thread(target=getArticles, args=(url_list.copy(), dataset)))
                url_list = []
                counter=0
                threads[-1].start()

        if len(url_list):
            threads.append(Thread(target=getArticles, args=(url_list.copy(), dataset)))
            threads[-1].start()

        for thread in threads:
            thread.join()

    return dataset

start=time.time()
writer = FileWriter("data/news.csv")
writer.write(getNewsDataset(pages=1,processors=23))
end=time.time()
print(end-start)


