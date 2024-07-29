import telebot

TOKEN = '6860367266:AAFhLhnfhv7t8VIdOCSQsY8-KWkTkeX4byc'  # Tokeningizni shu yerga kiriting
WEBHOOK_URL = 'https://your-domain.com/path'  # O'zingizning to'g'ri URL-ni kiriting

bot = telebot.TeleBot(TOKEN)

# Webhookni o'chirish
remove_webhook_response = bot.remove_webhook()
print("Webhook o'chirildi:", remove_webhook_response)

# Webhookni o'rnatish
set_webhook_response = bot.set_webhook(url=WEBHOOK_URL)
print("Webhook o'rnatildi:", set_webhook_response)
