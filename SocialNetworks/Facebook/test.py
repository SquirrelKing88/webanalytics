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

    soup=BeautifulSoup(html)

    div_links=soup.find_all('div',{'class':link_class})
    div_author=soup.find_all(('h5',{'class':author_class}))
    div_post = soup.find_all('div', {'class':post_class})




    for authors in div_author:
        author = authors.find('a')
        name = author['href']

    for posts in div_post:
        text_html=posts.find('div')
        text=str(posts.find('p'))
        cleaned_text1=text.replace('<p>','')
        cleaned_text2 = cleaned_text1.replace('</p>', '')
        cleaned_text = cleaned_text2.replace('<br/>', '')
        translator = GoogleTranslator()
        result1 = translator.get_translation(cleaned_text)
        translation_en=result1['translation']

    for links in div_links:
        link = links.find('a')
        url = link['href']
        data=links.find('abbr')
        datatime=data['title']

        result=dict()


        if url not in result:
            result[url]={
                         'author':name,
                         'data':datatime,
                         'text':cleaned_text,
                         'translation_en':translation_en}



        print(result)


