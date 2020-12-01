from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
import  logging

updater = Updater(token = "1445964032:AAEQjWjtVuRZ94vcTclsBiMgCdAWa7xkp8g", use_context = True)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
#need to update handler
dispatcher = updater.dispatcher

#function
def start(update, context):
	context.bot.send_message(chat_id = update.effective_chat.id, text = "hlo i m working")

start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

#2nd function
def echo(update, context):
	context.bot.send_message(chat_id = update.effective_chat.id, text =update.message.text)

message_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(message_handler)



updater.start_polling()

