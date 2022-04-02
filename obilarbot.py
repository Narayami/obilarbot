from lib2to3.pgen2 import token
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, InlineQueryHandler
import requests
import re
import os
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

PORT = int(os.environ.get('PORT', 8443))

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    image_url = contents['url']

    return image_url

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def dog(update, context):
    url = get_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def zatcho(update, context):    
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id, 'https://imgur.com/Pbtrt1V')
def snake(update, context):    
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id, 'https://imgur.com/BmQrayJ')
def cordy(update, context):    
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id, 'https://imgur.com/rjZwCbv')
def chubakamos(update, context):    
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id, 'https://imgur.com/B3Ydqe8')
def elguaranapo(update, context):    
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id, 'https://imgur.com/q8YFtb8')
def poko(update, context):    
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id, 'https://imgur.com/LQ0uiwX')

def error(update, context):
    """Logs Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    TOKEN = '5137857279:AAGEWytqKXAhMU2iHFeO4U_7zDAucNyU1OE'
    APP_NAME='https://obilarbot.herokuapp.com/'
    updater = Updater(TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('dog', dog))
    updater.dispatcher.add_handler(CommandHandler('zatcho', zatcho))
    updater.dispatcher.add_handler(CommandHandler('snake', snake))
    updater.dispatcher.add_handler(CommandHandler('cordy', cordy))
    updater.dispatcher.add_handler(CommandHandler('chubakamos', chubakamos))
    updater.dispatcher.add_handler(CommandHandler('elguaranapo', elguaranapo))
    updater.dispatcher.add_handler(CommandHandler('poko', poko))


    updater.dispatcher.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN, webhook_url=APP_NAME + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()