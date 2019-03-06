from Requests.Requester import Requester
from Country.Ukraine.News.PravdaUa.NewsScraper import NewsScraper
from bs4 import BeautifulSoup
from LanguageProcessing.Translation.GoogleTranslator import GoogleTranslator
from concurrent.futures import ThreadPoolExecutor
from Scraper.Writers.FileWriter import FileWriter
from multiprocessing import cpu_count
import functools



def parse_article_job(scraper, url):

    result = scraper.get_article_row()
    result['url'] = url

    # make new request to upload article data
    # and load html into soup
    requester = Requester(url=url, retries=5)
    response = requester.make_get_request()
    html = response.get_data()
    soup = BeautifulSoup(html, 'html.parser')

    result['date'] = scraper.parse_article_datetime(html=html, soup=soup)
    result['subtitle'] = scraper.parse_article_subtitle(html=html, soup=soup)
    result["html"], result["text"] = scraper.parse_article_text(html=html, soup=soup)

    # TODO translation as pool
    translator = GoogleTranslator()
    translation_result = translator.get_translation(result["text"])
    result["translation_en"] = translation_result['translation']
    # clear memory
    del translator

    print('Article {0} scraped'.format(url))

    return result


def parse_article_job_callback(job_response, dataset):
    article = job_response.result()
    dataset[article['url']].update({key: value for key, value in article.items() if value})






scraper = NewsScraper
max_workers = 100
pool = ThreadPoolExecutor(max_workers=max_workers)


requester = Requester(url=scraper.get_root_url(), retries=5, sleep_time=3)
response = requester.make_get_request()
html = response.get_data()


dataset = scraper.parse_articles_list(url_root=requester.get_url_root(), html=html)


with pool as executor:
    for url in list(dataset):
        job = executor.submit(functools.partial(parse_article_job, url=url, scraper=scraper))
        job.add_done_callback(functools.partial(parse_article_job_callback, dataset=dataset))




writer = FileWriter("data/news.csv")
writer.write(dataset)




