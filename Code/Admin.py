from telegram.ext import Updater
from datapy.datapy import Datapy

updater = Updater(token='224044671:AAG8-QYX2obXKvUpHcXVwJxM2Yk4WwsouxE')
dispatcher = updater.dispatcher
updater.start_polling()

datapy = Datapy("Answers.txt")
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
        elif msg.startswith("#replace "):
            if command_replace(msg[9:]) == True:
                bot.sendMessage(chat_id=update.message.chat_id,text="De vraag is netjes veranderd")
            else:
                bot.sendMessage(chat_id=update.message.chat_id,
                                text="Deze vraag bestaat niet, probeer iets anders.")
        elif msg.startswith("#remove "):
            if command_remove(msg[8:]) == True:
                bot.sendMessage(chat_id=update.message.chat_id, text="De vraag is netjes verwijderd")
            else:
                bot.sendMessage(chat_id=update.message.chat_id,
                                text="Deze vraag bestaat niet, probeer iets anders.")
    dispatcher.addTelegramMessageHandler(admin)


def command_add(msg):
    data = datapy.get("Answers.txt")
    arr = msg.split("||")
    key = arr[0]
    # Act if key is nothing
    res = arr[1]

    # Act if response is nothing
    if key in data.dictionary:
        return False
    else:
        data.add(key, res)
        print("Added Response: " + msg)
        return True


def command_replace(msg):
    data = datapy.get("Answers.txt")
    arr = msg.split("||")
    key = arr[0]
    # Act if key is nothing
    res = arr[1]

    # Act if response is nothing
    if key in data.dictionary:
        data.replace(key, res)
        print("Changed Response: " + msg)
        data.reload()
        return True
    else:
        return False


def command_remove(key):
    data = datapy.get("Answers.txt")

    # Act if response is nothing
    if key in data.dictionary:
        data.remove(key)
        print("Removed Response: " + key)
        return True
    else:
        return False