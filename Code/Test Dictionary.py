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

newDict = {}
with open('Answers.txt', 'r') as f:
    for line in f:
        splitLine = line.split("||")
        key = splitLine[0]
        answer = splitLine[1]
        newDict[key] = answer
print(newDict["geld"])
