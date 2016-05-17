import telegram
from telegram.ext import Updater
import Commands
import Admin

user_bot = telegram.Bot(token='210767489:AAG1Hfr1e3gdI7Ib6XiCB8Ff5pbFEhvgrrU')
admin_bot = telegram.Bot(token='224044671:AAG8-QYX2obXKvUpHcXVwJxM2Yk4WwsouxE')

print(user_bot.getMe())
print(admin_bot.getMe())
bot_updates = user_bot.getUpdates()
admin_updates = admin_bot.getUpdates();
print([u.message.text for u in bot_updates])
print([u.message.text for u in admin_updates])

questions = Commands.Questions
admin = Admin.Controller


# from Commands import Basic

# y = Basic.Start()
# x = Basic.FirstContact()

