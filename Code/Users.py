from telegram.ext import Updater
from tinydb import TinyDB, Query
import datetime

db = TinyDB('db.json')
uqdb = TinyDB('uqdb.json')
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
    ans = find(msg, "important")
    if ans == "":
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        newest = {'type': msg, 'datetime': date}
        uqdb.insert(newest)
        return "Ik heb hier geen antwoord op"
    return ans



def find(msg, category):
    Response = Query()
    for rap in db.search(Response.category == category):
        if rap['type'].find("&&") != -1:
            key_new = rap['type'].split("&&")
            if key_new[0] in msg and key_new[1] in msg:
                return rap['response']
        if rap['type'] in msg:
            return rap['response']
    return ""
