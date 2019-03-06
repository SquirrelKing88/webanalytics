from datetime import datetime
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
    # TODO put this method to LanguageProcessing
    def month_string_to_number(string):
        month = {
            'січень': 1,
            'лютий': 2,
            'березень': 3,
            'квітень': 4,
            'травень': 5,
            'червень': 6,
            'липень': 7,
            'серпень': 8,
            'вересень': 9,
            'жовтень': 10,
            'листопад': 11,
            'грудень': 12,

            'січня': 1,
            'лютого': 2,
            'березня': 3,
            'квітня': 4,
            'травня': 5,
            'червня': 6,
            'липня': 7,
            'серпня': 8,
            'вересня': 9,
            'жовтня': 10,
            'листопада': 11,
            'грудня': 12,
        }

        s = string.strip().lower()

        try:
            return month[s]
        except:
            raise ValueError('Not a month')

    @staticmethod
    def get_root_url():
        """

        :return: url for news page
        """
        return "https://www.pravda.com.ua/news/"

    @staticmethod
    def get_country_code():
        """

        :return: country code
        """
        return 'uk'

    @staticmethod
    def parse_articles_list(url_root=None, html=None, soup=None):

        """

        :param url_root:
        :param html:
        :param soup:
        :return: dataset filled
                            url
                            title
                            subtitle
        """
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

            # parse subtitle
            subtitle = article.find('div', {'class': ['article__subtitle']})
            if subtitle:
                subtitle = subtitle.text.strip()

            result[url] = CommonNewsHandler.get_article_row(url=url, title=link.text, subtitle=subtitle)

        return result

    @staticmethod
    def parse_article_datetime(html=None, soup=None, year=None, month=None, day=None, hours=None, minutes=None,
                               seconds=0):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        # post_news__date for pravda.com.ua
        # post__time for www.eurointegration.com.ua

        date_str = soup.find('div', {'class': ['post_news__date', 'post__time']})

        if not date_str:
            # TODO default value
            # TODO check error state
            date = datetime.now()
        else:
            day_month_year, hours_minutes = date_str.text.split(',')[1:3]
            day, month, year = day_month_year.split()
            hours, minutes = hours_minutes.split(':')
            date = datetime(year=int(year), month=NewsScraper.month_string_to_number(month), day=int(day), hour=int(hours), minute=int(minutes), second=seconds)

        return date


    @staticmethod
    def parse_article_subtitle(html=None, soup=None):
        """

        :param html: None
        :param soup: None
        :return: None as subtitle scraped in  parse_articles_list method already
        """
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


