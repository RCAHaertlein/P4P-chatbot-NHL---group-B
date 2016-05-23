from telegram.ext import Updater
from custom.database import Database

updater = Updater(token='224044671:AAG8-QYX2obXKvUpHcXVwJxM2Yk4WwsouxE')
dispatcher = updater.dispatcher
updater.start_polling()

data = Database("Answers.txt")
class Controller:

    def admin(bot, update):
        msg = update.message.text.lower()
        print("Admin Command: " + msg)
        if msg.startswith("#add "):
            if command_add(msg[5:]) == True:
                bot.sendMessage(chat_id=update.message.chat_id,text="De vraag is netjes toegevoegd")
            else:
                bot.sendMessage(chat_id=update.message.chat_id,
                                text="Deze vraag bestaat al, probeer iets anders.")




    dispatcher.addTelegramMessageHandler(admin)

def command_add(msg):
    arr = msg.split("||")
    key = arr[0]
    # Act if key is nothing
    res = arr[1]
    # Act if response is nothing
    if key in data.dictionary:
        #bot.sendMessage(chat_id=update.message.chat_id, text="I'm sorry but there already is an answer to this keyword")
        return False
    else:
        data.add(key, res)
        print("Added Response: " + msg)
        data.reload()
        return True
        #bot.sendMessage(chat_id=update.message.chat_id, text="The answer to " + key + " has been successfully added.")