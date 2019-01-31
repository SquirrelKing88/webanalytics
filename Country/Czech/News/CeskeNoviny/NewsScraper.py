from urllib.parse import urljoin

from Scraper.CommonNewsHandler import CommonNewsHandler
from Requests.Requester import Requester
import re
from bs4 import BeautifulSoup

class NewsScraper(CommonNewsHandler):
    """
    Inherit CommonNewsHandler for ceskenoviny.cz
    """

    @staticmethod
    def parse_articles_list(url_root=None, html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        div_links = soup.find_all('li', {'class': 'list-item'})

        result = dict()
        for article in div_links:
            link = article.find('a')
            if link is None:
                print('No link')
                continue
            url = link['href']
            title = link.find('h3', {'class': 'title'})

            if 'http' not in url:
                url = urljoin(url_root, url)

            result[url] = CommonNewsHandler.get_article_row(url=url, title=title.text)

        return result

    @staticmethod
    def parse_article_datetime(html=None, soup=None, year=None, month=None, day=None, hours=None, minutes=None, seconds=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        date_time = soup.find('div', {'class': 'box-article-info'})
        time = date_time.find('span', {'itemprop': 'datePublished'}).text

        line = re.search(r"\d{2}:\d{2}", time).group(0)
        hours = line[:2]
        minutes = line[3:]
        # TODO
        return int(hours), int(minutes)

    @staticmethod
    def parse_article_subtitle(html=None, soup=None):

        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        subtitle = soup.find_all('p', {'class': 'big'})

        if subtitle:
            return subtitle[0].text.strip()
        else:
            return None


    @staticmethod
    def parse_article_text(html=None, soup=None):

        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')
        text = soup.find('div', {'itemprop': 'articleBody'})
        #text = text.find('p').find_all_previous('ul')

        if text:
            [x.extract() for x in text.findAll('script')]
            html_text = text.prettify()
            cleaned_text = text.text

            return html_text, cleaned_text.strip()
        else:
            return None, None
