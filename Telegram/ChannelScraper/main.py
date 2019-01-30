
from telethon import TelegramClient, sync

from Scraper.Writters.FileWritter import FileWriter
from Telegram.ChannelScraper.Scraper import Scraper as d
from telethon import functions

from Telegram.TelegramHandler import TelegramHandler

scrapper=d()

def getPostsDataset(channel_name):
    dataset=dict()
    entity = client.get_entity(channel_name)

    for post in client.iter_messages(entity):
        id=scrapper.getPostId(post)
        dataset[id] = {'id': id,
                       'date': scrapper.getPostDate(post),
                       'text': scrapper.getPostMessage(post),
                       'forwarded_from': scrapper.getPostForwardedFrom(post),
                       'views': scrapper.getPostViews(post),
                       'edit_date': scrapper.getPostEditDate(post)
                       }

    return dataset


telegram = TelegramHandler()

client = telegram.get_client()

telegram_channel="amisnews"

writer = FileWriter(("data/{}.csv").format(telegram_channel))
writer.write(getPostsDataset(channel_name=telegram_channel))

print(getPostsDataset(telegram_channel))

