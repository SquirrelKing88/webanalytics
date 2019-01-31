from telethon.sessions import StringSession
from telethon import TelegramClient, sync
import os

class TelegramHandler:


    def __init__(self):
        # TODO create config file
        # TODO read config from file
        api_id = 688663
        api_hash = 'f15cce9a8c45a05c2b80ff878296d832'

        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, 'config', 'session'), 'r') as file:
            session = file.read()

        self.__client = TelegramClient(StringSession(session), api_id, api_hash).start()

        # session write
        # dir_path = os.path.dirname(os.path.realpath(__file__))
        # with open(os.path.join(dir_path, 'config', 'session'), 'w+') as file:
        #     session = StringSession.save(self.__client.session)
        #     file.write(session)

    def get_client(self):
        return self.__client