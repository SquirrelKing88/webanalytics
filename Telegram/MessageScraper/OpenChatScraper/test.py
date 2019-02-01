from telethon import TelegramClient, sync
from Telegram.MessageScraper.OpenChatScraper.ChatScraper import ChatScraper
from Telegram.TelegramHandler import TelegramHandler
from Scraper.Writers.FileWriter import FileWriter

channel_name = '@primat_chat'
client = TelegramHandler()
scraper = ChatScraper()
dataset = dict()
limit = 3000
for index, item in enumerate(scraper.iter_chat_dataset(client, channel_name=channel_name)):
    dataset[item['id']] = item
    if index >= limit:
        break

f = FileWriter('data/messages.csv')
f.write(dataset)
