import telegram
from telegram.ext import Updater, CommandHandler

# Вставьте сюда ваш токен API
TOKEN = '7730686653:AAGPAka_brixx23dXCxoK3VFjyFDx83ICfk'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я ваш новый бот.")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
