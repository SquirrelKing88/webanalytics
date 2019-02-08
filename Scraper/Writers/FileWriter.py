import json
import copy

from Scraper.Writers.CommonWriter import CommonWriter


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

                # data = self.__scrub(dictionary[url])
                data = dictionary[url]

                json.dump(data, file, indent=4, sort_keys=True, default=str)

                file.write("\n")

            file.flush()




    def __scrub(self,json_data):
        result = copy.deepcopy(json_data)

        # Handle dictionaries. Scrub all values
        if isinstance(json_data, dict):
            for k,v in result.items():
                result[k] = self.__scrub(v)
        # Handle None
        if json_data == None:
            result = ''
        # Finished scrubbing
        return result