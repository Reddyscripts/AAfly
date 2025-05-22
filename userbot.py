from telethon import TelegramClient, events
import os

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

SOURCE_CHAT_ID = int(os.environ["SOURCE_CHAT_ID"])
TARGET_CHAT_ID = int(os.environ["TARGET_CHAT_ID"])
TARGET_BOT_USERNAME = os.environ["TARGET_BOT_USERNAME"]

client = TelegramClient("userbot", api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHAT_ID))
async def handler(event):
    sender = await event.get_sender()
    if sender.username == TARGET_BOT_USERNAME:
        if event.text:
            await client.send_message(TARGET_CHAT_ID, event.text)
        elif event.media:
            await client.send_file(TARGET_CHAT_ID, event.media, caption=event.text)

client.start()
client.run_until_disconnected()
