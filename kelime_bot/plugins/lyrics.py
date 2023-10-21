from pyrogram import Client, filters
from pyrogram.types import Message
import requests

# "/lyrics" komutunu işleyen bir filtre oluşturun
@filters.command("lyrics")
def get_lyrics(_, message: Message):
    # Mesajdaki şarkı adını alın
    song_name = message.text.split("/lyrics", maxsplit=1)[1].strip()
    
    # Şarkı sözlerini almak için bir API isteği yapın
    response = requests.get(f"https://api.lyrics.ovh/v1/{song_name}")
    
    # İstek başarılı ise şarkı sözlerini gönderin
    if response.status_code == 200:
        lyrics = response.json()["lyrics"]
        message.reply_text(lyrics)
    else:
        message.reply_text("Şarkı sözleri bulunamadı.")

# Mesajları filtreleyin ve "/lyrics" komutunu işleyin
app.add_handler(get_lyrics)

