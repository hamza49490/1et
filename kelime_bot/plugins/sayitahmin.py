from pyrogram import Client, filters
from pyrogram.types import Message
import random

@Client.on_message(filters.command("start"))
def start(bot: Client, msg: Message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Sayı tahmin etme oyununa hoş geldiniz! 1 ile 100 arasında bir sayı tuttum. Tahminlerinizi yapabilirsiniz."
    )

@Client.on_message(filters.command("guess"))
def guess(bot: Client, message: Message):
    try:
        user_guess = int(message.text.split()[1])
        random_number = random.randint(1, 100)

        if user_guess == random_number:
            bot.send_message(
                chat_id=message.chat.id,
                text="Tebrikler! Doğru tahmin ettiniz."
            )
        elif user_guess < random_number:
            bot.send_message(
                chat_id=message.chat.id,
                text="Daha yüksek bir sayı tahmin edin."
            )
        else:
            bot.send_message(
                chat_id=message.chat.id,
                text="Daha düşük bir sayı tahmin edin."
            )
    except IndexError:
        bot.send_message(
            chat_id=message.chat.id,
            text="Lütfen bir sayı girin."
        )
    except ValueError:
        bot.send_message(
            chat_id=message.chat.id,
            text="Geçersiz bir sayı girdiniz."
        )
        
