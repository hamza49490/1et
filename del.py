import telebot
import requests
from datetime import datetime
from telebot import types
from bs4 import BeautifulSoup
import random
import time

TOKEN = '6559325433:AAECLK5t8nQUFWkI24Hx0NF-ASthWqBo3dU'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['lyrics'])
def send_lyrics(message):
    song_name = message.text.replace('/lyrics', '').strip()
    lyrics = get_lyrics(song_name)
    bot.reply_to(message, lyrics)

def get_lyrics(song_name):
    url = f'https://www.azlyrics.com/lyrics/{song_name}.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    lyrics_div = soup.find_all('div', class_='col-xs-12 col-lg-8 text-center')[0]
    lyrics = lyrics_div.find_all('div')[6].text.strip()
    return lyrics


target_number = None
start_time = None

@bot.message_handler(commands=['sayi'])
def start(message):
    global target_number
    global start_time

    if target_number is not None:
        bot.reply_to(message, "Zaten bir oyun aktif.")
        return

    bot.reply_to(message, "Sayı tahmin oyununa hoş geldiniz! 1 ile 100 arasında bir sayı tuttum. Tahmininizi yapabilirsiniz!")

    # Rastgele bir sayı seç
    target_number = random.randint(1, 100)

@bot.message_handler(commands=['isayi'])
def cancel(message):
    global target_number
    global start_time

    if target_number is None:
        bot.reply_to(message, "Zaten aktif bir oyun yok.")
    else:
        bot.reply_to(message, "Oyun iptal edildi.")
        target_number = None
        start_time = None


@bot.message_handler(func=lambda message: True)
def guess(message):
    global target_number
    global start_time

    try:
        guess_number = int(message.text)
    except ValueError:
        return

    if guess_number < target_number:
        bot.reply_to(message, "Daha büyük bir sayı tahmin edin.")
    elif guess_number > target_number:
        bot.reply_to(message, "Daha küçük bir sayı tahmin edin.")
    else:
        bot.reply_to(message, "Tebrikler! Doğru sayıyı buldunuz.")
        target_number = None
        return

    # Yeni bir tahmin yapıldığında süreyi sıfırla
    start_time = time.time()
    

bot.polling()



