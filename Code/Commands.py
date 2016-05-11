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
basicDict = {}
with open('Answers.txt', 'r') as f:
    for line in f:
        splitLine = line.split("||")
        newDict[splitLine[0]] = splitLine[1]
with open('Basic.txt', 'r') as f:
    for line in f:
        splitLine = line.split("||")
        basicDict[splitLine[0]] = splitLine[1]


def answer(update):
    msg = update.message.text.lower()
    print("Incoming Message ( " + msg + " )")
    ans = find(newDict,msg)
    with open('Questions.txt', 'a') as f:
        f.write(msg)
        if ans != "":
            f.write(" : " + ans + "\n")
            return ans
        else:
            ans = find(basicDict,msg)
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