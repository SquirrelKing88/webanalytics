class IInfo:


    def __init__(self):
        # keys
        self.__id = None
        self.__parent_id = None
        self.__url = None
        self.__parent_url = None

        self.__create_datetime = None
        self.__edit_datetime = None

        self.__title = None
        self.__description = None
        self.__tags = set()
        self.__raw_data = None
        self.__text = None  #retrieve it from Telegram text

        # facebook, twitter, instagram, news, telegram
        self.__source_id = None
        self.__source_url = None
        self.__source_type = None
        self.__source_name = None

        self.__author = None #IUser

        self.__location = {
                            'name': None,
                            'coordinates': {
                                                'latitude':None,
                                                'longitude': None,
                                            }
                          }

        # set of IUser
        self.__reaction = {
                            'like': set(),
                            'dislike': set(),
                            #TODO
                          }

        #self.__views = int    count of views

        self.__translation = {
                                'en': None
                             }
        self.__media = {
                        'images': set(), # IImage
                        'sounds': set(), #ISound
                        'videos': set(), #IVideo
                        'documents': set(), #IDocument
                        'stickers': set(), #ISticker
                       }

    def get_dictionary(self):
        return self.__dict__
