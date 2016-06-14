from telegram.ext import Updater
from tinydb import TinyDB, Query

# Admin bot for changing the database with the use of a assigned admin bot.
# Controller_NHLHelpdeskbot

updater = Updater(token='224044671:AAG8-QYX2obXKvUpHcXVwJxM2Yk4WwsouxE')
dispatcher = updater.dispatcher
updater.start_polling()

# A json database, the lib would also integrate well with mongodb
db = TinyDB('db.json')
class Controller:

    def admin(bot, update):
        msg = update.message.text

        # Add command for adding a new QA.
        if msg.startswith("#add "):
            if command_add(msg[5:]):
                bot.sendMessage(chat_id=update.message.chat_id,text="Deze vraag is netjes toegevoegd")
            else:
                bot.sendMessage(chat_id=update.message.chat_id,
                                text="Deze vraag bestaat al, probeer iets anders.")

        # Replace command for replacing an existing QA.
        elif msg.startswith("#replace "):
            if command_replace(msg[9:]):
                bot.sendMessage(chat_id=update.message.chat_id,text="Deze vraag is netjes veranderd")
            else:
                bot.sendMessage(chat_id=update.message.chat_id,
                                text="Deze vraag bestaat niet, probeer iets anders.")

        # Remove command for removing an existing QA.
        elif msg.startswith("#remove "):
            if command_remove(msg[8:]):
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
        cat = arr[2].lower()

    newest = {'type': key, 'response': res, 'category': cat}
    Answers = Query()

    if newest in db.search(Answers.type == key):
        return False
    else:
        db.insert(newest)
        print("Added Response: " + msg)
        return True


def command_remove(key):
    key = key.lower()
    Answers = Query()
    search = db.search(Answers.type == key)
    if len(search) >= 1:
        db.remove(Answers.type == key)
        print("Removed Response: " + key)
        return True
    else:
        return False

def command_replace(msg):
    arr = msg.split("||")
    key = arr[0].lower()
    if command_remove(key):
        if command_add(msg):
            return True
        return False
    return False