import codecs
import heroku3
import asyncio
import aiohttp
import math
import ssl
import requests
import random
import base64
import random
import time
import datetime
import shutil, psutil, traceback
import traceback
import aiofiles
import os, requests, time
import random, os, logging, asyncio
import telethon
import config
from config import *
from mesaj.botmesaj import *
from telethon.tl.types import MessageEntityBold
from telethon.sync import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerChannel
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.functions.users import GetFullUserRequest
from telethon.sessions import StringSession
from telethon.events import StopPropagation
from telethon.tl.functions.messages import ForwardMessagesRequest
from telethon.tl.types import InputPeerChat
from telethon.tl.types import User
from telethon.tl import types
from telethon.tl import functions
from pyrogram.handlers import MessageHandler
from telethon import errors
from time import time
from os import remove
from telethon.sync import types
from datetime import datetime 
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.functions.messages import SendMessageRequest
from telethon.sync import TelegramClient, events
from telethon.events import ChatAction
from telethon import events, sync
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User
from pyrogram.types.messages_and_media import Message
from pyrogram import Client, filters
from random import randint
from telethon.tl.functions import *
from telethon.tl import functions


logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

client = TelegramClient('client', config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN)


@client.on(events.NewMessage(pattern='/start', func=lambda e: e.is_private))
async def start(event):
    loading_message = await event.reply("🔄 **ʟᴜ̈ᴛғᴇɴ ʙᴇᴋʟᴇʏɪ̇ɴ .**")
    await asyncio.sleep(2)
    await client.edit_message(event.chat_id, loading_message.id, 
        f"""**🎉  ʜᴇʏ  {event.sender.first_name}\n\n🌿  sᴏɴ ᴅᴇʀᴇᴄᴇ ɢᴇʟɪ̇şᴍɪ̇ş, ʙɪ̇ʀ ᴄ̧ᴏᴋ ᴏ̈ᴢᴇʟʟɪ̇ɢ̆ᴇ sᴀʜɪ̇ᴘ ʙɪ̇ʀ ʙᴏᴛᴜᴍ !\n\n💥  ᴋᴏᴍᴜᴛʟᴀʀ ᴠᴇ ᴅᴇsᴛᴇᴋ ɪ̇ᴄ̧ɪ̇ɴ ᴀşᴀɢ̆ɪᴅᴀᴋɪ̇ ʙᴜᴛᴏɴʟᴀʀɪ ᴋᴜʟʟᴀɴɪɴ !\n\n❤️‍🔥 ᴅɪ̇ʟᴇʀsᴇɴɪ̇ᴢ ɢɪ̇ᴢʟɪ̇ & ᴀᴄ̧ɪᴋ ɪ̇ᴛɪ̇ʀᴀғʟᴀʀ ᴇᴅᴇʙɪ̇ʟɪ̇ʀsɪ̇ɴɪ̇ᴢ !**""",
        buttons=[
            [Button.url('✚  ʙᴇɴɪ̇ ɢʀᴜʙᴀ ᴇᴋʟᴇ  ✚', url=f'https://t.me/{BOT_USERNAME}?startgroup=a')],
            [Button.inline('📚  ᴋᴏᴍᴜᴛʟᴀʀ', data='help'), Button.url('🌟  ᴋᴀɴᴀʟ', url=f'https://t.me/{CHANNELL}')],
            [Button.url('❤️‍🔥  ᴅᴇsᴛᴇᴋ', url=f'https://t.me/{SUPPORT}')],
        ]
    )

    user_id = event.sender_id
    user_name = event.sender.first_name
    user_username = event.sender.username

    
    log_message = f"**🎂 ʙᴏᴛᴜ ᴘᴍ'ᴅᴇɴ ʙᴀşʟᴀᴛᴛɪ !\n\nᴋᴜʟʟᴀɴɪᴄɪ : {user_name}\nᴋᴜʟʟᴀɴɪᴄɪ ᴀᴅɪ : @{user_username}\nᴋᴜʟʟᴀɴɪᴄɪ ɪᴅ : `{user_id}`**"
    await client.send_message(LOG_CHANNEL, log_message)

