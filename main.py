import telebot

botTimeWeb = telebot.TeleBot('7299910315:AAFTVVuX0YHh-SIHlP-33R1YzAXYbepuUBA')

from telebot import types


@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
    first_mess = f"{message.chat.id}, привет!\nХочешь создать анкету?"
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    markup.add(button_yes)
    botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)


@botTimeWeb.callback_query_handler(func=lambda call: True)
def response(function_call):
    if function_call.message:
        if function_call.data == "yes":
            second_mess = "Но тебе сначала надо пройти 2 курса на этом сайте!"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://lyceum.yandex.ru/"))
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)


botTimeWeb.infinity_polling()
