from flask import Flask, request
import telebot

TOKEN = '6860367266:AAFhLhnfhv7t8VIdOCSQsY8-KWkTkeX4byc'  # Tokeningizni shu yerga kiriting
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/path', methods=['POST'])
def webhook():
    json_str = request.get_data(as_text=True)
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Portni kerakli port bilan almashtiring
