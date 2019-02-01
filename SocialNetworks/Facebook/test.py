from selenium import webdriver
from bs4 import BeautifulSoup
import os
import pickle
import re
from Requests.InfinityScroller import InfinityScroller
from Requests.WebBrowser.SiteRegistration.CookieRegistration import CookieRegistration
from Requests.WebBrowser.WebAction.ActionScroll import ActionScroll
from LanguageProcessing.Translation.GoogleTranslator import GoogleTranslator

my_page="https://www.facebook.com/profile.php?id=100011689171425&fref=pb&hc_location=friends_tab"


# README!!!!
# goto SeleniumBrowser look line 24 and comment but not commit SeleniumBrowser file



cookies = pickle.load(open("config/cookies.pkl", "rb"))

registration = CookieRegistration(url="https://www.facebook.com/", cookies=cookies)

scroll_action = ActionScroll()
scroller = InfinityScroller(url=my_page, actions=[scroll_action], scroll_pause=2,registration=registration)

html = scroller.scroll()

while html is not None:
    html = scroller.scroll()

    link_class=['_5pcp', '_5lel', '_2jyu', '_232_']
    author_class=['_14f3', '_14f5', '_5pbw', '_5vra']
    post_class=['5pcb', '_4b0l', '_2q8l']

    soup=BeautifulSoup(html,features="html.parser")

    div_links=soup.find_all('div',{'class':link_class})
    div_author=soup.find_all(('h5',{'class':author_class}))
    div_post = soup.find_all('div', {'class':post_class})




    for authors in div_author:
        author = authors.find('a')
        name = author['href']

    for posts in div_post:


        # search for link
        # if not link skip



        text_html=posts.find('div', {'class':['userContent']})

        link_div = posts.find('div', {'class': link_class})


        # link = link_div.find('a')
        # try:
        #     url = link['href']
        #     data = link.find('abbr')
        #     datatime = data['title']
        #
        #     print(url,ent=' ')
        # except Exception as e:
        #     # print('----------------------------------------------------------------------------------',link)
        #     pass

        # TODO delete spaces or \n\n\n\n\n\n
        print(text_html.get_text().strip())
        # translator = GoogleTranslator()
        # translation = translator.get_translation(text)
        # translation_en = None#translation['translation']
        #


    # for links in div_links:
    #     link = links.find('a')
    #     url = link['href']
    #     data=links.find('abbr')
    #     datatime=data['title']
    #
    #     result=dict()
    #
    #
    #     if url not in result:
    #         result[url]={
    #                      'author':name,
    #                      'data':datatime,
    #                      'text':cleaned_text,
    #                      'translation_en':translation_en}
    #
    #
    #
    #     print(result)


