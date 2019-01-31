from urllib.parse import urljoin
from datetime import datetime
from Scraper.PostsHandler import CommonPostsHandler
from bs4 import BeautifulSoup

class PostsScraper(CommonPostsHandler):
    """
           Inherit CommonUserPostsHandler for www.facebook.com
           """

    # TODO construct
    # def __init__(self,page_class= ['_5pcb' '_4b01'], post_class=['_5pcr userContentWrapper']):

    page_class = ['_5pcb', '_4b01','_2q8l']
    post_class = ['_5pcr userContentWrapper']
    post_like_class = ['_3dlg']
    link_class=['_5pcp', '_5lel', '_2jyu', '_232_']

    @staticmethod
    def parse_post_list(url_root=None, html=None, soup=None):
        if soup is None:
            soup = BeautifulSoup(html, 'html.parser')

        div_links=soup.find_all('div',{'class':PostsScraper.link_class})
        if not div_links:
            return None

        result = dict()
        for links in div_links:
            link = links.find('a')
            url = link['href']

            if 'http' not in url:
                 url = urljoin(url_root, url)

            result[url] = CommonPostsHandler.get_article_row(url=url, title=link.text)

        return result

