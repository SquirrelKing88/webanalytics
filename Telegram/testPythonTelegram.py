from telegram.client import Telegram

api_id = 529478
api_hash = 'b1f634fd04f304a28e021babb434bfc7'

tg = Telegram(
    api_id='api_id',
    api_hash='api_hash',
    phone='+380931655819',
    database_encryption_key='ChangeTheKey'
)

tg.login()

response = tg.get_chat_history(
    chat_id='@primat_chat',
    limit=100,
    from_message_id=1,
)
response.wait()
print(response)

