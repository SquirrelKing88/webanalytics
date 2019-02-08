from elasticsearch import Elasticsearch
from elasticsearch import helpers


class ElasticSearchWriter:

    def __init__(self, host='77.47.134.131', port=9200, index_name='news', doc_type='common'):
        """

        :param host: server ip
        :param port: server port
        :param index_name:  table name
        :param doc_type:  row classification by country
        """
        self.__host = host
        self.__port = port
        self.__index_name = index_name
        self.__doc_type = doc_type

        self.__connection = self.__get_connection()
        self.__create_index()

    def __get_connection(self):
        connection = Elasticsearch([{'host': self.__host, 'port': self.__port}])

        if not connection.ping():
            raise Exception("Connection error. Server not answer")

        return connection

    def __create_index(self):

        settings = {

            "settings": {
                "analysis": {
                    "analyzer": {
                        "my_analyzer": {
                            "tokenizer": "my_tokenizer"
                        }
                    },
                    "tokenizer": {
                        "my_tokenizer": {
                            "type": "ngram",
                            "min_gram": 3,
                            "max_gram": 3,
                            "token_chars": [
                                "letter",
                                "digit"
                            ]
                        }
                    }
                }

            },
            "mappings": {
                self.__index_name: {
                                        "dynamic": "strict",

                                        "properties": {  # TABLE DEFINITION

                                            "url": {
                                                "type": "text"
                                            },

                                            "title": {
                                                "type": "text"
                                            },

                                            "subtitle": {
                                                "type": "keyword"
                                            },
                                            "html": {
                                                "type": "text"
                                            },

                                            "text": {
                                                "type": "text",
                                                "fields": {
                                                    "ngram": {
                                                        "type": "string",
                                                        "analyzer": "my_analyzer"
                                                    }
                                                }
                                            },
                                            "date": {
                                                "type": "date",
                                                "format": "dd/mm/yyyy HH:mm:ss"
                                            }

                                        }
                                    }
            }
        }

        # Ignore 400 means to ignore "Index Already Exist" error.
        if not self.__connection.indices.exists(self.__index_name):
            self.__connection.indices.create(index=self.__index_name, ignore=400, body=settings)

    def delete_index(self):
        """
        Delete table
        :return:
        """
        self.__connection.indices.delete(index=self.__index_name, ignore=[400, 404])

    def write(self, dictionary):
        """
          :param dictionary: {'url1': {A}, 'url2': {B}}
        """
        actions = [
            {
                "_id": url,

                "_index": self.__index_name,
                "_type": self.__doc_type,

                "_source": dictionary[url],
                "doc_as_upsert": True
            }
            for url in dictionary
        ]

        """
        [
            {"_index":Table name, "_type":Row type, "_source": A},
            {"_index":Table name, "_type":Row type, "_source": B},
        ]
        """

        helpers.bulk(self.__connection, actions)
        # outcome = self.__connection.index(index=self.__index_name, doc_type=self.__doc_type, body=data)


if __name__ == '__main__':
    el = ElasticSearchWriter()
    el.delete_index()