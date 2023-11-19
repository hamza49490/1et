import wget
import logging
import datetime
import aiohttp
import asyncio
import datetime
import shutil, psutil, traceback, os
import random
import string
import traceback
import aiofiles
import yt_dlp
import ffmpeg
import aiohttp
import random
import youtube_dl, requests, time
import motor.motor_asyncio
from datetime import datetime, timedelta
from pyrogram import filters
from pyrogram.handlers import MessageHandler
from time import sleep
from random import shuffle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from mesaj.botmesaj import *
from mesaj.kelimeler import *
from mesaj.kelimeler import kelime_sec
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from pyrogram import Client, filters, types, __version__
from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch
from pyrogram.handlers import MessageHandler
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    PeerIdInvalid,
    UserIsBlocked,
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

API_ID = int(os.environ.get("API_ID", "26573250"))
API_HASH = os.environ.get("API_HASH", "6306d2d23b1083a6f757f64f0b0c609c")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "EpicTaggerBot")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6865081184:AAFcDOrflr2l_tibi7tvQ3A9Sv288XxevLA")
BOT_ID = int(os.environ.get("BOT_ID", "6865081184"))
OWNER_ID = int(os.environ.get("OWNER_ID", "5581058044"))
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://mervetopic:topicmerve@cluster0.vpfzgml.mongodb.net/?retryWrites=true&w=majority")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001983841726"))
PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001916993821"))
MCHANNEL = os.environ.get("MCHANNEL", "MuzikKayit")
CHANNELL = os.environ.get("CHANNELL", "BotsDuyuru")
GROUP_SUPPORT = os.environ.get("GROUP_SUPPORT", "BotsDuyuru")
GONDERME_TURU = os.environ.get("GONDERME_TURU", True)
LANGAUGE = os.environ.get("LANGAUGE", "TR")
OWNERNAME = "Sahip"

app = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN
    )

isleyen = []

