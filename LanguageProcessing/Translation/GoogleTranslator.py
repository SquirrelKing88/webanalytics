import json
import time
import re

from bs4 import BeautifulSoup
from LanguageProcessing.LanguageHandler import LanguageHandler
from Requests.WebBrowser.SeleniumBrowser import SeleniumBrowser


class GoogleTranslator:

    def __init__(self, destination_language='en', timeout=2):

        self.__browser = SeleniumBrowser()
        self.__destination_language = destination_language
        self.__timeout = timeout
        self.__browser.make_get_request('https://translate.google.com.ua/?tl={0}'.format(destination_language))


    def get_translation(self, original_text, max_symbols_count=2500):
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


        # TODO detected language
        paragraph = original_text[:100]
        original_language =''
        result['original_language'] = original_language


        if len(original_text) > max_symbols_count:
            tokenizer = LanguageHandler.get_tokenizer(original_language)
            sentences = tokenizer.tokenize(original_text.strip())
        else:
            sentences = [original_text]

        while sentences:
            block = ''
            while len(block) < max_symbols_count:
                block += sentences.pop()

            block_translation = self.__get_translation(block)

            if not (result['translation']):
                result['translation'] = block_translation['translation']
            else:
                result['translation'] += block_translation['translation']

        return result


    def __get_translation(self, original_text):
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

        translation = ''
        counter = 1
        while not translation and counter <= self.__timeout:

            self.__browser.set_element_text('source', json.dumps(original_text))
            time.sleep(1)

            html = self.__browser.get_html()
            soup = BeautifulSoup(html, 'html.parser')
            translation_html = soup.find('span', {'class': ['tlid-translation', 'translation']})
            translation = translation_html.text

            counter += 1

        # TODO check for arabic language
        language = soup.find('div', {'role': 'button', 'value' : 'auto'}).text
        language = re.split(' ', language)[2]
        original_language = language.replace('\n', '')

        # TODO if not detected
        if not len(translation):
            translation = None
            original_language = None

        return {
                    'original_language': original_language,
                    'original_text': original_text,
                    'translation_language': self.__destination_language,
                    'translation': translation
                }