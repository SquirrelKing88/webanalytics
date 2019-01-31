from Telegram.ChannelScraper.PostScraper import Scraper
from Scraper.Writers.FileWriter import FileWriter
from Telegram.TelegramHandler import TelegramHandler



scrapper=Scraper()

def getPost(post, dataset):
    dataset[scrapper.getPostId(post)] = {'id': scrapper.getPostId(post),
                                         'date': scrapper.getPostDate(post),
                                         'text': scrapper.getPostMessage(post),
                                         'forwarded_from': scrapper.getPostForwardedFrom(post),
                                         'views': scrapper.getPostViews(post),
                                         'edit_date': scrapper.getPostEditDate(post)
                                         }

def getLastPostsDataset(channel_name,posts):
    dataset = dict()
    entity = client.get_entity(channel_name)

    counter=0
    for post in client.iter_messages(entity):
        if (counter==posts):
            return dataset
        getPost(post,dataset)
        counter += 1

    return dataset

def getPostsToIdDataset(channel_name,stop_id):
    dataset = dict()
    entity = client.get_entity(channel_name)

    for post in client.iter_messages(entity):
        id = scrapper.getPostId(post)
        getPost(post, dataset)
        if id==stop_id:
            return dataset

    return dataset

def getPostsDataset(channel_name):
    dataset=dict()
    entity = client.get_entity(channel_name)

    for post in client.iter_messages(entity):
        getPost(post,dataset)

    return dataset


telegram = TelegramHandler()

client = telegram.get_client()

telegram_channel="amisnews"

writer = FileWriter(("data/{}.csv").format(telegram_channel))
writer.write(getPostsDataset(channel_name=telegram_channel))
#writer.write(getLastPostsDataset(channel_name=telegram_channel,posts=10))
#writer.write(getPostsToIdDataset(channel_name=telegram_channel,stop_id=100))