import wget
import pyrogram
from telethon import events
from yt_dlp import YoutubeDL
import os, youtube_dl, requests, time
from youtube_search import YoutubeSearch
from pyrogram.handlers import MessageHandler
import yt_dlp
from telethon import events
from telethon import errors
from telethon import TelegramClient
import random, os, logging, asyncio
from asyncio import sleep
from time import time
from os import remove
from telethon.sync import types
from datetime import datetime 
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from datetime import datetime
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.types import Message, User
from pyrogram.types.messages_and_media import Message
from pyrogram import Client, filters
import string
import time
import datetime
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import shutil, psutil, traceback
import traceback
import aiofiles
from random import randint
from pyrogram import Client, filters, __version__
from pyrogram.types import Message

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID","18049084"))
api_hash = os.environ.get("API_HASH","7e74b1e22026fcc291d32b3d431aa21e")
bot_token = os.environ.get("TOKEN","6581228589:AAE4JqoroTHjTT_EbcG3vD2a_9GDwrrm4pk")
BOT_ID = int(os.environ.get("BOT_ID", "6581228589"))
DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://ok:ok@cluster0.uooya.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") # MongoDB veritabanınızın url'si. Nasıl alacağınızı bilmiyorsanız destek grubu @RepoHaneX'e gelin.
BOT_USERNAME = os.environ.get("BOT_USERNAME","EpikTestBot") # Botunuzun kullanıcı adı.
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL","-1001983841726")) # Botunuzun eylemleri kaydedeceği kayıt grubunun id'si.
GROUP_SUPPORT = os.environ.get("GROUP_SUPPORT", "BuketBilgi") # Botunuzdan yasaklanan kullanıcıların itiraz işlemleri için başvuracağı grup, kanal veya kullanıcı. Boş bırakırsanız otomatik olarak OWNER_ID kimliğine yönlendirecektir.
GONDERME_TURU = os.environ.get("GONDERME_TURU", True) # Botunuzun yanıtladığınız mesajı gönderme türü. Eğer direkt iletmek isterseniz False, kopyasını göndermek isterseniz True olarak ayarlayın.
OWNER_ID = int(os.environ.get("OWNER_ID","6540285284")) # Sahip hesabın id'si
OWNERNAME = "ㅤᴀɪᴋᴏㅤ"
OWNER = [6540285284]
#SUDO_USERS = []
#SUDO = []
LANGAUGE = os.environ.get("LANGAUGE", "TR")

#SUDO_USERS = set()

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

app = Client("GUNC",
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token
             )

anlik_calisan = []
tekli_calisan = []
gece_tag = []
rxyzdev_tagTot = {}
rxyzdev_initT = {} 
rxyzdev_stopT = {}

ozel_list = [6156690167]
grup_sayi = []
etiketuye = []
isleyen = []
user_sayi = []

# ~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
startmesaj =  "**💘 ᴍᴇʀʜᴀʙᴀ\n\n🗨️ ʙᴇɴɪ ɢʀᴜʙᴜɴᴀ ᴇᴋʟᴇᴍᴇʏᴇ ɴᴇ ᴅᴇʀsɪɴ, ᴇʟɪᴍᴅᴇɴ ɢᴇʟᴇɴ ʜᴇʀşᴇʏɪ ʏᴀᴘᴍᴀʏᴀ ʜᴀᴢɪʀɪᴍ ...\n\n🗨️ sɪᴢᴇ ʏᴀʀᴅɪᴍᴄɪ ᴏʟᴀʙɪʟᴍᴇᴍ ɪᴄ̧ɪɴ ᴀşşᴀɢ̆ɪᴅᴀᴋɪ ʙᴜᴛᴏɴʟᴀʀɪ ᴋᴜʟʟᴀɴɪɴ ...**"
startbutton = "**♻️ ʟᴜ̈ᴛғᴇɴ ᴏᴋᴜʏᴜɴ :\n\n👁️‍🗨️ ʙᴇɴɪ ɢʀᴜʙᴜɴᴜᴢᴀ ᴇᴋʟᴇᴅɪᴋᴛᴇɴ sᴏɴʀᴀ, sᴀᴅᴇᴄᴇ | ᴍᴇsᴀᴊʟᴀʀɪ sɪʟᴍᴇ | ʏᴇᴛᴋɪsɪ ᴠᴇʀᴍᴇɴɪᴢ ʏᴇᴛᴇʀʟɪ'ᴅɪʀ ...\n\n🗒️ ɴᴏᴛ : \n• ᴛᴇᴋʟɪ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ᴀʀᴀʟɪɢ̆ɪ 5 sᴀɴɪʏᴇᴅɪʀ ...\n• ᴄ̧ᴏᴋʟᴜ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ᴀʀᴀʟɪɢ̆ɪ 2 sᴀɴɪʏᴇᴅɪʀ ...\n\n👤  ɪʟᴇᴛɪşɪᴍ  :**"
noadmin = "**✓  sᴀᴅᴇᴄᴇ ᴀᴅᴍɪɴʟᴇʀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀ ...**"
nogroup = "**✓  sᴀᴅᴇᴄᴇ ɢʀᴜᴘʟᴀʀᴅᴀ ᴋᴜʟʟᴀɴɪʟᴀʙɪʟɪʀ .**"


