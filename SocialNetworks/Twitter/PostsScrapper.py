from urllib.parse import urljoin
from datetime import datetime
from Scraper.CommonPostsHandler import CommonPostsHandler
import re
from bs4 import BeautifulSoup

class PostsScraper(CommonPostsHandler):

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
    def parse_post_list(url_root=None, html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        div_posts = soup.find_all('li', {'data-item-type':'tweet'})

        if not div_posts:
            return None

        result = dict()

        for post in div_posts:
            own=not(post.find('div')).has_attr("data-retweeter")

            url = url_root+(post.find('div')["data-permalink-path"])

            if 'http' not in url:
                url = urljoin(url_root, url)

            result[url] = CommonPostsHandler.get_post_row(url=url, own_post=own)
        return result

    @staticmethod
    def parse_post_datetime(html=None, soup=None, year=None, month=None, day=None, hours=None, minutes=None, seconds=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        line = soup.find('span', {'class':'metadata'}).find('span').text

        #7:01 AM - 28 Nov 2018

        hours,line=re.split(":",line,1)
        minutes,line=re.split(" ",line,1)
        half,line=re.split(" ",line,1)
        line=re.sub("- ","",line)
        day,line=re.split(" ",line,1)
        month,line=re.split(" ",line,1)
        year=line

        month=PostsScraper.months[month]

        if len(hours)!=2:
            hours='0'+hours

        if half=="PM":
            hours=int(hours)+12
        if hours==24:
            hours='00'

        date = datetime(year=int(year), month=month, day=int(day), hour=int(hours), minute=int(minutes),second=00)

        return date

    @staticmethod
    def parse_post_likes(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')
        likes=soup.find('a', {'class': 'request-favorited-popup'})
        if likes:
            return likes["data-tweet-stat-count"]
        return 0

    @staticmethod
    def parse_post_reposts(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        reposts=soup.find('a', {'class': 'request-retweeted-popup'})
        if reposts:
            return reposts["data-tweet-stat-count"]
        return 0

    @staticmethod
    def parse_post_comments(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        comments=soup.find('span', {'class': 'ProfileTweet-actionCount'})
        if comments:
            return comments["data-tweet-stat-count"]
        return 0

    @staticmethod
    def parse_post_text(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        div = soup.find('div', {'class': 'js-tweet-text-container'})
        text=div.find('p')

        if not text:
            return None, None

        return text.text, str(html)