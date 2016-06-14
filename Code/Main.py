import telegram
from telegram.ext import Updater
import Users
import Admin

user_bot = telegram.Bot(token='210767489:AAG1Hfr1e3gdI7Ib6XiCB8Ff5pbFEhvgrrU')
admin_bot = telegram.Bot(token='224044671:AAG8-QYX2obXKvUpHcXVwJxM2Yk4WwsouxE')

print(user_bot.getMe())
print(admin_bot.getMe())
admin_updates = admin_bot.getUpdates();
bot_updates = user_bot.getUpdates()
admin = Admin.Controller()
users = Users.Controller()