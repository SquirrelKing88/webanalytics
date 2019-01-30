from telethon import TelegramClient, sync
from Telegram.ChannelScrapper.Scrapper import Scrapper
from Scraper.Writters.FileWritter import FileWriter


scrapper=Scrapper()

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


api_id = 640696
api_hash = '8497ac9a9076f4adba67198f2cff4181'
client = TelegramClient('scrapping', api_id, api_hash).start()

telegram_channel="amisnews"
with open(("data/{}.csv").format(telegram_channel),'w+')as file:
    pass
writer = FileWriter(("data/{}.csv").format(telegram_channel))
writer.write(getPostsDataset(channel_name=telegram_channel))

