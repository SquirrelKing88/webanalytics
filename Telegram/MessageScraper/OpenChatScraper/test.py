from telethon import TelegramClient, sync
from Telegram.MessageScraper.OpenChatScraper.ChatScraper import ChatScraper

channel_name = '@primat_chat'
api_id = 529478
api_hash = 'b1f634fd04f304a28e021babb434bfc7'
scraper = ChatScraper(api_id=api_id, api_hash=api_hash)
dataset = dict()
counter = 0

for index, item in enumerate(scraper.iter_chat_dataset(channel_name=channel_name)):
    dataset[item['id']] = item

    if item['text']:
        pass
    else:
        counter += 1

    if not (index+1) % 1000:
        print('No text messages: ', counter)
        if input('Press enter to continue') == '':
            counter = 0
            continue
        else:
            break
