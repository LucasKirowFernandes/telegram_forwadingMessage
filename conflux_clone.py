from telethon import TelegramClient, events
from settings import COMBINATIONS, TELEGRAM_API_ID, TELEGRAM_API_HASH

client = TelegramClient('session', api_id=TELEGRAM_API_ID, api_hash=TELEGRAM_API_HASH)

# create a new function to receive NewMessages events
@client.on(events.NewMessage)
async def handle_new_message(event):
    # check if message is received form specific sender
    sender_chat_id = event.sender_id
    if sender_chat_id in list(COMBINATIONS.keys()):
        # send the message destination chat
        destination_chat_ids = COMBINATIONS.get(sender_chat_id, [])
        for chat_id in destination_chat_ids:
            await client.forward_messages(chat_id, event.message)

client.start()
client.run_until_disconnected()