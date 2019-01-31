from telethon import TelegramClient, sync
from Telegram.MessageScraper.PostScraper import Scraper


class ChatScraper:
    def __init__(self, api_id, api_hash):
        self.client = TelegramClient('session_name', api_id, api_hash)
        self.client.start()

    def __del__(self):
        self.client.disconnect()

    def get_chat_dataset(self, channel_name, limit):
        chat = self.client.get_entity(channel_name)
        batch = self.client.get_messages(chat,  limit=limit)
        dataset = dict()
        scrapper = Scraper()
        for post in batch:
            post_id = scrapper.getPostId(post)
            dataset[post_id] = {'id': post_id,
                                'date': scrapper.getPostDate(post),
                                'text': scrapper.getPostMessage(post),
                                'forwarded_from': scrapper.getPostForwardedFrom(post),
                                'views': scrapper.getPostViews(post),
                                'edit_date': scrapper.getPostEditDate(post)}
        return dataset

    def iter_chat_dataset(self, channel_name):
        chat = self.client.get_entity(channel_name)
        scrapper = Scraper()
        for post in self.client.iter_messages(chat):
            post_id = scrapper.getPostId(post)
            result = {'id': post_id,
                      'date': scrapper.getPostDate(post),
                      'text': scrapper.getPostMessage(post),
                      'forwarded_from': scrapper.getPostForwardedFrom(post),
                      'views': scrapper.getPostViews(post),
                      'edit_date': scrapper.getPostEditDate(post)}
            yield result