import telethon
from telethon.tl import types
from telethon import Button
from telethon.tl import types
from telethon.tl import functions

@client.on(events.NewMessage(pattern='/grup'))
async def grup_info(event):
    if event.is_private:
        await event.respond("**✓  sᴀᴅᴇᴄᴇ ɢʀᴜᴘʟᴀʀᴅᴀ ᴋᴜʟʟᴀɴɪʟᴀʙɪʟɪʀ .**")
        return

    user = await event.get_sender()
    user_first_name = f"[{user.first_name}](tg://user?id={user.id})"

    response_text = f'** {user_first_name} ʟᴜ̈ᴛғᴇɴ ʙᴇᴋʟᴇ ...**'
    response = await event.respond(response_text)
    await asyncio.sleep(2)
    await response.delete()

    chat = await event.get_chat()
    group_name = chat.title
    group_id = chat.id

    chat_info = await event.client.get_entity(group_id)

    deleted_count = 0
    active_count = 0
    bot_count = 0
    total_count = 0

    async for participant in event.client.iter_participants(chat_info):
        total_count += 1
        if participant.deleted:
            deleted_count += 1
        elif not participant.bot:
            active_count += 1
        elif participant.bot:
            bot_count += 1

    special_status = ""
    if deleted_count > 0:
        special_status += f'➻ **sɪʟɪɴᴇɴ ʜᴇsᴀᴘʟᴀʀ: {deleted_count}**\n'
    if bot_count > 0:
        special_status += f'➻ **ɢʀᴜᴘ ʙᴏᴛʟᴀʀɪ : {bot_count}**\n'

    if not special_status:
        special_status = "ʙᴜʟᴜɴᴀᴍᴀᴅɪ"
	    
    owner_username = "6540285284"

    owner_button = Button.inline("✅  ʏᴏ̈ɴᴇᴛɪᴄɪʟᴇʀ", data="admins")

    response_text = (
        f'➻ **ɢʀᴜᴘ ᴀᴅɪ : {group_name}**\n'
        f'➻ **ɢʀᴜᴘ ɪᴅ :** `-100{group_id}`\n'
	f'➻ **ᴜʏᴇ sᴀʏɪsɪ : {total_count}**\n'
        f'➻ **ᴀᴋᴛɪғ ᴋᴜʟʟᴀɴɪᴄɪʟᴀʀ : {active_count}**\n'
        f'{special_status}'
    )

    await event.respond(response_text, buttons=[[owner_button]])

@client.on(events.callbackquery.CallbackQuery(data="admins"))
async def show_admins(event):
    chat = await event.get_chat()
    admins = await event.client.get_participants(chat, filter=types.ChannelParticipantsAdmins)
    admin_list = ""
    for admin in admins:
        admin_list += f"\n➻  [{admin.first_name}](tg://user?id={admin.id})"
    await event.edit(f"**🗨️  ɢʀᴜᴘᴛᴀᴋɪ ᴀᴅᴍɪɴʟᴇʀ : \n{admin_list}**")

#@client.on(events.NewMessage(pattern="^/adminler ?(.*)"))
#async def mentionall(tagadmin):
#
#	if tagadmin.pattern_match.group(1):
#		seasons = tagadmin.pattern_match.group(1)
#	else:
#		seasons = ""
#
#	chat = await tagadmin.get_input_chat()
#	a_=0
#	await tagadmin.delete()
#	async for i in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
#		if a_ == 500:
#			break
#		a_+=5
#		await tagadmin.client.send_message(tagadmin.chat_id, "**[{}](tg://user?id={}) {}**".format(i.first_name, i.id, seasons))
#		sleep(1)
#____________________________________________________________________________

