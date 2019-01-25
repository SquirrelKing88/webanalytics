import time
from datetime import date as datetime
from urllib.parse import urljoin

from Scraper.CommonNewsHandler import CommonNewsHandler
from Requests.Requester import Requester
import re
from bs4 import BeautifulSoup
from Translation.GoogleTranslator import GoogleTranslator


class NewsScraper(CommonNewsHandler):
    @staticmethod
    def get_page_data(root_url=None, page=1):
        requester = Requester(url=root_url + str(page))
        response = requester.make_get_request()
        return response.data.decode('utf-8')

    @staticmethod
    def get_article_text_translation(original_text=None, destination_language='en'):
        if original_text is None:
            return None
        try:
            translator = GoogleTranslator()
            translation = translator.get_translation(original_text=original_text,
                                                     destination_language=destination_language)
            print('TRANSLATION', translation)
            return translation
        except Exception as e:
            print('EXCEPTION', e)
            return None

    @staticmethod
    def parse_articles_list(url_root=None, html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, "html.parser")
        result = list()
        div_news = soup.find_all("div", {'class': ['new_seccion']})
        if not div_news:
            return result
        for div in div_news:
            date = NewsScraper.parse_article_datetime(html=html, year=2019, month=1, day=1)
            title = NewsScraper.parse_article_title(html=html, soup=div)
            subtitle = NewsScraper.parse_article_subtitle(html=html, soup=div)
            text = NewsScraper.parse_article_text(html=html, soup=div)
            # translation = NewsScraper.get_article_text_translation(original_text=text, destination_language='en')
            article = dict(url=url_root, date=date, title=title, subtitle=subtitle, html=None, text=text, translation_en=None)
            result.append(article)
        return result

    @staticmethod
    def parse_article_datetime(html=None, soup=None, year=None, month=None, day=None, hours=None, minutes=None,
                               seconds=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')
        datetime = time.asctime()
        return '25 Jan 2019 16:53:54'

    @staticmethod
    def parse_article_text(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, "html.parser")
        caption = soup.find_all('div', {'class': ['caption']})
        text = caption[0].p
        if text is not None:
            text = text.text.strip()
        return text

    @staticmethod
    def parse_article_title(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, "html.parser")
        caption = soup.find_all('div', {'class': ['caption']})
        a = caption[0].find_all('a')
        if a[0] is None:
            return None
        return a[0].get_text().strip()

    @staticmethod
    def parse_article_subtitle(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, "html.parser")
        div_sub = soup.find_all('span', {'class': ['origen']})
        if div_sub is None or len(div_sub) == 0:
            return None
        return div_sub[0].text

