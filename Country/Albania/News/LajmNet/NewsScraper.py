from urllib.parse import urljoin
from datetime import datetime
from Scraper.CommonNewsHandler import CommonNewsHandler
import re
from bs4 import BeautifulSoup

class NewsScraper(CommonNewsHandler):

    months={'Jan':1,
           'Feb':2,
           'Mar':3,
           'Apr':4,
           'May':5,
           'Jun':6,
           'Jul':7,
           'Aug':8,
           'Sep':9,
           'Oct':10,
           'Nov':11,
           'Dec':12
           }

    @staticmethod
    def parse_articles_list(url_root=None, html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

            div_news = soup.find('div', {'id':'widget-content-magone-archive-blog-rolls'})

            if not div_news:
                return None

            articles = div_news.find_all('div',{'class':'shad'})
            result = dict()

            for article in articles:
                h3 = article.find('div',{'class':'item-content'}).find('h3')
                link = h3.find('a')
                url = link['href']

                subtitle = article.find('div', {'class':'item-snippet'}).text

                if 'http' not in url:
                    url = urljoin(url_root, url)

                result[url] = CommonNewsHandler.get_article_row(url=url, title=link["title"], subtitle=subtitle)
            return result

    @staticmethod
    def parse_article_datetime(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        time = soup.find('span',{'class':'value'}).text


        #Feb 8, 2019
        line=re.search('[A-Z][a-z]{2} \d+, \d+',time).group(0)
        month,line=re.split(' ',line,1)
        day,line=re.split(',',line,1)
        year=line.strip()

        date = datetime(year=int(year), month=NewsScraper.months[month], day=int(day))

        return date

    @staticmethod
    def parse_article_text(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        paragraphs = soup.find('div', {'class': 'post-body-inner'})

        if not paragraphs:
            return None

        paragraphs = paragraphs.find_all('p')

        result=""

        for article in paragraphs:
            result+=article.text

        return result, soup.prettify()