@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def tag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}",buttons=(
                     [
                      Button.inline("✅  ʏᴏ̈ɴᴇᴛɪᴄɪʟᴇʀ", data="admins")
                     ]
                   ), 
                 link_preview=False)
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__ᴇꜱᴋɪ ᴍᴇꜱᴀᴊʟᴀʀɪ ɢᴏʀᴇᴍɪʏᴏʀᴜᴍ!__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ᴍᴇꜱᴀᴊɪ ʏᴀᴢᴍᴀᴅɪɴ!__")
  else:
    return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\nᴠᴇʏᴀ ᴛɪᴋʟᴀʏɪɴ ➙ /tag**")
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏᴇ ʙᴀşʟɪʏᴏʀᴜᴍ ...**", buttons=(
                      [
                      Button.url('🗨️  ʙɪʟɢɪ ᴋᴀɴᴀʟɪ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)

    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in gece_tag:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**{usrtxt}  {msg}**")
        await asyncio.sleep(5)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...\n\n➻ {rxyzdev_initT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**", buttons=(
                      [
                      Button.url('🗨️  ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ  🗨️', f'https://t.me/{BOT_USERNAME}?startgroup=a')
                      ]
                    ),
                    link_preview=False)


@client.on(events.NewMessage(pattern="^/atag ?(.*)"))
async def mentionalladmin(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**✓  sᴀᴅᴇᴄᴇ ɢʀᴜᴘʟᴀʀᴅᴀ ᴋᴜʟʟᴀɴɪʟᴀʙɪʟɪʀ .**")
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**✓  sᴀᴅᴇᴄᴇ ᴀᴅᴍɪɴʟᴇʀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀ ...**",buttons=(
                     [
                      Button.inline("✅  ʏᴏ̈ɴᴇᴛɪᴄɪʟᴇʀ", data="admins")
                     ]
                   ), 
                 link_preview=False)
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**ᴇꜱᴋɪ ᴍᴇꜱᴀᴊʟᴀʀɪ ɢᴏʀᴇᴍɪʏᴏʀᴜᴍ!**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ᴍᴇꜱᴀᴊɪ ʏᴀᴢᴍᴀᴅɪɴ!**")
  else:
    return await event.respond("**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\nᴠᴇʏᴀ ᴛɪᴋʟᴀʏɪɴ ➙ /atag**")
	    
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏᴇ ʙᴀşʟɪʏᴏʀᴜᴍ ...**", buttons=(
                      [
                      Button.url('🗨️  ʙɪʟɢɪ ᴋᴀɴᴀʟɪ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
    async for usr in client.iter_participants(event.chat_id,filter=ChannelParticipantsAdmins):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in anlik_calisan:
        await event.respond("**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴅᴜʀᴅᴜʀᴅᴜᴍ ...**", buttons=(
                      [
                      Button.url('🗨️  ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ  🗨️', f'https://t.me/{BOT_USERNAME}?startgroup=a')
                      ]
                    ),
                    link_preview=False)
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**{usrtxt}  {msg}**")
        await asyncio.sleep(5)
        usrnum = 0
        usrtxt = ""

    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...**", buttons=(
                      [
                      Button.url('🗨️  ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ  🗨️', f'https://t.me/{BOT_USERNAME}?startgroup=a')
                      ]
                    ),
                    link_preview=False)

#mrt = await message.reply_text("✓ **Lütfen Bekleyin ...**")
#    await asyncio.sleep(2)
#    await mrt.edit(f"** xd **")
#########################
@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(BOT_ID):
            await msg.reply(
                f'''**💞 ᴍᴇʀʜᴀʙᴀ , {msg.from_user.mention}\n\n🗨️ ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇᴅɪɢ̆ɪɴ ɪᴄ̧ɪɴ ᴛᴇşşᴇᴋᴜ̈ʀ ᴇᴅᴇʀɪᴍ, ʙᴇɴɪ ʏᴏ̈ɴᴇᴛɪᴄɪ ʏᴀᴘᴍᴀʏɪ ᴜɴᴜᴛᴍᴀʏɪɴ ...\n\n🗯️ ᴅᴀʜᴀ ғᴀᴢʟᴀ ʙɪʟɢɪ ɪᴄ̧ɪɴ ᴀşşᴀɢ̆ɪᴅᴀᴋɪ ʙᴜᴛᴏɴᴜ ᴋᴜʟʟᴀɴɪɴ ...**''', 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🛡️  ʙᴜʀᴀʏᴀ ᴛɪᴋʟᴀ  ", url=f"https://t.me/{BOT_USERNAME}?start")]])
    )
        elif str(new_user.id) == str(OWNER_ID):
            await msg.reply('**🗯️ ᴅᴇɢ̆ᴇʀʟɪ sᴀʜɪʙɪᴍ [ㅤᴀɪᴋᴏㅤ](tg://openmessage?user_id=6540285284) ɢᴇʟᴅɪ, ʜᴏş ɢᴇʟᴅɪɴ ᴇғᴇɴᴅɪᴍ ...**')
		

app.run()
print(" Bot çalışıyor :)")
client.run_until_disconnected()
