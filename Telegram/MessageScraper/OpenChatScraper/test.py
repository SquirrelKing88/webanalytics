from telethon import TelegramClient, sync
from Telegram.MessageScraper.OpenChatScraper.ChatScraper import ChatScraper
from Scraper.Writers.FileWriter import FileWriter

channel_name = '@primat_chat'
api_id = 688663
api_hash = 'f15cce9a8c45a05c2b80ff878296d832'
scraper = ChatScraper(api_id=api_id, api_hash=api_hash)
dataset = dict()
limit = 3000

for index, item in enumerate(scraper.iter_chat_dataset(channel_name=channel_name)):
    dataset[item['id']] = item
    if index >= limit:
        break

print(dataset)
f = FileWriter('data/messages.csv')
f.write(dataset)