@client.on(events.NewMessage(pattern='(?i)/start|/help'))
async def start(event):
    if event.is_group:
        loading_message = await event.reply("**🔄 ʟᴜ‌ᴛғᴇɴ ʙᴇᴋʟᴇʏɪ‌ɴ .**")
        await asyncio.sleep(2)
        await client.edit_message(event.chat_id, loading_message.id, 
            f"""**👋🏻  ᴍᴇʀʜᴀʙᴀ {event.sender.first_name}\n\n🍀  ʏᴀʀᴅɪᴍ ɪ‌ᴄ‌ɪɴ ᴀs‌ᴀɢ‌ɪᴅᴀᴋɪ‌ ʙᴜᴛᴏɴʟᴀʀɪ ᴅᴇɴᴇʏɪ‌ɴ !**""",
            buttons=[
                [Button.url("📚  ᴋᴏᴍᴜᴛʟᴀʀ", url=f"https://t.me/{BOT_USERNAME}?start")],
                [Button.url("❤️‍🔥  ᴅᴇsᴛᴇᴋ", url=f"https://t.me/{SUPPORT}"),
                 Button.url("🌟  ᴋᴀɴᴀʟ", url=f"https://t.me/{CHANNELL}")]
            ]
	)

@client.on(events.callbackquery.CallbackQuery(data="start"))
async def start(event):
    smasaj = f"**👋🏻  ᴍᴇʀʜᴀʙᴀ\n\n🌿  sᴏɴ ᴅᴇʀᴇᴄᴇ ɢᴇʟɪ̇şᴍɪ̇ş, ʙɪ̇ʀ ᴄ̧ᴏᴋ ᴏ̈ᴢᴇʟʟɪ̇ɢ̆ᴇ sᴀʜɪ̇ᴘ ʙɪ̇ʀ ʙᴏᴛᴜᴍ !\n\n💥  ᴋᴏᴍᴜᴛʟᴀʀ ᴠᴇ ᴅᴇsᴛᴇᴋ ɪ̇ᴄ̧ɪ̇ɴ ᴀşᴀɢ̆ɪᴅᴀᴋɪ̇ ʙᴜᴛᴏɴʟᴀʀɪ ᴋᴜʟʟᴀɴɪɴ !\n\n❤️‍🔥 ᴅɪ̇ʟᴇʀsᴇɴɪ̇ᴢ ɢɪ̇ᴢʟɪ̇ & ᴀᴄ̧ɪᴋ ɪ̇ᴛɪ̇ʀᴀғʟᴀʀ ᴇᴅᴇʙɪ̇ʟɪ̇ʀsɪ̇ɴɪ̇ᴢ !**"
    await event.edit(smasaj, buttons=[
            [Button.url('✚  ʙᴇɴɪ̇ ɢʀᴜʙᴀ ᴇᴋʟᴇ  ✚', url=f'https://t.me/{BOT_USERNAME}?startgroup=a')],
            [Button.inline('📚  ᴋᴏᴍᴜᴛʟᴀʀ', data='help'), Button.url('🌟  ᴋᴀɴᴀʟ', url=f'https://t.me/{CHANNELL}')],
            [Button.url('❤️‍🔥  ᴅᴇsᴛᴇᴋ', url=f'https://t.me/{SUPPORT}')],
    ]
 )

@client.on(events.NewMessage(pattern='(?i)^/eros$|^/ship$|^eros$|^ship$'))
async def handle_eros(event):
    if event.is_private:
        return await event.reply(f"{nogroup}")

    chat = await client.get_entity(event.chat_id)
    if event.reply_to_msg_id:
        reply_msg = await event.get_reply_message()
        user1 = await client.get_entity(reply_msg.from_id)
        user2 = await client.get_entity(event.sender_id)
        love_percentage = random.randint(0, 100)
        await event.reply(f"**🌟 ᴇʀᴏs'ᴜɴ ᴏᴋᴜɴᴜ ᴀᴛᴛɪᴍ !\n\n[{user2.first_name}](tg://user?id={user2.id})  {random.choice(kalpss)}  [{user1.first_name}](tg://user?id={user1.id})\n\n✦ sᴇᴠɢɪ ᴏʀᴀɴɪ : %{love_percentage}**")
    else:
        participants = await client.get_participants(chat)
        active_users = [user for user in participants if not user.bot and not user.deleted and user.id != (await client.get_me()).id]
        if len(active_users) < 2:
            await event.reply("**🔹 ʏᴇᴛᴇʀʟɪ ᴀᴋᴛɪғ ᴋᴜʟʟᴀɴɪᴄɪ ʏᴏᴋ !**")
        else:
            user1, user2 = random.sample(active_users, 2)
            love_percentage = random.randint(0, 100)
            await event.reply(f"**🌟 ᴇʀᴏs'ᴜɴ ᴏᴋᴜɴᴜ ᴀᴛᴛɪᴍ !\n\n[{user1.first_name}](tg://user?id={user1.id})  {random.choice(kalpss)}  [{user2.first_name}](tg://user?id={user2.id})\n\n✦ sᴇᴠɢɪ ᴏʀᴀɴɪ : %{love_percentage}**")
		
