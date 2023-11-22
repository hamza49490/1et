import logging
import asyncio
import random
import string
import aiohttp
import random

import config
from config import *

from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters, types
from time import sleep
from random import shuffle
from mesaj.botmesaj import *
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

app = Client(
    "Chat-Bot",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN
)


isleyen = []
@app.on_message(filters.command("chatbot", prefixes="/"))
async def chatbot(client, message):
    if message.chat.type == "private":
        await message.reply("🔹 __**ʙᴜ ᴋᴏᴍᴜᴛᴜ ɢʀᴜᴘʟᴀʀᴅᴀ ᴋᴜʟʟᴀɴ !**__", parse_mode='markdown')
        return
     
    admins = []
    async for admin in client.iter_chat_members(message.chat.id, filter="administrators"):
        admins.append(admin.user.id)
    if message.from_user.id not in admins:
        return await message.reply(f"😏 __**ʏᴏ̈ɴᴇᴛɪ̇ᴄɪ̇ ᴅᴇɢ̆ɪ̇ʟsɪ̇ɴ ʙᴇʙᴇɢ̆ɪ̇ᴍ !**__")
    
    global isleyen
    if message.chat.id in isleyen:
        status = " ᴀᴋᴛɪ̇ғ"
    else:
        status = " ᴋᴀᴘᴀʟɪ"
    
    await message.reply(f"__**✦ ᴀşᴀɢ̆ɪᴅᴀɴ sᴇᴄ̧ɪ̇ᴍ ʏᴀᴘɪɴ ! \n\n✦ ᴅᴜʀᴜᴍ : {status}**__", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("✅ ᴀᴋᴛɪ̇ғ ᴇᴛ", callback_data="sohbetmod_on")],
            [InlineKeyboardButton("⛔ ᴋᴀᴘᴀᴛ", callback_data="sohbetmod_off")]
        ]
    ))

@app.on_callback_query()
async def callback_sohbetmod(client, callback_query):
    qrup = callback_query.message.chat.id
    if callback_query.data == "sohbetmod_on":
        if qrup not in isleyen:
            isleyen.append(qrup)
            aktiv_olundu = "__**✦ ʙᴀs‌ᴀʀɪʏʟᴀ ᴀᴋᴛɪғ ᴇᴅɪʟᴅɪ .\n\n✦ ᴀʀᴛıᴋ ᴋᴏɴᴜs‌ᴀʙɪʟɪʀɪᴍ !**__"
            await callback_query.edit_message_text(aktiv_olundu)
            await asyncio.sleep(3600)
            while qrup in isleyen:
                users = await client.get_chat_members(qrup)
                active_users = [user for user in users if not user.user.is_bot and not user.user.is_deleted]
                if active_users:
                    random_user = random.choice(active_users)
                    await client.send_message(qrup, f"**{random_user.mention} {random.choice(smesajs)}**")
                await asyncio.sleep(3600)
            return
        await callback_query.edit_message_text("__**✦ ᴄʜᴀᴛ ʙᴏᴛ ᴢᴀᴛᴇɴ ᴀᴋᴛɪ‌ғ .**__")
    elif callback_query.data == "sohbetmod_off":
        if qrup in isleyen:
            isleyen.remove(qrup)
            await callback_query.edit_message_text("__**✦ ʙᴀs‌ᴀʀɪʏʟᴀ ᴋᴀᴘᴀᴛɪʟᴅɪ .\n\n✦ ᴀʀᴛıᴋ ᴋᴏɴᴜs‌ᴀᴍᴀᴍ !**__")
            return
        await callback_query.edit_message_text("__**✦ ᴄʜᴀᴛ ʙᴏᴛ ᴢᴀᴛᴇɴ ᴋᴀᴘᴀʟɪ !**__")

