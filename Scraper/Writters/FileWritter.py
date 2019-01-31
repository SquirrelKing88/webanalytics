from Scraper.Writters.CommonWriter import CommonWriter
import json
import copy


class FileWritter(CommonWriter):
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

                data = copy.copy(dictionary[url])

                #Format datatime
                data['date'] = data['date'].strftime("%d/%m/%Y %H:%M:%S")

                json.dump(data, file)

                file.write("\n")

            file.flush()