@client.on(events.NewMessage(pattern='(?i)^/slap$|^slap$'))
async def slap(event):
    if event.is_private:
        return await event.reply(f"{nogroup}")

    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        user = reply_message.sender
        if user:
            user_name = f"[{user.first_name}](tg://user?id={user.id})"
            slap_phrases = [
                                        f"{user_name} 'ın Gözlerini Oydu! Kör Oldu Zavallı 😱",
	             	                   f"{user_name} 'ın Sırtına Bindi! At Gibi Koşuyorsun Mübarek .",
	             	                   f"{user_name} 'ın Kulağını Çekti! Acımış Olmalı 😕",
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
            ]
            slap_phrase = random.choice(slap_phrases)
            await event.reply(f"**[{event.sender.first_name}](tg://user?id={event.sender.id}) ,  {slap_phrase}**")
        else:
            await event.reply("**🔹 ʟᴀɴ, ᴋᴜʟʟᴀɴɪᴄɪʏɪ ʙᴜʟᴀᴍᴀᴅɪᴍ !**")
    else:
        await event.reply("**🔹 ʙɪ‌ʀ ᴍᴇsᴀᴊɪ ʏᴀɴɪᴛʟᴀ ʙᴇʙᴇɢ‌ɪ‌ᴍ !**")

@client.on(events.NewMessage(pattern='(?i)^/kiss$|^kiss$'))
async def kiss(event):
    if event.is_private:
        return await event.reply(f"{nogroup}")

    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        user = reply_message.sender
        if user:
            user_name = f"[{user.first_name}](tg://user?id={user.id})"
            kiss_phrases = [
		          	            f"{user_name} 'ın kulağından öptü 😱",
	          	                f"{user_name} 'ın boynundan öptü! Galiba birşeyler oluyor 😁",
		    	              	f"{user_name} 'ın ayaklarından öptü! Fantezi'ye bak sen 🤭",
	          	                f"Birilerini alnından öpmek istiyor! Bu şanslı kişi {user_name} oldu 💖",
	          	                f"yine birilerini öptü! {user_name} 'ı kaybediyoruz 😱",
		    	              	f"{user_name} 'ın çenesinden öptü 🤭",
		          	            f"{user_name} 'ın parmaklarından öpmeye çalışırken, gözleri oyuldu 😳",
	          	                f"{user_name} 'ı dudaktan öptü! Hemde herkesin gözünün önünde 😳",
		    	              	f"öpecek kimseyi bulamayınca {user_name} 'a yöneldi, kaç ulan kaç 😁",
	          	                f"Derya'ya öpücük gönderirken {user_name} tarafından fark edildi 👀",
	          	                f"{user_name} 'ı burnundan öptü! ıyyyy iğrenç, ağzını yıkamayı unutma 🤮",
		    	              	f"{user_name} 'ı dudaktan öptü! Rahatsızlık vermeyelim, biz gidiyoruz 😌",
		          	            f"{user_name} 'ı kulak memesinden öptü! Olamaz 😳💖",
	          	                f"{user_name} 'ı baygın iken öptü! Sence nerenden öpmüş olabilir 😁",
		    	              	f"{user_name} 'ı boynundan öptü! Anlaşılan niyeti bozdu 🤭",
	          	                f"{user_name} 'ı ellerinden öptü! Galiba harçlık istiyor 😅",
	          	                f"{user_name} 'ı öpmek isterken utancından bayıldı 😂",
		    	              	f"{user_name} 'ı ayak parmaklarından öptü! Yavaş ol yiğidim 😏",
		              	        f"{user_name} 'ın yanağına masum ve saf bir öpücük kondurdu 😌",
	          	                f"{user_name} 'ın saçlarından öpüp kokladı! Oha 😳",
            ]
            kiss_phrases = random.choice(kiss_phrases)
            await event.reply(f"**[{event.sender.first_name}](tg://user?id={event.sender.id}) ,  {kiss_phrases}**")
        else:
            await event.reply("**🔹 ʟᴀɴ, ᴋᴜʟʟᴀɴɪᴄɪʏɪ ʙᴜʟᴀᴍᴀᴅɪᴍ !**")
    else:
        await event.reply("**🔹 ʙɪ‌ʀ ᴍᴇsᴀᴊɪ ʏᴀɴɪᴛʟᴀ ʙᴇʙᴇɢ‌ɪ‌ᴍ !**")

