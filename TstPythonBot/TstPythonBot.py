import telebot

bot = telebot.TeleBot("789395928:AAFBmhaqbbOvFaj0fb-5Hl-xGdPZJDVhtks")


@bot.message_handler(content_types=["text"])
def send_echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
