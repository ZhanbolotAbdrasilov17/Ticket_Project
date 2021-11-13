import telebot
from telebot import types
from config import TOKEN
from dodo import get_data1
from imperia import get_data2
from kfc import get_data3
from sushihouse import get_data4
from sushiwok import get_data5

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands = ['start'])
def start(message):
    text = "Здравствуйте! \nДобро пожаловать в наш телеграмм бот! \nНаш бот покажет вам все акции известных заведений города Бишкек \nВыберите свои дальнейшие действия!"
    photo = open('Sales Bot-02.jpg', 'rb')
    bot.send_photo(message.chat.id, photo=photo)
    bot.send_message(message.chat.id, text)
    

@bot.message_handler(commands = ['exit'])
def exit(message):
    text = 'До свидания! \nВсего вам доброго!'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands = ['menu'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width= 6)
    btn1 = types.InlineKeyboardButton('Dodo Pizza', callback_data = 'dodopizza')
    btn2 = types.InlineKeyboardButton('Империя пиццы', callback_data = 'imperia')
    btn3 = types.InlineKeyboardButton('KFC', callback_data = 'kfc')
    btn5 = types.InlineKeyboardButton('SUSHI HOUSE', callback_data = 'sushihouse')
    btn6 = types.InlineKeyboardButton('СУШИWOK', callback_data = 'sushiwok')
    markup.add(btn1, btn2, btn3)
    markup.add(btn5, btn6 )
    text = "Выберите кафе, чтобы узнать их акции!"
    bot.send_message(message.chat.id, text=text, reply_markup=markup)


@bot.callback_query_handler(func =lambda call: call.data == 'dodopizza')
def echo(call):
    sales_list = get_data1()
    title = sales_list[0]
    text = 'Акции \U0001f600'
    photo = sales_list[2]
    markup = types.InlineKeyboardMarkup(row_width = 1)
    items = types.InlineKeyboardButton('Описание', callback_data='dodo_description')
    markup.add(items)
    bot.edit_message_text(chat_id = call.message.chat.id,text= text, message_id=call.message.message_id)
    bot.send_photo(call.message.chat.id, photo=photo)
    bot.send_message(call.message.chat.id, text = ' \n\n'.join(title), reply_markup=markup)

@bot.callback_query_handler(func =lambda call: call.data == 'imperia')
def echo1(call):
    sales_list = get_data2()
    title = sales_list[0]
    text = 'Акции \U0001f600'
    markup = types.InlineKeyboardMarkup(row_width = 1)
    items = types.InlineKeyboardButton('Описание', callback_data='imperia_description')
    markup.add(items)
    bot.edit_message_text(chat_id = call.message.chat.id,text= text, message_id=call.message.message_id)
    bot.send_photo(call.message.chat.id, photo=sales_list[2])
    bot.send_message(call.message.chat.id, text = ' \n\n'.join(title), reply_markup=markup)

@bot.callback_query_handler(func =lambda call: call.data == 'kfc')
def echo(call):
    sales_list = get_data3()
    title = sales_list[0]
    text = 'Акции \U0001f600'
    markup = types.InlineKeyboardMarkup(row_width = 1)
    items = types.InlineKeyboardButton('Описание', callback_data='kfc_description')
    markup.add(items)
    bot.edit_message_text(chat_id = call.message.chat.id,text= text, message_id=call.message.message_id)
    bot.send_photo(call.message.chat.id, photo=sales_list[2])
    bot.send_message(call.message.chat.id, text = ' \n\n'.join(title), reply_markup=markup)

@bot.callback_query_handler(func =lambda call: call.data == 'sushihouse')
def echo(call):
    sales_list = get_data4()
    title = sales_list[0]
    text = 'Акции \U0001f600'
    markup = types.InlineKeyboardMarkup(row_width = 1)
    items = types.InlineKeyboardButton('Описание', callback_data='sushihouse_description')
    markup.add(items)
    bot.edit_message_text(chat_id = call.message.chat.id,text= text, message_id=call.message.message_id)
    bot.send_photo(call.message.chat.id, photo=sales_list[2])
    bot.send_message(call.message.chat.id, text = ' \n\n'.join(title), reply_markup=markup)

@bot.callback_query_handler(func =lambda call: call.data == 'sushiwok')
def echo(call):
    sales_list = get_data5()
    title = sales_list[0]
    text = 'Акции \U0001f600'
    markup = types.InlineKeyboardMarkup(row_width = 1)
    items = types.InlineKeyboardButton('Описание', callback_data='sushiwok_description')
    markup.add(items)
    bot.edit_message_text(chat_id = call.message.chat.id,text= text, message_id=call.message.message_id)
    bot.send_photo(call.message.chat.id, photo=sales_list[2])
    bot.send_message(call.message.chat.id, text = ' \n\n'.join(title), reply_markup=markup)


@bot.callback_query_handler(func =lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'imperia_description':
            sales_list = get_data2()
            description = sales_list[1]
            text = ' \n\n'.join(description)
            bot.edit_message_text(chat_id=call.message.chat.id,text = text, message_id=call.message.message_id, reply_markup=None)

        elif call.data == 'dodo_description':
            sales_list = get_data1()
            description = sales_list[1]
            text = ' \n\n'.join(description)
            bot.edit_message_text(chat_id=call.message.chat.id,text = text, message_id=call.message.message_id, reply_markup=None)

        elif call.data == 'kfc_description':
            sales_list = get_data3()
            description = sales_list[1]
            text = ' \n\n'.join(description)
            bot.edit_message_text(chat_id=call.message.chat.id,text = text, message_id=call.message.message_id, reply_markup=None)

        elif call.data == 'sushihouse_description':
            sales_list = get_data4()
            description = sales_list[1]
            text = ' \n\n'.join(description)
            bot.edit_message_text(chat_id=call.message.chat.id,text = text, message_id=call.message.message_id, reply_markup=None)

        elif call.data == 'sushiwok_description':
            sales_list = get_data5()
            description = sales_list[1]
            text = ' \n\n'.join(description)
            bot.edit_message_text(chat_id=call.message.chat.id,text = text, message_id=call.message.message_id, reply_markup=None)


bot.polling(none_stop=True)