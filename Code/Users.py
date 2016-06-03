from telegram.ext import Updater
from tinydb import TinyDB, Query
import datetime

db = TinyDB('db.json')
uqdb = TinyDB('uqdb.json')
userCat = {}


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

    ans = find(msg, update.message.chat_id)
    if ans == "":
        ans = find(msg, update.message.chat_id)
        if ans == "":
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            newest = {'type': msg, 'datetime': date}
            uqdb.insert(newest)
            return "Ik heb hier geen antwoord op"
    return ans



def find(msg, id):

    try:
        category = userCat[id]
    except:
        userCat[id] = category = "important"

    Response = Query()



    for cat in db.all():
        if cat['category'] in msg:
            userCat[id] = cat['category']
            break

    for rap in db.search(Response.category == userCat[id]):
        if rap['type'].find("&&") != -1:
            key_new = rap['type'].split("&&")
            if key_new[0] in msg and key_new[1] in msg:
                return rap['response']
        if rap['type'] in msg:
            return rap['response']
    try:
        if userCat[id] is "important":
            userCat[id] = "low"
        else:
            userCat[id] = "important"
    except:
        userCat[id] = "important"

    return ""
