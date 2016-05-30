from telegram.ext import Updater
from tinydb import TinyDB, Query

db = TinyDB('db.json')
class Controller:
    updater = Updater(token='210767489:AAG1Hfr1e3gdI7Ib6XiCB8Ff5pbFEhvgrrU')
    dispatcher = updater.dispatcher
    updater.start_polling()

    def result(bot, update):
        ans = answer(update)
        print("Outcomming Message ( " + ans + " )")
        if ans != "":
            bot.sendMessage(chat_id=update.message.chat_id, text=ans)

    dispatcher.addTelegramMessageHandler(result)

    # from Commands import Basic

    # y = Basic.Start()
    # x = Basic.FirstContact()


def answer(update):
    msg = update.message.text.lower()
    print("Incoming Message ( " + msg + " )")
    return find(msg)



def find(msg):
    Response = Query()
    for rap in db.all():
        if rap['type'].find("&&") != -1:
            key_new = rap['type'].split("&&")
            if key_new[0] in msg and key_new[1] in msg:
                return rap['response']
        if rap['type'] in msg:
            return rap['response']
    return "Ik heb hier geen antwoord op."