from telegram.ext import Updater

class Questions:
    updater = Updater(token='210767489:AAG1Hfr1e3gdI7Ib6XiCB8Ff5pbFEhvgrrU')
    dispatcher = updater.dispatcher

    updater.start_polling()

    def money(bot, update):
        if "geld" in update.message.text.lower():
            bot.sendMessage(chat_id=update.message.chat_id, text="Je kunt meer informatie vinden over je geldzaken op duo.nl, (TIP: Voor een specifiek antwoord gebruik je bijvoorbeeld studiefinanciering.")
    dispatcher.addTelegramMessageHandler(money)

    def other(bot, update):
        if "info" in update.message.text.lower() or "informatie" in update.message.text.lower():
            bot.sendMessage(chat_id=update.message.chat_id, text="Waar wil je meer informatie over? (bv. Geld, OV-chipkaart, etc.)")
        if "studiefinanciering" in update.message.text.lower():
            bot.sendMessage(chat_id=update.message.chat_id, text="Studiefinanciering kun je snel en makkelijk online aanvragen. Het enige dat je daarvoor nodig hebt, is een eigen DigiD met sms-functie. Je logt in bij DUO.nl met je DigiD. Zodra je bent ingelogd, zie je een keuzemenu aan de linkerkant. Een van de keuzes in het menu is 'Studiefinanciering aanvragen'.")
    dispatcher.addTelegramMessageHandler(other)


    # from Commands import Basic

    # y = Basic.Start()
    # x = Basic.FirstContact()

