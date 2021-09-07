import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Вылечить рак")
    item2 = types.KeyboardButton("Точно по мог ло?")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот, созданный, чтобы лечить. Это "
                     "важно!".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Вылечить рак':
            if random.randint(0, 1) == 0:
                bot.send_message(message.chat.id, "message.chat.id, Рак вылеченнннннннн, поздравляю! С вас пять тысяч.")
            else:
                bot.send_message(message.chat.id, "message.chat.id, Не хочу тебя расстраивать, но лечение не "
                                                  "сработало и тебе осталось жить еще десять секунд. Ищи самый "
                                                  "смешной видос в ютубе...котики очень милые) elif message.text == "
                                                  "'Не помогло, а жаль...':")

            markup = types.InlineKeyboardMarkup(row_width=2)

        else:
            bot.send_message(message.chat.id, 'Я не смог прочитать эту фразу. Пожалуйста, попробуйте что-нибудь исчо')


# RUN
bot.polling(none_stop=True)