from googletrans import Translator

class GoogleTranslator:

    def __init__(self):

        self.__translator = Translator(service_urls=[
                                                      'translate.google.com'
                                                    ])

    def get_translation(self, original_text, destination_language='en'):
        """
        :param original_text: text to translate
        :param destination_language: language abbreviation
        :return: dictionary{'original_language': , 'original_text': , 'translation_language': , 'translation': }
        """

        translation = self.__translator.translate(original_text, dest=destination_language)
        return {
            'original_language': translation.src,
            'original_text': original_text,
            'translation_language': destination_language,
            'translation': translation.text
        }
