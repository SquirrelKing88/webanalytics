from urllib.parse import urljoin

from Scraper.CommonNewsHandler import CommonNewsHandler
from Requests.Requester import Requester
import re
from bs4 import BeautifulSoup

class NewsScraper(CommonNewsHandler):
    """
    Inherit CommonNewsHandler for pravda.com.ua
    """

    @staticmethod
    def parse_articles_list(url_root=None, html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        div_news = soup.find_all('div', {'class': ['news_all']})

        if not div_news:
            return None

        div_links = div_news[0].find_all('div', {'class': ['article']})

        result = dict()

        for article in div_links:
            link = article.find('a')
            url = link['href']

            if 'http' not in url:
                url = urljoin(url_root, url)

            result[url] = CommonNewsHandler.get_article_row(url=url, title=link.text)

        return result

    @staticmethod
    def parse_article_time(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        # TODO
        return None, None, None

    @staticmethod
    def parse_article_subtitle(html=None, soup=None):

        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        subtitle = soup.find_all('div', {'class': ['article__subtitle']})

        if subtitle:
            return subtitle[0].text.strip()
        else:
            return None


    @staticmethod
    def parse_article_text(html=None, soup=None):

        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        text = soup.find_all('div', {'class': ['post_news__text', 'post__text']})

        if text:
            html_text = text[0].prettify()
            cleaned_text = text[0]
            [x.extract() for x in cleaned_text.findAll('script')]

            return html_text, cleaned_text.text.strip()
        else:
            return None, None
