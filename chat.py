import wget
import logging
import youtube_dl, requests, time
import os
import traceback
import yt_dlp
import ffmpeg
import aiohttp
import datetime
import string
import time
import datetime
import asyncio
import random
import config 
from config import *
from datetime import datetime, timedelta
from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters, types
from time import sleep
from random import shuffle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch
from mesaj.botmesaj import *

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

app = Client(
    "Tag-Bot",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN
)


isleyen = []
@app.on_message(filters.command("chatbot", prefixes="/"))
async def chatbot(client, message):
    if message.chat.type == "private":
        await message.reply("Bu komut yalnızca gruplarda kullanılabilir.", parse_mode='markdown')
        return
     
    admins = []
    async for admin in client.iter_chat_members(message.chat.id, filter="administrators"):
        admins.append(admin.user.id)
    if message.from_user.id not in admins:
        return await message.reply(f"noadmin")
    
    global isleyen
    if message.chat.id in isleyen:
        status = "✅ Aktif"
    else:
        status = "⛔ Kapalı"
    
    await message.reply(f"✦ Bir buton seçin ..!\n\n✦ Durum: {status}", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("✅ Aktif Et", callback_data="sohbetmod_on")],
            [InlineKeyboardButton("⛔ Kapat", callback_data="sohbetmod_off")]
        ]
    ))

@app.on_callback_query()
async def callback_sohbetmod(client, callback_query):
    qrup = callback_query.message.chat.id
    if callback_query.data == "sohbetmod_on":
        if qrup not in isleyen:
            isleyen.append(qrup)
            aktiv_olundu = "✦ ʙᴀs‌ᴀʀɪʏʟᴀ ᴀᴋᴛɪғ ᴇᴅɪʟᴅɪ .\n\n✦ ᴀʀᴛıᴋ ᴋᴏɴᴜs‌ᴀʙɪʟɪʀɪᴍ !"
            await callback_query.edit_message_text(aktiv_olundu)
            await asyncio.sleep(3600)
            while qrup in isleyen:
                users = await client.get_chat_members(qrup)
                active_users = [user for user in users if not user.user.is_bot and not user.user.is_deleted]
                if active_users:
                    random_user = random.choice(active_users)
                    await client.send_message(qrup, f"{random_user.user.first_name} {random.choice(smesajs)}")
                await asyncio.sleep(3600)
            return
        await callback_query.edit_message_text("✦ ᴄʜᴀᴛ ʙᴏᴛ ᴢᴀᴛᴇɴ ᴀᴋᴛɪ‌ғ .")
    elif callback_query.data == "sohbetmod_off":
        if qrup in isleyen:
            isleyen.remove(qrup)
            await callback_query.edit_message_text("✦ ʙᴀs‌ᴀʀɪʏʟᴀ ᴋᴀᴘᴀᴛɪʟᴅɪ .\n\n✦ ᴀʀᴛıᴋ ᴋᴏɴᴜs‌ᴀᴍᴀᴍ !")
            return
        await callback_query.edit_message_text("✦ ᴄʜᴀᴛ ʙᴏᴛ ᴢᴀᴛᴇɴ ᴋᴀᴘᴀʟɪ !")
	    
@app.on_message()
async def chatbot(client, message):
    global isleyen
    mesaj = str(message.text)
    qrup = message.chat.id
    if qrup not in isleyen:
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


