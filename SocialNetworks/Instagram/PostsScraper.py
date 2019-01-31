from Scraper.InstagramPostHandler import InstagramPostHandler
from Requests.Requester import Requester
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin
import re

class PostsScraper():
    @staticmethod
    def parse_posts_list(url_root=None, html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')
        div_posts = soup.find_all('div',{'class':['Nnq7C', 'weEfm']})
        if div_posts is not None:
            return div_posts
        else:
            return None
        result = dict()
        for div in div_posts:
            link = div.find('a')
            url = link['href']
       # url = div_posts[0].a.get('href')
        result[url] = InstagramPostHandler.get_posts_row(url=url)
        print("LINKS", div_posts)
        return result

    @staticmethod
    def parse_post_datetime(html=None, soup=None, year=None, month=None, day=None, hours=None, minutes=None,
                               seconds=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        datetime =soup.find_all('time', {'class': ['_1o9PC Nzb55']})
        if datetime is None or len(datetime) == 0:
            return None
        return datetime[0].text

    @staticmethod
    def parse_post_text(html=None, soup=None):

        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        text = soup.find_all('li', {'class': ['gElp9']})

        if text:
            html_text = text[0].prettify()
            cleaned_text = text[0].span
            return html_text, cleaned_text.text.strip()
        else:
            return None, None

    @staticmethod
    def parse_post_hashtags(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')
        hashtags = soup.find_all('h2', {'class':['_6lAjh']})
        if hashtags:
            html_hashtags = hashtags[0].prettify()
            cleaned_hash = hashtags[0].a['href']
            return html_hashtags, cleaned_hash
        else:
            return None,None

    @staticmethod
    def parse_posts_receivers(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')
        receivers = soup.find_all('h3', {'class':['_6lAjh']})
        if receivers:
            html_receivers = receivers[0].prettify()
            cleaned_rec = receivers[0].a['href']
            return html_receivers, cleaned_rec
        else:
            return None,None

    @staticmethod
    def parse_posts_users(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')
        users = soup.find_all('div', {'class':['KlCQn G14m- EtaWk']})
        if users:
            html_users = users[0].prettify()
            cleaned_users = users[0].a['href']
            return html_users, cleaned_users
        else:
            return None, None

    @staticmethod
    def parse_posts_geo(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')
        geo = soup.find_all('div', {'class':['M30cS']})
        if geo:
            html_geo = geo[0].prettify()
            cleaned_geo = geo[0].a['href']
            return html_geo, cleaned_geo
        else:
            return None, None