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
values_list_day = ['0'] 
values_list_night = ['0']
save_counter = 1
# Временное хранилище для сообщений
message_temp_str = ''
message_temp_list = []

# Принимаем команду /start и начинаем ввод данных в список 
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(chat_id, 'Отлично! Показания следует вводить таком виде: день/ночь')
    bot.send_message(chat_id, 'Введите показания для кв.1:')

# Получает сообщение, сохраняет во временное хранилище, проверяет правильность ввода, сохраняет сообщение в список
@bot.message_handler(func=lambda message: True)
 
def confirm(message):
    global save_counter, values_list_day, values_list_night, message_temp_str, message_temp_list
    
    if message.text == f'Подтвердить значение: {message_temp_str} кВт*ч':
        values_list_day.append(message_temp_list[0])
        try:
            values_list_night.append(message_temp_list[1])
        except:
            values_list_night.append('0')
        save_counter += 1
        bot.send_message(chat_id, f'Введите показания для кв.{save_counter}:')
    
    elif message.text.startswith('Подтвердит') == False:
        message_temp_str = message.text
        try:
            message_temp_list = message.text.split('/')
        except:
            message_temp_list.append(message.text)
        markup_confirm = types.ReplyKeyboardMarkup(row_width=1)
        itembtn_confirm = types.KeyboardButton(f'Подтвердить значение: {message_temp_str} кВт*ч')
        markup_confirm.add(itembtn_confirm)
        bot.send_message(chat_id, f'Подтвердите ввод {message_temp_str} кВт*ч для кв.{save_counter} либо введите новое значение:', reply_markup = markup_confirm)
    
  

    
    
    


       
bot.polling()
