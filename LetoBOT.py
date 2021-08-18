import telebot


TOKEN = '1959827955:AAGyaZ8JH8ICuhTLz1bN9kqAy9odxZhAM1o'

bot = telebot.TeleBot(TOKEN, parse_mode=None)


bot.polling()