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
        #TODO
        month = {
            '1': 1,
            'feb': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9':9,
            '10':10,
            '11':11,
            '12':12

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

        div_news = soup.find('div', {'class': ['todays-news__hits']})
        result = dict()

        div_links = div_news.find_all('a')

        for element in div_links:
            url = element['href']
            title=element.find('h3').text

            if 'http' not in url:
                url = urljoin(url_root, url)

            result[url] = CommonNewsHandler.get_article_row(url=url, title=title)
        return result


    @staticmethod
    def parse_article_datetime(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        div_links = soup.find_all('a',{'class':['todays-news__hit']})

        for element in div_links:
            dates = element.find('time').text.split(' ')
            day = int(dates[0])
            month = int(NewsScraper.month_string_to_number(dates[1]))
            year = int(dates[2])
            time = dates[4].split('.')
            hours = int(time[0])
            minutes = int(time[1])

            date = datetime(year=year, month=month, day=day, hour=hours, minute=minutes)

        return div_links

    @staticmethod
    def parse_article_subtitle(html=None, soup=None):


        return None

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