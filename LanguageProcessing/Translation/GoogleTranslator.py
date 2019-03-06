import json
import time

from bs4 import BeautifulSoup
from LanguageProcessing.LanguageHandler import LanguageHandler
from Requests.WebBrowser.SeleniumBrowser import SeleniumBrowser

from polyglot.detect import Detector

class GoogleTranslator:

    def __init__(self, destination_language='en', timeout=2):

        self.__browser = SeleniumBrowser()
        self.__destination_language = destination_language
        self.__timeout = timeout
        self.__browser.make_get_request('https://translate.google.com.ua/?tl={0}'.format(destination_language))


    def get_translation(self, original_text, max_symbols_count=2500, original_language=None):
        """
        :param original_text: text to translate
        :param destination_language: language abbreviation
        :param max_sentence_count: text will be divided on parts with max_sentence_count size
        :return: dictionary{'original_language': , 'original_text': , 'translation_language': , 'translation': }
        """

        result = {
                        'original_language': None,
                        'original_text': original_text,
                        'translation_language': self.__destination_language,
                        'translation': None
                    }
        if not original_text:
            return result

        # Language detection
        if not original_language:
            detector = Detector(original_text[:100])
            result['original_language'] = detector.language.code
        else:
            result['original_language'] = original_language


        # Input data prepare
        if len(original_text) > max_symbols_count:
            tokenizer = LanguageHandler.get_tokenizer(result['original_language'])
            sentences = tokenizer.tokenize(original_text.strip())
        else:
            sentences = [original_text]

        result['translation'] = ''
        while sentences:
            block = ''

            # TODO speed up by deleting pop
            while len(block) < max_symbols_count and sentences:
                block += sentences.pop(0)+' '

            block_translation = self.__get_translation(block,result['original_language'])

            result['translation'] += block_translation['translation']

        return result


    def __get_translation(self, original_text, original_language):
        """
        :param original_text: text to translate
        :return: dictionary{'original_language': , 'original_text': , 'translation_language': , 'translation': }
        """

        if not original_text:
            return {
                        'original_language': None,
                        'original_text': original_text,
                        'translation_language': self.__destination_language,
                        'translation': None
                    }

        self.__browser.set_element_text('source', json.dumps(' '))

        # wait until clean input div
        while True:
            html = self.__browser.get_html()
            soup = BeautifulSoup(html, 'html.parser')
            translation_html = soup.find('span', {'class': ['tlid-translation', 'translation']})

            if not translation_html:
                break
            # type space to show delete button
            self.__browser.set_element_text('source', json.dumps(' '))
            # click on delete button
            self.__browser.push_element(parent_tag='div', parent_class='clear-wrap', element_tag='div', element_class='jfk-button-img')

        translation = ''
        begin = time.monotonic()
        end = time.monotonic()
        self.__browser.set_element_text('source', json.dumps(original_text))

        while not translation and (end-begin) <= self.__timeout:

            end = time.monotonic()
            html = self.__browser.get_html()
            soup = BeautifulSoup(html, 'html.parser')
            translation_html = soup.find('span', {'class': ['tlid-translation', 'translation']})
            if translation_html:
                translation = translation_html.text

        # clear browser
        self.__browser.set_element_text('source', json.dumps(' '))

        return {
                    'original_language': original_language,
                    'original_text': original_text,
                    'translation_language': self.__destination_language,
                    'translation': translation
                }