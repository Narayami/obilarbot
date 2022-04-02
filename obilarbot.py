from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, InlineQueryHandler
import requests
import re
import os

PORT = int(os.environ.get('PORT', 5000))
TOKEN = '5137857279:AAGEWytqKXAhMU2iHFeO4U_7zDAucNyU1OE'

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

updater = Updater('5137857279:AAGEWytqKXAhMU2iHFeO4U_7zDAucNyU1OE')

#---RANDOM DOGS
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
#END RANDOM

#----CUSTOM----
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
#-------END CUSTOM---------

def main():
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('dog', dog))
    updater.dispatcher.add_handler(CommandHandler('zatcho', zatcho))
    updater.dispatcher.add_handler(CommandHandler('snake', snake))
    updater.dispatcher.add_handler(CommandHandler('cordy', cordy))
    updater.dispatcher.add_handler(CommandHandler('chubakamos', chubakamos))
    updater.dispatcher.add_handler(CommandHandler('elguaranapo', elguaranapo))
    updater.dispatcher.add_handler(CommandHandler('poko', poko))

    #old
    #updater.start_polling()
    #new
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://obilarbot.herokuapp.com/' + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()