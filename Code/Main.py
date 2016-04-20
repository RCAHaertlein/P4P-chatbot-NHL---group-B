import telegram
from telegram.ext import Updater


bot = telegram.Bot(token='210767489:AAG1Hfr1e3gdI7Ib6XiCB8Ff5pbFEhvgrrU')

print(bot.getMe())
updates = bot.getUpdates()
print([u.message.text for u in updates])

chat_id = bot.getUpdates()[-1].message.chat_id
# except:
# print("Game breaking error")
bot.sendMessage(chat_id=chat_id, text="test")

print(chat_id)

updater = Updater(token='210767489:AAG1Hfr1e3gdI7Ib6XiCB8Ff5pbFEhvgrrU')
dispatcher = updater.dispatcher


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Ik ben een bot die hulp ""bied aan nieuwe NHL studenten")

dispatcher.addTelegramCommandHandler('start', start)

updater.start_polling()


def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Ik ben een bot. Ik ben ontworpen om de nieuwe studenten aan "
                                                         "het NHL te helpen met het begin van hun opleiding")

dispatcher.addTelegramMessageHandler(echo)


# from Commands import Basic

# y = Basic.Start()
# x = Basic.FirstContact()

