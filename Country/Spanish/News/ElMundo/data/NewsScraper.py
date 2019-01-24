from urllib.parse import urljoin

from Scraper.CommonNewsHandler import CommonNewsHandler
from Requests.Requester import Requester
import re
from bs4 import BeautifulSoup


class NewsScraper(CommonNewsHandler):
    @staticmethod
    def get_page_data(root_url=None, page=1):
        requester = Requester(url=root_url + str(page))
        response = requester.make_get_request()
        return response.data.decode('utf-8')

    @staticmethod
    def parse_articles_list(url_root=None, html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, "html.parser")

        div_news = soup.find_all("div", {'class': ['new_seccion']})
        print('NEWS', div_news)
        if not div_news:
            return None
        div_links = div_news[0].find_all('div', {'class': ['article']})
        if not div_links:
            return None
        result = dict()
        for article in div_links:
            link = article.find('a')
            url = link['href']
            if 'http' not in url:
                url = urljoin(url_root, url)
            result[url] = CommonNewsHandler.get_article_row(url=url, title=link.text)
        return result

    @staticmethod
    def parse_article_subtitle(html=None, soup=None):
        result = dict()

        return result

    @staticmethod
    def parse_article_text(html=None, soup=None):
        result = dict()

        return result

    @staticmethod
    def parse_article_time(html=None, soup=None):
        result = dict()

        return result
