from telegram.ext import Updater
from custom.database import Database

updater = Updater(token='224044671:AAG8-QYX2obXKvUpHcXVwJxM2Yk4WwsouxE')
dispatcher = updater.dispatcher
updater.start_polling()

Database_Primary = Database("Answers.txt")
Database_Secondary = Database("Basic.txt")

def result(update):
    msg = update.message.text.lower()
    if msg.startswith("/add "):
        command_add(msg[4:])

def command_add(msg):
    arr = msg.split("||")
    key = arr[0]
    ans = arr[1]