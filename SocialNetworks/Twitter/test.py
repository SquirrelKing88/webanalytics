from SocialNetworks.Twitter.PostsScrapper import PostsScraper
from Requests.Requester import Requester
from threading import Thread
import time
from Scraper.Writters.FileWritter import FileWriter

def getArticles(url_list, dataset):
    for url in url_list:
        requester = Requester(url=url, retries=5, sleep_time=3)
        response = requester.make_get_request()
        html = response.data


        dataset[url]["date"] = (PostsScraper.parse_post_datetime(html=html))
        dataset[url]["text"], dataset[url]["html"] = (PostsScraper.parse_post_text(html=html))
        dataset[url]["likes"] = PostsScraper.parse_post_likes(html=html)
        dataset[url]["reposts"] = (PostsScraper.parse_post_reposts(html=html))
        dataset[url]["comments"] = (PostsScraper.parse_post_comments(html=html))


        try:
            translation_result = translator.get_translation(dataset[url]["text"])
            dataset[url]["translation_en"] = translation_result['translation']
        except Exception:
            pass
            #print("Translation error with url {0} and text {1}".format(url, dataset[url]["text"]))


def getPostsDataset(twitter_account,processors=1):
    dataset=dict()
    requester = Requester(url="https://twitter.com/"+twitter_account, retries=5, sleep_time=3)
    response = requester.make_get_request()
    html = response.data

    dataset.update(PostsScraper.parse_post_list(url_root=requester.get_url_root(),html=html))

    threads = []

    batch_size = len(dataset) // processors
    if (len(dataset) % processors):
        batch_size += 1

    url_list = []
    counter = 0
    for post in dataset:
        url_list.append(post)
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
twitter_account="iloverochev"
with open(("tweets/{}.csv").format(twitter_account),'w')as file:
    pass
writer = FileWriter(("tweets/{}.csv").format(twitter_account))
writer.write(getPostsDataset(twitter_account=twitter_account,processors=16))
end=time.time()
print(end-start)
