import telebot
from telebot import types

chat_id = 790886004
TOKEN = '0001959827955:AAGyaZ8JH8ICuhTLz1bN9kqAy9odxZhAM1o'

bot = telebot.TeleBot(TOKEN, parse_mode=None)

# Убеждаемся в том, что человек готов начать вводить данные, рисуем кнопку start и предлагаем нажать на неё

markup_start = types.ReplyKeyboardMarkup(row_width=1)
itembtn_start = types.KeyboardButton('/start')
markup_start.add(itembtn_start)
bot.send_message(chat_id, 'Если вы готовы начать, нажмите на кнопку ниже:', reply_markup = markup_start)



# Создаём список показаний по квартирам,  и счётчик добавления значения для квартиры
values_list_day = ['0'] 
values_list_night = ['0']
meter_value = []
save_counter = 1
# Временное хранилище для сообщений
message_temp_str = ''
message_temp_list = []

# Принимаем команду /start и начинаем ввод данных в список 
@bot.message_handler(commands=['start', 'finish'])
def send_welcome(message):
    markup_variants = types.ReplyKeyboardMarkup(row_width=2)
    itembtn_flats = types.KeyboardButton('Ввод показаний по квартирам')
    itembtn_house = types.KeyboardButton('Ввод показаний общедомового счётчика')
    markup_variants.add(itembtn_flats, itembtn_house)
    bot.send_message(chat_id, 'Отлично! Выберите показания, которые хотите ввести.', reply_markup = markup_variants)
    
# Получает сообщение, сохраняет во временное хранилище, проверяет правильность ввода, сохраняет сообщение в список
@bot.message_handler(func=lambda message: True)
 
def message_use(message):
    global save_counter, values_list_day, values_list_night, message_temp_str, message_temp_list, meter_value
    
    if message.text == 'Ввод показаний по квартирам':
        bot.send_message(chat_id, f'Введите показания для кв.{save_counter}:')
        
    if message.text[0].isdigit() == True and message_temp_str != 'Ввод показаний общедомового счётчика':
        
        message_temp_str = message.text
        try:
            message_temp_list = message.text.split('/')
        except:
            message_temp_list.append(message.text)
            
        markup_confirm = types.ReplyKeyboardMarkup(row_width=1)
        itembtn_confirm = types.KeyboardButton(f'Подтвердить значение: {message_temp_str} кВт*ч')
        markup_confirm.add(itembtn_confirm)
        bot.send_message(chat_id, f'Подтвердите ввод {message_temp_str} кВт*ч для кв.{save_counter} либо введите новое значение:', reply_markup = markup_confirm)    
       
    if message.text == f'Подтвердить значение: {message_temp_str} кВт*ч':
        values_list_day.append(message_temp_list[0])
        
        try:
            values_list_night.append(message_temp_list[1])
        except:
            values_list_night.append('0')
            
        save_counter += 1
        if save_counter > 5:
            markup_finish = types.ReplyKeyboardMarkup(row_width=1)
            itembtn_finish = types.KeyboardButton('/finish')
            markup_finish.add(itembtn_finish)
            bot.send_message(chat_id, 'Данные по квартирам успешно введены', reply_markup = markup_finish)
        else:
            bot.send_message(chat_id, f'Введите показания для кв.{save_counter}:')
                
    if message_temp_str == 'Ввод показаний общедомового счётчика':
        message_temp_str = message.text
        markup_confirm = types.ReplyKeyboardMarkup(row_width=1)
        itembtn_confirm = types.KeyboardButton(f'Подтвердить значение: {message.text} кВт*ч для общедомого счётчика')
        markup_confirm.add(itembtn_confirm)
        bot.send_message(chat_id, f'Подтвердите ввод {message.text} кВт*ч для общедомого счётчика либо введите новое значение:', reply_markup = markup_confirm)        
    
    if message.text == 'Ввод показаний общедомового счётчика':
        message_temp_str = message.text
        bot.send_message(chat_id, f'Введите показание общедомового счётчика:')
        
    
        
    if message.text.count('кВт*ч для общедомого счётчика') > 0:
        try:
            meter_value = message_temp_str.split('/')
        except:
            meter_value.append('0')
        markup_finish = types.ReplyKeyboardMarkup(row_width=1)
        itembtn_finish = types.KeyboardButton('/finish')
        markup_finish.add(itembtn_finish)
        bot.send_message(chat_id, 'Данные по общедомовому счётчику успешно введены', reply_markup = markup_finish)    
        
        
    
bot.polling()
