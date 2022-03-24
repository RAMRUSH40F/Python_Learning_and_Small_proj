import telebot
from telebot import types
from config import token
import csv
import pickle
import re


bot = telebot.TeleBot(token)
# hideBoard = types.ReplyKeyboardRemove()

def message_filter(message):

    #  ГЛАВНОЕ МЕНЮ
    if message.text in ['меню', 'Меню', 'кк','@renatakamilabot','Старт','старт','Начать','Привет','привет','Назад']:
        main_menue(message)

    #Раздел списка продуктов
    elif message.text in [ 'Список Продуктов','Посмотреть список продуктов','Добавить продукты']:
        if message.text == 'Список Продуктов' : shopping_menue(message)
        elif message.text == 'Посмотреть список продуктов': show_shopping_list(message)
        elif message.text == 'Добавить продукты': add_to_shop_list(message)

    #  Модерируем плохие слова ( НЕ ГОТОВО).
    elif censorship(message.text) : bot.delete_message(message.chat.id,message.id)

def main_menue(message):
    menu = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_back = types.KeyboardButton(text= 'Назад')
    btn_weather = types.KeyboardButton(text='Погода(в доработке)')
    btn_store_list = types.KeyboardButton(text= 'Список Продуктов')
    btn_cleaning = types.KeyboardButton(text='Уборка(в доработке)')

    menu.add(btn_store_list, btn_weather, btn_cleaning)
    bot.send_message(message.chat.id,'Вот список моих функций на сегодня. Пользуйся :) ', reply_markup=menu)

 # open a shopping menue
def shopping_menue(message):
    bot.delete_message(message.chat.id, message.id)
    shopping_menue = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_back = types.KeyboardButton(text='Назад')
    btn_show_shopping_list = types.KeyboardButton(text='Посмотреть список продуктов')
    btn_add_to_shopping_list = types.KeyboardButton(text='Добавить продукты')

    shopping_menue.add(btn_back, btn_show_shopping_list, btn_add_to_shopping_list)
    bot.send_message(message.chat.id, 'Ты можешь посмотреть или добавить в список продуктов ', reply_markup=shopping_menue)


def show_shopping_list(message):
    bot.delete_message(message.chat.id,message.id)
    # bot.send_photo(message.chat.id, r'https://ucarecdn.com/e3c749ec-5426-40f9-9060-20f7a236cb4b/', 'Камень с глазами 1000$')
    bot.send_message(message.chat.id, '<b>Текущий список покупок:</b>', parse_mode='HTML')
    with open('shoplistfile.bin', 'rb') as file:
        shoplist_info = pickle.load(file)
        str = ', '.join(shoplist_info)
        bot.send_message(message.chat.id, str)



def add_to_shop_list(message):
    list_temp = []
    to_reply = bot.send_message(message.chat.id, 'В следующем предложении ты можешь написать список продуктов '
                                      'через пробел или написать продукт из списка и удалить его')
    with open('shoplistfile.bin', 'rb') as file:
        list_temp = pickle.load(file)
        # file = open('shoplistfile.bin', 'rb')

    # save next message and split it with add_to_shop_list_assistante func
    bot.register_next_step_handler(to_reply, add_to_shop_list_assistante)

    list_temp +=
    with open('shoplistfile.bin', 'wb') as file:
        pickle.dump(list_temp, file)
        # shoplist_info = pickle.load(file)

def add_to_shop_list_assistante(message):
    text = message.text
    text = text.lower()
    text = text.split(' ')
    for i in range(len(text)): text[i] = text[i][0].upper() + text [i][1:]
    return text
    # takes a message and split it, correct, return list of items in message

def censorship(text):
    return text in ['плохой','какашка']



@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Рад видеть и служить вам. Напишите либо старт либо начать либо привет, чтобы увидеть,что я могу')


@bot.message_handler(content_types=['text'])
def main(message):
    message_filter(message)


# @bot.message_handler()

#
# @bot.message_handler(func = lambda message: True)
# def gagagw(message):
#     # callback = f'Я пробил информацию\nid чата:{message.chat.id}\nid пользователя:{message.from_user.id}\nИмя:{message.from_user.first_name}\nФамилия{message.from_user.last_name}\nПсевдоним:{message.from_user.username}\n Текст сообщения:/start'
#     kb = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width=1)
#     btn_buy = types.KeyboardButton(text= 'Купить')
#
#     kb.add(btn_buy)
#     bot.send_message(message.chat.id,'1', reply_markup=hideBoard)


if __name__ == '__main__':
    bot.infinity_polling()
