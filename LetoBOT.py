import telebot
from telebot import types

chat_id = 790886004
TOKEN = '1959827955:AAGyaZ8JH8ICuhTLz1bN9kqAy9odxZhAM1o'

bot = telebot.TeleBot(TOKEN, parse_mode=None)

# Убеждаемся в том, что человек готов начать вводить данные, рисуем кнопку start и предлагаем нажать на неё
markup_start = types.ReplyKeyboardMarkup(row_width=1)
itembtn_start = types.KeyboardButton('/start')
markup_start.add(itembtn_start)
bot.send_message(chat_id, 'Если вы готовы начать, нажмите на кнопку ниже:', reply_markup = markup_start)
# Создаём список показаний по квартирам и счётчик добавления значения для квартиры
values_list = ['0']
save_counter = 1
message_temp = ''

# Принимаем команду /start и начинаем ввод данных в список 
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(chat_id, 'Введите показания для кв.1:')

# Проверяет сообщение, если оно в
@bot.message_handler(func=lambda message: True)
 
def confirm(message):
    global save_counter
    global values_list
    global message_temp
    if message.text == 'Подтвердить':
        values_list.append(message_temp)
        save_counter += 1
        bot.send_message(chat_id, f'Введите показания для кв.{save_counter}:')
    else: #если пришло любое значение кроме Confirm
        message_temp = message.text
        markup_confirm = types.ReplyKeyboardMarkup(row_width=1)
        itembtn_confirm = types.KeyboardButton('Подтвердить')
        markup_confirm.add(itembtn_confirm)
        bot.send_message(chat_id, 'Подтвердите введенное значение либо введите новое значение:', reply_markup = markup_confirm)
    
  
    
    
    
    


       
bot.polling())
