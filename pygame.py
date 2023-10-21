import random
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = "6404904263:AAHP25SjaF85qCncHTq5NE9zA4A-ASD5XNA"

def tahmin_et(bot, update):
    # Rastgele bir sayı seç
    sayi = random.randint(1, 1000)
    
    # Tahmin döngüsü
    while True:
        # Kullanıcıdan tahmin al
        tahmin = int(update.message.text)
        
        # Tahmini kontrol et
        if tahmin < sayi:
            bot.send_message(chat_id=update.message.chat_id, text='Daha yüksek bir sayı tahmin et.')
        elif tahmin > sayi:
            bot.send_message(chat_id=update.message.chat_id, text='Daha düşük bir sayı tahmin et.')
        else:
            bot.send_message(chat_id=update.message.chat_id, text='Tebrikler, doğru tahmin ettin!')
            break

updater = Updater(token='TOKEN')

updater.dispatcher.add_handler(MessageHandler(Filters.text, tahmin_et))

updater.start_polling()
updater.idle()
