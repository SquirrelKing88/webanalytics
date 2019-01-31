import os
import nltk
import sys

class LanguageHandler:

    languages = {
        'spanish': 'es',
        'italian': 'it',
        'hindi': 'hi',
        'mongolian': 'mn',
        'ukrainian': 'uk',
        'french': 'fr',
        'indonesian': 'id',
        'english': 'en',
        'russian': 'ru',
        'icelandic': 'is',
        'greek': 'el',
        'polish': 'pl',
        'german': 'de',
        'czech': 'cs'
    }

    @staticmethod
    def get_language_abbreviation(language):
        """
        Get language abbrevation by its name

        :param language: string language name
        :return: str language abbrevation

        :examples:
            abbevation = LanuageHandler.get_language_abbreviation('Ukrainian')
        """


        return LanguageHandler.languages[language.lower()]

    @staticmethod
    def get_tokenizer(language_abbreviation):
        """

        :param language_abbreviation: language
        :return: nltk tokenizer based on pickle file for choosen language
        """
        language  = list(LanguageHandler.languages.keys())[list(LanguageHandler.languages.values()).index(language_abbreviation)]

        pickle_file = os.path.join(LanguageHandler.get_punctuation_model_path(), "{}.pickle".format(language.lower()))

        return nltk.data.load('file:'+pickle_file)

    @staticmethod
    def get_punctuation_model_path():
        dir_path = os.path.dirname(os.path.realpath(__file__))

        return os.path.join(dir_path, 'Models', 'Punctuation', 'tokenizers', 'punkt')