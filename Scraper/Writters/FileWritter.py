import json
import copy

from Scraper.Writters.CommonWriter import CommonWriter


class FileWriter(CommonWriter):
    """
    Write dictionary to file
    """

    def __init__(self, filepath):
        """

        :param filepath: result path
        """
        self.filepath = filepath


    def write(self, dictionary):
        """
        Write any dictionary to file

        :param dictionary: any dictionary
        :return: None.
        """
        with open(self.filepath, mode='a+', encoding="utf-8") as file:
            for url in dictionary:
                # TODO delete shallow copy
                data = copy.copy(dictionary[url])

                data['date'] = data['date'].strftime("%d/%m/%Y %H:%M:%S")

                json.dump(data, file)

                file.write("\n")

            file.flush()
