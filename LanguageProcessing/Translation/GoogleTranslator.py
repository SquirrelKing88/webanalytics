from googletrans import Translator
from LanguageProcessing.LanguageHandler import LanguageHandler


class GoogleTranslator:

    def __init__(self):

        self.__translator = Translator(service_urls=[
                                                      'translate.google.com'
                                                    ])

    def get_translation(self, original_text, destination_language='en', max_sentence_count=10):
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
                        'translation_language': destination_language,
                        'translation': None
                    }


        # TODO if not detected
        detected = self.__translator.detect(original_text[:100])
        original_language = detected.lang

        tokenizer = LanguageHandler.get_tokenizer(original_language)
        sentences = tokenizer.tokenize(original_text.strip())

        sentenses_count = len(sentences)

        batch_count = sentenses_count//max_sentence_count
        if sentenses_count%max_sentence_count:
            batch_count+=1

        translation=""
        for batch in range(batch_count):

            text_batch = sentences[max_sentence_count*batch:(batch+1)*max_sentence_count]
            translation_result = self.__translator.translate(" ".join(text_batch), dest=destination_language)
            translation += translation_result.text



        return {
            'original_language': original_language,
            'original_text': original_text,
            'translation_language': destination_language,
            'translation': translation
        }

