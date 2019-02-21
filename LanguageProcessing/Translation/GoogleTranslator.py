import json
import time
import re

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


    def get_translation(self, original_text, max_symbols_count=2500):
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

        original_text = original_text.replace('\n',' ')
        sentences = original_text.split('\n')

        formated_text=[]

        words = 0
        temp = ''
        for sentence in sentences:
            words += len(sentence)
            temp+=sentence
            if words > 2500:
                if words >4900:
                    temp = ''
                    words = 0
                    new_sentences=sentence.split('.')
                    for new_sentence in new_sentences:
                        new_sentence+='.'
                        words += len(new_sentence)
                        temp += new_sentence
                        if words > 2500:
                            #print(words)
                            formated_text.append(temp)
                            words = 0
                            temp = ''
                #print(words)
                formated_text.append(temp)
                words = 0
                temp = ''

        if temp:
            formated_text.append(temp)

        #print(len(formated_text))

        result = []

        original_language = None

        for text in formated_text:
            #try:
            text=text.replace('\n','')
            self.__browser.set_element_text('source', json.dumps(text))
            #self.__browser.push_element(parent_tag='div', parent_class='go-button', element_tag='div',element_class='jfk-button-img')

            time.sleep(self.__timeout)

            html = self.__browser.get_html()
            soup = BeautifulSoup(html, 'html.parser')
            translation_html = soup.find('span', {'class': ['tlid-translation', 'translation']})

            translation = translation_html.text

            if not original_language:
                language = soup.find('div', {'role': 'button', 'value':'auto'}).text
                #print(language)
                language = re.split(' ',language)[2]
                language = language.replace('\n', '')
                self.__browser.set_element_text('source', json.dumps(language))
                # self.__browser.push_element(parent_tag='div', parent_class='go-button', element_tag='div',element_class='jfk-button-img')

                time.sleep(self.__timeout)

                html = self.__browser.get_html()
                soup = BeautifulSoup(html, 'html.parser')
                original_language = soup.find('span', {'class': ['tlid-translation', 'translation']}).text.lower()


            result.append(translation)
            #print(translation)

            #except Exception:
            #    translation = None

        #print(result)

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

        translation = ''
        for text in result:
            translation += text

        return {
            'original_language': original_language,
            'original_text': original_text,
            'translation_language': self.__destination_language,
            'translation': translation
        }

