from Country.CountryHandler import CountryHandler
from config import GOOGLE_API_KEY
import googlemaps

class GeoGoogle:

    def __init__(self):
        """
            Google client initialization with api key from config package
        """

        self.__gmaps = googlemaps.Client(key=GOOGLE_API_KEY)
        self.__country_handler = CountryHandler()


    def get_country_coordinates(self, country_name):
        """

        :param country_name: name of country
        :return: dictionary  {'lat': 48.379433, 'lng': 31.1655799}
        :raises: Exception if country name not found
        """

        if not self.__country_handler.is_country_name(country_name):
            raise Exception("{} is not country name".format(country_name))

        result = self.__gmaps.find_place(country_name, 'textquery')

        # TODO check response status
        if (result["status"]!=200):
            raise Exception("Response status = {}".format(result["status"]))
        # TODO check data availability

        candidate = result['candidates'][0]['place_id']
        information = self.__gmaps.place(candidate)
        return information['result']['geometry']['location']