import wget
import os
import logging
import random

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery 
from yt_dlp import YoutubeDL
import os, youtube_dl, requests, time
from youtube_search import YoutubeSearch
from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters
import yt_dlp
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)
  
##############################
@Client.on_message(filters.command(["bul", "song"]) & ~filters.edited)
async def bul(_, message):
    try:
        await message.delete()
    except:
        pass
    query = " ".join(message.command[1:])
    m = await message.reply("➻  **şᴀʀᴋɪ ᴀʀᴀɴɪʏᴏʀ !**")
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
        await m.edit("➻  **şᴀʀᴋɪ ʙᴜʟᴜɴᴀᴍᴀᴅɪ !**")
        print(str(e))
        return
    await m.edit("➻  **şᴀʀᴋɪ ɪɴᴅɪʀɪʟɪʏᴏʀ !**")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"**➻ ᴘᴀʀᴄ̧ᴀ : {title[:35]}\n➻ sᴜ̈ʀᴇ : {duration}\n\n➻ ɪsᴛᴇʏᴇɴ : {message.from_user.first_name}**"
        res = f"**➻ ᴘᴀʀᴄ̧ᴀ : {title[:35]}\n➻ sᴜ̈ʀᴇ : {duration}\n\n➻ ɪsᴛᴇʏᴇɴ : {message.from_user.first_name}**"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        await m.edit("➻ **şᴀʀᴋɪ ʏᴜ̈ᴋʟᴇɴɪʏᴏʀ !**")
        await message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name, performer="♫︎ 𝐌𝐮̈𝐳𝐢𝐤 𝐈𝐧𝐝𝐢𝐫𝐢𝐜𝐢 ♫︎")
        await m.delete()
        await _.send_audio(chat_id=PLAYLIST_ID, audio=audio_file, caption=res, performer="♫︎ 𝐌𝐮̈𝐳𝐢𝐤 𝐈𝐧𝐝𝐢𝐫𝐢𝐜𝐢 ♫︎", parse_mode='md', title=title, duration=dur, thumb=thumb_name)
    except Exception as e:
        await m.edit("🗨️ **ʙᴇɴɪ ʏᴏɴᴇᴛɪᴄɪ ʏᴀᴘɪɴ !**")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

@Client.on_message(filters.command(["vbul", "vsong"]) & ~filters.edited)
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
        results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]
        message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("➻  **ᴠɪᴅᴇᴏ ᴀʀᴀɴɪʏᴏʀ !**")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"➻  **ᴠɪᴅᴇᴏ ʙᴜʟᴜɴᴀᴍᴀᴅɪ !**")
    preview = wget.download(thumbnail)
    await msg.edit("➻  **ᴠɪᴅᴇᴏ ɪɴᴅɪʀɪʟɪʏᴏʀ !**")
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=ytdl_data["title"],
    )
    try:
        os.remove(file_name)
        await msg.delete()
    except Exception as e:
        print(e)

@Client.on_message(filters.command(["ara", "search"]) & ~filters.edited)
async def ytsearch(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        if len(message.command) < 2:
            return await message.reply_text("**➻ sᴏɴᴜᴄ̧ ʙᴜʟᴜɴᴀᴍᴀᴅɪ !**")
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("**➻  ᴀʀɪʏᴏʀᴜᴍ !**")
        results = YoutubeSearch(query, max_results=6).to_dict()
        i = 0
        text = ""
        while i < 6:
            text += f"**💬 ᴘᴀʀᴄ̧ᴀ : {results[i]['title']}**\n"
            text += f"**⌚ sᴜ̈ʀᴇ : {results[i]['duration']}**\n"
            text += f"**🔗 ʟɪɴᴋ : [ ʏᴏᴜᴛᴜʙᴇ'ᴅᴇɴ ɪᴢʟᴇ ](https://youtube.com{results[i]['url_suffix']})**\n\n"
            i += 1
        await m.edit_text(
            text=text,
            disable_web_page_preview=True,
        )
    except Exception as e:
        await message.reply_text(str(e))

@Client.on_message(filters.command(["reload"], ["/"]) & ~filters.private & ~filters.channel)
async def reload(client: Client, message: Message):
    await message.reply_text("**♻️ ʙᴏᴛ ʏᴇɴɪᴅᴇɴ ʙᴀşʟᴀᴅɪ .\n♻️ ᴀᴅᴍɪɴ ʟɪsᴛᴇsɪ ɢᴜ̈ɴᴄᴇʟʟᴇɴᴅɪ .**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✅  ʏᴏ̈ɴᴇᴛɪᴄɪʟᴇʀ", callback_data="admins"),
                ],
            ],
        ),
    )	 
  
#@app.on_message(filters.command(["eros"],["/", ""]))
#async def eros(c:Client, m:Message):
#    users = await c.get_chat_members(m.chat.id, limit=1000)
#    
#    users_l = []
#    for user in users:
#        if user.user.is_bot or user.user.is_deleted:
#            pass
#        else:
#            users_l.append(user.user)
#    count = len(users_l)
    
#    ilk = users_l[randint(0,count)]
#    iki = users_l[randint(0,count)]
    
#    if ilk.id==1550788256 or ilk.id==5576614947 or iki.id==5375589992 or iki.id==5576614947:
#        await m.reply(f"**💘 ᴇʀᴏs'ᴜɴ ᴏᴋᴜɴᴜ ᴀᴛᴛɪᴍ .\n✓  ɢɪᴢʟɪ ᴀşɪᴋʟᴀʀ :\n\n[ ✍🏻 ](tg://user?id=5053767281) ❤️ [ . ](tg://user?id=5533927130)**")
        
#    else:
#        await m.reply(f"**💘 ᴇʀᴏs'ᴜɴ ᴏᴋᴜɴᴜ ᴀᴛᴛɪᴍ .\n✓  ɢɪᴢʟɪ ᴀşɪᴋʟᴀʀ :\n\n{ilk.mention} ❣️ {iki.mention}\n\n💞 sᴇᴠɢɪ ᴏʀᴀɴɪ : %{random.choice(say)}**")
