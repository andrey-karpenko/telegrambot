from flask import Flask
import telebot
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def homepage():
    the_time = datetime.now()

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)


if __name__ == '__main__':

    bot = telebot.TeleBot("789395928:AAFBmhaqbbOvFaj0fb-5Hl-xGdPZJDVhtks")

    @bot.message_handler(content_types=["text"])
    def send_echo(message):
        bot.send_message(message.chat.id, message.text)

    #bot.polling(none_stop=True)

    app.run(debug=True, use_reloader=True)

