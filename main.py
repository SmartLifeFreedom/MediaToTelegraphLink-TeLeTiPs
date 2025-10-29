import os
from telethon import TelegramClient, events
from telegraph import upload_file

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply("👋 Inviami una foto o un video e ti restituirò il link Telegraph!")

@bot.on(events.NewMessage)
async def handle_media(event):
    if event.photo or event.video:
        media = await event.download_media()
        try:
            response = upload_file(media)
            link = "https://telegra.ph" + response[0]
            await event.reply(f"✅ Ecco il tuo link:\n{link}")
        except Exception as e:
            await event.reply(f"❌ Errore durante l’upload: {e}")
    else:
        await event.reply("📸 Inviami una foto o un video, non testo!")

print("✅ Bot avviato con successo!")
bot.run_until_disconnected()