@client.on(events.NewMessage(pattern='(?i)^/d$|^d$'))
async def dsoru(event):
    await event.reply(f"**🌹 ᴅᴏɢ̆ʀᴜʟᴜᴋ sᴇᴄ̧ᴛɪɴ, ᴄ̧ᴏᴋ ɢᴜ̈ᴢᴇʟ .\n\n✦ sᴀɴᴀ sᴏʀᴜᴍ : {random.choice(d)}**")
	
@client.on(events.NewMessage(pattern='(?i)^/c$|^c$'))
async def csoru(event):
    await event.reply(f"**🌹 ᴄᴇsᴀʀᴇᴛ sᴇᴄ̧ᴛɪɴ, sᴀɴɪʀɪᴍ ғᴀᴢʟᴀ ᴄᴇsᴀʀᴇᴛʟɪsɪɴ .\n\n✦ ʏᴀᴘᴍᴀɴ ɢᴇʀᴇᴋᴇɴ : {random.choice(c)}**")
	
@client.on(events.NewMessage(pattern='(?i)^/soz$'))
async def sozu(event):
    await event.reply(f"**✦ ɢᴜ̈ᴢᴇʟ sᴏ̈ᴢ :\n\n{random.choice(guzelsoz)}**")

anlik_calisan = []
tekli_calisan = []
gece_tag = []
rxyzdev_tagTot = {}
rxyzdev_initT = {} 
rxyzdev_stopT = {}
isleyen = []
	
@client.on(events.NewMessage(pattern="^(?i)/atag ?(.*)"))
async def atag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.reply(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.reply(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
      mode = "text_on_cmd"
      msg = ""
    else:
      mode = "text_on_cmd"
      msg = msg_list[1]
      if msg == "/atag":
        mode = "text_on_cmd"
        msg = ""
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
      mode = "text_on_cmd"
      msg = ""
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
      mode = "text_on_cmd"
      msg = ""
    else:
      mode = "text_on_cmd"
      msg = msg_list[1]
  else:
    mode = "text_on_cmd"
    msg = ""
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.reply(f"{ibaslama}")

    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""   
    async for usr in client.iter_participants(event.chat_id):
      if usr.bot or usr.deleted:
        continue
      if usr.id in admins:  # Yalnızca yöneticileri etiketleyin
        rxyzdev_tagTot[event.chat_id] += 1
        usrnum += 1
        usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})"  # Kullanıcı adını kullanarak yöneticiyi etiketleyin
        if event.chat_id not in gece_tag:
          return
        if usrnum == 1:
          await client.send_message(event.chat_id, f"**{usrtxt}  {msg}**")
          await asyncio.sleep(2)
          usrnum = 0
          usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:
      await event.reply(f"**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...\n\n👤  {rxyzdev_initT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**")
  gece_tag = []  # gece_tag listesini boşalt
	