'''
bot_token = '6404904263:AAHP25SjaF85qCncHTq5NE9zA4A-ASD5XNA'

bot_active = False

bot = telebot.TeleBot(bot_token)

# /yas komutuna yanıt veren bir işlev
@bot.message_handler(commands=['yas'])
def calculate_age(message):
    try:
        # Komutu kullanan kullanıcının doğum tarihini alın
        birthday_str = message.text.split()[-1]
        birthday = datetime.strptime(birthday_str, "%d.%m.%Y")

        # Şu anki tarihi alın
        current_date = datetime.now()

        # Kullanıcının yaşını hesaplayın
        age = current_date.year - birthday.year - ((current_date.month, current_date.day) < (birthday.month, birthday.day))

        # Doğum gününün ne kadar zaman sonra olduğunu hesaplayın
        next_birthday = datetime(current_date.year, birthday.month, birthday.day)
        if current_date > next_birthday:
            next_birthday = datetime(current_date.year + 1, birthday.month, birthday.day)
        days_until_birthday = (next_birthday - current_date).days

        # Kullanıcıya cevap verin
        reply_message = f"🎉 sᴇᴠɢɪʟɪ {message.from_user.first_name}\n"
        reply_message += f"💭 şᴜᴀɴᴅᴀ {age} ʏᴀşɪɴᴅᴀsɪɴ .\n\n"
        reply_message += f"🎂 ᴅᴏɢ̆ᴜᴍ ɢᴜ̈ɴᴜ̈ɴ {days_until_birthday} ɢᴜ̈ɴ sᴏɴʀᴀ ."
        bot.reply_to(message, reply_message)
    except ValueError:
        bot.reply_to(message, "🗒️ ɢᴇᴄ̧ᴇʀsɪᴢ ᴛᴀʀɪʜ .\nᴅᴏɢ̆ʀᴜ ʙɪʀ ᴛᴀʀɪʜ ɢɪʀɪɴ .\nᴏ̈ʀɴᴇᴋ : 30.01.2000")
    except Exception as e:
        bot.reply_to(message, "🗒️ ʙɪʀ ʜᴀᴛᴀ ᴏʟᴜşᴛᴜ .\nsᴏɴʀᴀ ᴛᴇᴋʀᴀʀ ᴅᴇɴᴇʏɪɴ .")

# /burc komutuna yanıt veren bir işlev
@bot.message_handler(commands=['burc'])
def calculate_zodiac_sign(message):
    try:
        # Komutu kullanan kullanıcının doğum tarihini alın
        birthday_str = message.text.split()[-1]
        birthday = datetime.strptime(birthday_str, "%d.%m.%Y")

        # Burçları ve tarih aralıklarını tanımlayın
        zodiac_signs = [
            {"name": "𝗄𝗈𝖼̧", "start_date": datetime(birthday.year, 3, 21), "end_date": datetime(birthday.year, 4, 19)},
            {"name": "𝖻𝗈𝗀̆𝖺", "start_date": datetime(birthday.year, 4, 20), "end_date": datetime(birthday.year, 5, 20)},
            {"name": "𝗂𝗄𝗂𝗓𝗅𝖾𝗋", "start_date": datetime(birthday.year, 5, 21), "end_date": datetime(birthday.year, 6, 20)},
            {"name": "𝗒𝖾𝗇𝗀𝖾𝖼̧", "start_date": datetime(birthday.year, 6, 21), "end_date": datetime(birthday.year, 7, 22)},
            {"name": "𝖺𝗌𝗅𝖺𝗇", "start_date": datetime(birthday.year, 7, 23), "end_date": datetime(birthday.year, 8, 22)},
            {"name": "𝖻𝖺𝗌̧𝖺𝗄", "start_date": datetime(birthday.year, 8, 23), "end_date": datetime(birthday.year, 9, 22)},
            {"name": "𝗍𝖾𝗋𝖺𝗓𝗂", "start_date": datetime(birthday.year, 9, 23), "end_date": datetime(birthday.year, 10, 22)},
            {"name": "𝖺𝗄𝗋𝖾𝗉", "start_date": datetime(birthday.year, 10, 23), "end_date": datetime(birthday.year, 11, 21)},
            {"name": "𝗒𝖺𝗒", "start_date": datetime(birthday.year, 11, 22), "end_date": datetime(birthday.year, 12, 21)},
            {"name": "𝗈𝗀̆𝗅𝖺𝗄", "start_date": datetime(birthday.year, 12, 22), "end_date": datetime(birthday.year, 1, 19)},
            {"name": "𝗄𝗈𝗏𝖺", "start_date": datetime(birthday.year, 1, 20), "end_date": datetime(birthday.year, 2, 18)},
            {"name": "𝖻𝖺𝗅ı𝗄", "start_date": datetime(birthday.year, 2, 19), "end_date": datetime(birthday.year, 3, 20)},
        ]

        # Kullanıcının burcunu bulun
        zodiac_sign = None
        for sign in zodiac_signs:
            if sign["start_date"] <= birthday <= sign["end_date"]:
                zodiac_sign = sign["name"]
                break

        if zodiac_sign:
            bot.reply_to(message, f"💭 {birthday_str} ᴛᴀʀɪʜɪɴᴅᴇ \n🌟 ᴅᴏɢ̆ᴅᴜɢ̆ᴜɴᴜᴢᴀ ɢᴏ̈ʀᴇ ...\n\n✓ ʙᴜʀᴄᴜɴᴜᴢ : {zodiac_sign}")
        else:
            bot.reply_to(message, "🗒️ ɢᴇᴄ̧ᴇʀsɪᴢ ᴛᴀʀɪʜ ᴠᴇʏᴀ ʙᴜʀᴄ̧ ʜᴇsᴀᴘʟᴀɴᴀᴍᴀᴅɪ ...")
    except ValueError:
        bot.reply_to(message, "🗒️ ɢᴇᴄ̧ᴇʀsɪᴢ ᴛᴀʀɪʜ .\nᴅᴏɢ̆ʀᴜ ʙɪʀ ᴛᴀʀɪʜ ɢɪʀɪɴ .\nᴏ̈ʀɴᴇᴋ : 30.01.2000")
    except Exception as e:
        bot.reply_to(message, "🗒️ ʙɪʀ ʜᴀᴛᴀ ᴏʟᴜşᴛᴜ .\nsᴏɴʀᴀ ᴛᴇᴋʀᴀʀ ᴅᴇɴᴇʏɪɴ .")

# SUS KOMUTUNA YANIT VEREN BİR İŞLEV
@bot.message_handler(commands=['susjdkrkr'])
def deactivate_bot(message):
    global bot_active
    bot_active = False
    bot.reply_to(message, "Bot şu an pasif.")

# KONUS KOMUTUNA YANIT VEREN BİR İŞLEV
@bot.message_handler(commands=['konuskdjdk'])
def activate_bot(message):
    global bot_active
    bot_active = True
    bot.reply_to(message, "Bot şu an aktif.")

# İP KOMUTUNA YANIT VEREN BİR İŞLEV
@bot.message_handler(commands=['ipdndjr'])
def ip_sorgu(message):
    try:
        ip = message.text.split()[-1]

        # IP sorgusu işlemi
        response = requests.get(f"http://ip-api.com/json/{ip}").json()

        if response["status"] == "success":
            # IP sorgusu başarılı ise sonucu özelleştirin
            result = "🌐 IP Bilgileri 🌐\n\n"
            result += f"🔹 **IP Adresi:** `{response['query']}`\n"
            result += f"🔹 **Ülke:** `{response['country']}`\n"
            result += f"🔹 **Şehir:** `{response['city']}`\n"
            result += f"🔹 **Posta Kodu:** `{response['zip']}`\n"
            result += f"🔹 **Koordinatlar:** `{response['lat']}, {response['lon']}`\n"

            bot.reply_to(message, result)
        else:
            bot.reply_to(message, "IP sorgusu başarısız oldu.")
    except IndexError:
        bot.reply_to(message, "❌ İşlem Başarısız\n❗️ Lütfen Geçerli Bir IP Adresi Giriniz!\n\nÖrnek: /ip 8.8.8.8")
    except Exception as e:
        bot.reply_to(message, "❌ Bir Hata Oluştu\n\nLütfen Daha Sonra Tekrar Deneyin. . .⏳")

# DNS KOMUTUNU İŞLEYİN
@bot.message_handler(commands=['dnsjsdjkd'])
def dns_sorgu(message):
    try:
        domain = message.text.split()[-1]

        # DNS sorgusu işlemi
        response = requests.get(f"http://ip-api.com/json/{domain}").json()

        if response["status"] == "success":
            # DNS sorgusu başarılı ise sonucu özelleştirin
            result = "🌐 DNS Sorgusu 🌐\n\n"
            result += f"🔹 **Domain Adı:** `{domain}`\n"
            result += f"🔹 **IP Adresi:** `{response['query']}`\n"

            bot.reply_to(message, result, parse_mode='Markdown')
        else:
            bot.reply_to(message, "❌ DNS sorgusu başarısız oldu veya bu domain için herhangi bir IP adresi bulunamadı.")
    except IndexError:
        bot.reply_to(message, "❌ İşlem Başarısız\n❗️ Lütfen Geçerli Bir Domain Adı Giriniz!\n\nÖrnek: /dns example.com")
    except Exception as e:
        bot.reply_to(message, f"❌ Bir Hata Oluştu\n\nHata Detayı: {str(e)}")

# Bot'u çalıştırın
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        pass
'''
