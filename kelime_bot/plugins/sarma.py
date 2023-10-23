from pyrogram import Client, filters
import requests
import time


buket sadece harflerle yazılan mesajları algılasın, diğer mesajları algılamasın, kodları buna göre düzenle ve paylaş .

@app.on_message(filters.command(["start"]))
def start(client, message):
    buttons = [
        ["/single", "/multi"]
    ]
    client.send_message(
        chat_id=message.chat.id,
        text="Merhaba! Kelime sarmalı oyununa hoş geldiniz. Oyuna başlamak için aşağıdaki butonlardan birini seçebilirsiniz.",
        reply_markup=client.build_reply_markup(buttons)
    )

@app.on_message(filters.command(["single"]))
def single_mode(client, message):
    if message.chat.type == "private":
        client.send_message(
            chat_id=message.chat.id,
            text="Tekli mod sadece gruplarda kullanılabilir."
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="Tekli mod seçildi. 10 saniye içinde bir kelime yazmalısınız."
        )
        word = get_random_word()
        client.send_message(
            chat_id=message.chat.id,
            text=f"Sıradaki harf: {word[0]}"
        )
        time.sleep(10)
        client.send_message(
            chat_id=message.chat.id,
            text="Süre doldu! Oyun iptal edildi."
        )

@app.on_message(filters.command(["multi"]))
def multi_mode(client, message):
    if message.chat.type == "private":
        client.send_message(
            chat_id=message.chat.id,
            text="Çoklu mod sadece gruplarda kullanılabilir."
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="Çoklu mod seçildi. 10 saniye içinde her bir oyuncu bir kelime yazmalıdır."
        )
        word = get_random_word()
        client.send_message(
            chat_id=message.chat.id,
            text=f"Sıradaki harf: {word[0]}"
        )
        time.sleep(10)
        client.send_message(
            chat_id=message.chat.id,
            text="Süre doldu! Oyun iptal edildi."
        )

@app.on_message(filters.text)
def check_word(client, message):
    if message.chat.type == "private":
        client.send_message(
            chat_id=message.chat.id,
            text="Komutları sadece gruplarda kullanabilirsiniz."
        )
        elif word[0] != word[0].lower():
            client.send_message(
                chat_id=message.chat.id,
                text=f"Kelimenin baş harfi {word[0]} olmalıdır."
            )
        else:
            # Kelimeyi kontrol etme ve işleme devam etme kodları
            pass

def get_random_word():
    response = requests.get("https://sozluk.gov.tr/icerik")
    data = response.json()
    word = data["madde"]
    if word is None:
        return "Kelime TDK sözlüğünde yok."
    else:
        return word

def count_known_words(words):
    count = 0
    for word in words:
        response = requests.get(f"https://sozluk.gov.tr/icerik/{word}")
        data = response.json()
        if data["madde"] is not None:
            count += 1
    return count


