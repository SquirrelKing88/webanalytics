from urllib.parse import urljoin

from Twitter.PostsHandler import PostsHandler
import re
from bs4 import BeautifulSoup
from datetime import datetime


class PostsScraper(PostsHandler):

    @staticmethod
    def parse_posts_list(url_root=None, html=None, acc=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        div_posts = soup.find_all('div', {'class': 'tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content original-tweet js-original-tweet'})
        result = dict()
        for post in div_posts:
            part_url = post['data-permalink-path']
            url = urljoin(url_root, part_url)
            if acc in url:
                is_retweet = False
            else:
                is_retweet = True

            result[url] = PostsHandler.get_article_row(url=url, is_retweet=is_retweet)

        return result

    @staticmethod
    def parse_post_text(html=None, soup=None):

        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        text_container = soup.find('div', {'class': 'js-tweet-text-container'})
        text = text_container.find('p').text
        if text:
            return text
        else:
            return None

    @staticmethod
    def parse_post_datetime(html=None, soup=None, year=None, month=None, day=None, hour=None, minute=None, second=None):

        months = [0,'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        line = soup.find('span', {'class': 'metadata'}).find('span').text
        day = line[-11:-9]
        month = months.index(line[-8:-5])
        year = line[-4:]

        time = re.search(r'\d{2}\:\d{2}\s[A-Z]{2}', '0'+line).group(0)
        hour = int(time[:2])
        minute = int(time[3:5])
        second = 00
        period = time[-2:]
        if period == 'PM':
            hour += 12
        date = datetime(year=int(year), month=int(month), day=int(day), hour=hour, minute=minute, second=second)
        return date

    @staticmethod
    def parse_post_likes(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        likes = soup.find('li', {'class': 'js-stat-count js-stat-favorites stat-count'}).find('strong').text

        return likes

    @staticmethod
    def parse_post_retweets(html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        retweets = soup.find('li', {'class': 'js-stat-count js-stat-retweets stat-count'}).find('strong').text

        return retweets

    @staticmethod
    def parse_post_comments(html=None, soup=None):

        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        comments_container = soup.find('ol', class_="stream-items js-navigable-stream")
        comments_list = comments_container.find_all('li', {'class': 'ThreadedConversation'})
        comments = [a.find('p', class_="TweetTextSize js-tweet-text tweet-text").text for a in comments_list]
        return comments
