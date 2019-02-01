from telethon import TelegramClient, sync
from Telegram.MessageScraper.PostScraper import Scraper


class ChatScraper:
    @staticmethod
    def get_chat_dataset(client, channel_name, limit):
        chat = client.get_client().get_entity(channel_name)
        batch = client.get_client().get_messages(chat,  limit=limit)
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

    @staticmethod
    def iter_chat_dataset(client, channel_name):
        chat = client.get_client().get_entity(channel_name)
        scrapper = Scraper()
        for post in client.get_client().iter_messages(chat):
            post_id = scrapper.getPostId(post)
            result = {'id': post_id,
                      'date': scrapper.getPostDate(post),
                      'text': scrapper.getPostMessage(post),
                      'forwarded_from': scrapper.getPostForwardedFrom(post),
                      'views': scrapper.getPostViews(post),
                      'edit_date': scrapper.getPostEditDate(post)}
            yield result



