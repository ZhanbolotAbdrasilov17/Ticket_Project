import telebot
from telebot import types
from config3 import TOKEN
from dodo import get_data


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width= 2)
    btn1 = types.KeyboardButton('Dodo Pizza')
    btn2 = types.KeyboardButton('PapaJohns')
    markup.add(btn1, btn2)
    text = "Здравствуйте! \nДобро пожаловать в наш телеграмм бот! \n Наш бот будет отправлять вам все акции известных кафе города Бишкек \nВыберите свои дальнейшие действия!"
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def echo(message):
    get_message = message.text
    if get_message == 'Dodo Pizza':
        sales_list = get_data()
        for sale in sales_list:
            markup = types.InlineKeyboardMarkup(row_width = 1)
            items = types.InlineKeyboardButton('Описание', callback_data=str(sale['number']))
            markup.add(items)
            bot.send_message(message.chat.id, sale['title'],  reply_markup=markup)

@bot.callback_query_handler(func =lambda call: True)
def callback_inline(call):
    if call.message:
        sales_list = get_data()
        for sale in sales_list:
            if call.data == str(sale['number']):
                text = sale['description']
                bot.edit_message_text(chat_id=call.message.chat.id,text = text, message_id=call.message.message_id, reply_markup=None)






bot.polling(none_stop=True)
