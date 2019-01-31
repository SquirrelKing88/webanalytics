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
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        news = soup.findAll('div', {'class': 'blog_articles'})

        result = dict()

        for article in news:
            link = article.find('h1').find('a')
            url = link['href']
            title = link.text
            subtitle = article.find('div', {'class': 'col-xs-8'}).text

            if 'http' not in url:
                url = urljoin(url_root, url)

            result[url] = CommonNewsHandler.get_article_row(url=url, title=title, subtitle=subtitle)

        return result





    @staticmethod
    def parse_article_datetime(html=None, soup=None, year=None, month=None, day=None, hours=None, minutes=None, seconds=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        date = soup.find('span', {'itemprop': 'datePublished'})['content']

        result = datetime.strptime(date[:-1:], "%Y-%m-%dT%H:%M:%S")

        if year:
            date.replace(year=year)
        if month:
            date.replace(month=month)
        if day:
            date.replace(day=day)
        if hours:
            date.replace(hours=hours)
        if minutes:
            date.replace(minutes=minutes)
        if seconds:
            date.replace(seconds=seconds)

        return result

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


