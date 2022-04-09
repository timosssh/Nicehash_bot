# -*- coding: utf-8 -*-
import telebot
import config
import time
import keyboard
from keyboard import *
import requests

bot = telebot.TeleBot(config.TOKEN)
next_step = bot.register_next_step_handler  # Переход бота на следующий шаг


def send_optional(message, msg_type='text', body=()):
    chat = message.chat.id
    if msg_type == 'text':
        bot.send_message(chat, body)
    elif msg_type == 'picture':
        photo = open(body, 'rb')
        bot.send_photo(chat, photo)
    elif msg_type == 'gif':
        gif = open(body, 'rb')
        bot.send_animation(chat, gif)
    elif msg_type == 'video':
        video = open(body)
        bot.send_photo(chat, video)
    elif msg_type == 'voice':
        voice = open(body, 'rb')
        bot.send_photo(chat, voice)
    return


# Приветствие бота, по команде /start
@bot.message_handler(commands=['start'])
def start_message(message):
    chat = message.chat.id
    bot.send_message(chat,
                     'Привет, ' + str(message.from_user.first_name) + '! Рад нашей встречи!')
    time.sleep(1)
    bot.send_message(chat,
                     config.hello_message)
    time.sleep(1)
    bot.send_message(chat,
                     config.hello_description)
    bot.send_message(chat,
                     "Выбери интересующий тебя чат или канал",
                     reply_markup=keyboard_start)

# Главное меню, отрабатывается по вызову клавиатуры keyboard_start
@bot.message_handler()
def main_menu(message):
    # пользователь выбирает на всплывающей клавиатуре категорию меню
    chat = message.chat.id

#Раздел №1
    if message.text == category_1_btn:
        bot.send_message(chat,
                         'Ты выбрал раздел ' + str(message.text))
        photo = open('photo_btn1.png', 'rb')
        bot.send_photo(chat, photo)
        time.sleep(1)
        # описание выбранной категории
        msg = bot.send_message(chat,
                               msg_category_1_btn,
                                reply_markup=category_1_btn_choose)
        next_step(msg, category_1_1_menu)
    else:
        bot.send_message(chat, 'Бот не знает такой команды')
        message_startup = bot.send_message(chat,
                                           "Выбери интересующую тебя категорию",
                                           reply_markup=keyboard_start)
        next_step(message_startup, main_menu)

def category_1_1_menu(message):
    chat = message.chat.id
    if message.text == gpu_btn_1:
        bot.send_message(chat,
                            'Ты выбрал ' + str.lower(message.text))
        bot.send_message(chat,
                            msg_category_1_1_btn)
        msg = bot.send_message(chat,
                                'Нажмите кнопку готово чтобы отправить обьявление на проверку',
                               reply_markup=category_1_1_btn_choose)
        next_step(msg, work_menu)

# Раздел Категория_1_1



# раздел Работа
def work_menu(message):
    chat = message.chat.id
    if message.text == 'хуй':
        keyboard_rabo = telebot.types.ReplyKeyboardMarkup(True)
        keyboard_rabo.row('Переходи в этот чат', 'Или этот чат')
        bot.send_message(chat, 'Хорошо, мы за три дня побили этот питон и аренда не дублируется!!!! УРАААА',
                         reply_markup=keyboard_rabo)
    elif message.text == 'Предложить работу':
        keyboard_rabo2 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard_rabo2.row('Я частник', 'Я ип')
        bot.send_message(chat, 'Урааа ты нажал предложить работу', reply_markup=keyboard_rabo2)
    elif message.text == 'Аренда':
        keyboard_rabo2 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard_rabo2.row('Я арендник', 'Я ип')
        bot.send_message(chat, 'Очень славно, кнопка аренды стала независимой', reply_markup=keyboard_rabo2)


bot.polling(none_stop=True, interval=0)
