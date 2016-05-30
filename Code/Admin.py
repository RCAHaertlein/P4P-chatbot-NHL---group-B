from telegram.ext import Updater
from tinydb import TinyDB, Query

updater = Updater(token='224044671:AAG8-QYX2obXKvUpHcXVwJxM2Yk4WwsouxE')
dispatcher = updater.dispatcher
updater.start_polling()

db = TinyDB('db.json')
class Controller:

    def admin(bot, update):
        msg = update.message.text
        print("Admin Command: " + msg)
        if msg.startswith("#add "):
            if command_add(msg[5:]) == True:
                bot.sendMessage(chat_id=update.message.chat_id,text="Deze vraag is netjes toegevoegd")
            else:
                bot.sendMessage(chat_id=update.message.chat_id,
                                text="Deze vraag bestaat al, probeer iets anders.")
        elif msg.startswith("#replace "):
            if command_replace(msg[9:]) == True:
                bot.sendMessage(chat_id=update.message.chat_id,text="Deze vraag is netjes veranderd")
            else:
                bot.sendMessage(chat_id=update.message.chat_id,
                                text="Deze vraag bestaat niet, probeer iets anders.")
        elif msg.startswith("#remove "):
            if command_remove(msg[8:]) == True:
                bot.sendMessage(chat_id=update.message.chat_id, text="Deze vraag is netjes verwijderd")
            else:
                bot.sendMessage(chat_id=update.message.chat_id,
                                text="Deze vraag bestaat niet, probeer iets anders.")




    dispatcher.addTelegramMessageHandler(admin)

def command_add(msg):
    if msg.find("||") < 1:
        return False
    arr = msg.split("||")
    key = arr[0].lower()
    res = arr[1]
    cat = 'important'
    if len(arr) > 2:
        cat = arr[2]

    newest = {'type': key, 'response': res, 'category': cat}
    Answers = Query()

    if newest in db.search(Answers.type == key):
        return False
    else:
        db.insert(newest)
        print("Added Response: " + msg)
        return True

def command_replace(msg):
    arr = msg.split("||")
    key = arr[0].lower()
    if command_remove(key):
        if command_add(msg):
            return True
        return False
    return False

def command_remove(key):
    # Act if response is nothing
    key = key.lower()
    Answers = Query()
    print(key)
    search = db.search(Answers.type == key)
    if len(search) >= 1:
        db.remove(Answers.type == key)
        print("Removed Response: " + key)
        return True
    else:
        return False