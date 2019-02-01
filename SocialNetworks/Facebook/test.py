
from selenium import webdriver

import os
import pickle

from datetime import datetime

from Requests.Requester import Requester
from SocialNetworks.Facebook.UserPostScraping import PostsScraper
from bs4 import BeautifulSoup
from Requests.InfinityScroller import InfinityScroller
from Requests.WebBrowser.SiteRegistration.CookieRegistration import CookieRegistration
from Requests.WebBrowser.WebAction.ActionScroll import ActionScroll

url="https://www.facebook.com/profile.php?id=100011689171425&fref=pb&hc_location=friends_tab"


# README!!!!
# goto SeleniumBrowser look line 24 and comment but not commit SeleniumBrowser file



cookies = pickle.load(open("config/cookies.pkl", "rb"))

registration = CookieRegistration(url="https://www.facebook.com/", cookies=cookies)

scroll_action = ActionScroll()
scroller = InfinityScroller(url=url, actions=[scroll_action], scroll_pause=2,registration=registration)

requester = Requester(url=url, retries=5, sleep_time=3)
response = requester.make_get_request()
html = scroller.scroll()


while html is not None:
    html = scroller.scroll()
    print(html)

dataset = PostsScraper.parse_articles_list(url_root=requester.get_url_root(),html=html)


# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

#push!!!!

#scroll
# while driver.find_element_by_tag_name('div'):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     Divs=driver.find_element_by_tag_name('div').text
#
#
#     if 'End of Results' in Divs:
#         print ('end')
#         break
#     else:
#         continue
# result=list()
dataset.encode('utf-8')
print(dataset)