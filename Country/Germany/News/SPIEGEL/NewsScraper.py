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
        div_news = soup.find_all('h2', {'class': ['article-title']})
        if not div_news:
            return None

        result = dict()

        for article in div_news:
            try:
                url = article.a['href']
                title = article.a['title']
            except TypeError:
                continue
            if not 'http' in url:
                url = urljoin(url_root, url)
                result[url] = CommonNewsHandler.get_article_row(url=url, title=title)
            else:
                continue
        return result

    @staticmethod
    def parse_article_subtitle(html=None, soup=None):

        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        subtitle = soup.find_all('p')

        if subtitle:
            return subtitle[0].text.strip()
        else:
            return None

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

        elif re.findall('\d\d.\d\d.\d\d\d\d', str(soup.p)) and re.findall('\d\d:\d\d', str(soup.p)):
            datetime_line = soup.p

            date_line = re.findall('\d\d.\d\d.\d\d\d\d', str(datetime_line))
            date_li = re.split('\.', date_line[0])
            day, month, year = int(date_li[0]), int(date_li[1]), int(date_li[2])

            time_line = re.findall('\d\d:\d\d', str(datetime_line))
            time_li = re.split(':', time_line[0])
            hours, minutes, seconds = int(time_li[0]), int(time_li[1]), 00
            date = datetime(year, month, day, hours, minutes, seconds)

        else:
            date = None

        return date

