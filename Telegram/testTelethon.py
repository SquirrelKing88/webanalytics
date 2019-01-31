from telethon import TelegramClient, sync


api_id = 529478
api_hash = 'b1f634fd04f304a28e021babb434bfc7'

with TelegramClient('session_name', api_id, api_hash) as client:
    iterator_messages = client.iter_messages('@primat_chat')
    for counter in range(0, 50):
        mess = next(iterator_messages)
        print(mess.message)
