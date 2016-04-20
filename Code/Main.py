import telegram
from telegram.ext import Updater


bot = telegram.Bot(token='210767489:AAG1Hfr1e3gdI7Ib6XiCB8Ff5pbFEhvgrrU')

print(bot.getMe())
updates = bot.getUpdates()
print([u.message.text for u in updates])

chat_id = bot.getUpdates()[-1].message.chat_id
# except:
# print("Game breaking error")
bot.sendMessage(chat_id=chat_id, text="Hallo, ik ben een NHL bot die jou probeert te helpen om te starten met jou studie.")

print(chat_id)

updater = Updater(token='210767489:AAG1Hfr1e3gdI7Ib6XiCB8Ff5pbFEhvgrrU')
dispatcher = updater.dispatcher

updater.start_polling()


def echo(bot, update):
    if "info" in update.message.text.lower() or "informatie" in update.message.text.lower():
        bot.sendMessage(chat_id=update.message.chat_id, text="Waar wil je meer informatie over? (bv. Geld, OV-chipkaart, etc.)")
    if "geld" in update.message.text.lower():
        bot.sendMessage(chat_id=update.message.chat_id, text="Je kunt meer informatie vinden over je geldzaken op duo.nl, (TIP: Voor een specifiek antwoord gebruik je bijvoorbeeld studiefinanciering.")
    if "studiefinanciering" in update.message.text.lower():
        bot.sendMessage(chat_id=update.message.chat_id, text="Studiefinanciering kun je snel en makkelijk online aanvragen. Het enige dat je daarvoor nodig hebt, is een eigen DigiD met sms-functie. Je logt in bij DUO.nl met je DigiD. Zodra je bent ingelogd, zie je een keuzemenu aan de linkerkant. Een van de keuzes in het menu is 'Studiefinanciering aanvragen'.")
dispatcher.addTelegramMessageHandler(echo)


# from Commands import Basic

# y = Basic.Start()
# x = Basic.FirstContact()

