from telegram.ext import Updater
from custom.database import Database

updater = Updater(token='224044671:AAG8-QYX2obXKvUpHcXVwJxM2Yk4WwsouxE')
dispatcher = updater.dispatcher
updater.start_polling()

Database_Primary = Database("Answers.txt")
Database_Secondary = Database("Basic.txt")

class Controller:
    def admin(bot,update):
        bot.chat_id = update.message.chat_id
        msg = update.message.text.lower()
        print("Admin Command: " + msg)
        if msg.startswith("#add "):
            bot.sendMessage(chat_id=bot.chat_id, text="Thanks for making me smarter")
            command_add(msg[5:])

    dispatcher.addTelegramMessageHandler(admin)

def command_add(msg):
    arr = msg.split("||")
    key = arr[0]
    ans = arr[1]
    Database_Primary.add(key,ans)
    print("Added Response: "+msg)