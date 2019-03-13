import functools
from concurrent.futures.thread import ThreadPoolExecutor

from bs4 import BeautifulSoup

from LanguageProcessing.Translation.GoogleTranslator import GoogleTranslator
from Requests.Requester import Requester


class ScraperJob:

    def __init__(self, scraper):

        self.__scraper = scraper

    def __parse_article_job(self, scraper, url):
        article = scraper.get_article_row()
        article['url'] = url

        # make new request to upload article data
        # and load html into soup
        requester = Requester(url=url, retries=5)
        response = requester.make_get_request()
        html = response.get_data()
        soup = BeautifulSoup(html, 'html.parser')

        article['date'] = scraper.parse_article_datetime(html=html, soup=soup)
        article['subtitle'] = scraper.parse_article_subtitle(html=html, soup=soup)
        article["html"], article["text"] = scraper.parse_article_text(html=html, soup=soup)

        # TODO translation as pool
        translator = GoogleTranslator()
        translation_result = translator.get_translation(article["text"])
        article["translation_en"] = translation_result['translation']
        # clear memory
        del translator

        print('Article {0} scraped'.format(url))

        return article

    def __parse_article_job_callback(self, job_response, dataset):
        article = job_response.result()
        dataset[article['url']].update({key: value for key, value in article.items() if value})



    def scrape(self):

        #max_workers = 100
        max_workers = 1
        pool = ThreadPoolExecutor(max_workers=max_workers)
        requester = Requester(url=self.__scraper.get_root_url(), retries=5, sleep_time=3)
        response = requester.make_get_request()
        html = response.get_data()

        # TODO remove repeating scraping
        dataset = self.__scraper.parse_articles_list(url_root=requester.get_url_root(), html=html)

        with pool as executor:
            for url in list(dataset):
                job = executor.submit(functools.partial(self.__parse_article_job, url=url, scraper=self.__scraper))
                job.add_done_callback(functools.partial(self.__parse_article_job_callback, dataset=dataset))


        return dataset
