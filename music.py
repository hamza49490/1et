import wget
import logging
import datetime
import asyncio
import datetime
import shutil, psutil, traceback, os
import random
import string
import time
import traceback
import aiofiles
import motor.motor_asyncio
import yt_dlp
import ffmpeg
import aiohttp
import random
import os, youtube_dl, requests, time
from pyrogram import filters
from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch
from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters, types
from time import sleep
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

API_ID = int(os.environ.get("API_ID", "26573250"))
API_HASH = os.environ.get("API_HASH", "6306d2d23b1083a6f757f64f0b0c609c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6818189349:AAF0zbFx_KRY3umEPO5zSUHqlslBb9M62lg")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "YildizMuzikBot")
MCHANNEL = os.environ.get("MCHANNEL", "MuzikKayit")
PLAYLIST_ID = -1001916993821

app = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN
)

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

  print("")
app.run()
