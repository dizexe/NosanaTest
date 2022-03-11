import telebot	
import config	
from telebot import types 

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

	bot.send_message(message.chat.id, "Привет, {0.first_name}\nЯ - <b>{1.first_name}</b>.".format(message.from_user, bot.get_me()),
		parse_mode='html')

@bot.message_handler(commands=['help'])
def help(message):

	bot.send_message(message.chat.id, "Я умею отвечать на несколько простых фраз. Вот их список: 'привет', 'как дела?', 'что делаешь?', 'сколько тебе лет?'.".format(message.from_user, bot.get_me()),
		parse_mode='html')

@bot.message_handler(content_types= ['text'])
def get_text(message):
	if message.text.lower() == 'привет':
		bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html')
	elif message.text.lower() == 'как дела?':
		bot.send_message(message.chat.id, "Отлично! У тебя как?".format(message.from_user, bot.get_me()),
		parse_mode='html')
	elif message.text.lower() == 'что делаешь?':
		bot.send_message(message.chat.id, "Существую, а ты?".format(message.from_user, bot.get_me()),
		parse_mode='html')
	elif message.text.lower() == 'сколько тебе лет?':
		bot.send_message(message.chat.id, "Неважно, а тебе?".format(message.from_user, bot.get_me()),
		parse_mode='html')


bot.polling(none_stop=True, interval=0)
