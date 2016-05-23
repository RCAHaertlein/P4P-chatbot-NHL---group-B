from telegram.ext import Updater
from datapy.datapy import Datapy

datapy = Datapy("Basic.txt")

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
    data_high = datapy.get("Answers.txt")
    data_low = datapy.get("Basic.txt")

    ans = find(data_high.dictionary, msg)
    with open('Questions.txt', 'a') as f:
        f.write(msg)
        if ans != "":
            f.write(" : " + ans + "\n")
            return ans
        else:
            ans = find(data_low.dictionary, msg)
            if ans != "":
                f.write(" : " + ans + "\n")
                return ans
        f.write(" : Ik heb hier geen antwoord op. \n")
    return "Ik heb hier geen antwoord op."


def find(dicti,msg):
    for key in dicti:
        if key.find("&&") != -1:
            key_new = key.split("&&")
            if key_new[0] in msg and key_new[1] in msg:
                return dicti[key]

        if msg.find(key) > -1:
            return dicti[key]

    return ""