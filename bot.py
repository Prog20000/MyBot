import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('6289934861:AAGAEeSD6O0zjfDqkDGIQily4fEzin4LbSo')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_photo(message.chat.id, photo='https://www.pngmart.com/files/15/Barack-Obama-Waving-Hand-PNG.png',
                   caption='Здравствуй,пользователь! Для начала игры напиши: /go')


ki = 0
'''
@bot.callback_query_handler(func=lambda call: True)
def handle(call):
    bot.send_message(call.message.chat.id, 'Data: {}'.format(str(call.data)))
    bot.answer_callback_query(call.id)
'''
kol = 0


@bot.message_handler(commands=['go'])
def go(message):
    global ki
    global kol
    kol = 0
    ki = 0
    markup = types.InlineKeyboardMarkup()
    buttonA = types.InlineKeyboardButton('Сальвадор', callback_data='a')
    buttonB = types.InlineKeyboardButton('Никарагуа', callback_data='b')
    buttonC = types.InlineKeyboardButton('Уганда', callback_data='c')

    markup.row(buttonA, buttonB)
    markup.row(buttonC)
    bot.send_photo(message.chat.id,
                   photo='https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Flag_of_Uganda.svg/1599px-Flag_of_Uganda.svg.png')
    bot.send_message(message.chat.id, 'Какая это страна?', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle(call):
    global ki
    global kol
    if str(call.data) != 'c':
        bot.send_message(call.message.chat.id, 'Неверно!')
        kol += 1
    else:
        bot.send_message(call.message.chat.id, 'Верно!')
        ki += 1
        if ki == 1:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Коста-Рика', callback_data='c')
            buttonB = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonC = types.InlineKeyboardButton('Россия', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://infoearth.ru/wp-content/uploads/2020/04/grazhdanskij-flag-kosta-riki.png')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 2:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 3:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('ДРК', callback_data='a')
            buttonC = types.InlineKeyboardButton('Россия', callback_data='c')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://catherineasquithgallery.com/uploads/posts/2021-03/1614632369_72-p-rossiya-fon-dlya-fotoshop-83.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 4:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('США', callback_data='c')
            buttonC = types.InlineKeyboardButton('Сальвадор', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='http://rabstol.net/uploads/gallery/main/229/rabstol_net_flags_57.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 5:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Сальвадор', callback_data='c')
            buttonB = types.InlineKeyboardButton('Никарагуа', callback_data='b')
            buttonC = types.InlineKeyboardButton('Оман', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://i.pinimg.com/originals/60/62/26/606226f464726e876bcd8184c4d76afc.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 6:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Бразилия', callback_data='a')
            buttonB = types.InlineKeyboardButton('ЧАД', callback_data='b')
            buttonC = types.InlineKeyboardButton('Доминика', callback_data='c')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://cdn.freebiesupply.com/logos/large/2x/dominica-logo-png-transparent.png')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
            ki += 36
        elif ki == 7:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 8:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 9:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 10:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 11:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 12:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 13:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 14:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 15:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 16:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 17:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 18:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 19:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 20:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 21:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 22:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 23:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 24:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 25:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 26:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 27:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 28:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 29:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 30:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 31:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 32:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 33:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 34:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 35:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 36:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 37:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 38:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 39:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 40:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 41:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 42:
            markup = types.InlineKeyboardMarkup()
            buttonA = types.InlineKeyboardButton('Нидерланды', callback_data='b')
            buttonB = types.InlineKeyboardButton('КНДР', callback_data='c')
            buttonC = types.InlineKeyboardButton('США', callback_data='a')

            markup.row(buttonA, buttonB)
            markup.row(buttonC)
            bot.send_photo(call.message.chat.id,
                           photo='https://news-postseven.com/uploads/2017/06/North-KOREA-2.jpg')
            bot.send_message(call.message.chat.id, 'Какая это страна?', reply_markup=markup)
        elif ki == 43:
            bot.send_message(call.message.chat.id, f'Игра окончена! Количество ошибок: {kol}')
            con = sqlite3.connect('datas.db')

            cur = con.cursor()

            result = cur.execute("""SELECT 
                Score
            FROM 
                Records1
            WHERE 
                Score == Score
            """).fetchall()
            con.close()
            uma = 0
            if result[0][0] < kol:
                bot.send_message(call.message.chat.id, f'Максимальный результат: {kol}')
                con = sqlite3.connect('datas.db')

                cur = con.cursor()

                cur.execute("""UPDATE 
                    Records1
                SET 
                   Score = kol
                WHERE 
                    num = 'f'
                """)
                con.commit()
                con.close()
            else:
                bot.send_message(call.message.chat.id, f'Максимальный результат: {result[0][0]}')


@bot.message_handler(commands=['stop'])
def stop(message):
    global ki
    global kol
    kol = 0
    ki = 0
    bot.send_message(message.chat.id, 'Игра приостановлена. Для повторного начала напишите: /go')


bot.polling()
