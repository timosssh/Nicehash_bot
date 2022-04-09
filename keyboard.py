# -*- coding: utf-8 -*-
import telebot.types

# Главное меню
keyboard_start = telebot.types.ReplyKeyboardMarkup(True, True)
category_1_btn: str = ('Раздел 1')
category_2_btn: str = ('Раздел 2')
category_3_btn: str = ('Раздел 3')
category_4_btn: str = ('Раздел 4')
keyboard_start.row(category_1_btn, category_2_btn, category_3_btn, category_4_btn)

# Раздел category_1
category_1_btn_choose = telebot.types.ReplyKeyboardMarkup(True)
msg_category_1_btn = ('Отлично, нажми кнопку')
gpu_btn_1 = 'Разместить обьявление в этой категории'
gpu_btn_2 = 'Посмотреть обьявления в канале НЕНАЖИМАТЬ'
category_1_btn_choose.row(gpu_btn_1, gpu_btn_2)

# Раздел category_1_1
category_1_1_btn_choose = telebot.types.ReplyKeyboardMarkup(True)
msg_category_1_1_btn = ('Напишите ваше обьявление здесь\n'
                        'После проверки модератором ваше обьявление будет опубликовано в ближайшее время')
cat_1_1_btn_1 = 'Готово'
cat_1_1_btn_2 = 'Нихуя не готово'
category_1_1_btn_choose.row(cat_1_1_btn_1, cat_1_1_btn_2)


