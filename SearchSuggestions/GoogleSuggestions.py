import json
from Requests.Requester import Requester
from Requests.RequesterException import RequesterException

class GoogleSuggestions:

    def __init__(self):
        """
        create requester with Google API url: http://suggestqueries.google.com/complete/search
        """
        self.__requester = Requester(url="http://suggestqueries.google.com/complete/search")

    def get_suggestions(self, words):
        """
        :param query: list of words
        :return: list of suggestions

        :raise: RequesterException
        """
        parameters ={"client":"chrome", "q":" ".join(words)}

        response = self.__requester.get_request(parameters=parameters)

        return json.loads(response.data.decode('utf-8'))[1]

