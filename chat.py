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


itiraf_eden = "Kullanıcı Seçilmedi"
mesaj = "Mesaj Görünmedi"

itiraf_modu = False
ilk_mesaj = True

     
@client.on(events.callbackquery.CallbackQuery(data="itiraf"))
async def handler(event):
    global itiraf_modu, ilk_mesaj
    itiraf_modu = True
    await event.edit(f"{itirafyaz}", buttons=(
        [
            Button.inline("🏠 Ana Sayfa", data="start")
        ]
    ),
    link_preview=False)
    ilk_mesaj = True

@client.on(events.NewMessage)
async def yeni_mesaj(event: events.NewMessage.Event):
    global mesaj, itiraf_modu, ilk_mesaj
    if event.is_private:
        if itiraf_modu and ilk_mesaj:
            if event.raw_text != "/start":
                mesaj = str(event.raw_text)
                await client.send_message(event.chat_id, f"{itirafmsg}", buttons=(
                    [
                        Button.inline("🔒 Gizli", data="anonim"),
                        Button.inline("🔓 Açık", data="acik")
                    ],
                    [
                        Button.inline("🏠 Ana Sayfa", data="start")
                    ]
                ),
                link_preview=False)
                ilk_mesaj = False
        elif event.raw_text == "/start":
            return
        else:
            pass
	  
itiraf_anonim = b"\xF0\x9F\x92\x8C\x20\x45\x74\x69\x72\x61\x66\x20\x42\x6F\x74\x0A\xF0\x9F\x93\xB2\x20\x54\x65\x6C\x65\x74\x68\x6F\x6E\x20\x2D\x20\x31\x2E\x32\x34\x2E\x30\x0A\xF0\x9F\x93\xA3\x20\x53\x75\x70\x70\x6F\x72\x74\x20\x2D\x20\x40\x52\x6F\x42\x6F\x74\x6C\x61\x72\x69\x6D\x54\x67\x0A\xF0\x9F\x91\xA8\xF0\x9F\x8F\xBB\xE2\x80\x8D\xF0\x9F\x92\xBB\x20\x4F\x77\x6E\x65\x72\x20\x2D\x20\x40\x61\x79\x6B\x68\x61\x6E\x5F\x73"
@client.on(events.callbackquery.CallbackQuery(data="anonim"))
async def anonim(event):
    global mesaj
    global onay
    async for usr in client.iter_participants(event.chat_id):
     gonderen = f"[{usr.first_name}](tg://user?id={usr.id})"
     itiraf_eden = "Gizli"
     sonluq = f"\n❤️‍🔥 Hey Sende İtiraf Etmek İstiyorsan @{BOT_USERNAME}'una edebilirsin !"
     yeni_itiraf = await client.send_message(LOG_CHANNEL, f"**🖇️ Yeni itiraf\n\n🗣️ İtiraf Eden : {itiraf_eden} \n📮 Edilen İtiraf : {mesaj}\n{sonluq}**")
     onay = await yeni_itiraf.reply("**➻ Yeni İtiraf !**", buttons=(
                      [
                       Button.inline("✅ Onayla", data="onay"
                       ),
                       Button.inline("🗑️ Sil", data="sil")
                      ]
                    ),
                    link_preview=False)
    await client.send_message(LOG_CHANNEL, f"**ℹ️ {gonderen} Gizli İtiraf Yazdı !**")
    await event.edit(f"{gonderildi}", buttons=(
                      [
                       Button.inline("📮 Yeni İtiraf", data="itiraf"),
                       Button.inline("🏠 Ana Sayfa", data="start")
                      ]
                    ),
                    link_preview=False)
anonim = itiraf_anonim.decode("utf8")
 