@app.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
    await message.reply_photo(
        "https://telegra.ph/file/608001bdce5b396b50ea2.jpg",
        caption=f"""✦ Merhaba {message.from_user.mention}\n\n✦ Son Derece Gelişmiş ve Birçok Özelliğe Sahip Bir Telegram Botuyum !\n\n✦ Komutlar veya Destek için Aşağıdaki Butonları Kullanın !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('✚  𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾  ✚', url=f'https://t.me/{BOT_USERNAME}?startgroup=a'),
                ],
                [
                    InlineKeyboardButton("📚 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋", callback_data="help"),
                    InlineKeyboardButton('🗨️ 𝖡𝗂𝗅𝗀𝗂 𝖪𝖺𝗇𝖺𝗅ı', url=f'https://t.me/{CHANNELL}')
                ],
                [
                    InlineKeyboardButton('✦  𝖣𝖾𝗌𝗍𝖾𝗄', url=f'tg://openmessage?user_id={OWNER_ID}')
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("start"))
async def start(_, query: CallbackQuery):
    startmesaj = "**✦ Merhaba !\n\n✦ Son Derece Gelişmiş ve Birçok Özelliğe Sahip Bir Telegram Botuyum !\n\n✦ Komutlar veya Destek için Aşağıdaki Butonları Kullanın !**"
    await query.message.edit_text(startmesaj, reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("➕  𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾  ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=a")
            ],
            [
                InlineKeyboardButton("📚 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋", callback_data="help"),
                InlineKeyboardButton("🗨️ 𝖡𝗂𝗅𝗀𝗂 𝖪𝖺𝗇𝖺𝗅ı", url=f"https://t.me/{CHANNELL}")
            ],
            [
                InlineKeyboardButton("✦  𝖲𝖺𝗁𝗂𝗉  ✦", url=f"tg://openmessage?user_id={OWNER_ID}")
            ]
        ]
    )
)

@app.on_callback_query(filters.regex("help"))
async def help(_, query: CallbackQuery):
    startbutton = "✦  Lütfen Buton Seçin !"
    await query.message.edit_text(startbutton, reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📇 𝖤𝗍𝗂𝗄𝖾𝗍 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋ı", callback_data="tag1")
            ],
            [
                InlineKeyboardButton("🗒️ 𝖤𝗄 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋", callback_data="tag2")
            ],
            [
                InlineKeyboardButton("🎯 𝖮𝗒𝗎𝗇 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋ı", callback_data="tag4")
            ],
            [
                InlineKeyboardButton("➡️ 𝖦𝖾𝗋𝗂 𝖣𝗈‌𝗇", callback_data="start")
            ]
        ]
    )
)

@app.on_callback_query(filters.regex("tag1"))
async def tag1(_, query: CallbackQuery):
    etikett = "**✦ Etiket Komutları :\n\n✓ Not : Silinen Hesapları ve Botları Etiketlemez !\n\n» /utag - Üyeleri Toplu Etiketler !\n\n» /tag - Üyeleri Tek Tek Etiketler !\n\n» /atag - Yöneticileri Tek Tek Etiketler !\n\n» /etag - Üyeleri Emojilerle Etiketler !\n\n» /stag - Üyeleri Sözlerle Etiketler !\n\n» /vtag - Üyeleri Sorularla Etiketler !\n\n» /otag - Üyeleri Rütbelerle Etiketler !\n\n» /cancel - Etiketlemeyi Durdurur !\n\n» /cagir - Aktif Üyeleri Oyuna Çağırır !**"
    await query.message.edit_text(etikett, reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("➡️ 𝖦𝖾𝗋𝗂 𝖣𝗈‌𝗇", callback_data="help")
            ]
        ]
    )
)

@app.on_callback_query(filters.regex("tag2"))
async def tag2(_, query: CallbackQuery):
    extraa = "**✦ Ek Komutlar :\n\n» /reload - Yönetici Listesini Yeniler !\n\n» /grup - Grup Hakkında Bilgi Verir !\n\n» /dels - Toplu Mesaj Siler !\n\n» /id - Kullanıcı ID'si Atar !\n\n» /chatbot - Chatbotu Aktif Edin !\n\n» /kurt - Kurt Oyunu Rolleri !**"
    await query.message.edit_text(extraa, reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("➡️ 𝖦𝖾𝗋𝗂 𝖣𝗈‌𝗇", callback_data="help")
            ]
        ]
    )
)

@app.on_callback_query(filters.regex("tag4"))
async def tag4(_, query: CallbackQuery):
    oyunn = "**✦ Oyun Komutları :\n\n» /eros - Gruptaki Üyeleri Shipler !\n\n» /slap - Eğlenmek için Kullanın !\n\n» /sayi - Sayı Tahmin Oyunu Açar !\n\n» /d - Doğruluk Sorusu Atar !\n\n» /c - Cesaret Sorusu Atar !\n\n» /soz - Çeşitli Sözler Atar !\n\n» /turet - Kelime Türet Oyunu Başlatır !\n\n» /iptal - Oyunu İptal Eder !\n\n » /zar - Zar Atar !\n\n » /bow - Bowling Atar !\n\n » /basket - Basket Atar !\n\n » /slots - Slot Atar !\n\n » /top - Top Atar !\n\n » /ok - Ok Atar !**"
    await query.message.edit_text(oyunn, reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("➡️ 𝖦𝖾𝗋𝗂 𝖣𝗈‌𝗇", callback_data="help")
            ]
        ]
    )
)
	    
'''
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
        rep = f"**__✦ ᴘᴀʀᴄ̧ᴀ__ : {title[:35]}\n__✦ sᴜ̈ʀᴇ__ : {duration}\n\n__✦ ɪsᴛᴇʏᴇɴ__ : [{message.from_user.first_name}](tg://user?id={message.from_user.id})**"
        res = f"**__✦ ᴘᴀʀᴄ̧ᴀ__ : {title[:35]}\n__✦ sᴜ̈ʀᴇ__ : {duration}\n\n__✦ ɪsᴛᴇʏᴇɴ__ : [{message.from_user.first_name}](tg://user?id={message.from_user.id})**"
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
        caption=f"**__✦ ᴘᴀʀᴄ̧ᴀ__ : {ytdl_data['title']}\n__✦ sᴜ̈ʀᴇ__ : {duration}\n\n__✦ ɪsᴛᴇʏᴇɴ__ : [{message.from_user.first_name}](tg://user?id={message.from_user.id})**",
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
'''  
anlik_calisan = []
tekli_calisan = []
gece_tag = []
rxyzdev_tagTot = {}
rxyzdev_initT = {} 
rxyzdev_stopT = {}

@app.on_message(filters.command("atag", prefixes="/"))
async def atag(client, message):
    global gece_tag
    rxyzdev_tagTot[message.chat.id] = 0
    if message.chat.type == "private":
        return await message.reply("nogroup")
  
    admins = []
    async for admin in client.iter_chat_members(message.chat.id, filter="administrators"):
        admins.append(admin.user.id)
    if message.from_user.id not in admins:
        return await message.reply("noadmin")
  
    if len(message.command) > 1:
        mode = "text_on_cmd"
        msg_list = message.text.split(None, 1)
        if len(msg_list) < 2:
            return await message.reply("Bir Mesaj Verin")
        msg = msg_list[1]
        if msg == "/atag":
            return await message.reply("Bir Mesaj Verin")
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message.message_id
        if msg == None:
            return await message.reply("Bir Mesaj Verin")
    elif len(message.command) > 1 and message.reply_to_message:
        mode = "text_on_cmd"
        msg_list = message.text.split(None, 1)
        if len(msg_list) < 2:
            return await message.reply("Bir Mesaj Verin")
        msg = msg_list[1]
    else:
        return await message.reply("Bir Mesaj Verin")
  
    if mode == "text_on_cmd":
        anlik_calisan.append(message.chat.id)
        usrnum = 0
        usrtxt = ""
        await message.reply("ibaslama")

        gece_tag.append(message.chat.id)
        usrnum = 0
        usrtxt = ""   
        async for usr in client.iter_chat_members(message.chat.id):
            if usr.user.is_bot or usr.user.is_deleted:
                continue
            if usr.user.id in admins:  # Yalnızca yöneticileri etiketleyin
                rxyzdev_tagTot[message.chat.id] += 1
                usrnum += 1
                usrtxt += f"{usr.user.first_name} , "
                if message.chat.id not in gece_tag:
                    return
                if usrnum == 1:
                    await client.send_message(message.chat.id, f"➻ {msg}\n\n{usrtxt}")
                    await asyncio.sleep(2)
                    usrnum = 0
                    usrtxt = ""
     
    sender = message.from_user
    rxyzdev_initT = f"{sender.first_name}"      
    if message.chat.id in rxyzdev_tagTot:
        await message.reply(f"🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...\n\n➻  {rxyzdev_initT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[message.chat.id]}")

@app.on_message(filters.command("utag", prefixes="/"))
async def utag(client, message):
    global gece_tag
    rxyzdev_tagTot[message.chat.id] = 0
    if message.chat.type == "private":
        return await message.reply("nogroup")
  
    admins = []
    async for admin in client.iter_chat_members(message.chat.id, filter="administrators"):
        admins.append(admin.user.id)
    if message.from_user.id not in admins:
        return await message.reply("noadmin")
  
    if len(message.command) > 1:
        mode = "text_on_cmd"
        msg_list = message.text.split(None, 1)
        if len(msg_list) < 2:
            return await message.reply("Bir Mesaj Verin")
        msg = msg_list[1]
        if msg == "/utag":
            return await message.reply("Bir Mesaj Verin")
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message.message_id
        if msg == None:
            return await message.reply("Bir Mesaj Verin")
    elif len(message.command) > 1 and message.reply_to_message:
        mode = "text_on_cmd"
        msg_list = message.text.split(None, 1)
        if len(msg_list) < 2:
            return await message.reply("Bir Mesaj Verin")
        msg = msg_list[1]
    else:
        return await message.reply("Bir Mesaj Verin")
  
    if mode == "text_on_cmd":
        anlik_calisan.append(message.chat.id)
        usrnum = 0
        usrtxt = ""
        await message.reply("ibaslama")

        gece_tag.append(message.chat.id)
        usrnum = 0
        usrtxt = ""   
        async for usr in client.iter_chat_members(message.chat.id):
            if usr.user.is_bot or usr.user.is_deleted:
                continue
            rxyzdev_tagTot[message.chat.id] += 1
            usrnum += 1
            usrtxt += f"{usr.user.first_name} , "
            if message.chat.id not in gece_tag:
                return
            if usrnum == 1:
                await client.send_message(message.chat.id, f"➻ {msg}\n\n{usrtxt}")
                await asyncio.sleep(2)
                usrnum = 0
                usrtxt = ""
     
    sender = message.from_user
    rxyzdev_initT = f"{sender.first_name}"      
    if message.chat.id in rxyzdev_tagTot:
        await message.reply(f"🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...\n\n➻  {rxyzdev_initT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[message.chat.id]}")

@app.on_message(filters.command("cancel", prefixes="/"))
async def cancel(client, message):
    global gece_tag
    if message.chat.type == "private":
        return await message.reply("nogroup")
  
    admins = []
    async for admin in client.iter_chat_members(message.chat.id, filter="administrators"):
        admins.append(admin.user.id)
    if message.from_user.id not in admins:
        return await message.reply("noadmin")

    if message.chat.id not in gece_tag:
        return await message.reply("• ᴀᴋᴛɪ‌ғ ʙɪ‌ʀ ɪ‌s‌ʟᴇᴍ ʏᴏᴋ !")

    gece_tag.remove(message.chat.id)
    sender = message.from_user
    rxyzdev_stopT = f"{sender.first_name}"
    await message.reply(f"⛔ ɪs‌ʟᴇᴍɪ ɪᴘᴛᴀʟ ᴇᴛᴛɪᴍ ...\n\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[message.chat.id]}\n\n👤 ɪᴘᴛᴀʟ ᴇᴅᴇɴ ᴋᴜʟʟᴀɴɪᴄɪ : {rxyzdev_stopT}")
	
@app.on_message(filters.command(["slap"], prefixes=['/', '']))
async def slap(client: Client, message: Message):
    if message.chat.type == "private":
        return await message.reply(f"nogroup")

    if message.reply_to_message:
        reply_message = message.reply_to_message
        user = reply_message.from_user
        if user:
            user_name = f"[{user.first_name}](tg://user?id={user.id})"
            slap_phrases = [
	          	                f"{user_name} 'ın Gözlerini Oydu! Kör Oldu Zavallı 😱",
	             	                f"{user_name} 'ın Sırtına Bindi! At Gibi Koşuyorsun Mübarek .",
	             	                f"{user_name} 'ın Kulağını Çekti! Acımış Olmalı 😕",
		                        f"{user_name} 'ı Arabayla Ezdi! Öldün Bebek 🥴",
		                        f"{user_name} 'ı Soydu! 5 Kuruş'u Kaldı 😕",
		                        f"{user_name} 'ı Yemeğe Çıkardı! Hayrola İnşallah 🤭",
		                        f"{user_name} 'a Sarıldı! Sevgi Dolu Kucaklaşma 💞",
		                        f"{user_name} 'ın Üstüne Çay Döktü! Yanıyorsun Fuat Abi 🔥",
                                        f"{user_name} 'ın Üzerine Pasta Fırlattı! Afiyet Olsun 😋",
                                        f"{user_name} 'ın Üstüne Benzin Döktü!",
                                        f"{user_name} 'ı Ateşe Attı! Yanıyorsun Ayten 🤣",
                                        f"{user_name} 'ın Üstüne Su Döktü!",
                                        f"{user_name} 'a Osmanlı Tokatı Attı! Yerle Bir Oldu :)",
                                        f"{user_name} 'a Çikolata Verdi! Hadi Yine İyisin 🥳",
                                        f"{user_name} 'ı Zencilere Sattı! Geçmiş Olsun 🥳",
                                        f"{user_name} 'ı Turşu Kavonozuna Soktu! Turşu {user_name}",
                                        f"{user_name} 'ın Üzerine Buz Dolabı Attı!",
                                        f"{user_name} 'ın Kafasını Duvara Sürterek Yaktı! Zavallı Ağlicak :)",
                                        f"{user_name} 'ı Ormana Kaçırdı! Acaba Ne Olacak 🤭",
                                        f"{user_name} 'ı Banyoda Suikast Etti! Banyoda Ne İşin Vardı 🤣",
		                        f"{user_name} 'a Kafa Attı! Mermiler Seksin, Alemde Teksin 😁",
		                        f"{user_name} 'a Harçlık Verdi! Kendine Çikolata Alırsın 😁",
                                        f"{user_name} 'a Kavanoz Fırlattı! Başka Bişey Bulamadı Sanırım 🙄",
	  	                        f"{user_name} 'a Domates Fırlattı! Suratı Kıp Kırmızı Oldu 😁",
		                        f"{user_name} 'a Kanepeyi Fırlattı! Öyle Ölmez Füze Atsaydın 😱",
		                        f"{user_name} 'a İğne Sapladı! Bu Acıtmıştır Sanırım 🥲",
		                        f"{user_name} 'a Çelme Taktı! Geber 😁",
		                        f"{user_name} 'ın Yüzüne Tükürdü 🤬",
		                        f"{user_name} 'a Kanepeyi Fırlattı! Öyle Ölmez Füze Atsaydın 😱",
		                        f"{user_name} 'a Omuz attı! Ne bakıyon Birader !",
		                        f"{user_name} 'a Yumurta Fırlattı! Tam isabet 🎯",
		                        f"{user_name} 'ın Saçını Çekti! Acıdı mı 😁",
		                        f"{user_name} 'a Taş Attı! Kafası Yarıldı 🤭",
		                        f"{user_name} 'ın Kafasında Şişe Kırdı! Kafası Acımış Olmalı 🥲",
		                        f"{user_name} 'a Taş Attı! Kafası Yarıldı 🤭",
		                        f"{user_name} 'a Kafa Attı! Burnu Kırıldı 😱",
		                        f"{user_name} 'a Yumruk attı ! Buz Koy Morarmasın 🤕",
		                        f"{user_name} 'ın Kafasına Taş Attı! Rahmetliyi Sevmezdik 🥴",
                                        f"{user_name} 'a 619 Çekti! Zavallı Bayıldı 😁",
                                        f"{user_name} 'a Osmanlı Tokatı Attı! Şamar Oğlana Döndü 😱",
                                        f"Marketten Beyin Satın Aldı! Artık {user_name} 'ın Beyni Var .",
                                        f"Beyni'nin Yarısını {user_name} 'a Verdi! Artık Aç Kalmayacak 😋",
                                        f"{user_name} 'ı Camdan Attı! Kafası Yarıldı ve Öldü .",
                                        f"{user_name} 'ın Ayağına Taş Bağlayıp Denize Attı! Boğuluyor 😨",
                                        f"{user_name} 'ın Gözüne Parmak Attı! Kör Oldu 🤣",
                                        f"{user_name} 'ın Üzerine Pitbull Köpeğini Saldı! Parçalara Ayrıldı 😱",
		                        f"{user_name} ''a Uçan Tekme Attı! Jetli misin mübarek 😳",  
            ]
            slap_phrase = random.choice(slap_phrases)
            await message.reply(f"**[{message.from_user.first_name}](tg://user?id={message.from_user.id}) ,  {slap_phrase}**")
        else:
            await message.reply("Üzgünüm, kullanıcıyı bulamıyorum!")
    else:
        await message.reply("Bir mesaja yanıt verin!")
        
@app.on_message(filters.command(["eros", "ship"], prefixes=['/', '']))
async def handle_eros(client: Client, message: Message):
    if message.chat.type == "private":
        return await message.reply(f"nogroup")

    chat = await client.get_chat(message.chat.id)
    if message.reply_to_message:
        reply_msg = message.reply_to_message
        user1 = await client.get_chat_member(chat.id, reply_msg.from_user.id)
        user2 = await client.get_chat_member(chat.id, message.from_user.id)
        love_percentage = random.randint(0, 100)
        await message.reply_text(f"**💘 ᴇʀᴏs'ᴜɴ ᴏᴋᴜɴᴜ ᴀᴛᴛɪᴍ .\n✦  ɢɪᴢʟɪ ᴀşɪᴋʟᴀʀ :\n\n[{user2.user.first_name}](tg://user?id={user2.user.id})  💕  [{user1.user.first_name}](tg://user?id={user1.user.id}) \n\n💞 sᴇᴠɢɪ ᴏʀᴀɴɪ : %{love_percentage}**")
    else:
        participants = await client.get_chat_members(chat.id)
        active_users = [user for user in participants if not user.user.is_bot and not user.user.is_deleted and not user.user.is_self]
        if len(active_users) < 2:
            await message.reply_text("**__⛔ ʏᴇᴛᴇʀʟɪ ᴀᴋᴛɪғ ᴋᴜʟʟᴀɴɪᴄɪ ʏᴏᴋ !__**")
        else:
            user1, user2 = random.sample(active_users, 2)
            love_percentage = random.randint(0, 100)
            await message.reply_text(f"**__💘 ᴇʀᴏs'ᴜɴ ᴏᴋᴜɴᴜ ᴀᴛᴛɪᴍ .\n✦  ɢɪᴢʟɪ ᴀşɪᴋʟᴀʀ :__\n\n[{user1.user.first_name}](tg://user?id={user1.user.id})  💕  [{user2.user.first_name}](tg://user?id={user2.user.id}) \n\n__💞 sᴇᴠɢɪ ᴏʀᴀɴɪ : %{love_percentage}__**")

@app.on_message(filters.command('group', prefixes='/'))
async def grup_info(client: Client, message: Message):
    if message.chat.type == "private":
        return await message.reply(f"nogroup")
     
    chat = message.chat
    group_name = chat.title
    group_id = chat.id

    chat_info = await client.get_chat(group_id)

    deleted_count = 0
    active_count = 0
    bot_count = 0
    total_count = 0

    async for participant in client.iter_chat_members(chat_info.id):
        total_count += 1
        if participant.user.is_deleted:
            deleted_count += 1
        elif not participant.user.is_bot:
            active_count += 1
        elif participant.user.is_bot:
            bot_count += 1

    special_status = ""
    if deleted_count > 0:
        special_status += f'➻ sɪʟɪɴᴇɴ ʜᴇsᴀᴘ sᴀʏɪsɪ : {deleted_count}\n'
    if bot_count > 0:
        special_status += f'➻ ɢʀᴜᴘ ʙᴏᴛ sᴀʏɪsɪ : {bot_count}\n'

    if not special_status:
        special_status = "ʙᴜʟᴜɴᴀᴍᴀᴅɪ"

    response_text = (
        f'➻ ɢʀᴜᴘ ᴀᴅɪ : {group_name}\n'
        f'➻ ɢʀᴜᴘ ɪᴅ : -100{group_id}\n'
        f'➻ ᴜʏᴇ sᴀʏɪsɪ : {total_count}\n'
        f'➻ ᴀᴋᴛɪғ ᴜʏᴇ sᴀʏɪsɪ : {active_count}\n'
        f'{special_status}'
    )

    await message.reply_text(response_text)
	
@app.on_message(filters.command(["bots"], prefixes="/"))
async def show_bots(client: Client, message: Message):
    if message.chat.type == "private":
        return await message.reply(f"nogroup")
	    
    all_users = await client.get_chat_members(message.chat.id)
    bot_list = []
    for user in all_users:
        if user.user.is_bot:
            bot_list.append(user.user.username)
    if bot_list:
        await message.reply_text(f"🤖 ɢʀᴜᴘᴛᴀᴋɪ ʙᴏᴛʟᴀʀ :\n\n➻  @" + "\n➻  @".join(bot_list))
    else:
        await message.reply_text("🤖 ʙᴜ ɢʀᴜᴘᴛᴀ ʜɪᴄ‌ ʙᴏᴛ ʏᴏᴋ .")
	    
@app.on_message(filters.command("admins", prefixes="/"))
async def show_admins(client: Client, message: Message):
    if message.chat.type == "private":
        return await message.reply(f"nogroup")

    chat = message.chat
    admins = await client.get_chat_members(chat.id, filter="administrators")
    admin_list = ""
    for admin in admins:
        user = admin.user
        admin_list += f"\n➻  [{user.first_name}](tg://user?id={user.id})"
    await message.reply_text(f"🗨️  ɢʀᴜᴘᴛᴀᴋɪ ᴀᴅᴍɪɴʟᴇʀ : \n{admin_list}")
	
@app.on_message(filters.group & filters.command(["info", "id"], prefixes="/"))
async def get_user_info(client: Client, message: types.Message):
    user = None

    if message.reply_to_message:
        user = message.reply_to_message.from_user
    elif len(message.command) > 1:
        username = message.command[1]
        user = await client.get_users(username)

    if user:
        chat_member = await client.get_chat_member(message.chat.id, user.id)
        if chat_member.status == "administrator" or chat_member.status == "creator":
            status = "Durumu: Yönetici"
        else:
            status = "Durumu: Üye"
        info = f"Kullanıcı: {user.first_name}\n" \
               f"Kullanıcı Adı: @{user.username}\n" \
               f"Kullanıcı ID: {user.id}\n" \
               f"Grup ID: {message.chat.id}\n" \
               f"{status}"
        button = InlineKeyboardButton(text="Profil", url=f"tg://openmessage?user_id={user.id}")
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
        await message.reply_text(info, reply_markup=keyboard)
    else:
        chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
        if chat_member.status == "administrator" or chat_member.status == "creator":
            status = "Durumu: Yönetici"
        else:
            status = "Durumu: Üye"
        info = f"Kullanıcı: {message.from_user.first_name}\n" \
               f"Kullanıcı Adı: @{message.from_user.username}\n" \
               f"Kullanıcı ID: {message.from_user.id}\n" \
               f"Grup ID: {message.chat.id}\n" \
               f"{status}"
        button = InlineKeyboardButton(text="Kullanıcı Profili", url=f"tg://openmessage?user_id={message.from_user.id}")
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
        await message.reply_text(info, reply_markup=keyboard)
	
@app.on_message(filters.command("reload", prefixes="/") & filters.group)
async def reload_command(client: Client, message: Message):
    if message.chat.type == "private":
        return await message.reply(f"nogroup")
	    
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status in ["creator", "administrator"]:
        await client.send_message(message.chat.id, "🎄 ʙᴏᴛ ʏᴇɴɪᴅᴇɴ ʙᴀs‌ʟᴀᴅɪ !\n🎄 ᴀᴅᴍɪɴ ʟɪsᴛᴇsɪ ɢüɴᴄᴇʟʟᴇɴᴅɪ !")
    else:
        await client.send_message(
            message.chat.id,
            "✨ ʟüᴛғᴇɴ ʙᴇɴɪ ʏöɴᴇᴛɪᴄɪ ʏᴀᴘɪɴ !"
	)
	    
@app.on_message(filters.new_chat_members, group=1)
async def zar(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(BOT_ID):
            await msg.reply(
                f'''**__✦ ᴍᴇʀʜᴀʙᴀ__ , {msg.from_user.mention}\n\n__✦ ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇᴅɪɢ̆ɪɴ ɪᴄ̧ɪɴ ᴛᴇşşᴇᴋᴜ̈ʀ ᴇᴅᴇʀɪᴍ, ʙᴇɴɪ ʏᴏ̈ɴᴇᴛɪᴄɪ ʏᴀᴘᴍᴀʏɪ ᴜɴᴜᴛᴍᴀʏɪɴ !\n\n✦ ᴅᴀʜᴀ ғᴀᴢʟᴀ ʙɪʟɢɪ ɪᴄ̧ɪɴ ᴀşşᴀɢ̆ɪᴅᴀᴋɪ ʙᴜᴛᴏɴᴜ ᴋᴜʟʟᴀɴɪɴ !__**''', 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✦  𝖡𝗎𝗋𝖺𝗒𝖺 𝖳ı𝗄𝗅𝖺  ✦", url=f"https://t.me/{BOT_USERNAME}?start")]])
    )
        elif str(new_user.id) == str(OWNER_ID):
            await msg.reply(f'**__✦ ᴅᴇɢ̆ᴇʀʟɪ sᴀʜɪʙɪᴍ [{OWNERNAME}](tg://openmessage?user_id={OWNER_ID}) ɢᴇʟᴅɪ, ʜᴏş ɢᴇʟᴅɪɴ ᴇғᴇɴᴅɪᴍ ...__**')

@app.on_message(filters.command(["zar"], ["/", ""]))
def zar_at(client: Client, message: Message):
    client.send_dice(message.chat.id)

@app.on_message(filters.command(["bow"], ["/", ""]))
def bowling_at(client: Client, message: Message):
    client.send_dice(message.chat.id, emoji="🎳")

@app.on_message(filters.command(["basket"], ["/", ""]))
def basket_at(client: Client, message: Message):
    client.send_dice(message.chat.id, emoji="🏀")

@app.on_message(filters.command(["slots"], ["/", ""]))
def slot_at(client: Client, message: Message):
    client.send_dice(message.chat.id, emoji="🎰")

@app.on_message(filters.command(["top"], ["/", ""]))
def top_at(client: Client, message: Message):
    client.send_dice(message.chat.id, emoji="⚽️")

@app.on_message(filters.command(["ok"], ["/", ""]))
def ok_at(client: Client, message: Message):
    client.send_dice(message.chat.id, emoji="🎯")
    
@app.on_message(filters.command(["c"], ["/", ""]))
async def csor(client: Client, message: Message):
    await message.reply_text(f"**__🗨️ ᴄᴇsᴀʀᴇᴛ sᴇᴄ̧ᴛɪɴ, sᴀɴɪʀɪᴍ ғᴀᴢʟᴀ ᴄᴇsᴀʀᴇᴛʟɪsɪɴ .\n\n✦ ʏᴀᴘᴍᴀɴ ɢᴇʀᴇᴋᴇɴ__ : {random.choice(c)}**")

@app.on_message(filters.command(["d"], ["/", ""]))
async def dsor(client: Client, message: Message):
    await message.reply_text(f"**__🗨️ ᴅᴏɢ̆ʀᴜʟᴜᴋ sᴇᴄ̧ᴛɪɴ, ᴄ̧ᴏᴋ ɢᴜ̈ᴢᴇʟ .\n\n✦ sᴀɴᴀ sᴏʀᴜᴍ__ : {random.choice(d)}**")

@app.on_message(filters.command(["soz"], ["/", ""]))
async def dsor(client: Client, message: Message):
    await message.reply_text(f"**🌹 𝖦𝗎̈𝗓𝖾𝗅 𝖲𝗈̈𝗓 :\n\n{random.choice(guzelsoz)}**")

oyun = {}
rating = {}
@app.on_message(filters.command("turet") & ~filters.private & ~filters.channel)
async def kelimeoyun(c:Client, m:types.Message):
    if message.chat.type == "private":
        return await message.reply(f"{nogroup}")

    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**✦ Oyunu Durdurmak için ➻ /iptal**")
    else:
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

        text = f"""**{m.from_user.mention}  oyunu başlattı .
        
🎯 Raund : {oyun[m.chat.id]['round']}/80
📖 Kelime :   <code>{kelime_list}</code>
💰 Kazandıracak Puan : 1
🔎 İpucu : 1. {oyun[m.chat.id]["kelime"][0]}
🌟 Uzunluk : {int(len(kelime_list)/2)} 

👁️‍🗨️ Karışık Harflerden Doğru Kelimeyi Bulun . . .
        **"""
        
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("✦  Pass Geç  ✦", callback_data="pass")]
            ]
        )
        
        await c.send_message(m.chat.id, text, reply_markup=keyboard)

@app.on_callback_query(filters.regex("pass"))
async def passs(c:Client, cb:types.CallbackQuery):
    global oyun
    
    try:
        aktif = oyun[cb.message.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        if oyun[cb.message.chat.id]["pass"] < 5:
            oyun[cb.message.chat.id]["pass"] += 1 
            pass_hakki = 5 - oyun[cb.message.chat.id]["pass"]
            
            oyun[cb.message.chat.id]["kelime"] = kelime_sec()
            oyun[cb.message.chat.id]["aktif"] = True
            
            kelime_list = ""
            kelime = list(oyun[cb.message.chat.id]['kelime'])
            shuffle(kelime)
            
            for harf in kelime:
                kelime_list+= harf + " "
            
            text = f"""**{cb.from_user.mention}  pass geçti .
➻ {pass_hakki} Pass Hakkın Kaldı.

🎯 Raund : {oyun[cb.message.chat.id]['round']}/80
📖 Kelime :   <code>{kelime_list}</code>
💰 Kazandıracak Puan : 1
🔎 İpucu : 1. {oyun[cb.message.chat.id]["kelime"][0]}
🌟 Uzunluk : {int(len(kelime_list)/2)} 

👁️‍🗨️ Karışık Harflerden Doğru Kelimeyi Bulun . . .
            **"""

            keyboard = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("✦  Pass Geç  ✦", callback_data="pass")]
                ]
            )
            
            await c.send_message(cb.message.chat.id, text, reply_markup=keyboard)
            
        else:
            await c.send_message(cb.message.chat.id, f"**✦ Pass Hakkın Tükendi .\n✦ Oyunu Bitirmek için ➻ /iptal**")
     
@app.on_message(filters.command("iptal") & ~filters.private & ~filters.channel)
async def stop(c:Client, m:Message):
    if message.chat.type == "private":
        return await message.reply(f"{nogroup}")

    global oyun
    
    if m.chat.id in oyun and "oyuncular" in oyun[m.chat.id]:
        siralama = []
        for i in oyun[m.chat.id]["oyuncular"]:
            siralama.append(f" {i}  :  {oyun[m.chat.id]['oyuncular'][i]}  Puan")
        siralama.sort(key=lambda x: x.split(":")[1].strip(), reverse=True)
        siralama_text = ""
        for i, sira in enumerate(siralama, start=1):
            siralama_text += f"{i}) {sira}\n"     
    
        await c.send_message(m.chat.id, f"**✦ Oyun İptal Edildi !\n\n🎖️  Puan Tablosu  🎖️\n\n{siralama_text}**", reply_to_message_id=m.message_id)
        oyun[m.chat.id] = {}

@app.on_message(filters.text & ~filters.private & ~filters.channel)
async def buldu(c: Client, m: Message):
    global oyun
    global rating
    try:
        if m.chat.id in oyun:
            if m.text.lower().replace(" ", "") == oyun[m.chat.id]["kelime"]:
                if f"{m.from_user.mention}" in rating:
                    rating[f"{m.from_user.mention}"] += 1
                else:
                    rating[f"{m.from_user.mention}"] = 1

                try:
                    puan = oyun[m.chat.id]["oyuncular"].get(str(m.from_user.mention), 0)
                    oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)] = puan + 1
                except KeyError:
                    oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)] = 1

                oyun[m.chat.id]["kelime"] = kelime_sec()
                oyun[m.chat.id]["round"] = oyun[m.chat.id]["round"] + 1

                if not oyun[m.chat.id]["round"] <= 80:
                    siralama = []
                    for i in oyun[m.chat.id]["oyuncular"]:
                        siralama.append(f" {i} : {oyun[m.chat.id]['oyuncular'][i]} Puan")                    
                    siralama.sort(key=lambda x: int(x.split(" : ")[1]) if x.split(" : ")[1].isdigit() else 0)
                    siralama_text = "\n".join([f"{index+1}) {siralama[index]}" for index in range(len(siralama))])
                    oyun[m.chat.id] = {}
                    return await c.send_message(m.chat.id, f"**✦ Oyun Bitti !\n\n🎖️ Puan Tablosu 🎖️\n\n{siralama_text}**")

                kelime_list = ""
                kelime = list(oyun[m.chat.id]['kelime'])
                shuffle(kelime)
                for harf in kelime:
                    kelime_list += harf + " "

                text = f"""**{m.from_user.mention}  kelimeyi buldu !

🎯 Raund: {oyun[m.chat.id]['round']}/80
📖 Kelime: <code>{kelime_list}</code>
💰 Kazandıracak Puan: 1
🔎 İpucu: 1. {oyun[m.chat.id]["kelime"][0]}
🌟 Uzunluk: {int(len(kelime_list) / 2)}

👁️‍🗨️ Karışık Harflerden Doğru Kelimeyi Bulun . . .
            **"""

                keyboard = InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("✦ Pass Geç ✦", callback_data="pass")]
                    ]
                )

                await c.send_message(m.chat.id, text, reply_markup=keyboard)
    except KeyError:
        pass
                
'''
@app.on_message(filters.command("skorssk"))
async def ratingsa(c:Client, m:Message):
    if message.chat.type == "private":
        return await message.reply(f"{nogroup}")

    metin = """**🎖️  Global Top 20  🎖️**

"""
    eklenen = 1
    s = sorted(rating.items(), key=lambda x: x[1], reverse=True)
    for kisi in s:
        if eklenen == 1:
            metin +=  f"🥇  **{kisi[0]}  :  {kisi[1]}  Puan**\n" 
        if eklenen == 2:
            metin +=  f"🥈  **{kisi[0]}  :  {kisi[1]}  Puan**\n"
        if eklenen == 3:
            metin +=  f"🥉  **{kisi[0]}  :  {kisi[1]}  Puan**\n"
        if  not eklenen in [1,2,3]:
            metin +=  f" **{eklenen})  {kisi[0]}**  :  **{kisi[1]}  Puan**\n" 
        eklenen+=1
        if eklenen == 21:
            break
    await c.send_message(m.chat.id, metin)
'''

@app.on_message(filters.command("sinfo") & filters.user(OWNER_ID))
async def ksayi(c:Client, m:Message):
    await m.reply(f"**Sistemde kayıtlı {len(kelimeler)} kelime bulunmakta .**")

blocked_users = []
@app.on_message(filters.command("block") & filters.user(OWNER_ID))
def block_user(client: Client, message: Message):
    if len(message.command) == 2:
        user_id = int(message.command[1])
        if user_id not in blocked_users:
            blocked_users.append(user_id)
            user_name = client.get_chat(user_id).first_name
            message.reply_text(f"Kullanıcı {user_id} ({user_name}) kara listeye alındı.")
        else:
            message.reply_text(f"Kullanıcı {user_id} zaten kara listede.")
    else:
        message.reply_text("Kullanım: /block <kullanıcı_id>")

@app.on_message(filters.command("unblock") & filters.user(OWNER_ID))
def unblock_user(client: Client, message: Message):
    if len(message.command) == 2:
        user_id = int(message.command[1])
        if user_id in blocked_users:
            blocked_users.remove(user_id)
            user_name = client.get_chat(user_id).first_name
            message.reply_text(f"Kullanıcı {user_id} ({user_name}) kara listeden çıkarıldı.")
        else:
            message.reply_text(f"Kullanıcı {user_id} zaten kara listede değil.")
    else:
        message.reply_text("Kullanım: /unblock <kullanıcı_id>")

@app.on_message(filters.command("blocklist") & filters.user(OWNER_ID))
def blocklist(client: Client, message: Message):
    if len(blocked_users) > 0:
        blocked_users_text = ""
        for user_id in blocked_users:
            user_name = client.get_chat(user_id).first_name
            blocked_users_text += f"{user_id} - {user_name}\n"
        message.reply_text(f"Kara listede olan kullanıcılar:\n{blocked_users_text}")
    else:
        message.reply_text("Kara listede hiç kullanıcı yok.")

@app.on_message(~filters.user(OWNER_ID))
def handle_messages(client: Client, message: Message):
    if message.from_user.id in blocked_users:
        # Kara listedeki kullanıcının mesajını algılama
        return
        
################### VERİTABANI VERİ GİRİŞ ÇIKIŞI #########################
class Database: 
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id): # Veritabanına yeni kullanıcı ekler
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat(),
            ban_status=dict(
                is_banned=False,
                ban_duration=0,
                banned_on=datetime.date.max.isoformat(),
                ban_reason="",
            ),
        )

    async def add_user(self, id): # Veritabına yeni kullanıcı eklemek için ön def
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id): # Bir kullanıcının veritabında olup olmadığını kontrol eder.
        user = await self.col.find_one({"id": int(id)})
        return bool(user)

    async def total_users_count(self): # Veritabanındaki toplam kullanıcıları sayar.
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self): # Veritabındaki tüm kullanıcıların listesini verir.
        return self.col.find({})

    async def delete_user(self, user_id): # Veritabından bir kullanıcıyı siler.
        await self.col.delete_many({"id": int(user_id)})

    async def ban_user(self, user_id, ban_duration, ban_reason): # Veritabanınızdaki bir kullanıcıyı yasaklılar listesine ekler.
        ban_status = dict(
            is_banned=True,
            ban_duration=ban_duration,
            banned_on=datetime.date.today().isoformat(),
            ban_reason=ban_reason,
        )
        await self.col.update_one({"id": user_id}, {"$set": {"ban_status": ban_status}})

    async def remove_ban(self, id): # Veritabanınızdaki yasaklılar listesinde bulunan bir kullanıcın yasağını kaldırır.
        ban_status = dict(
            is_banned=False,
            ban_duration=0,
            banned_on=datetime.date.max.isoformat(),
            ban_reason="",
        )
        await self.col.update_one({"id": id}, {"$set": {"ban_status": ban_status}})

    async def get_ban_status(self, id): # Bir kullanıcın veritabanınızda yasaklılar listesinde olup olmadığını kontrol eder.
        default = dict(
            is_banned=False,
            ban_duration=0,
            banned_on=datetime.date.max.isoformat(),
            ban_reason="",
        )
        user = await self.col.find_one({"id": int(id)})
        return user.get("ban_status", default)

    async def get_all_banned_users(self): # Veritabınızdaki yasaklı kullanıcılar listesini verir.
        return self.col.find({"ban_status.is_banned": True})


db = Database(DATABASE_URL, BOT_USERNAME)
mongo_db_veritabani = MongoClient(DATABASE_URL)
dcmdb = mongo_db_veritabani.handlers



################## KULLANICI KONTROLLERİ #############
async def handle_user_status(bot: Client, cmd: Message): # Kullanıcı kontrolü
    chat_id = cmd.chat.id
    if not await db.is_user_exist(chat_id):
        if cmd.chat.type == "private":
            await db.add_user(chat_id)
            await bot.send_message(LOG_CHANNEL,LAN.BILDIRIM.format(cmd.from_user.first_name, cmd.from_user.id, cmd.from_user.first_name, cmd.from_user.id))
        else:
            await db.add_user(chat_id)
            chat = bot.get_chat(chat_id)
            if str(chat_id).startswith("-100"):
                new_chat_id = str(chat_id)[4:]
            else:
                new_chat_id = str(chat_id)[1:]
            await bot.send_message(LOG_CHANNEL,LAN.GRUP_BILDIRIM.format(cmd.from_user.first_name, cmd.from_user.id, cmd.from_user.first_name, cmd.from_user.id, chat.title, cmd.chat.id, cmd.chat.id, cmd.message_id))

    ban_status = await db.get_ban_status(chat_id) # Yasaklı Kullanıcı Kontrolü
    if ban_status["is_banned"]:
        if int((datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])).days) > int(ban_status["ban_duration"]):
            await db.remove_ban(chat_id)
        else:
            if GROUP_SUPPORT:
                msj = f"@{GROUP_SUPPORT}"
            else:
                msj = f"[{LAN.SAHIBIME}](tg://user?id={OWNER_ID})"
            if cmd.chat.type == "private":
                await cmd.reply_text(LAN.PRIVATE_BAN.format(msj), quote=True)
            else:
                await cmd.reply_text(LAN.GROUP_BAN.format(msj),quote=True)
                await bot.leave_chat(cmd.chat.id)
            return
    await cmd.continue_propagation()




############### Broadcast araçları ###########
broadcast_ids = {}


async def send_msg(user_id, message): # Mesaj Gönderme
    try:
        if GONDERME_TURU is False:
            await message.forward(chat_id=user_id)
        elif GONDERME_TURU is True:
            await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(int(e.x))
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id}: {LAN.NOT_ONLINE}\n"
    except UserIsBlocked:
        return 400, f"{user_id}: {LAN.BOT_BLOCKED}\n"
    except PeerIdInvalid:
        return 400, f"{user_id}: {LAN.USER_ID_FALSE}\n"
    except Exception:
        return 500, f"{user_id}: {traceback.format_exc()}\n"

async def main_broadcast_handler(m, db): # Ana Broadcast Mantığı
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = "".join(random.choice(string.ascii_letters) for i in range(3))
        if not broadcast_ids.get(broadcast_id):
            break
    out = await m.reply_text(
        text=LAN.BROADCAST_STARTED)
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(total=total_users, current=done, failed=failed, success=success)
    async with aiofiles.open("broadcast-logs-g4rip.txt", "w") as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(user_id=int(user["id"]), message=broadcast_msg)
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user["id"])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(current=done, failed=failed, success=success))
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(text=LAN.BROADCAST_STOPPED.format(completed_in, total_users, done, success, failed), quote=True,)
    else:
        await m.reply_document(document="broadcast-logs-g4rip.txt", caption=LAN.BROADCAST_STOPPED.format(completed_in, total_users, done, success, failed), quote=True,)
    os.remove("broadcast-logs-g4rip.txt")



# Genelde müzik botlarının mesaj silme özelliği olur. Bu özelliği ReadMe.md dosyasındaki örnekteki gibi kullanabilirsiniz.
delcmdmdb = dcmdb.admins

async def delcmd_is_on(chat_id: int) -> bool: # Grup için mesaj silme özeliğinin açık olup olmadığını kontrol eder.
    chat = await delcmdmdb.find_one({"chat_id": chat_id})
    return not chat


async def delcmd_on(chat_id: int): # Grup için mesaj silme özeliğini açar.
    already_del = await delcmd_is_on(chat_id)
    if already_del:
        return
    return await delcmdmdb.delete_one({"chat_id": chat_id})


async def delcmd_off(chat_id: int): # Grup için mesaj silme özeliğini kapatır.
    already_del = await delcmd_is_on(chat_id)
    if not already_del:
        return
    return await delcmdmdb.insert_one({"chat_id": chat_id})



################# SAHİP KOMUTLARI #############
# Verileri listeleme komutu
@app.on_message(filters.command("istatistik") & filters.user(OWNER_ID))
async def botstats(bot: Client, message: Message):
    g4rip = await bot.send_message(message.chat.id, LAN.STATS_STARTED.format(message.from_user.mention))
    all_users = await db.get_all_users()
    groups = 0
    pms = 0
    async for user in all_users:
        if str(user["id"]).startswith("-"):
            groups += 1
        else:
            pms += 1
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    total_users = await db.total_users_count()
    await g4rip.edit(text=LAN.STATS.format(BOT_USERNAME, total_users, groups, pms, total, used, disk_usage, free, cpu_usage, ram_usage, __version__), parse_mode="md")



# Botu ilk başlatan kullanıcıların kontrolünü sağlar.
@app.on_message()
async def G4RIP(bot: Client, cmd: Message):
    await handle_user_status(bot, cmd)



# Broadcast komutu
@app.on_message(filters.command("reklam") & filters.user(OWNER_ID) & filters.reply)
async def broadcast_handler_open(_, m: Message):
    await main_broadcast_handler(m, db)


############## BELİRLİ GEREKLİ DEF'LER ###########
def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "K", 2: "M", 3: "G", 4: "T"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


########### ÇOKLU DİL ##############
class LAN(object):

    if LANGAUGE == "TR":

        BILDIRIM = "**🏷 Kullanıcı : {}\n📮 ID : {}\n🧝🏻‍♂️ Profili : [{}](tg://user?id={})**"
        GRUP_BILDIRIM = "**🏷 Kullanıcı : {}\n📮 ID : {}\n🧝🏻‍♂️ Profili : [{}](tg://user?id={})\n💬 Grub : {}\n🌟 Grub ID: {}\n🎲 Mesaj Linki : [Buraya Tıkla](https://t.me/c/{}/{})**"
        SAHIBIME = "sahibime"
        NOT_ONLINE = "Aktif değil"
        BOT_BLOCKED = "Botu engellemiş"
        USER_ID_FALSE = "**Kullanıcı ID Yanlış .**"
        BROADCAST_STARTED = "**✓ Reklam başlatıldı!**"
        BROADCAST_STOPPED = "**✓ Reklam ( {} )  tamamlandı .\n\n👤 Kayıtlı Kullanıcı : {}\n♻️ Gönderme Denemesi : {}\n✅ Başarılı : {}\n⛔ Başarısız : {}**"
        STATS_STARTED = "{} **Veriler Toplanıyor !**"
        STATS = """**@{} Kullanıcıları :\n\n» Toplam Sohbetler : {}\n» Grup Sayısı : {}\n» PM Sayısı : {}**"""


print("Pyrogram Aktif !")
app.run()
