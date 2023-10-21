from pyrogram import Client, filters
import random

@Client.on_message(filters.command("start"))
def start(client, message):
    client.send_message(
        chat_id=message.chat.id,
        text="Sayı tahmin etme oyununa hoş geldiniz! 1 ile 100 arasında bir sayı tuttum. Tahminlerinizi yapabilirsiniz."
    )

@Client.on_message(filters.command("guess"))
def guess(client, message):
    try:
        user_guess = int(message.text.split()[1])
        random_number = random.randint(1, 100)

        if user_guess == random_number:
            client.send_message(
                chat_id=message.chat.id,
                text="Tebrikler! Doğru tahmin ettiniz."
            )
        elif user_guess < random_number:
            client.send_message(
                chat_id=message.chat.id,
                text="Daha yüksek bir sayı tahmin edin."
            )
        else:
            client.send_message(
                chat_id=message.chat.id,
                text="Daha düşük bir sayı tahmin edin."
            )
    except IndexError:
        client.send_message(
            chat_id=message.chat.id,
            text="Lütfen bir sayı girin."
        )
    except ValueError:
        client.send_message(
            chat_id=message.chat.id,
            text="Geçersiz bir sayı girdiniz."
        )
        