itiraf_acik = b"\xE2\x84\xB9\xEF\xB8\x8F\x20\x42\x6F\x74\x20\x62\x61\xC5\x9F\x6C\x61\x64\xC4\xB1\x6C\x64\xC4\xB1\x20\x70\x72\x6F\x62\x6C\x65\x6D\x20\x79\x61\x72\x61\x6E\x64\xC4\xB1\x71\x64\x61\x20\x73\x75\x70\x70\x6F\x72\x74\x20\x71\x72\x75\x70\x75\x6E\x61\x20\x79\x61\x7A\xC4\xB1\x6E\x0A\xE2\x9A\xA1\x20\x42\x6F\x74\x75\x6E\x75\x7A\x20\x53\x75\x70\x65\x72\x20\xC4\xB0\xC5\x9F\x6C\x65\x79\x69\x72\x2E\x2E\x2E"
@client.on(events.callbackquery.CallbackQuery(data="acik"))
async def aciq(event):
    global mesaj
    global onay
    async for usr in client.iter_participants(event.chat_id):
     itiraf_eden = f"[{usr.first_name}](tg://user?id={usr.id})"
     sonluq = f"\n❤️‍🔥 Hey Sende İtiraf Etmek İstiyorsan @{BOT_USERNAME}'una edebilirsin !"
     yeni_itiraf = await client.send_message(LOG_CHANNEL, f"**🖇️ Yeni itiraf\n\n🗣️ İtiraf Eden :** {itiraf_eden} \n**📮 Edilen İtiraf : {mesaj}\n{sonluq}**")
     onay = await yeni_itiraf.reply("**➻ Yeni İtiraf !**", buttons=(
                      [
                       Button.inline("✅ Onayla", data="onay"
                       ),
                       Button.inline("🗑️ Sil", data="sil")
                      ]
                    ),
                    link_preview=False)
    await client.send_message(LOG_CHANNEL, f"**ℹ️ {itiraf_eden} Açık İtiraf Yazdı !**")
    await event.edit(f"{gonderildi}", buttons=(
                      [
                       Button.inline("📮 Yeni İtiraf", data="itiraf"),
                       Button.inline("🏠 Ana Sayfa", data="start")
                      ]
                    ),
                    link_preview=False)
acik = itiraf_acik.decode("utf8")
  
@client.on(events.callbackquery.CallbackQuery(data="onay"))
async def onay(event):
    global onay
    async for usr in client.iter_participants(event.chat_id):
      tesdiqliyen = f"[{usr.first_name}](tg://user?id={usr.id})"
    if onay.reply_to_msg_id:
      itiraff = await onay.get_reply_message()
      itiraf = itiraff.text
      await client.send_message(İTİRAF_GRUP, itiraf)
      await event.edit(f"**🎉 İtiraf Onaylandı !**")
      
@client.on(events.callbackquery.CallbackQuery(data="sil"))
async def sil(event):
    global onay
    if not onay.is_reply:
      return await onay.edit("**💥 HATA !**")
    if onay.is_reply:
      itiraf = await onay.get_reply_message()
      await itiraf.delete()
      await event.edit("**🗑️ İtiraf başarıyla Silindi !**")
	    
anlik_calisan = []
tekli_calisan = []
gece_tag = []
rxyzdev_tagTot = {}
rxyzdev_initT = {} 
rxyzdev_stopT = {}
isleyen = []

@client.on(events.NewMessage(pattern='(?i)/cagir'))
async def handle_tagging(event):
    if event.is_private:
        await event.reply(f"{nogroup}", parse_mode='markdown')
        return
    # Komutu kullanan kişinin kullanıcı adını al
    sender_username = f"[{event.sender.first_name}](tg://user?id={event.sender.id})"
    
    # Tüm kullanıcıları al
    all_users = await client.get_participants(event.chat_id)
    
    # Etiketlenecek kullanıcı sayısı
    tag_count = 100
    
    # Botlar ve silinen hesapları hariç tut
    valid_users = [user for user in all_users if not user.bot and not user.deleted]
    
    # İlk tag_count kullanıcıyı al
    tagged_users = valid_users[:tag_count]
    
    # Etiketleri oluştur
    tags = ' , '.join([f'[{user.first_name}](tg://user?id={user.id})' for user in tagged_users])
    
    # Mesajı oluştur
    message = f'**{tags}\n\n👤  {sender_username}\n🔹 sɪᴢɪ ᴏʏᴜɴᴀ ᴄ̧ᴀɢ̆ɪʀɪʏᴏʀ !**'
    
    # Mesajı gönder
    await client.send_message(event.chat_id, message)
	

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
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) , "
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
	

@client.on(events.NewMessage(pattern="^(?i)/tektag ?(.*)"))
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

