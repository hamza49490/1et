from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *

@Client.on_message(filters.command("game") & ~filters.edited)
async def gameoyun(_, message: Message):
    await c.send_message(m.chat.id, text_message, kanal)
    
text_message = """ Lütfen Seçim Yapın  """
    
@Client.on_callback_query(filters.regex("turet"))
async def kelimeoyun(_, query: CallbackQuery):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**💭 Zaten Aktif Oyun Var .\n♻️ Durdurmak için /kapat Yazın . . .**", reply_markup=destek)
    else:
        await m.reply(f"**{m.from_user.mention} Tarafından .\n💡 Kelime Oyunu Başladı .\n\n🥳 Hızlı Olan Kazanır . . .**")
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["pass"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""**🎯 Raund : {oyun[m.chat.id]['round']}/80
📖 Kelime :   <code>{kelime_list}</code>
💰 Kazandıracak Puan : 1
🔎 İpucu : 1. {oyun[m.chat.id]["kelime"][0]}
🌟 Uzunluk : {int(len(kelime_list)/2)} 

♻️ Karışık Harflerden Doğru Kelimeyi Bulun . . .
            **"""
        await c.send_message(m.chat.id, text)
