from urllib.parse import urljoin
from datetime import datetime
from Scraper.CommonNewsHandler import CommonNewsHandler
from Requests.Requester import Requester
import re
from bs4 import BeautifulSoup

class NewsScraper(CommonNewsHandler):
    """
    Inherit CommonNewsHandler for www.ansa.it
    """

    @staticmethod
    # TODO put this method to Scraper
    def month_string_to_number(string):
        month = {
            'gennaio': 1,
            'febbraio': 2,
            'marzo': 3,
            'aprile': 4,
            'maggio': 5,
            'giugno': 6,
            'luglio': 7,
            'agosto': 8,
            'settembre': 9,
            'ottobre': 10,
            'novembre': 11,
            'dicembre': 12,


        }

        s = string.strip().lower()

        try:
            return month[s]
        except:
            raise ValueError('Not a month')

    @staticmethod
    def parse_articles_list(url_root=None, html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        div_news = soup.find_all('div', {'class': ['span6', 'pp-column', 'pull-right']})

        if not div_news:
            return None

        div_links = div_news[0].find_all('article', {'class': ['news small']})

        result = dict()

        for article in div_links:
            link = article.find('a')
            url = link['href']

            if 'http' not in url:
                url = urljoin(url_root, url)

            result[url] = CommonNewsHandler.get_article_row(url=url, title=link.text)

        return result


    @staticmethod
    def parse_article_datetime(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        lines = soup.find_all('div', {'class': ['news-time']})
        for line in lines:
            dates = line.find('strong').text.split(' ')
            month = int(NewsScraper.month_string_to_number(dates[1]))
            day = int(dates[0])
            year = int(dates[2])
            time = line.find('span').text.split(':')
            hours = int(time[0])
            minutes = int(time[1])

            date = datetime(year=year, month=month, day=day, hour=hours, minute=minutes)

        return date


    @staticmethod
    def parse_article_subtitle(html=None, soup=None):

        post_links = soup.find_all('h3', {'class': ['news-title']})
        for posts in post_links:
            subtitle = posts.text

        return subtitle

    @staticmethod
    def parse_article_text(html=None, soup=None):

        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        text = soup.find_all('div', {'class': ['news-txt']})

        if text:
            html_text = text[0].prettify()
            cleaned_text = text[0]
            [x.extract() for x in cleaned_text.findAll('script')]

            return html_text, cleaned_text.text.strip()
        else:
            return None, None