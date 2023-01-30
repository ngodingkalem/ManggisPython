from module import Telegram

bot = Telegram('BOT_TOKEN', 'TIME_ZONE')

while True:
    if bot.centMessage:
        if bot.coftMessage():
            bot.postReq()
    if bot.trigger():
        bot.postReq()