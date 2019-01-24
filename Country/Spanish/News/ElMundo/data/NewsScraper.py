from urllib.parse import urljoin

from Scraper.CommonNewsHandler import CommonNewsHandler
from Requests.Requester import Requester
import re
from bs4 import BeautifulSoup
from Translation.GoogleTranslator import GoogleTranslator

translator = GoogleTranslator()


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

        if not div_news:
            return None
        for div in div_news:
            header = div.find_all("div", {'class': ['caption']})
            text = header[0].p
            if text is not None:
                text = text.text
            a = header[0].find_all("a")
            header_text = a[0].get_text()
            header_link = a[0].get('href')
            div_sub = soup.find_all("span", {'class': ['origen']})
            subtitle = div_sub[0]
            if subtitle is not None:
                subtitle = subtitle.text
            article = {
                'url': url_root,
                'date': '',
                'title': header_text,
                'subtitle': subtitle,
                "html": '',
                "text": text,
                "translation_en":''
            }
            print('ARTICLE', article)

