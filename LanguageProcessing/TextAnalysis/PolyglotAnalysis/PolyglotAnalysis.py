import os

import polyglot
from polyglot.text import Text
from polyglot.downloader import downloader
from polyglot.detect import Detector







class PolyglotAnalysis:

  def __init__(self, text):

    self.__text = text

    detector = Detector(text)
    self.__language_abbreviation = detector.language.code


    model_path = os.path.join(polyglot.polyglot_path, 'ner2', self.__language_abbreviation)

    if not os.path.isdir(model_path):

      # upload model
      # TODO other models
      downloader.download("ner2.{0}".format(self.__language_abbreviation))
      downloader.download("embeddings2.{0}".format(self.__language_abbreviation))


    #Entity Location Persons

    text = Text(text)


    for sentence in text.sentences:
      for entity in sentence.entities:
        print(entity.tag, entity)



  def get_persons(self):
    """

    Get all person mentioned in text
    For name translation user transliteration but not translation
    https://polyglot.readthedocs.io/en/latest/Transliteration.html


    NO DUBLICATES

    :return: dictionary{
                        person: ['Ігор Терещенко',...],
                        person_en:['Igor Tereshchenko',...]
                        }

    """
    return None



  def get_locations(self):
    """

    Get all location mentioned in text

    For name translation GoogleTranslator


    NO DUBLICATES


    :return: dictionary{
                          location: ['Україна','Польша',...],
                          location_en:['Ukraine','Poland',...],
                          coordinates: [
                                          {
                                            latitude: ...,
                                            longitude: ...
                                          },
                                          {
                                            latitude: ...,
                                            longitude: ...
                                          },
                                          ...
                                        ]

                        }

    """
    return None


  def get_organizations(self):

    """

    Get all organization mentioned in text

    NO DUBLICATES

    :return: dictionary{
                          organizations: ['КПІ','Samsung',...],
                          organizations_en:['KPI','Samsung',...],

                        }
    """

    return None


