import os
import time
from random import randint
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from urllib3 import ProxyManager, make_headers, PoolManager, disable_warnings
from selenium import webdriver

from Requests.SiteRegistration import IRegistration


class InfinityRequester:

    def __init__(self, url,parent_element, parent_element_classes, child_element, child_element_classes,
                 url_classes=None, registration=None):
        """

           :param url: resourse
           :param parent_element: tag name
           :param parent_element_classes: list of classes
           :param child_element: tag name
           :param child_element_classes: list of classes
           :param registration: IRegistration instance
       """



        dir_path = os.path.dirname(os.path.realpath(__file__))
        chromedriver = os.path.join(dir_path, 'drivers', 'chromedriver_win')

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1200x400')  # optional
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)

        self.__browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

        if registration:
            registration.register(self.__browser)

        self.__url = url

        self.__parent_element=parent_element
        self.__parent_element_classes=parent_element_classes
        self.__child_element=child_element
        self.__child_element_classes=child_element_classes
        self.__url_classes = url_classes




    def __get_elements(self, html_content):
        """

        :param html_content: html of load page
        :return: dictionary {'url': html_child_content,...}
        """

        result = dict()

        soup = BeautifulSoup(html_content, 'html.parser')

        parent = soup.find(self.__parent_element, {'class': self.__parent_element_classes})

        childs = parent.find_all(self.__child_element, {'class': self.__child_element_classes})

        # url extraction
        for child in childs:
            url = child.find('a', {'class': self.__url_classes})

            result[url['href']] = child

        return result


    def make_get_request(self):
        """

        :return: dictionary {'url': html_child_content,...}
        """
        self.__browser.get(self.__url)
        html_content = self.__browser.page_source

        elements = self.__get_elements(html_content)

        SCROLL_PAUSE_TIME = 1

        last_height = self.__browser.execute_script("return document.body.scrollHeight")
        new_height = 0

        while new_height != last_height:
            last_height = new_height

            # Scroll down to bottom
            self.__browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # upload data
            html_content = self.__browser.page_source

            elements.update(
                                self.__get_elements(html_content)
                            )
            # Calculate new scroll height and compare with last scroll height
            new_height = self.__browser.execute_script("return document.body.scrollHeight")

            # TODO delete all prints
            print('Scrolling...')


        return elements