@app.on_message()
async def chatbot(client, message):
    global isleyen
    mesaj = str(message.text)
    qrup = message.chat.id
    if qrup not in isleyen:
        if "derya" in mesaj.lower().split(" "):
            await message.reply("__**✦ ᴄʜᴀᴛ ʙᴏᴛ s‌ᴜᴀɴ ᴋᴀᴘᴀʟɪ !\n✦ ᴀᴄ‌ᴍᴀᴋ ɪ‌ᴄ‌ɪɴ ➻ /chatbot**__")
        return
    
    me = await client.get_me()
    if message.from_user.id == me.id:
        return
    
    kelimeler = mesaj.lower().split(" ")  # Mesajı küçük harfe çevirip kelimelere ayır

    if "derya" in kelimeler:
        cevap = random.choice(bkt)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
        return
  
    if kelimeler[0] in ["bot"]:
        cevap = random.choice(bottst)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
        return

    if "selamün aleyküm" in mesaj.lower() or kelimeler[0] in ["slm", "selam", "sa", "sea"]:
        cevap = random.choice(selam)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
        return
	
    if "ne haber" in mesaj.lower() or kelimeler[0] in ["nasılsın", "naber", "nbr"]:
        cevap = random.choice(nasilsin)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["erkek", "adam"]:
        cevap = random.choice(adam)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["iyiyim", "mükemmel", "harika"]:
        cevap = random.choice(iyiyim)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if "hoş geldin" in mesaj.lower() or kelimeler[0] in ["hg"]:
        cevap = random.choice(hoş)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["merhaba", "mrb"]:
        cevap = random.choice(merhaba)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["ban", "/ban", "banned", "banla"]:
        cevap = random.choice(ban)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if "ne yapıyorsun" in mesaj.lower() or kelimeler[0] in ["nabiyon", "napıyorsun"]:
        cevap = random.choice(nabiyon)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["😔", "🥺", "😢"]:
        cevap = random.choice(uzgun)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["valla", "vallahi", "yemin"]:
        cevap = random.choice(valla)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    	    
    if kelimeler[0] in ["sg", "siktir"]:
        cevap = random.choice(sg)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["mal", "gerizekalı", "it", "şrfsz", "şerefsiz"]:
        cevap = random.choice(mal)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["balım", "bebeğim", "aşkım"]:
        cevap = random.choice(balim)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["canım", "bitanem", "yavrum"]:
        cevap = random.choice(canim)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["gidiyorum", "gittim", "görüşürüz"]:
        cevap = random.choice(gidiyorum)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["sinirlendim", "sinirliyim", "sinirleniyorum", "😡", "😤"]:
        cevap = random.choice(sinirlendim)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if "tanışabilir miyiz" in mesaj.lower() or "tanışalım mı" in mesaj.lower():
        cevap = random.choice(tanis)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if "adın ne" in mesaj.lower() or "ismin ne" in mesaj.lower():
        cevap = random.choice(adne)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if "idare eder" in mesaj.lower() or kelimeler[0] in ["kötü", "iyi"]:
        cevap = random.choice(iyisen)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["😅", "😂", "🤣"]:
        cevap = random.choice(gullu)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["büyüğüm", "büyük"]:
        cevap = random.choice(buyuk)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	
    if kelimeler[0] in ["aiko"]:
        cevap = random.choice(aiko)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["günaydın", "günaydınnn", "gny", "rojbaş"]:
        cevap = random.choice(gnyy)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if "iyi akşamlar" in mesaj.lower() or "iyi geceler" in mesaj.lower():
        cevap = random.choice(igece)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if "kaç yaşındasın" in mesaj.lower() or "yaşın kaç" in mesaj.lower():
        cevap = random.choice(kyas)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["nerelisin"]:
        cevap = random.choice(nereli)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["konuşma", "sus", "knşma"]:
        cevap = random.choice(pms)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["kırdı", "krldm", "kırıcı", "kırıldım"]:
        cevap = random.choice(krdn)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["skldm", "sıkıldım"]:
        cevap = random.choice(skdm)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["hm", "hmmm"]:
        cevap = random.choice(hms)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if "geçmiş olsun" in mesaj.lower():
        cevap = random.choice(bts)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["oyun", "game"]:
        cevap = random.choice(trt)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["evt", "evet"]:
        cevap = random.choice(evt)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["hyr", "hayır"]:
        cevap = random.choice(hyrr)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["🙄"]:
        cevap = random.choice(gzs)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["of", "offf"]:
        cevap = random.choice(ofs)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["çikolata"]:
        cevap = random.choice(cklta)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["lan", "ln"]:
        cevap = random.choice(lna)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["dedim"]:
        cevap = random.choice(dddm)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["yalan", "yalancı"]:
        cevap = random.choice(ylna)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["sağol"]:
        cevap = random.choice(sgll)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["çirkin"]:
        cevap = random.choice(crkn)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["dm", "pm"]:
        cevap = random.choice(dmy)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["tatlı", "yemek"]:
        cevap = random.choice(tymm)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["kes", "kesss"]:
        cevap = random.choice(kmm)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["kanka", "knk", "kanki"]:
        cevap = random.choice(kankas)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["öp"]:
        cevap = random.choice(opsss)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["sanane", "sağne", "sanne"]:
        cevap = random.choice(sgne)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["banne", "banane", "bağne"]:
        cevap = random.choice(bgne)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["ben", "bennn"]:
        cevap = random.choice(bnen)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["sen", "sennn"]:
        cevap = random.choice(snen)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')


print(" Chat çalışıyor :)")
app.run()  
