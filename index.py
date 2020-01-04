from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
import requests
import re
import logging


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def chooseYourdDestiny(update, context):
    if (context == "овен"):
         context.bot.send_message(chat_id=update.effective_chat.id, text="pidr")



def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ну и какой твой знак зодиака?")
def main():
    updater = Updater('996860285:AAH0TI4Lb7rqKXQ8VLZUAu2TmnngolK1_J8', use_context=True)
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
    dp = updater.dispatcher
    start_handler = CommandHandler('start', start)
    choose_handler = CommandHandler('sign', chooseYourdDestiny)
    echo_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(echo_handler)
    dp.add_handler(start_handler)
    dp.add_handler(choose_handler)
    updater.start_polling()
    updater.idle()

main()
