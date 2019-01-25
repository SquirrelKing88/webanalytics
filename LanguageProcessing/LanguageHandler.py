import os
import nltk

class LanuageHandler:

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
        'german': 'de'
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


        return LanuageHandler.languages[language.lower()]

    @staticmethod
    def get_tokenizer(language_abbreviation):
        """

        :param language_abbreviation: language
        :return: nltk tokenizer based on pickle file for choosen language
        """
        language  = list(LanuageHandler.languages.keys())[list(LanuageHandler.languages.values()).index(language_abbreviation)]

        dir_path = os.path.dirname(os.path.realpath(__file__))
        pickle_file = os.path.join(dir_path,'SentenceSplitter','punkt',language.lower()+".pickle")

        return nltk.data.load('file:'+pickle_file)

