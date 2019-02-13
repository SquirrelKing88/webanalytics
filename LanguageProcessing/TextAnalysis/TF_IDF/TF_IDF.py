from sklearn.feature_extraction.text import TfidfVectorizer

from LanguageProcessing.Translation.GoogleTranslator import GoogleTranslator


class TF_IDF:

    def __init__(self, articles):
        """

        :param articles: list of text documents
        """


        self.__articles = articles
        vectorizer = TfidfVectorizer()

        # tokenize and build vocab
        vectorizer.fit(articles)

        print(vectorizer.vocabulary_)
        print(vectorizer.idf_)

        translator = GoogleTranslator()

        self.__tf_idf_result = {
                                word: {
                                        'tf_idf':value,
                                        'translation_en': translator.get_translation(word)['translation']
                                      } for (word, value) in zip(vectorizer.vocabulary_, vectorizer.idf_)
                                }



    def get_tf_idf(self, max_count):
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