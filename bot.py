import telebot
from telebot import types
from config3 import TOKEN
from dodo import get_data
from imperia import get_data1

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands = ['start'])
def start(message):
    text = "Здравствуйте! \nДобро пожаловать в наш телеграмм бот! \n Наш бот будет отправлять вам все акции известных кафе города Бишкек \nВыберите свои дальнейшие действия!"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands = ['menu'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width= 2)
    btn1 = types.InlineKeyboardButton('Dodo Pizza', callback_data = 'dodopizza')
    btn2 = types.InlineKeyboardButton('Империя пиццы', callback_data = 'imperia')
    markup.add(btn1, btn2)
    text = "Выберите кафе, чтобы узнать их акции!"
    bot.send_message(message.chat.id, text=text, reply_markup=markup)


@bot.callback_query_handler(func =lambda call: call.data == 'dodopizza')
def echo(call):
    sales_list = get_data()
    title = sales_list[0]
    text = 'Акции \U0001f600'
    markup = types.InlineKeyboardMarkup(row_width = 1)
    items = types.InlineKeyboardButton('Описание', callback_data='dodo_description')
    markup.add(items)
    bot.edit_message_text(chat_id = call.message.chat.id,text= text, message_id=call.message.message_id)
    bot.send_photo(call.message.chat.id, photo=sales_list[3])
    bot.send_message(call.message.chat.id, text = ' \n'.join(title), reply_markup=markup)

@bot.callback_query_handler(func =lambda call: call.data == 'imperia')
def echo1(call):
    sales_list = get_data1()
    title = sales_list[0]
    text = 'Акции \U0001f600'
    markup = types.InlineKeyboardMarkup(row_width = 1)
    items = types.InlineKeyboardButton('Описание', callback_data='imperia_description')
    markup.add(items)
    bot.edit_message_text(chat_id = call.message.chat.id,text= text, message_id=call.message.message_id)
    bot.send_photo(call.message.chat.id, photo=sales_list[2])
    bot.send_message(call.message.chat.id, text = ' \n'.join(title), reply_markup=markup)

@bot.callback_query_handler(func =lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'imperia_description':
            sales_list = get_data1()
            description = sales_list[1]
            text = ' \n'.join(description)
            bot.edit_message_text(chat_id=call.message.chat.id,text = text, message_id=call.message.message_id, reply_markup=None)

        elif call.data == 'dodo_description':
            sales_list = get_data()
            description = sales_list[1]
            text = ' \n'.join(description)
            bot.edit_message_text(chat_id=call.message.chat.id,text = text, message_id=call.message.message_id, reply_markup=None)

bot.polling(none_stop=True)