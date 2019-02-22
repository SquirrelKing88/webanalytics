import json
from polyglot.text import Text
from polyglot.detect import Detector
from LanguageProcessing.Translation.GoogleTranslator import GoogleTranslator
from Requests.Requester import Requester


class PolyglotAnalysis:

    def __init__(self, text):

        self.__text = text

        detector = Detector(text)
        self.__language_abbreviation = detector.language.code

        self.__polyglot_text = Text(text, hint_language_code=self.__language_abbreviation)



        self.__persons = dict()
        self.__locations = dict()
        self.__organizations = dict()


        for sentence in self.__polyglot_text.sentences:
            for entity in sentence.entities:
                if entity.tag == 'I-PER':
                  self.__persons.update(self.__get_person(entity))

                elif entity.tag == 'I-LOC':
                  self.__locations.update(self.__get_location(entity))

                elif entity.tag == 'I-ORG':
                  self.__organizations.update(self.__get_organization(entity))

                print(entity.tag, entity)


    # ============================================================================

    def __get_person_id(self, person):
        # TODO get person id by person data
        return repr(person)

    def __get_person(self, entity):
        """

    Get person mentioned in text
    For name translation user transliteration but not translation
    https://polyglot.readthedocs.io/en/latest/Transliteration.html

    :return: dictionary{
                        # found in database or generated a new one
                        person_id:{
                                    # set of words
                                    person: {'Ігор', 'Терещенко'}
                                    person_en: {'Igor', 'Tereshchenko'}
                                  }
                        }

    """

        person = set()
        person_en = set()

        for el in entity:
            person.add(el.lower())
            person_en.add(Text(el, hint_language_code=self.__language_abbreviation).transliterate('en')[0])

        person_id = self.__get_person_id(person)

        return {person_id:
            {
                'person': person,
                'person_en': person_en
            }
        }

    # ============================================================================

    def __get_location_id(self, location):
      # TODO get location id from DB
      return repr(location)

    def __get_location(self, entity):
        """

    Get location mentioned in text

    :return: dictionary = {
                        # found in database or generated a new one
                        location_id:
                                      {
                                        location: {'Україна'}
                                        location_en:{'Ukraine'}
                                        coordinates:  {
                                                          latitude: ...,
                                                          longitude: ...
                                                        }
                                      }
                        }

    """

        location = set()
        location_en = set()

        for el in entity:
          location.add(el.lower())

          # TODO transliterate VS Translation
          location_en.add(Text(el, hint_language_code=self.__language_abbreviation).transliterate('en')[0])

        location_name = ' '.join(entity)

        requester = Requester(url='https://nominatim.openstreetmap.org/search')

        # TODO location_name which language better
        response = requester.make_get_request(parameters={'q': location_name, 'format': 'json', 'limit': 1}).get_data()
        response = response.decode('utf-8')
        response = json.loads(response)[0]

        location_id = self.__get_location_id(location)
        return {
                location_id: {
                                'location': location,
                                'location_en': location_en,
                                'coordinates': {
                                                'latitude': response['lat'],
                                                'longitude': response['lon']
                                               }
                              }
              }


    # ============================================================================


    def __get_organization_id(self,organization):
      # TODO get location id from DB
      return repr(organization)

    def __get_organization(self, entity):
      """

    Get organization mentioned in text

    :return: dictionary = {
                        # found in database or generated a new one
                        organization_id:
                                      {
                                        organization: {'КПІ'}
                                        organization_en:{'KPI'}
                                      }
                        }

    """

      organization = set()
      organization_en = set()

      for el in entity:
        organization.add(el.lower())

        # TODO transliterate VS Translation
        organization_en.add(Text(el, hint_language_code=self.__language_abbreviation).transliterate('en')[0])

        organization_id = self.__get_organization_id(organization)
      return {
                organization_id: {
                                    'organization': organization,
                                    'organization_en': organization_en
                                  }
              }

    def get_persons(self):
        return self.__persons

    def get_organizations(self):
        return self.__organizations

    def get_locations(self):
        return self.__locations
