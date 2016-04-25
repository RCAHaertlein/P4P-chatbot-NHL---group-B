import telegram
from telegram.ext import Updater
import Commands
import sys


bot = telegram.Bot(token='210767489:AAG1Hfr1e3gdI7Ib6XiCB8Ff5pbFEhvgrrU')

print(bot.getMe())
updates = bot.getUpdates()
print([u.message.text for u in updates])

try:
    chat_id = bot.getUpdates()[-1].message.chat_id
except:
    sys.exit("Error: make sure there are new messages, before starting the bot")

# except:
# print("Game breaking error")
bot.sendMessage(chat_id=chat_id, text="Hallo, ik ben een NHL bot die jou probeert te helpen om te starten met jou studie.")

questions = Commands.Questions

def echo(bot, update):
    questions.money(bot, update)
    questions.other(bot, update)

# from Commands import Basic

# y = Basic.Start()
# x = Basic.FirstContact()