@app.on_message(filters.command(["bul", "song"]) & ~filters.edited)
async def bul(_, message):
    try:
        await message.delete()
    except:
        pass
    query = " ".join(message.command[1:])
    m = await message.reply("**__✦ şᴀʀᴋɪ ᴀʀᴀɴɪʏᴏʀ !__**")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]
    
    except Exception as e:
        await m.edit("**__✦ şᴀʀᴋɪ ʙᴜʟᴜɴᴀᴍᴀᴅɪ !__**")
        print(str(e))
        return
    await m.edit("**__✦ şᴀʀᴋɪ ɪɴᴅɪʀɪʟɪʏᴏʀ !__**")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"**__✦ ᴘᴀʀᴄ̧ᴀ__ : {title[:35]}\n__✦ sᴜ̈ʀᴇ__ : {duration}\n\n__✦ ɪsᴛᴇʏᴇɴ__ : {message.from_user.mention}**"
        res = f"**__✦ ᴘᴀʀᴄ̧ᴀ__ : {title[:35]}\n__✦ sᴜ̈ʀᴇ__ : {duration}\n\n__✦ ɪsᴛᴇʏᴇɴ__ : {message.from_user.mention}**"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        await m.edit("**__✦ şᴀʀᴋɪ ʏᴜ̈ᴋʟᴇɴɪʏᴏʀ !__**")
        await message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name, performer="✦  𝐌𝐮̈𝐳𝐢𝐤 𝐁𝐨𝐭  ✦", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✦  𝖬𝗎̈𝗓𝗂𝗄 𝖪𝖺𝗒ı𝗍  ✦", url=f"t.me/{MCHANNEL}")]]))
        await m.delete()
        await _.send_audio(chat_id=PLAYLIST_ID, audio=audio_file, caption=res, performer="✦  𝐌𝐮̈𝐳𝐢𝐤 𝐁𝐨𝐭  ✦", parse_mode='md', title=title, duration=dur, thumb=thumb_name)
    except Exception as e:
        await m.edit("**__✦ ʙᴇɴɪ ʏᴏɴᴇᴛɪᴄɪ ʏᴀᴘɪɴ !__**")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

@app.on_message(filters.command(["vbul", "vsong"]) & ~filters.edited)
async def vsong(client, message):
    try:
        await message.delete()
    except:
        pass
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]
        views = results[0]["views"]
        mention = message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("**__✦ ᴠɪᴅᴇᴏ ᴀʀᴀɴɪʏᴏʀ !__**")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"**__✦ ᴠɪᴅᴇᴏ ʙᴜʟᴜɴᴀᴍᴀᴅɪ !__**")
    preview = wget.download(thumbnail)
    await msg.edit("**__✦ ᴠɪᴅᴇᴏ ɪɴᴅɪʀɪʟɪʏᴏʀ !__**")
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=f"**__✦ ᴘᴀʀᴄ̧ᴀ__ : {ytdl_data['title']}\n__✦ sᴜ̈ʀᴇ__ : {duration}\n\n__✦ ɪsᴛᴇʏᴇɴ__ : {message.from_user.mention}**",
    )
    try:
        os.remove(file_name)
        os.remove(thumb_name)
        await msg.delete()
    except Exception as e:
        print(e)

@app.on_message(filters.command(["ara", "search"]) & ~filters.edited)
async def ytsearch(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        if len(message.command) < 2:
            return await message.reply_text("**__✦ sᴏɴᴜᴄ̧ ʙᴜʟᴜɴᴀᴍᴀᴅɪ !**")
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("**__✦ ᴀʀɪʏᴏʀᴜᴍ !__**")
        results = YoutubeSearch(query, max_results=6).to_dict()
        i = 0
        text = ""
        while i < 6:
            text += f"**__💬 ᴘᴀʀᴄ̧ᴀ__ : {results[i]['title']}**\n"
            text += f"**__⌚ sᴜ̈ʀᴇ__ : {results[i]['duration']}**\n"
            text += f"**__🔗 ʟɪɴᴋ__ : [ ʏᴏᴜᴛᴜʙᴇ'ᴅᴇɴ ɪᴢʟᴇ ](https://youtube.com{results[i]['url_suffix']})**\n\n"
            i += 1
        await m.edit_text(
            text=text,
            disable_web_page_preview=True,
        )
    except Exception as e:
        await message.reply_text(str(e))

print(" Chat çalışıyor :)")
app.run()  
