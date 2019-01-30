import pickle

import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk import word_tokenize
from nltk import data as dt
import wikipedia
from LanguageProcessing.LanguageHandler import LanguageHandler

dt.path.append(LanguageHandler.get_punctuation_model_path())





class SentenceSplitterTrainer:


    def __init__(self, language, articles_count):
        """

        :param language: language to train
        :param articles_count: count of items to train
        """
        self.__language = language
        self.__articles_count = articles_count


    def train(self):
        """
        Train new language

        :return: trained file in tokenizers folder
        """
        text = self.__collect_wiki_corpus(self.__language, self.__articles_count)
        self.__train_sentence_splitter(self.__language,text)


    def __collect_wiki_corpus(self,language, articles_count):
        """
        Download <articles_count> random wikipedia articles in language <language>

        :param language - language name
        :param articles_count - count of items

        :return scrapped text
        """


        abbevation = LanguageHandler.get_language_abbreviation(language)


        wikipedia.set_lang(abbevation)
        random_pages = wikipedia.random(articles_count)

        text = ""
        counter=0
        for random in random_pages:
            try:
                page = wikipedia.page(random)

                p_tokenized = ' '.join(word_tokenize(page.content))

                text += p_tokenized + "\n"

                counter+=1
                print("Article #{0} scraped".format(counter))

            except wikipedia.exceptions.DisambiguationError as e:
                continue

        return text


    def __train_sentence_splitter(self,language,text):
        """
        Train an NLTK tokenizers tokenizer for sentence splitting.
        http://www.nltk.org

        :param language name
        :param text some text to train

        :return None. Write pickle file
        """

        # Train tokenizer
        # TODO create better implementation
        # TODO python 2 and python 3 version
        tokenizer = PunktSentenceTokenizer()
        tokenizer.train(text)

        # Dump pickled tokenizer
        pickle_file = "../tokenizers/%s.pickle" % (language.lower())
        out = open(pickle_file, "wb")
        pickle.dump(tokenizer, out)
        out.close()


