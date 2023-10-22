import requests
from pyrogram import Client, filters


# Burç yorumlarını sağlayan bir API'ye bağlanmak için kullanılan URL
API_URL = "https://www.sabah.com.tr/teknoloji/2018/06/22/kurumlara-ve-girisimcilere-isi-buyutecek-anahtar-api"

# /burç komutunu işleyen bir filtre
@filters.command("burç")
def burc_yorum(client, message):
    # Kullanıcının girdiği burcu alın
    burc = message.text.split()[1].lower()

    # API'ye istek gönderin ve burç yorumunu alın
    response = requests.get(f"{API_URL}/{burc}")
    if response.status_code == 200:
        yorum = response.json()["yorum"]
        # Burç yorumunu yanıt olarak gönderin
        message.reply_text(yorum)
    else:
        message.reply_text("Bir hata oluştu, lütfen daha sonra tekrar deneyin.")
