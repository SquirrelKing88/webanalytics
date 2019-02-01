from SocialNetworks.Telegram.ChannelScraper.PostScraper import Scraper
from Scraper.Writers.FileWriter import FileWriter
from SocialNetworks.Telegram.TelegramHandler import TelegramHandler
from LanguageProcessing.Translation.GoogleTranslator import GoogleTranslator


scrapper=Scraper()
translator=GoogleTranslator()

def getPost(post, dataset):
    text=scrapper.getPostMessage(post)
    try:
        translation_result = translator.get_translation(text)
        print(translation_result["translation"])
    except:
        #print("Translation error in "+text)
        translation_result={'translation':None}
    dataset[scrapper.getPostId(post)] = {'id': scrapper.getPostId(post),
                                         'date': scrapper.getPostDate(post),
                                         'text': scrapper.getPostMessage(post),
                                         'forwarded_from': scrapper.getPostForwardedFrom(post),
                                         'translation_en': translation_result['translation'],
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

from watson_developer_cloud import PersonalityInsightsV3
import json

def insights(dataset):
    personality_insights = PersonalityInsightsV3(
        version='2018-08-01',
        iam_apikey='3SxyLvrknAbDrpuUwKZAhkyx6Y8pfYbSRUBrpM1x5yCW',
        url='https://gateway-lon.watsonplatform.net/personality-insights/api'
    )

    data={'contentItems':[]}
    for id in dataset:
        data['contentItems'].append({'content':dataset[id]['translation_en']})
    print(data)
    profile = personality_insights.profile(
        data,
        content_type='application/json',
        consumption_preferences=True,
        raw_scores=True
    ).get_result()

    print(json.dumps(profile, indent=2))

telegram = TelegramHandler()

client = telegram.get_client()

telegram_channel="dekanat_fpm"

writer = FileWriter(("data/{}.csv").format(telegram_channel))
insights(getPostsDataset(channel_name=telegram_channel))
#writer.write(getPostsDataset(channel_name=telegram_channel))
#writer.write(getLastPostsDataset(channel_name=telegram_channel,posts=10))
#writer.write(getPostsToIdDataset(channel_name=telegram_channel,stop_id=100))