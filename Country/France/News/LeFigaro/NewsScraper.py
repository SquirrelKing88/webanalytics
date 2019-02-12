from datetime import datetime
from urllib.parse import urljoin

from Scraper.CommonNewsHandler import CommonNewsHandler
from Requests.Requester import Requester
import re
from bs4 import BeautifulSoup

class NewsScraper(CommonNewsHandler):

    @staticmethod
    def parse_articles_list(url_root=None, html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')
        div_news = soup.find_all('h2', {'class': ['fig-profile__headline']})
        if not div_news:
            return None

        result = dict()

        for article in div_news:
            try:
                url = article.a['href']
                title = article.a['title']
            except TypeError:
                continue
            result[url] = CommonNewsHandler.get_article_row(url=url, title=title)
        return result

    @staticmethod
    def parse_article_text(html=None, soup=None):

        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')
        subtitle = soup.find_all('p')
        list_of_text = []
        for string in subtitle:
            text = string.string
            if text != None:
                list_of_text.append(text)

        text = '.'.join(list_of_text)
        html = soup.prettify()

        return html, text

    def parse_article_datetime(html=None, soup=None, year=None, month=None, day=None, hours=None, minutes=None,
                               seconds=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')


        if 'datetime' in str(soup.time):

            datetime_line = soup.time['datetime']

            #date
            date = re.findall('\d\d\d\d-\d\d-\d\d',datetime_line)
            date = date[0]
            date = date.split('-')
            year = int(date[0])
            month = int(date[1])
            day = int(date[2])

            #time
            time = re.findall('\d\d:\d\d:\d\d',datetime_line)
            time = re.split(':', time[0])
            hours = int(time[0])
            minutes = int(time[1])
            seconds = int(time[2])
            date = datetime(year, month, day, hours, minutes, seconds)

        else:
            year = 1111
            month = 1
            day = 1
            hours = 11
            minutes = 11
            seconds = 11
            date = datetime(year, month, day, hours, minutes, seconds)

        return date

