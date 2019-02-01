
from selenium import webdriver

import os
import pickle

from Requests.InfinityScroller import InfinityScroller
from Requests.WebBrowser.SiteRegistration.CookieRegistration import CookieRegistration
from Requests.WebBrowser.WebAction.ActionScroll import ActionScroll

my_page="https://www.facebook.com/profile.php?id=100011689171425&fref=pb&hc_location=friends_tab"


# README!!!!
# goto SeleniumBrowser look line 24 and comment but not commit SeleniumBrowser file



cookies = pickle.load(open("config/cookies.pkl", "rb"))

registration = CookieRegistration(url="https://www.facebook.com/", cookies=cookies)

scroll_action = ActionScroll()
scroller = InfinityScroller(url=my_page, actions=[scroll_action], scroll_pause=2,registration=registration)

html = scroller.scroll()
print(html)
while html is not None:
    html = scroller.scroll()
    print(html)


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
