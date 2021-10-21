import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.Token)


@bot.message_handler(commands=['start'])
def welcome(message):
    welcomeText = "Здравствуйте, вас приветствует WithoutFear! Здесь вы можете узнать больше о киберзапугивании, найти полезные советы о том, как его избежать и защитить себя;)"
    # bot.send_message(message.chat.id, welcomeText)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Что такое киберзапугивание", callback_data='info')
    item2 = types.InlineKeyboardButton("Оставить жалобу ", callback_data='complaint')
    item3 = types.InlineKeyboardButton("Служба Поддержки", callback_data='support')
    item4 = types.InlineKeyboardButton("Информация для родителей", callback_data='parents',
                                       url="https://egov.kz/cms/ru/articles/legal_relations/kiberbulling")

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id,
                     welcomeText.format(message.from_user, bot.get_me()),
                     parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, "I don't understand")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'info':
                bot.send_message(call.message.chat.id,
                                 "Киберзапугивание - это запугивание и преследование с использованием цифровых технологий. Это может происходить в социальных сетях, в приложениях для обмена сообщениями, на игровых платформах и в мобильных телефонах")

            elif call.data == 'complaint':

                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Instagram", url="https://help.instagram.com/547601325292351")
                item2 = types.InlineKeyboardButton("Facebook",
                                                   url="https://support.tiktok.com/ru/privacy-safety/report-inappropriate-content-ru")
                item3 = types.InlineKeyboardButton("Tik Tok",
                                                   url="https://support.google.com/youtube/answer/2802027?hl=ru")
                item4 = types.InlineKeyboardButton("Facebook", url="https://www.facebook.com/help/181495968648557")

                markup.add(item1, item2, item3, item4)
                bot.send_message(call.message.chat.id,
                                 "Есть ссылки на службу поддержки конкретной социальной сети",
                                 reply_markup=markup)

            elif call.data == 'support':
                bot.send_message(call.message.chat.id, "Вы можете задать вопрос, который беспокоит вас конкретно:"
                                                       "номера служб поддержки Республики Казахстан/n"
                                                       "телефон доверия 116-16"
                                                       "национальный телефон доверия для детей: 150")
            # elif call.data == 'parents':
            #     bot.send_message(call.message.chat.id, "parents link")

            bot.answer_callback_query(callback_query_id=call.id,
                                      show_alert=False,
                                      text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11",
                                      reply_markup=markup)
    except Exception as e:
        print(repr(e))


@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
