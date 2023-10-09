

from telegram import Update
from telegram.ext import Application,ComandHandler,MessageHandler,filters,ContextTypes

token = '6480837188:AAGuOMa7Xq8r2Y_Ibk5aOoXqf7dIpmoL-kY'
user_name = 'jefemaestrobot'

async def start(update: Update , context:ContextTypes):
    await update.message.reply_text('hola soy un bot en que puedo ayudarte')

async def help(update: Update , context:ContextTypes):
    await update.message.reply_text('Ayudaaaaaaaa')

async def custom(update: Update , context:ContextTypes):
    await update.message.reply_text(update.message.text)


def handle_response(text:str,context: ContextTypes,update:Update):
    proccesed_text = text.lower()

    print(proccesed_text)
    if 'hola' in proccesed_text:
        return 'hola como estas'
    elif 'adios' in proccesed_text:
        return 'adios'
    else:
        return 'no te entiendo '
