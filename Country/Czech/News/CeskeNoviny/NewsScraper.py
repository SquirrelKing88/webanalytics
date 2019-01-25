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
    def parse_articles_list(url_root=None, html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        div_links = soup.find_all('li', {'class': 'list-item'})

        result = dict()
        for article in div_links:
            # проверяем дату, чтоб достать новости только за один день:
            #date_time = article.find('span', {'class': ['tag blue']}).text
            #print(date_time)
            #if date_time[:2] != '25':
            #    break
            link = article.find('a')
            if link == None:
                break
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
        article = soup.find('div', itemprop='articleBody')
        text = article.find_all('p')

        if text:
            full_text = ''
            html_text = ''
            for p in text:
                html_p = p.prettify()
                html_text += html_p + '\n'
                p.extract()
                #[x.extract() for x in p.findall('script')] #extract убирает комменты
                full_text += p.text
            cleaned_text = full_text

            return html_text, cleaned_text.strip()
        else:
            return None, None