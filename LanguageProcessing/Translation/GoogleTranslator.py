import json
import time

from bs4 import BeautifulSoup
from googletrans import Translator
from LanguageProcessing.LanguageHandler import LanguageHandler
from Requests.WebBrowser.SeleniumBrowser import SeleniumBrowser


class GoogleTranslator:

    def __init__(self, destination_language='en', timeout=2):

        self.__browser = SeleniumBrowser()
        self.__destination_language = destination_language
        self.__timeout = timeout
        self.__browser.make_get_request('https://translate.google.com.ua/?tl={0}'.format(destination_language))


    def get_translation(self, original_text, max_sentence_count=10):
        """
        :param original_text: text to translate
        :param destination_language: language abbreviation
        :param max_sentence_count: text will be divided on parts with max_sentence_count size
        :return: dictionary{'original_language': , 'original_text': , 'translation_language': , 'translation': }
        """

        if not original_text:
            return {
                        'original_language': None,
                        'original_text': original_text,
                        'translation_language': self.__destination_language,
                        'translation': None
                    }

        try:
            self.__browser.set_element_text('source', json.dumps(original_text))
            self.__browser.push_element(parent_tag='div', parent_class='go-button', element_tag='div',
                                 element_class='jfk-button-img')

            time.sleep(self.__timeout)

            html = self.__browser.get_html()
            soup = BeautifulSoup(html, 'html.parser')
            translation_html = soup.find('span', {'class': ['tlid-translation', 'translation']})

            translation = translation_html.text

        except Exception:
            translation = None

        # # TODO if not detected
        # detected = self.__translator.detect(original_text[:100])
        # original_language = detected.lang
        #
        # tokenizer = LanguageHandler.get_tokenizer(original_language)
        # sentences = tokenizer.tokenize(original_text.strip())
        #
        # sentenses_count = len(sentences)
        #
        # batch_count = sentenses_count//max_sentence_count
        # if sentenses_count%max_sentence_count:
        #     batch_count+=1
        #
        # translation=""
        # for batch in range(batch_count):
        #
        #     text_batch = sentences[max_sentence_count*batch:(batch+1)*max_sentence_count]
        #     translation_result = self.__translator.translate(" ".join(text_batch), dest=destination_language)
        #     translation += translation_result.text



        return {
            'original_language': '#TODO',
            'original_text': original_text,
            'translation_language': self.__destination_language,
            'translation': translation
        }