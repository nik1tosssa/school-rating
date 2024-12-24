import telebot
from telebot import types

# Ваш токен, полученный от BotFather
TOKEN = '7730686653:AAGPAka_brixx23dXCxoK3VFjyFDx83ICfk'

bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    clear_button = types.InlineKeyboardButton("Очистить чат", callback_data="clear_chat") 
    markup.add(clear_button) 


    btn1 = types.KeyboardButton("clear all")
    btn2 = types.KeyboardButton("Кнопка 2")
    btn3 = types.KeyboardButton("Кнопка 3")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Привет! Выберите одну из опций:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "clear_chat")
def clear_chat(call): 
    # Удаляем все сообщения в чате 
    bot.delete_message(call.message.chat.id, call.message.message_id) 
    #bot.send_message(call.message.chat.id, "Чат очищен!")

    
# Обработчик нажатий на кнопки
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "clear all":
        clear_chat()
    elif message.text == "Кнопка 2":
        bot.reply_to(message, "Вы нажали на кнопку 2")
    elif message.text == "Кнопка 3":
        bot.reply_to(message, "Вы нажали на кнопку 3")
    else:
        bot.reply_to(message, "Неизвестная команда")



# Запуск бота
bot.polling()
