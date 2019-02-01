from Requests.Requester import Requester
from SocialNetworks.Facebook.UserCommentsScraping import UserCommentsScraper
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import selenium
import os
import requests
import time

url="https://www.facebook.com/barackobama/photos/a.10155401589571749/10156387081516749/?type=3&theater"

dataset = [url]

for url in list(dataset):

    driver = webdriver.Chrome('chromedriver.exe')
    dir_path = os.path.dirname(os.path.realpath('chromedriver.exe'))
    chromedriver = os.path.join(dir_path, 'drivers', 'chromedriver_win')
    options = webdriver.ChromeOptions()

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)

    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    driver.get("https://www.facebook.com/")
    driver.find_element_by_css_selector("#email").send_keys("lb.team.user@gmail.com")
    driver.find_element_by_css_selector("#pass").send_keys("lbteam2018")
    driver.find_element_by_css_selector("#u_0_2").click()
    driver.get(url)

    '''actions = ActionChains(driver)
    actions.move_by_offset(372, 79).perform()
    time.sleep(20)
    actions.click().perform()'''

    r = requests.get(url)
    print(r.text)

    #scroll
    while driver.find_element_by_tag_name('div'):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    Divs=driver.find_element_by_tag_name('div').text

    if 'End of Results' in Divs:
        print ('end')
        break
    else:
        continue





    soup = BeautifulSoup(html, 'html.parser')

    comments = UserCommentsScraper.parse_post_comments(html=html, soup=soup)

    date = UserCommentsScraper.parse_comment_datetime(html=html, soup=soup)

    html, text = UserCommentsScraper.parse_comment_text(html=html, soup=soup)

    dataset[url]['post_url'] = url
    dataset[url]['comment_url'] = comment_url
    dataset[url]['datetime'] = datetime
    dataset[url]['author'] = author
    dataset[url]['text'] = text
    dataset[url]['html'] = html
    dataset[url]['translation_en'] = translation_en
