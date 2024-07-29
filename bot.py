import telebot
import os

TOKEN = '6860367266:AAFhLhnfhv7t8VIdOCSQsY8-KWkTkeX4byc'  # Tokeningizni shu yerga kiriting
bot = telebot.TeleBot(TOKEN)

# Fayllarni saqlash uchun papka
DOWNLOAD_FOLDER = 'downloads'
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Start komandasini qayta ishlash
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Salom! Menga fayllarni yuboring.")

# Fayllarni qabul qilish
@bot.message_handler(content_types=['document'])
def handle_docs(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # Faylni saqlash
    file_path = os.path.join(DOWNLOAD_FOLDER, message.document.file_name)
    with open(file_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(message.chat.id, "Faylingiz saqlandi!")

# Botni ishga tushirish
bot.polling(none_stop=True)
