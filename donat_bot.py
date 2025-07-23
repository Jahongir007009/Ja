
import telebot

TOKEN = 'YOUR_TOKEN'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Assalomu alaykum! Bu Blood Strike donat bot.")

bot.polling(non_stop=True)
