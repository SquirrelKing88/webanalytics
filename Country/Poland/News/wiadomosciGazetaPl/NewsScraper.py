from urllib.parse import urljoin
from datetime import datetime
from Scraper.CommonNewsHandler import CommonNewsHandler
import re
from bs4 import BeautifulSoup

class NewsScraper(CommonNewsHandler):

    @staticmethod
    def parse_articles_list(url_root=None, html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        div_news = soup.find_all('li', {'class':'entry'})

        if not div_news:
            return None

        result = dict()

        for article in div_news:
            link = article.find('a')
            url = link['href']

            if 'http' not in url:
                url = urljoin(url_root, url)

            result[url] = CommonNewsHandler.get_article_row(url=url, title=link["title"])
        return result

    @staticmethod
    def parse_article_subtitle(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        article = soup.find('div', {'id':'gazeta_article_lead'})

        return article.text

    @staticmethod
    def parse_article_datetime(html=None, soup=None, year=None, month=None, day=None, hours=None, minutes=None, seconds=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        time = soup.find('time')

        line = re.search(r"\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}",time.text).group(0)

        #23.01.2019 13:42

        day,line=line.split(".",1)
        month,line=line.split(".",1)
        year=line[0:3]
        line=re.search("\d{2}:\d{2}",line)
        line=line.group(0)
        hour=line[0:1]
        minute=line[3:4]
        second=00

        date = datetime(year=int(year), month=int(month), day=int(day), hour=int(hour), minute=int(minute), second=int(second))

        return date

    @staticmethod
    def parse_article_text(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        articles = soup.find_all('p', {'class': 'art_paragraph'})

        if not articles:
            return None

        result=""

        for article in articles:
            result+=article.text

        return result, article.prettify()



