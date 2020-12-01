from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
import  logging
import os

PORT = int(os.environ.get("PORT", 5000))
TOKEN = "1445964032:AAEQjWjtVuRZ94vcTclsBiMgCdAWa7xkp8g"
updater = Updater(token = "1445964032:AAEQjWjtVuRZ94vcTclsBiMgCdAWa7xkp8g", use_context = True)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
#need to update handler
dispatcher = updater.dispatcher

#function
def start(update, context):
	context.bot.send_message(chat_id = update.effective_chat.id, text = "Hey! Master I am anonymou_sender Bot And I m Alive")

start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

#2nd function
def echo(update, context):
	context.bot.send_message(chat_id = update.effective_chat.id, text =update.message.text)

message_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(message_handler)

if __name__ == "__main__":
	updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
updater.bot.setWebhook('https://anonymous-boter.herokuapp.com/' + TOKEN)

