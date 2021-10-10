def data_check(message):
    with open("Github Data", "r") as file:
        bot.send_message(message.chat.id, file.read())
