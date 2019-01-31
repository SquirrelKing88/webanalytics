from urllib.parse import urljoin

from Scraper.CommonNewsHandler import CommonNewsHandler
from Requests.Requester import Requester
import re
from datetime import datetime
from bs4 import BeautifulSoup

class NewsScraper(CommonNewsHandler):
    """
    Inherit CommonNewsHandler for pravda.com.ua
    """

    @staticmethod
    def parse_articles_list(url_root=None, html=None, soup=None):
        # The main difference of this branch is this function. Now it is a generator.
        # Thus we don't need RAM for storing dataset as we are returning it by elements.
        # But it makes sense only when this function returns a really huge amount of data.
        # Though it won't do it simply because this function scrapes one HTML page with about 20 links we need.
        # So most likely this code is useless :)
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        news = soup.findAll('div', {'class': 'blog_articles'})

        for article in news:
            link = article.find('h1').find('a')
            url = link['href']
            if 'http' not in url:
                url = urljoin(url_root, url)

            yield url


    @staticmethod
    def parse_article_datetime(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        date = soup.find('span', {'itemprop': 'datePublished'})['content']

        result = datetime.strptime(date[:-1:], "%Y-%m-%dT%H:%M:%S")

        return result

    @staticmethod
    def parse_article_title(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        title = soup.find('h1', {'class': 'article_title'}).text

        return title

    @staticmethod
    def parse_article_subtitle(html=None, soup=None):
        return None


    @staticmethod
    def parse_article_text(html=None, soup=None):

        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        text = soup.find('div', {'class': 'description'})

        if text:
            html_text = text.prettify()
            text = text.text

            return html_text, text.strip()
        else:
            return None, None


