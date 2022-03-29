import telebot
from telebot import types
from config import token, sayhi
from weather_api import get_weather
from SQLighter import SQLighter
import csv
import pickle
import re


bot = telebot.TeleBot(token)
# hideBoard = types.ReplyKeyboardRemove()


def message_filter(message):

    #  ГЛАВНОЕ МЕНЮ
    if message.text in ['меню', 'Меню', '@renatakamilabot', 'Старт', 'старт', 'Начать','начать', 'Привет', 'привет', 'Назад']:
        main_menue(message)

    #  Послать погоду
    elif message.text in ['Погода',"погода"]: send_weather(message.chat.id)

    #  Раздел списка продуктов
    elif message.text in ['Список Продуктов', 'Посмотреть список продуктов', 'Добавить продукты']:
        if message.text == 'Список Продуктов': shopping_menue(message)
        elif message.text == 'Посмотреть список продуктов': show_shopping_list(message)
        elif message.text == 'Добавить продукты': add_to_shop_list(message)

    #  Раздел уборки
    elif message.text in ['Уборка',"уборка",'Заявить об уборке','Посмотреть баллы']:
        if message.text in ['Уборка',"уборка"]: cleaning_menu(message)
        elif message.text == 'Заявить об уборке': cleaning_done_menu(message)
        elif message.text == 'Посмотреть баллы': get_scores(message)

    #  Модерируем плохие слова ( НЕ ГОТОВО).
    elif censorship(message.text): bot.delete_message(message.chat.id, message.id)


# open a main menue
def main_menue(message):
    menu = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_weather = types.KeyboardButton(text='Погода')
    btn_store_list = types.KeyboardButton(text='Список Продуктов')
    btn_cleaning = types.KeyboardButton(text='Уборка')

    menu.add(btn_store_list, btn_cleaning, btn_weather)
    bot.send_message(message.chat.id, 'Вот список моих функций на сегодня. Пользуйся :) ', reply_markup=menu)


#  open a shopping menue
def shopping_menue(message):
    bot.delete_message(message.chat.id, message.id)
    btn_back = types.KeyboardButton(text='Назад')
    btn_show_shopping_list = types.KeyboardButton(text='Посмотреть список продуктов')
    btn_add_to_shopping_list = types.KeyboardButton(text='Добавить продукты')

    shopping_menue = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    shopping_menue.add(btn_back, btn_show_shopping_list, btn_add_to_shopping_list)
    bot.send_message(message.chat.id, 'Ты можешь посмотреть или добавить в список продуктов ', reply_markup=shopping_menue)


# shopping list button
def show_shopping_list(message):
    bot.delete_message(message.chat.id,message.id)
    bot.send_message(message.chat.id, '<b>Текущий список покупок:</b>', parse_mode='HTML')
    bot.send_message(message.chat.id, ', '.join(get_shoplist()))


def add_to_shop_list(message):
    sent = bot.send_message(message.chat.id, 'В следующем предложении ты можешь написать список продуктов <b>через пробел</b> или написать какой-то из них из списка и удалить его', parse_mode='HTML')
    bot.register_next_step_handler(sent, write_to_shoplist_from_message)


#  return a current shop_list as a list[]
def get_shoplist():
    with open('shoplistfile.bin', 'rb') as file:
        temp_list = pickle.load(file)
        return temp_list

# def delete_shoplist():
#     randomrandom22 = []
#     with open('shoplistfile.bin', 'wb') as file:
#         pickle.dump(randomrandom22, file)

def write_to_shoplist_from_message(message):
    text = message.text
    text = text.lower()
    text = text.split(' ')
    for i in range(len(text)): text[i] = text[i][0].upper() + text[i][1:]

    temp_list = get_shoplist() + text
    temp_list = set(temp_list)
    temp_list = list(temp_list)
    # print(temp_list)
    with open('shoplistfile.bin', 'wb') as file:
        pickle.dump(temp_list, file)

def send_weather(chatid):
    weather , path = get_weather()
    bot.send_message(chatid, weather)
    with open(path, 'rb') as weather_icon:
        bot.send_photo(chatid, weather_icon)

def censorship(text):
    return text in ['плохой','какашка']

def cleaning_menu(message):
    menu = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_scores = types.KeyboardButton(text='Посмотреть баллы')
    btn_declare = types.KeyboardButton(text='Заявить об уборке')
    btn_back = types.KeyboardButton(text='Назад')

    menu.add(btn_declare, btn_scores,btn_back)
    sent = bot.send_message(message.chat.id, 'Выбери нужный пункт.', reply_markup=menu)
    # bot.delete_message(sent.chat.id, sent.id)

def cleaning_done_menu(message):
    menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn_toilet = types.KeyboardButton(text='Туалет')
    btn_kitchen = types.KeyboardButton(text='Кухня')
    btn_bathroom = types.KeyboardButton(text='Ванная')
    btn_way = types.KeyboardButton(text='Коридор')
    btn_dishes = types.KeyboardButton(text='Посуда')
    btn_back = types.KeyboardButton(text='Назад')

    menu.add(btn_toilet,btn_kitchen,btn_bathroom,btn_way,btn_dishes,btn_back)
    sent = bot.send_message(message.chat.id, 'Чем ты помог?', reply_markup=menu)

def get_scores(message):

    # Подключаемся к БД
    db = SQLighter('scores.db', message)

    res = db.get_all_scores()
    for j in range(len(res)): bot.send_message(message.chat.id, res[j])

    db.close()

@bot.message_handler(commands=['start'])
def hello(message):
    # sayhi - variable for starting message
    bot.send_message(message.chat.id, sayhi)


@bot.message_handler(content_types=['text'])
def main(message):
    message_filter(message)

if __name__ == '__main__':
    bot.infinity_polling()
