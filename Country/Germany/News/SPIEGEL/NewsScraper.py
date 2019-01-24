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
    def parse_article_time(html=None, soup=None):

        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')
        time_line = soup.time['datetime']
        time = re.findall('\d\d:\d\d:\d\d',time_line)
        time = re.split(':', time[0])
        hours = time[0]
        minutes = time[1]
        seconds = time[2]

        return hours, minutes, seconds

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

        return html, text


    def parse_article_date(html=None, soup=None):

        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        date_line = soup.time['datetime']
        date = re.findall('\d\d-\d\d-\d\d',date_line)
        date = date[0]

        return date

