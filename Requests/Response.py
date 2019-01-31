class Response:

    def __init__(self, status, data):
        self.__status = status
        self.__data = data

    def get_data(self):
        return self.__data

    def get_status(self):
        return self.__status