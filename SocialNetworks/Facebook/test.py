from Facebook.UserPostScraping import PostsScraper
from Requests.Requester import Requester
from threading import Thread
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from Scraper.Writters.FileWritter import FileWriter
from selenium.webdriver.chrome.options import Options


my_page="https://www.facebook.com/profile.php?id=100011689171425&fref=pb&hc_location=friends_tab"

driver = webdriver.Chrome('chromedriver.exe')
dir_path = os.path.dirname(os.path.realpath('chromedriver.exe'))
chromedriver = os.path.join(dir_path, 'drivers', 'chromedriver_win')
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x400')
driver.get("https://www.facebook.com/")
driver.find_element_by_css_selector("#email").send_keys("lb.team.user@gmail.com")
driver.find_element_by_css_selector("#pass").send_keys("lbteam2018")
driver.find_element_by_css_selector("#u_0_2").click()
driver.get(my_page)

#push!!!!

#scroll
while driver.find_element_by_tag_name('div'):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    Divs=driver.find_element_by_tag_name('div').text


    if 'End of Results' in Divs:
        print ('end')
        break
    else:
        continue
result=list()
