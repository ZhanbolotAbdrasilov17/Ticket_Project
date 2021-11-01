import telebot
from telebot import types
from config3 import TOKEN
from service3 import main


bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.
    text = "Здравствуйте! \nДобро пожаловать в наш телеграмм бот! \nВыберите свои дальнейшие действия!"
    bot.send_message(message.chat.id, text.lstrip())



bot.polling(none_stop=True)
