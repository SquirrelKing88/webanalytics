from googletrans import Translator
from threading import Thread
import nltk.data

from LanguageProcessing.LanguageHandler import LanuageHandler


class GoogleTranslator:

    def __init__(self):

        self.__translator = Translator(service_urls=[
                                                      'translate.google.com'
                                                    ])

    def translate_batch(self, batch, text_batch, destination_language, result):
        result[batch] = self.__translator.translate(" ".join(text_batch), dest=destination_language)

    def get_translation(self, original_text, destination_language='en', max_sentence_count=10):
        """
        :param original_text: text to translate
        :param destination_language: language abbreviation
        :param max_sentence_count: text will be devided on parts with max_sentence_count size
        :return: dictionary{'original_language': , 'original_text': , 'translation_language': , 'translation': }
        """

        if not original_text:
            return {
            'original_language': None,
            'original_text': original_text,
            'translation_language': destination_language,
            'translation': None
        }


        # TODO if not detected
        detected = self.__translator.detect(original_text[:100])
        original_language = detected.lang


        tokenizer = LanuageHandler.get_tokenizer(original_language)
        sentences = tokenizer.tokenize(original_text.strip())

        sentenses_count = len(sentences)

        batch_count = sentenses_count//max_sentence_count
        if sentenses_count%max_sentence_count:
            batch_count+=1

        translation=""

        threads=[]

        result=dict()

        for batch in range(batch_count):
            text_batch = sentences[max_sentence_count*batch:(batch+1)*max_sentence_count]
            threads.append(Thread(target=self.translate_batch,args=(batch, text_batch, destination_language, result)))
            result[batch]=""
            threads[batch].start()

        print(result)

        for thread in threads:
            thread.join()

        for element in result:
            translation+=result[element].text

        return {
            'original_language': original_language,
            'original_text': original_text,
            'translation_language': destination_language,
            'translation': translation
        }
