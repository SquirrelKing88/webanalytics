from LanguageProcessing.Translation.GoogleTranslator import GoogleTranslator
from Requests.Requester import Requester
from Twitter.PostsScraper import PostsScraper
from bs4 import BeautifulSoup

from Scraper.Writters.FileWritter import FileWriter
from threading import Thread

translator = GoogleTranslator()

url = "https://twitter.com/"
acc = 'realDonaldTrump'

requester = Requester(url=url+acc, retries=5, sleep_time=3)
response = requester.make_get_request()
html = response.data

dataset = PostsScraper.parse_posts_list(url_root=requester.get_url_root(), html=html, acc=acc)

def scrape_url(url, dataset=dataset):
    print('new thread started scrapping')

    requester = Requester(url=url, retries=5)
    response = requester.make_get_request()
    html = response.data

    soup = BeautifulSoup(html, 'html.parser')

    text = PostsScraper.parse_post_text(html=html, soup=soup)

    if dataset[url]['is_retweet'] is False:

        comments = PostsScraper.parse_post_comments(html=html, soup=soup)
        likes = PostsScraper.parse_post_likes(html=html, soup=soup)
        retweets = PostsScraper.parse_post_retweets(html=html, soup=soup)
        datetime = PostsScraper.parse_post_datetime(html=html, soup=soup)

    dataset[url]['comments'] = comments
    dataset[url]['likes'] = likes
    dataset[url]['date'] = datetime
    dataset[url]["text"] = text
    dataset[url]["retweets"] = retweets

    translation_result = translator.get_translation(text)
    dataset[url]["translation_en"] = translation_result['translation']


for url in list(dataset):
    th = Thread(target=scrape_url, args=(url, ))
    th.start()

th.join()

writer = FileWriter("posts.csv")
writer.write(dataset)
