import telegram
from telegram.ext import Updater
import Commands


bot = telegram.Bot(token='210767489:AAG1Hfr1e3gdI7Ib6XiCB8Ff5pbFEhvgrrU')

print(bot.getMe())
updates = bot.getUpdates()
print([u.message.text for u in updates])

questions = Commands.Questions


def echo(bot, update):
    print("Echo")
    questions.result(bot, update)

# from Commands import Basic

# y = Basic.Start()
# x = Basic.FirstContact()

