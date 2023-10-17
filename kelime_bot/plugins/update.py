import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.types import ChannelParticipantsBots
from telethon.tl.functions.users import GetFullUserRequest
from time import time
from datetime import datetime
from random import choice
from pyrogram import Client, filters, idle
from pyrogram import Client as USER
from pyrogram import enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import pyrogram
from datetime import datetime
from telethon.errors.rpcerrorlist import MessageDeleteForbiddenError
import secrets
import aiohttp
from pyrogram import filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User
from pyrogram.types.messages_and_media import Message
from pyrogram import Client, filters
import time
from kelime_bot import OWNER_ID
from os import remove
import datetime
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import asyncio
import datetime
import shutil, psutil, traceback, os
import random
import string
import time
import traceback
import aiofiles
from pyrogram import Client, filters, __version__
from pyrogram.types import Message
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    PeerIdInvalid,
    UserIsBlocked,
)


@app.on_message(filters.command('me', [".", "!", "@", "/"]))
async def info(bot, update):
    
    text = f"""  **ℹ MƏLUMAT**
 

🙋🏻‍♂️ **İsdifadəçi Adı:** {update.from_user.mention()}
👥 **İkinci Ad :** {update.from_user.last_name if update.from_user.last_name else 'None'}
🆔 **Telegram ID :** {update.from_user.id}
🗒 **Kulanıcı Adı :** @{update.from_user.username}
🌏 **DİL :** {update.from_user.language_code}
📱 **M.NÖMRƏ :** {update.from_user.phone_number}
🏷 **STATUS :** {str(update.from_user.status)[11:]}
🆔 **Qrup İD :** {(update.forward_from_chat or update.chat).id}
🗨 **Qrup Adı :** {update.chat.title}"""


    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=mesil
    )

@app.on_message(filters.command('admins', [".", "!", "@", "/"]))
async def admins(client, message):
  try: 
    adminList = []
    ownerList = []
    async for admin in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
      if admin.privileges.is_anonymous == False:
        if admin.user.is_bot == True:
          pass
        elif admin.status == ChatMemberStatus.OWNER:
          ownerList.append(admin.user)
        else:  
          adminList.append(admin.user)
      else:
        pass   
    lenAdminList= len(ownerList) + len(adminList)  
    text2 = f"👮‍♂️ QRUP İDARƏÇİLƏRİ - {message.chat.title}\n\n"
    try:
      owner = ownerList[0]
      if owner.username == None:
        text2 += f"👑 Kurucu\n└ {owner.mention}\n\n👮🏻 Admin\n"
      else:
        text2 += f"👑 Kurucu\n└ @{owner.username}\n\n👮🏻 Admin\n"
    except:
      text2 += f"👑 Kuruu\n└ <i>Hidden</i>\n\n👮🏻 Admins\n"
    if len(adminList) == 0:
      text2 += "└ <i>Admins are hidden</i>"  
      await app.send_message(message.chat.id, text2)   
    else:  
      while len(adminList) > 1:
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"├ {admin.mention}\n"
        else:
          text2 += f"├ @{admin.username}\n"    
      else:    
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"└ {admin.mention}\n\n"
        else:
          text2 += f"└ @{admin.username}\n\n"
      text2 += f"✅ | Toplam Yönətici Sayı: {lenAdminList}\n❌ | Botlar Və Gizli Yönəticilər Iəğv Edildi"  
      await app.send_message(message.chat.id, text2)           
  except FloodWait as e:
    await asyncio.sleep(e.value)


@app.on_message(filters.command('del', [".", "!", "@", "/"]) & filters.group)
async def delAcc(client, msj):
    # ayuyes
    chat_id = msj.chat.id
    DELETED = []
    members = app.get_chat_members(chat_id)
    async for m in members:
        if m.user.is_deleted == True:
            DELETED.append(str(m.user.id)) # silinen hesablar

    shesablar = '\n'.join(DELETED) 
    await app.send_message(chat_id, f"{shesablar}\n\n🗑 **Silinən Hesabların Sayı -{len(DELETED)}**\n**🗨 Qrup:** {msj.chat.title}\n👤 **İcraçı:** {msj.from_user.mention}")	


@app.on_message(filters.command('admins', [".", "!", "@", "/"]))
async def admins(client, message):
  try: 
    adminList = []
    ownerList = []
    async for admin in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
      if admin.privileges.is_anonymous == False:
        if admin.user.is_bot == True:
          pass
        elif admin.status == ChatMemberStatus.OWNER:
          ownerList.append(admin.user)
        else:  
          adminList.append(admin.user)
      else:
        pass   
    lenAdminList= len(ownerList) + len(adminList)  
    text2 = f"👮‍♂️ QRUP İDARƏÇİLƏRİ - {message.chat.title}\n\n"
    try:
      owner = ownerList[0]
      if owner.username == None:
        text2 += f"👑 Kurucu\n└ {owner.mention}\n\n👮🏻 Admin\n"
      else:
        text2 += f"👑 Kurucu\n└ @{owner.username}\n\n👮🏻 Admin\n"
    except:
      text2 += f"👑 Kuruu\n└ <i>Hidden</i>\n\n👮🏻 Admins\n"
    if len(adminList) == 0:
      text2 += "└ <i>Admins are hidden</i>"  
      await app.send_message(message.chat.id, text2)   
    else:  
      while len(adminList) > 1:
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"├ {admin.mention}\n"
        else:
          text2 += f"├ @{admin.username}\n"    
      else:    
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"└ {admin.mention}\n\n"
        else:
          text2 += f"└ @{admin.username}\n\n"
      text2 += f"✅ | Toplam Yönətici Sayı: {lenAdminList}\n❌ | Botlar Və Gizli Yönəticilər Iəğv Edildi"  
      await app.send_message(message.chat.id, text2)           
  except FloodWait as e:
    await asyncio.sleep(e.value)
