import telebot
import requests
from datetime import datetime
import config
from config import *
import random
import time

bot = telebot.TeleBot(config.BOT_TOKEN)

target_number = None
start_time = None

@bot.message_handler(commands=['sayi'])
def start(message):
    if message.chat.type == 'private':
        bot.reply_to(message, "✦ <b>Sadece gruplarda kullanılabilir .</b>", parse_mode="HTML")
        return
    global target_number
    global start_time

    if target_number is not None:
        bot.reply_to(message, "✦ <b>Zaten aktif oyun var .\n✦ İptal etmek için ➡️ /iptal</b>", parse_mode="HTML")
        return

    bot.reply_to(message, "✦ <b>Aklımda 1 - 1000 arasında bir sayı tuttum , hadi tahmin et !</b>", parse_mode="HTML")

    target_number = random.randint(1, 1000)

@bot.message_handler(commands=['iptal'])
def cancel(message):
    global target_number
    global start_time

    if target_number is None:
        return
    else:
        bot.reply_to(message, "✦ <b>Sayı Tahmin Oyunu iptal edildi .</b>", parse_mode="HTML")
        target_number = None
        start_time = None

@bot.message_handler(func=lambda message: True)
def guess(message):
    global target_number
    global start_time
    global guess_count

    guess_count = 0

    try:
        guess_number = int(message.text)
    except ValueError:
        return

    if target_number is None:
        return

    guess_count += 1

    if guess_number < target_number:
        bot.reply_to(message, "🔺<b> Daha büyük bir sayı tahmin edin .</b>", parse_mode="HTML")
    elif guess_number > target_number:
        bot.reply_to(message, "🔻<b> Daha küçük bir sayı tahmin edin .</b>", parse_mode="HTML")
    else:
        bot.reply_to(message, f"✦<b> Tebrikler , Doğru sayıyı buldunuz .\n✦ Bulunan Sayı : {guess_number} </b>", parse_mode="HTML")
        target_number = None
        guess_count = 0
        return

    start_time = time.time()
    
    
print("DEL.PY AKTİF !")
bot.polling()

