from sklearn.feature_extraction.text import TfidfVectorizer

from LanguageProcessing.Translation.GoogleTranslator import GoogleTranslator


class TF_IDF:

    def __init__(self, articles, language):
        """

        :param articles: list of text documents on same language
        """

        self.__articles = articles
        self.__language = language
        vectorizer = TfidfVectorizer()
        vectorizer.fit(articles)

        translator = GoogleTranslator()

        self.__tf_idf_result = {
                                word: {
                                        'tf_idf':value,
                                        'translation_en': translator.get_translation(original_text=word, original_language=self.__language)['translation']
                                      } for (word, value) in zip(vectorizer.vocabulary_, vectorizer.idf_)
                                }



    def get_tf_idf(self, max_count=None):
        """

        Return max_count of words with tf_idf characteristics order by tf_idf

        :return: dictionary{
                            'word':{
                                        'tf_idf':
                                        'translation_en': translation
                                    },
                                    ...
                }
        """

        # TODO use max_count
        return self.__tf_idf_result