@client.on(events.NewMessage(pattern="^(?i)/utag ?(.*)"))
async def utag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.reply(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.reply(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
      mode = "text_on_cmd"
      msg = ""
    else:
      mode = "text_on_cmd"
      msg = msg_list[1]
      if msg == "/utag":
        mode = "text_on_cmd"
        msg = ""
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
      mode = "text_on_cmd"
      msg = ""
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
      mode = "text_on_cmd"
      msg = ""
    else:
      mode = "text_on_cmd"
      msg = msg_list[1]
  else:
    mode = "text_on_cmd"
    msg = ""
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.reply(f"{ibaslama}")

    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""   
    async for usr in client.iter_participants(event.chat_id):
      if usr.bot or usr.deleted:
        continue
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})  ,  "
      if event.chat_id not in gece_tag:
        return
      if usrnum == 7:
        await client.send_message(event.chat_id, f"**{msg}\n\n{usrtxt}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:
      await event.reply(f"**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...\n\n👤  {rxyzdev_initT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**")
  gece_tag = []  # gece_tag listesini boşalt
	
@client.on(events.NewMessage(pattern="^(?i)/tag ?(.*)"))
async def tag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.reply(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.reply(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
      mode = "text_on_cmd"
      msg = ""
    else:
      mode = "text_on_cmd"
      msg = msg_list[1]
      if msg == "/tag":
        mode = "text_on_cmd"
        msg = ""
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
      mode = "text_on_cmd"
      msg = ""
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
      mode = "text_on_cmd"
      msg = ""
    else:
      mode = "text_on_cmd"
      msg = msg_list[1]
  else:
    mode = "text_on_cmd"
    msg = ""
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.reply(f"{ibaslama}")

    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""   
    async for usr in client.iter_participants(event.chat_id):
      if usr.bot or usr.deleted:
        continue
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in gece_tag:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**{usrtxt}  {msg}**")
        await asyncio.sleep(4)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:
      await event.reply(f"**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...\n\n👤  {rxyzdev_initT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**")
  gece_tag = []  # gece_tag listesini boşalt

@client.on(events.NewMessage(pattern="^(?i)/etag ?(.*)"))
async def etag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.reply(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.reply(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
      mode = "text_on_cmd"
      msg = ""
    else:
      mode = "text_on_cmd"
      msg = msg_list[1]
      if msg == "/etag":
        mode = "text_on_cmd"
        msg = ""
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
      mode = "text_on_cmd"
      msg = ""
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
      mode = "text_on_cmd"
      msg = ""
    else:
      mode = "text_on_cmd"
      msg = msg_list[1]
  else:
    mode = "text_on_cmd"
    msg = ""
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.reply(f"{ibaslama}")

    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""   
    async for usr in client.iter_participants(event.chat_id):
      if usr.bot or usr.deleted:
        continue
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(emj)}](tg://user?id={usr.id}) , "
      if event.chat_id not in gece_tag:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"**{msg}\n\n{usrtxt}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:
      await event.reply(f"**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...\n\n👤  {rxyzdev_initT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**")
  gece_tag = []  # gece_tag listesini boşalt
	
@client.on(events.NewMessage(pattern="^(?i)/vtag ?(.*)"))
async def vtag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.reply(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.reply(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
      mode = "text_on_cmd"
      msg = ""
    else:
      mode = "text_on_cmd"
      msg = msg_list[1]
      if msg == "/vtag":
        mode = "text_on_cmd"
        msg = ""
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
      mode = "text_on_cmd"
      msg = ""
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
      mode = "text_on_cmd"
      msg = ""
    else:
      mode = "text_on_cmd"
      msg = msg_list[1]
  else:
    mode = "text_on_cmd"
    msg = ""
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.reply(f"{ibaslama}")

    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""   
    async for usr in client.iter_participants(event.chat_id):
      if usr.bot or usr.deleted:
        continue
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in gece_tag:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**{usrtxt}  {random.choice(sor)}**")
        await asyncio.sleep(4)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:
      await event.reply(f"**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...\n\n👤  {rxyzdev_initT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**")
  gece_tag = []  # gece_tag listesini boşalt	

@client.on(events.NewMessage(pattern="^(?i)/otag ?(.*)"))
async def otag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.reply(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.reply(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
      mode = "text_on_cmd"
      msg = ""
    else:
      mode = "text_on_cmd"
      msg = msg_list[1]
      if msg == "/otag":
        mode = "text_on_cmd"
        msg = ""
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
      mode = "text_on_cmd"
      msg = ""
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
      mode = "text_on_cmd"
      msg = ""
    else:
      mode = "text_on_cmd"
      msg = msg_list[1]
  else:
    mode = "text_on_cmd"
    msg = ""
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.reply(f"{ibaslama}")

    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""   
    async for usr in client.iter_participants(event.chat_id):
      if usr.bot or usr.deleted:
        continue
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(rutbe)}](tg://user?id={usr.id})"
      if event.chat_id not in gece_tag:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**{usrtxt}**")
        await asyncio.sleep(4)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:
      await event.reply(f"**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...\n\n👤  {rxyzdev_initT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**")
  gece_tag = []  # gece_tag listesini boşalt

@client.on(events.NewMessage(pattern="^(?i)/itag ?(.*)"))
async def itag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.reply(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.reply(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
      mode = "text_on_cmd"
      msg = ""
    else:
      mode = "text_on_cmd"
      msg = msg_list[1]
      if msg == "/itag":
        mode = "text_on_cmd"
        msg = ""
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
      mode = "text_on_cmd"
      msg = ""
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
      mode = "text_on_cmd"
      msg = ""
    else:
      mode = "text_on_cmd"
      msg = msg_list[1]
  else:
    mode = "text_on_cmd"
    msg = ""
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.reply(f"{ibaslama}")

    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""   
    async for usr in client.iter_participants(event.chat_id):
      if usr.bot or usr.deleted:
        continue
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(gsos)}](tg://user?id={usr.id})"
      if event.chat_id not in gece_tag:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**{usrtxt}**")
        await asyncio.sleep(4)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:
      await event.reply(f"**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...\n\n👤  {rxyzdev_initT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**")
  gece_tag = []  # gece_tag listesini boşalt
	
@client.on(events.NewMessage(pattern="^(?i)/stag ?(.*)"))
async def stag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.reply(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.reply(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
      mode = "text_on_cmd"
      msg = ""
    else:
      mode = "text_on_cmd"
      msg = msg_list[1]
      if msg == "/stag":
        mode = "text_on_cmd"
        msg = ""
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
      mode = "text_on_cmd"
      msg = ""
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
      mode = "text_on_cmd"
      msg = ""
    else:
      mode = "text_on_cmd"
      msg = msg_list[1]
  else:
    mode = "text_on_cmd"
    msg = ""
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.reply(f"{ibaslama}")

    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""   
    async for usr in client.iter_participants(event.chat_id):
      if usr.bot or usr.deleted:
        continue
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in gece_tag:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**{usrtxt}  {random.choice(guzelsoz)}**")
        await asyncio.sleep(4)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:
      await event.reply(f"**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...\n\n👤  {rxyzdev_initT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**")
  gece_tag = []  # gece_tag listesini boşalt
	
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global gece_tag
  if event.is_private:
    return await event.reply(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.reply(f"{noadmin}")

  if event.chat_id not in gece_tag:
    return await event.reply("**🎂 ᴀᴋᴛɪ‌ғ ʙɪ‌ʀ ɪ‌s‌ʟᴇᴍ ʏᴏᴋ !**")

  gece_tag = []  # gece_tag listesini boşalt
  sender = await event.get_sender()
  rxyzdev_stopT = f"[{sender.first_name}](tg://user?id={sender.id})"      
  if event.chat_id in rxyzdev_tagTot:
    await event.reply(f"**⛔ ɪşʟᴇᴍɪ ɪᴘᴛᴀʟ ᴇᴛᴛɪᴍ ...\n\n👤  {rxyzdev_stopT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**")

@client.on(events.NewMessage)
async def chatbot(event):
    global isleyen
    mesaj = str(event.raw_text)
    qrup = event.chat_id
    if qrup not in isleyen:
        return
    
    me = await client.get_me()
    if event.sender_id == me.id:
        return
    
    kelimeler = mesaj.lower().split()  # Mesajı küçük harfe çevirip kelimelere ayır

    if "bot" in kelimeler:
       cevap = random.choice(bottst)
       bold_cevap = f"<b>{cevap}</b>"
       await event.reply(bold_cevap, parse_mode='html')	    
	
    if "derya" in kelimeler:
       cevap = random.choice(bkt)
       bold_cevap = f"<b>{cevap}</b>"
       await event.reply(bold_cevap, parse_mode='html')

    if "gamze" in kelimeler:
       cevap = random.choice(gmze)
       bold_cevap = f"<b>{cevap}</b>"
       await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "selam" or kelimeler[0] == "selamün aleyküm" or kelimeler[0] == "slm" or kelimeler[0] == "sea" or kelimeler[0] == "sa":
       cevap = random.choice(selam)
       bold_cevap = f"<b>{cevap}</b>"
       await event.reply(bold_cevap, parse_mode='html')
	    	    
    if kelimeler[0] == "nasılsın" or kelimeler[0] == "naber" or kelimeler[0] == "ne haber" or kelimeler[0] == "nbr":
        cevap = random.choice(nasilsin)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "adam" or kelimeler[0] == "erkek":
        cevap = random.choice(adam)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "iyiyim" or kelimeler[0] == "harika" or kelimeler[0] == "mükemmel":
        cevap = random.choice(iyiyim)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "hoş geldin" or kelimeler[0] == "hg":
        cevap = random.choice(hoş)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "merhaba" or kelimeler[0] == "mrb":
        cevap = random.choice(merhaba)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "ban" or kelimeler[0] == "banned" or kelimeler[0] == "banla" or kelimeler[0] == "/ban":
        cevap = random.choice(ban)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "nabıyon" or kelimeler[0] == "napıyorsun" or kelimeler[0] == "ne yapıyorsun":
        cevap = random.choice(nabiyon)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "😔" or kelimeler[0] == "🥺"  or kelimeler[0] == "😥":
        cevap = random.choice(uzgun)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "valla" or kelimeler[0] == "vallahi" or kelimeler[0] == "yemin":
        cevap = random.choice(valla)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    	    
    if kelimeler[0] == "sg" or kelimeler[0] == "siktir":
        cevap = random.choice(sg)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "mal" or kelimeler[0] == "gerizekalı" or kelimeler[0] == "it" or kelimeler[0] == "şrfsz" or kelimeler[0] == "şerefsiz":
        cevap = random.choice(mal)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "balım" or kelimeler[0] == "bebeğim" or kelimeler[0] == "aşkım":
        cevap = random.choice(balim)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "canım" or kelimeler[0] == "bitanem" or kelimeler[0] == "yavrum":
        cevap = random.choice(canim)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "gidiyorum" or kelimeler[0] == "gittim" or kelimeler[0] == "görüşürüz":
        cevap = random.choice(gidiyorum)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "sinirlendim" or kelimeler[0] == "😡" or kelimeler[0] == "🤬" or kelimeler[0] == "sinirliyim":
        cevap = random.choice(sinirlendim)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "tanışalım mı" or kelimeler[0] == "tanışabilir miyiz":
        cevap = random.choice(tanis)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "ismin ne" or kelimeler[0] == "adın ne":
        cevap = random.choice(adne)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "iyi" or kelimeler[0] == "kötü" or kelimeler[0] == "idare eder":
        cevap = random.choice(iyisen)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "😅" or kelimeler[0] == "😂" or kelimeler[0] == "🤣":
        cevap = random.choice(gullu)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "büyüğüm" or kelimeler[0] == "büyük":
        cevap = random.choice(buyuk)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	
    if kelimeler[0] == "aiko":
        cevap = random.choice(aiko)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "günaydın" or kelimeler[0] == "gny" or kelimeler[0] == "günaydınnn" or kelimeler[0] == "rojbaş":
        cevap = random.choice(gnyy)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "iyi geceler" or kelimeler[0] == "iyi akşamlar":
        cevap = random.choice(igece)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "kaç yaşındasın" or kelimeler[0] == "yaşın kaç":
        cevap = random.choice(kyas)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "nerelisin":
        cevap = random.choice(nereli)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "konuşma" or kelimeler[0] == "sus" or kelimeler[0] == "knşma":
        cevap = random.choice(pms)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "kırdın" or kelimeler[0] == "kırıldım" or kelimeler[0] == "kırıcı" or kelimeler[0] == "krldm":
        cevap = random.choice(krdn)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "sıkıldım" or kelimeler[0] == "skldm":
        cevap = random.choice(skdm)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "hm" or kelimeler[0] == "hmmm":
        cevap = random.choice(hms)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "geçmiş olsun":
        cevap = random.choice(bts)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "oyun" or kelimeler[0] == "game":
        cevap = random.choice(trt)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "evet" or kelimeler[0] == "evt":
        cevap = random.choice(evt)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "hyr" or kelimeler[0] == "hayır":
        cevap = random.choice(hyrr)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "🙄":
        cevap = random.choice(gzs)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "of" or kelimeler[0] == "offf":
        cevap = random.choice(ofs)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "çikolata":
        cevap = random.choice(cklta)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "lan" or kelimeler[0] == "ln":
        cevap = random.choice(lna)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "dedim":
        cevap = random.choice(dddm)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "yalan" or kelimeler[0] == "yalancı":
        cevap = random.choice(ylna)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "sağol":
        cevap = random.choice(sgll)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "çirkin":
        cevap = random.choice(crkn)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "dm" or kelimeler[0] == "pm":
        cevap = random.choice(dmy)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "tatlı" or kelimeler[0] == "yemek":
        cevap = random.choice(tymm)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "kes":
        cevap = random.choice(kmm)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "kanka" or kelimeler[0] == "knk" or kelimeler[0] == "kanki":
        cevap = random.choice(kankas)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "öp":
        cevap = random.choice(opsss)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "sanane" or kelimeler[0] == "sağne":
        cevap = random.choice(sgne)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] == "banane" or kelimeler[0] == "bağne":
        cevap = random.choice(bgne)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "ben":
        cevap = random.choice(bnen)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] == "sen":
        cevap = random.choice(snen)
        bold_cevap = f"<b>{cevap}</b>"
        await event.reply(bold_cevap, parse_mode='html')
	    

@client.on(events.NewMessage(pattern="(?i)/chatbot"))
async def chatbot(event):
    if event.is_private:
        await event.reply(f"{nogroup}", parse_mode='markdown')
        return

    admins = []
    async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
        admins.append(admin.id)
    if not event.sender_id in admins:
        return await event.reply(f"{noadmin}")
  
    global isleyen
    if event.chat_id in isleyen:
        status = "ᴀᴋᴛɪ‌ғ"
    else:
        status = "ᴋᴀᴘᴀʟɪ"
    
    await event.reply(f"__**✦ ᴀşᴀɢ̆ɪᴅᴀɴ sᴇᴄ̧ɪ̇ᴍ ʏᴀᴘɪɴ !\n\n✦ ᴅᴜʀᴜᴍ : {status}**__", buttons=[
        [Button.inline("✅ ᴀᴋᴛɪ‌ғ ᴇᴛ", data="sohbetmod_on")],
        [Button.inline("⛔ ᴋᴀᴘᴀᴛ", data="sohbetmod_off")]
    ])


@client.on(events.CallbackQuery(pattern=b"sohbetmod_on"))
async def callback_sohbetmod_on(event):
    qrup = event.chat_id
    if qrup not in isleyen:
        isleyen.append(qrup)
        aktiv_olundu = "**__✦ ʙᴀşᴀʀɪʏʟᴀ ᴀᴋᴛɪғ ᴇᴅɪʟᴅɪ .\n\n✦ ᴀʀᴛıᴋ ᴋᴏɴᴜs‌ᴀʙɪʟɪʀɪᴍ !__**"
        await event.edit(aktiv_olundu)
        await asyncio.sleep(3600)
        while qrup in isleyen:
            users = await client.get_participants(qrup)
            active_users = [user for user in users if not user.bot and not user.deleted]
            if active_users:
                random_user = random.choice(active_users)
                await client.send_message(qrup, f"**[{random_user.first_name}](tg://user?id={random_user.id}) {random.choice(smesajs)}**")
            await asyncio.sleep(3600)
        return
    await event.edit("**__✦ ᴄʜᴀᴛ ʙᴏᴛ ᴢᴀᴛᴇɴ ᴀᴋᴛɪ̇ғ .__**")
		

@client.on(events.CallbackQuery(pattern=b"sohbetmod_off"))
async def callback_sohbetmod_off(event):
    qrup = event.chat_id
    if qrup in isleyen:
        isleyen.remove(qrup)
        await event.edit("**__✦ ʙᴀşᴀʀɪʏʟᴀ ᴋᴀᴘᴀᴛɪʟᴅɪ .\n\n✦ ᴀʀᴛıᴋ ᴋᴏɴᴜs‌ᴀᴍᴀᴍ !__**")
        return
    await event.edit("**__✦ ᴄʜᴀᴛ ʙᴏᴛ ᴢᴀᴛᴇɴ ᴋᴀᴘᴀʟɪ !__**")


@client.on(events.NewMessage(pattern=r"(?i)(/|)derya", incoming=True))
async def buket_handler(event):
    if event.is_private:
        return
    chat_id = event.chat_id
    if chat_id in isleyen:
        return
    if event.is_group:
        await event.reply("**__✦ ᴄʜᴀᴛ ʙᴏᴛ s‌ᴜᴀɴ ᴋᴀᴘᴀʟɪ !\n✦ ᴀᴄ‌ᴍᴀᴋ ɪ‌ᴄ‌ɪɴ ➻ /chatbot__**")	


print("BOT AKTİF !")
client.start()
client.run_until_disconnected()
