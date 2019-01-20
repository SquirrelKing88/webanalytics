import time
from random import randint
import urllib3


from Requests.RequesterException import RequesterException


# https://urllib3.readthedocs.io/en/latest/user-guide.html

class Requester:

    def __init__(self, url, retries=4, timeout=30, sleep_time=10):
        """
        :param url: server url
        :param retries: you can control the retries using the retries parameter to request
        :param timeout: Timeouts allow you to control how long requests are allowed to run before being aborted
        :param sleep_time: Average waiting time before next retry
        """

        self.__url = url
        self.__retries = retries
        self.__timeout = timeout
        self.__sleep_time = sleep_time

        self.__http = urllib3.PoolManager()

    def get_request(self, parameters=None):
        """
        :param parameters: dictionary {key:value}
        :return: http response
        """

        response = None
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

        for counter in range(self.__retries):
            try:

                response = self.__http.request('GET',self.__url, headers = headers, fields = parameters,timeout=self.__timeout)

                # Success
                if response.status==200:
                    break

            except Exception as e:

                if counter == self.__retries - 1:
                    raise RequesterException("Retries {0} overlimit".format(self.__retries), self.__url)
                else:
                    # wait a random amount of time between requests to avoid bot detection
                    random_delta = randint(1, self.__sleep_time)
                    time.sleep(self.__sleep_time * (counter - 1)+random_delta)

        return response