import telebot

bot = telebot.TeleBot('7299910315:AAFTVVuX0YHh-SIHlP-33R1YzAXYbepuUBA')

from telebot import types


@bot.message_handler(commands=['start'])
def startBot(message):
    first_mess = f"{message.from_user.first_name}, привет!\nХочешь создать анкету?"
    markup = types.InlineKeyboardMarkup(row_width=1)
    button_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    markup.add(button_yes)
    bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def response(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, 'Как тебя зовут?')


num = 0


@bot.message_handler(content_types=['text'])
def get_info(message):
    global num
    word = message.text.strip().lower()
    print(word)
    num += 1
    if num == 1:
        bot.send_message(message.chat.id, 'Сколько тебе лет?')
    elif num == 2:
        bot.send_message(message.chat.id, 'Расскажи о себе')


bot.polling(none_stop=True)
