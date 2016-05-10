from telegram.ext import Updater


class Questions:
    updater = Updater(token='210767489:AAG1Hfr1e3gdI7Ib6XiCB8Ff5pbFEhvgrrU')
    dispatcher = updater.dispatcher

    updater.start_polling()

    def result(bot, update):
        ans = answer(update)
        if ans != "":
            bot.sendMessage(chat_id=update.message.chat_id, text=ans)

    dispatcher.addTelegramMessageHandler(result)

    # from Commands import Basic

    # y = Basic.Start()
    # x = Basic.FirstContact()

newDict = {}
with open('Answers.txt', 'r') as f:
    for line in f:
        splitLine = line.split("||")
        newDict[splitLine[0]] = splitLine[1]


def answer(update):
    msg = update.message.text.lower()
    print("Incoming Message")
    for key in newDict:
        if key.find("&&") != -1:
            newKey = key.split("&&")
            if newKey[0] in msg and newKey[1] in msg:
                return newDict[key]

        if msg.find(key) != -1:
            return newDict[key]

    return "Ik heb hier geen antwoord op."

