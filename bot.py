import telegram
import logging
from telegram.ext import Updater, CommandHandler

#Configurar el logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#Inicializar el bot con el token
bot = telegram.Bot(token='TOKEN_DE_TELEGRAM')

#Inicializar el Updater
updater = Updater(token='TOKEN_DE_TELEGRAM', use_context=True)
dispatcher = updater.dispatcher

#Manejador para el comando /info
def info(update, context):
    #Obtener la información del usuario
    user_id = update.message.from_user.id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    username = update.message.from_user.username
    
    #Enviar la información del usuario al chat
    message = f"ID: {user_id}\nNombre: {first_name} {last_name}\nUsername: @{username}"
    update.message.reply_text(message)

#Añadir el manejador para el comando /info
dispatcher.add_handler(CommandHandler('info', info))

#Iniciar el bot
updater.start_polling()
