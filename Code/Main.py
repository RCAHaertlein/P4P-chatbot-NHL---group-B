import telegram
from telegram.ext import Updater
import Commands as Command


bot = telegram.Bot(token='210767489:AAG1Hfr1e3gdI7Ib6XiCB8Ff5pbFEhvgrrU')

print(bot.getMe())
updates = bot.getUpdates()
print([u.message.text for u in updates])

chat_id = bot.getUpdates()[-1].message.chat_id
# except:
# print("Game breaking error")
bot.sendMessage(chat_id=chat_id, text="Hallo, ik ben een NHL bot die jou probeert te helpen om te starten met jou studie.")

questions = Command.Questions

def echo(bot, update):
    questions.money(bot, update)
    questions.other(bot, update)

# from Commands import Basic

# y = Basic.Start()
# x = Basic.FirstContact()

