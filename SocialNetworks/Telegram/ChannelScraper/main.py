from SocialNetworks.Telegram.ChannelScraper.PostScraper import Scraper
from Scraper.Writers.FileWriter import FileWriter
from SocialNetworks.Telegram.TelegramHandler import TelegramHandler
from LanguageProcessing.Translation.GoogleTranslator import GoogleTranslator


scrapper=Scraper()
translator=GoogleTranslator()

def getPost(post, dataset):
    text=scrapper.getPostMessage(post)
    #ation_result = translator.get_translation(text)
    #print(translation_result['translation'])
    dataset[scrapper.getPostId(post)] = {'id': scrapper.getPostId(post),
                                         'date': scrapper.getPostDate(post),
                                         'text': scrapper.getPostMessage(post),
                                         'forwarded_from': scrapper.getPostForwardedFrom(post),
                                         #'translation_en': translation_result['translation'],
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

telegram_channel="biochemistry_memes"

writer = FileWriter(("data/{}.csv").format(telegram_channel))
writer.write(getPostsDataset(channel_name=telegram_channel))
#writer.write(getLastPostsDataset(channel_name=telegram_channel,posts=10))
#writer.write(getPostsToIdDataset(channel_name=telegram_channel,stop_id=100))