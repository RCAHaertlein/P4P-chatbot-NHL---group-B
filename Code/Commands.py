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


def answer(update):
    msg = update.message.text.lower()
    print("Incomming Message")
    if "deeltijdopleiding" in msg:
        if "lang" in msg:
            return "De duur van een opleiding hangt af van verschillende factoren. Associate degrees duren 2 jaar, bacheloropleidingen 4 jaar en masteropleidingen 2 à 3 jaar. Studenten die al eerder een hbo- of universitaire opleiding hebben afgerond, komen vaak in aanmerking voor een verkort traject. Ook verwante vooropleidingen en werkervaring kunnen vrijstellingen opleveren."
        return "NHL Hogeschool biedt circa 40 deeltijdopleidingen aan op twee verschillende niveaus: bachelor en master. Volg je liever een (korte) cursus of leergang? Ook dat kan bij de NHL."

    if "vrijstelling" in msg:
        return "Dat hangt af van jouw vooropleiding en werkervaring. Veel opleidingen voeren een persoonlijk intakegesprek met aankomende studenten. Tijdens dit gesprek wordt bekeken of je in aanmerking komt voor een verkort traject. Ook kun je bellen met een contactpersoon van de opleiding"

    if "lestijd" in msg:
        return "Informatie over de lestijden kun je vinden bij de opleidingsinformatie (nhl.nl). Meestal worden de lessen ’s avonds gegeven. Bij sommige opleidingen vinden de lessen overdag plaats of moet je overdag stage lopen (denk bijvoorbeeld aan de lerarenopleidingen)."

    if "info" in msg or "informatie" in msg:
        return "Waar wil je meer informatie over? (bv. Geld, OV-chipkaart, etc.)"
    if "studiefinanciering" in msg:
        return "Studiefinanciering kun je snel en makkelijk online aanvragen. Het enige dat je daarvoor nodig hebt, is een eigen DigiD met sms-functie. Je logt in bij DUO.nl met je DigiD. Zodra je bent ingelogd, zie je een keuzemenu aan de linkerkant. Een van de keuzes in het menu is 'Studiefinanciering aanvragen'."

    if "geld" in msg:
        return "Je kunt meer informatie vinden over je geldzaken op duo.nl, (TIP: Voor een specifiek antwoord gebruik je bijvoorbeeld studiefinanciering."

    return ""