##################################################
##################################################
##################################################
@client.on(events.NewMessage(pattern='(?i)(/|)/werewolfrole'))
async def start(event):
     await event.reply(f"{rols}", buttons=(
                      [
                       Button.inline('👱 Köylü Takımı', data='koylutakim')
                      ],
                      [
                       Button.inline('🐺 Kurtlar & Müttefikleri', data='kurttakim')
                      ],
                      [
                       Button.inline('👤 Bireysel Düşmanlar', data='bireysel')
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="gwolf"))
async def start(event):
     await event.edit(f"{rols}",
                    buttons=(
                      [
                       Button.inline('👱 Köylü Takımı', data='koylutakim')
                      ],
                      [
                       Button.inline('🐺 Kurtlar & Müttefikleri', data='kurttakim')
                      ],
                      [
                       Button.inline('👤 Bireysel Düşmanlar', data='bireysel')
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="koylutakim"))
async def handler(event):
    await event.edit(f"{bilgis}", buttons=(
                      [
                      Button.inline("Köylü 👱", data="koylu"),
                      Button.inline("Sarhoş 🍻", data="sarhos")
                      ],
                      [
                      Button.inline("Gözcü 👳", data="gozcu"),
                      Button.inline("Yancı 💋", data="yanci")
                      ],
                      [
                      Button.inline("Seyirci 👁", data="seyirci"),
                      Button.inline("Silahşör 🔫", data="silahsor")
                      ],
                      [
                      Button.inline("Koruyucu Melek 👼", data="kmelek"),
                      Button.inline("Aptal 🃏", data="aptal")
                      ],
                      [
                      Button.inline("Mason 👷", data="mason"),
                      Button.inline("Dedektif 🕵", data="dedektif")
                      ],
                      [
                      Button.inline("Gözcü Çırağı 🙇", data="gozcuc"),
                      Button.inline("Tarikatçı Avcı 💂", data="tavci")
                      ],
                      [
                      Button.inline("Eros 🏹", data="eros"),
                      Button.inline("Avcı 🎯", data="avci")
                      ],
                      [
                      Button.inline("Beceriksiz 🤕", data="beceriksiz"),
                      Button.inline("Demirci ⚒", data="demirci")
                      ],
                      [
                      Button.inline("Kara kurt 🐺🌑", data="karak")
                      ],
                      [
                      Button.inline("Prens 💍", data="prens"),
                      Button.inline("Belediye Başkanı 🎖", data="bbaskani")
                      ],
                      [
                      Button.inline("Kahin 🌀", data="kahin"),
                      Button.inline("Hükümdar 👑", data="hukumdar")
                      ],
                      [
                      Button.inline("Barışçıl ☮️", data="bariscil"),
                      Button.inline("Yaşlı Bilge 📚", data="ybilge")
                      ],
                      [
                      Button.inline("Uyutucu 💤", data="uyutucu"),
                      Button.inline("Kurdumsu 👱‍🌚", data="kurdumsu")
                      ],
                      [
                      Button.inline("Şehit 🔰", data="sehit"),
                      Button.inline("Simyacı 🍵", data="simyaci")
                      ],
                      [
                      Button.inline("Efendi 🛡", data="efendi"),
                      Button.inline("Güzel 💅", data="guzel")
                      ],
                      [
                      Button.inline("Fırtına Getiren 🌩", data="fgetiren"),
                      Button.inline("Hain 🖕", data="hain")
                      ],
                      [
                      Button.inline("Yabani Çocuk 👶", data="ycocuk"),
                      Button.inline("Lanetli 😾", data="lanetli")
                      ],
                      [
                      Button.inline("👈 Geri", data="gwolf")
                      ]
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kurttakim"))
async def handler(event):
    await event.edit(f"{bilgis}", buttons=(
                      [
                      Button.inline("Kurtadam 🐺", data="kurtadam"),
                      Button.inline("Alfa Kurt ⚡️", data="alfakurt")
                      ],
                      [
                      Button.inline("Falcı 🔮", data="falci"),
                      Button.inline("Yavru Kurt 🐶", data="yavrukurt")
                      ],
                      [
                      Button.inline("Lycan 🐺🌝", data="lycan")
                      ],
                      [
                      Button.inline("Haydut 🦉", data="haydut"),
                      Button.inline("Mistik ☄️", data="mistik")
                      ],
                      [
                      Button.inline("Düzenbaz Kurt 🐑", data="duzenbaz"),
                      Button.inline("Kara Melek 👼🐺", data="karmelek")
                      ],
                      [
                      Button.inline("👈 Geri", data="gwolf")
                      ]
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="bireysel"))
async def handler(event):
    await event.edit(f"{bilgis}", buttons=(
                      [
                      Button.inline("İblis 👺", data="iblis"),
                      Button.inline("Tarikatçı 👤", data="tarikatci")
                      ],
                      [
                      Button.inline("Rahip ✝️", data="rahip"),
                      Button.inline("Hırsız 😈", data="hirsiz")
                      ],
                      [
                      Button.inline("Çift - Giden 🎭", data="cgiden")
                      ],
                      [
                      Button.inline("Kukla ustası 🕴", data="kustasi"),
                      Button.inline("Seri Katil 🔪", data="skatil")
                      ],
                      [
                      Button.inline("Kundakçı 🔥", data="kundakci"),
                      Button.inline("Necromancer ⚰️", data="necromancer")
                      ],
                      [
                      Button.inline("👈 Geri", data="gwolf")
                      ]
                    ),
                    link_preview=False)




@client.on(events.callbackquery.CallbackQuery(data="koylu"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Köylü 👱\n\n🗯️ Hakkında :\n**{koyluu}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="sarhos"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Sarhoş 🍻\n\n🗯️ Hakkında :\n**{sarhoss}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="gozcu"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Gözcü 👳\n\n🗯️ Hakkında :\n**{gozcuu}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="yanci"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Yancı 💋\n\n🗯️ Hakkında :\n**{yancii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="seyirci"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Seyirci 👁\n\n🗯️ Hakkında :\n**{seyircii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="silahsor"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Silahşör 🔫\n\n🗯️ Hakkında :\n**{silahsorr}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kmelek"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Koruyucu Melek 👼\n\n🗯️ Hakkında :\n**{kmelekk}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="aptal"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Aptal 🃏\n\n🗯️ Hakkında :\n**{aptall}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="mason"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Mason 👷\n\n🗯️ Hakkında :\n**{masonn}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="dedektif"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Dedektif 🕵\n\n🗯️ Hakkında :\n**{dedektiff}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="gozcuc"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Gözcü Çırağı 🙇\n\n🗯️ Hakkında :\n**{gozcucc}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="tavci"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Tarikatçı Avcı 💂\n\n🗯️ Hakkında :\n**{tavcii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="eros"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Eros 🏹\n\n🗯️ Hakkında :\n**{eross}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="avci"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Avcı 🎯\n\n🗯️ Hakkında :\n**{avcii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="beceriksiz"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Beceriksiz 🤕\n\n🗯️ Hakkında :\n**{beceriksizz}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="demirci"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Demirci ⚒\n\n🗯️ Hakkında :\n**{demircii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="karak"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Kara kurt 🐺🌑\n\n🗯️ Hakkında :\n**{karakk}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="prens"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Prens 💍\n\n🗯️ Hakkında :\n**{prenss}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="bbaskani"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Belediye Başkanı 🎖\n\n🗯️ Hakkında :\n**{bbaskanii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kahin"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Kahin 🌀\n\n🗯️ Hakkında :\n**{kahinn}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="hukumdar"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Hükümdar 👑\n\n🗯️ Hakkında :\n**{hukumdarr}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="bariscil"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Barışçıl ☮️\n\n🗯️ Hakkında :\n**{bariscill}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="ybilge"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Yaşlı Bilge 📚\n\n🗯️ Hakkında :\n**{ybilgee}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="uyutucu"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Uyutucu 💤\n\n🗯️ Hakkında :\n**{uyutucuu}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kurdumsu"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Kurdumsu 👱‍🌚\n\n🗯️ Hakkında :\n**{kurdumsuu}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)
    
@client.on(events.callbackquery.CallbackQuery(data="sehit"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Şehit 🔰\n\n🗯️ Hakkında :\n**{sehitt}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="simyaci"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Simyacı 🍵\n\n🗯️ Hakkında :\n**{simyacii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="efendi"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Efendi 🛡\n\n🗯️ Hakkında :\n**{efendii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="guzel"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Güzel 💅\n\n🗯️ Hakkında :\n**{guzell}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="fgetiren"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Fırtına Getiren 🌩\n\n🗯️ Hakkında :\n**{fgetirenn}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="hain"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Hain 🖕\n\n🗯️ Hakkında :\n**{hainn}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)
    
@client.on(events.callbackquery.CallbackQuery(data="ycocuk"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Yabani Çocuk 👶\n\n🗯️ Hakkında :\n**{ycocukk}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="lanetli"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Lanetli 😾\n\n🗯️ Hakkında :\n**{lanetlii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="koylutakim")
                      ],
                    ),
                    link_preview=False)

################################

@client.on(events.callbackquery.CallbackQuery(data="kurtadam"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Kurtadam 🐺\n\n🗯️ Hakkında :\n**{kurtadamm}", buttons=(
                      [
                      Button.inline("👈 Geri", data="kurttakim")
                      ],
                    ),
                    link_preview=False)
    
@client.on(events.callbackquery.CallbackQuery(data="alfakurt"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Alfa Kurt ⚡️\n\n🗯️ Hakkında :\n**{alfakurtt}", buttons=(
                      [
                      Button.inline("👈 Geri", data="kurttakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="falci"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Falcı 🔮\n\n🗯️ Hakkında :\n**{falcii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="kurttakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="yavrukurt"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Yavru Kurt 🐶\n\n🗯️ Hakkında :\n**{yavrukurtt}", buttons=(
                      [
                      Button.inline("👈 Geri", data="kurttakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="lycan"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Lycan 🐺🌝\n\n🗯️ Hakkında :\n**{lycann}", buttons=(
                      [
                      Button.inline("👈 Geri", data="kurttakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="haydut"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Haydut 🦉\n\n🗯️ Hakkında :\n**{haydutt}", buttons=(
                      [
                      Button.inline("👈 Geri", data="kurttakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="mistik"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Mistik ☄️\n\n🗯️ Hakkında :\n**{mistikk}", buttons=(
                      [
                      Button.inline("👈 Geri", data="kurttakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="duzenbaz"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Düzenbaz Kurt 🐑\n\n🗯️ Hakkında :\n**{duzenbazz}", buttons=(
                      [
                      Button.inline("👈 Geri", data="kurttakim")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="karmelek"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Kara Melek 👼🐺\n\n🗯️ Hakkında :\n**{karmelekk}", buttons=(
                      [
                      Button.inline("👈 Geri", data="kurttakim")
                      ],
                    ),
                    link_preview=False)

################################

@client.on(events.callbackquery.CallbackQuery(data="iblis"))
async def handler(event):
    await event.edit(f"**🌟 Rol : İblis 👺\n\n🗯️ Hakkında :\n**{ibliss}", buttons=(
                      [
                      Button.inline("👈 Geri", data="bireysel")
                      ],
                    ),
                    link_preview=False)
    
@client.on(events.callbackquery.CallbackQuery(data="tarikatci"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Tarikatçı 👤\n\n🗯️ Hakkında :\n**{tarikatcii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="bireysel")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="rahip"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Rahip ✝️\n\n🗯️ Hakkında :\n**{rahipp}", buttons=(
                      [
                      Button.inline("👈 Geri", data="bireysel")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="hirsiz"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Hırsız 😈\n\n🗯️ Hakkında :\n**{hirsizz}", buttons=(
                      [
                      Button.inline("👈 Geri", data="bireysel")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kustasi"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Kukla ustası 🕴\n\n🗯️ Hakkında :\n**{kustasii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="bireysel")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="cgiden"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Çift - Giden 🎭\n\n🗯️ Hakkında :\n**{cgidenn}", buttons=(
                      [
                      Button.inline("👈 Geri", data="bireysel")
                      ],
                    ),
                    link_preview=False)
    
@client.on(events.callbackquery.CallbackQuery(data="skatil"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Seri Katil 🔪\n\n🗯️ Hakkında :\n**{skatill}", buttons=(
                      [
                      Button.inline("👈 Geri", data="bireysel")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kundakci"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Kundakçı 🔥\n\n🗯️ Hakkında :\n**{kundakcii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="bireysel")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="necromancer"))
async def handler(event):
    await event.edit(f"**🌟 Rol : Necromancer ⚰️\n\n🗯️ Hakkında :\n**{necromancerr}", buttons=(
                      [
                      Button.inline("👈 Geri", data="bireysel")
                      ],
                    ),
                    link_preview=False)
	
print("CHAT.PY AKTİF !")
client.start()
client.run_until_disconnected()
	  
