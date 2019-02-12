import os

import polyglot
from polyglot.text import Text
from polyglot.downloader import downloader
from polyglot.detect import Detector
from LanguageProcessing.LanguageHandler import LanguageHandler






class PolyglotAnalysis:

  def __init__(self, text):

    self.__text = text

    detector = Detector(text)
    self.__language_abbreviation = detector.language.code


    model_path = os.path.join(polyglot.polyglot_path, 'ner2', self.__language_abbreviation)

    if not os.path.isdir(model_path):

      # upload model
      for value in LanguageHandler.languages.values():
        downloader.download("ner2.{0}".format(value))
        downloader.download("embeddings2.{0}".format(value))


    #Entity Location Persons

    text = Text(text)


    for sentence in text.sentences:
      for entity in sentence.entities:
        print(entity.tag, entity)






