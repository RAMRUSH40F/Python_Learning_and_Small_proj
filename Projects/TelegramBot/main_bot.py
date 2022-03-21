import telebot
from telebot import types
from config import token

bot = telebot.TeleBot(token)
hideBoard = types.ReplyKeyboardRemove()

@bot.message_handler(func = lambda message: True, commands=['Купить'])
def menue(message):

    menu = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_back = types.KeyboardButton(text= 'Назад')
    btn_stone = types.KeyboardButton(text= 'Камень с глазами')

    menu.add(btn_back, btn_stone)
    bot.send_message(message.chat.id,'Выбирайте зи широкого ассортимента', reply_markup=menu)

@bot.message_handler(func = lambda message: True, commands=['камень с глазами'])
def price(message):
    bot.send_photo(message.chat.id, r'https://ucarecdn.com/e3c749ec-5426-40f9-9060-20f7a236cb4b/', 'Камень с глазами 1000$')


@bot.message_handler(func = lambda message: True)
def gagagw(message):
    # callback = f'Я пробил информацию\nid чата:{message.chat.id}\nid пользователя:{message.from_user.id}\nИмя:{message.from_user.first_name}\nФамилия{message.from_user.last_name}\nПсевдоним:{message.from_user.username}\n Текст сообщения:/start'
    kb = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width=1)
    btn_buy = types.KeyboardButton(text= 'Купить')

    kb.add(btn_buy)
    bot.send_message(message.chat.id,'1', reply_markup=hideBoard)



if __name__ == '__main__':
    bot.infinity_polling()
