import wget
import logging
import datetime
import asyncio
import shutil, psutil, traceback, os
import random
import time
import traceback
import aiofiles
import yt_dlp
import ffmpeg
import aiohttp
import random
import requests
import os, youtube_dl, requests, time

import config
from config import *

from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch
from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters, types
from time import sleep
from random import shuffle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from mesaj.botmesaj import *
from mesaj.kelimeler import *
from mesaj.kelimeler import kelime_sec


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

@app.on_message(filters.command("start") & filters.private)
async def start(_, message: Message):
    loading_message = await message.reply_text("🔄 __**ʟᴜ̈ᴛғᴇɴ ʙᴇᴋʟᴇʏɪ̇ɴ .**__")
    await asyncio.sleep(2)
    await app.edit_message_text(
        chat_id=message.chat.id,
        message_id=loading_message.message_id,
        text=f"""**🎉  ʜᴇʏ  {message.from_user.mention}\n\n🌿  sᴏɴ ᴅᴇʀᴇᴄᴇ ɢᴇʟɪ̇şᴍɪ̇ş, ʙɪ̇ʀ ᴄ̧ᴏᴋ ᴏ̈ᴢᴇʟʟɪ̇ɢ̆ᴇ sᴀʜɪ̇ᴘ ʙɪ̇ʀ ʙᴏᴛᴜᴍ !\n\n💥  ᴋᴏᴍᴜᴛʟᴀʀ ᴠᴇ ᴅᴇsᴛᴇᴋ ɪ̇ᴄ̧ɪ̇ɴ ᴀşᴀɢ̆ɪᴅᴀᴋɪ̇ ʙᴜᴛᴏɴʟᴀʀɪ ᴋᴜʟʟᴀɴɪɴ !**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('✚  ʙᴇɴɪ̇ ɢʀᴜʙᴀ ᴇᴋʟᴇ  ✚', url=f'https://t.me/{BOT_USERNAME}?startgroup=a'),
                ],
                [
                    InlineKeyboardButton("📚  ᴋᴏᴍᴜᴛʟᴀʀ", callback_data="help"),
                    InlineKeyboardButton('🗨️  ᴋᴀɴᴀʟ', url=f'https://t.me/{CHANNELL}')
                ],
                [
                    InlineKeyboardButton('🔹  ᴅᴇsᴛᴇᴋ', url=f'https://t.me/{GROUP_SUPPORT}')
                ]
            ]
        )
    )
	
    # Kullanıcı id ve adını al
    user_id = message.from_user.id
    user_name = message.from_user.mention
    user_username = message.from_user.username
    
    # Log grubuna kullanıcı id ve adını bildir
    log_message = f"**🎂 ʙᴏᴛᴜ ᴘᴍ'ᴅᴇɴ ʙᴀşʟᴀᴛᴛɪ !\n\nᴋᴜʟʟᴀɴɪᴄɪ : {user_name}\nᴋᴜʟʟᴀɴɪᴄɪ ᴀᴅɪ : @{user_username}\nᴋᴜʟʟᴀɴɪᴄɪ ɪᴅ : `{user_id}`**"
    await app.send_message(LOG_CHANNEL, log_message)

@app.on_message(filters.command(["start", "help"]) & filters.group)
async def start(_, message: Message):
    loading_message = await message.reply_text("🔄 __**ʟᴜ̈ᴛғᴇɴ ʙᴇᴋʟᴇʏɪ̇ɴ .**__")
    await asyncio.sleep(2)
    await app.edit_message_text(
        chat_id=message.chat.id,
        message_id=loading_message.message_id,
        text=f"""**🎉  ʜᴇʏ  {message.from_user.mention}\n\n🍀  ʏᴀʀᴅɪᴍ ɪ̇ᴄ̧ɪ̇ɴ ᴘᴍ'ᴅᴇɴ ʙᴀɴᴀ ᴜʟᴀşɪɴ .**""",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔹 ʙᴜʀᴀʏᴀ ᴛɪᴋʟᴀʏɪɴ", url=f"https://t.me/{BOT_USERNAME}?start")]])
    )

@app.on_callback_query(filters.regex("start"))
async def start(_, query: CallbackQuery):
    startmesaj = f"**🎉  ʜᴇʏ  {query.from_user.mention}\n\n🌿  sᴏɴ ᴅᴇʀᴇᴄᴇ ɢᴇʟɪ̇şᴍɪ̇ş, ʙɪ̇ʀ ᴄ̧ᴏᴋ ᴏ̈ᴢᴇʟʟɪ̇ɢ̆ᴇ sᴀʜɪ̇ᴘ ʙɪ̇ʀ ʙᴏᴛᴜᴍ !\n\n💥  ᴋᴏᴍᴜᴛʟᴀʀ ᴠᴇ ᴅᴇsᴛᴇᴋ ɪ̇ᴄ̧ɪ̇ɴ ᴀşᴀɢ̆ɪᴅᴀᴋɪ̇ ʙᴜᴛᴏɴʟᴀʀɪ ᴋᴜʟʟᴀɴɪɴ !**"
    await query.message.edit_text(startmesaj, reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✚  ʙᴇɴɪ̇ ɢʀᴜʙᴀ ᴇᴋʟᴇ  ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=a")
            ],
            [
                InlineKeyboardButton("📚  ᴋᴏᴍᴜᴛʟᴀʀ", callback_data="help"),
                InlineKeyboardButton("🗨️  ᴋᴀɴᴀʟ", url=f"https://t.me/{CHANNELL}")
            ],
            [
                InlineKeyboardButton("🔹  ᴅᴇsᴛᴇᴋ", url=f"https://t.me/{GROUP_SUPPORT}")
            ]
        ]
    )
)
	
@app.on_callback_query(filters.regex("help"))
async def help(_, query: CallbackQuery):
    startbutton = "**🔹 ᴀşᴀɢ̆ɪᴅᴀɴ ʙᴜᴛᴏɴ sᴇᴄ̧ɪ̇ɴ .**"
    await query.message.edit_text(startbutton, reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📚 ᴇᴛɪ̇ᴋᴇᴛ ᴋᴏᴍᴜᴛʟᴀʀɪ", callback_data="tag1"),
                InlineKeyboardButton("🔹 ᴏʏᴜɴ ᴋᴏᴍᴜᴛʟᴀʀɪ", callback_data="tag2")
            ],
            [
	        InlineKeyboardButton("⚙️ ᴅɪ̇ɢ̆ᴇʀ ᴋᴏᴍᴜᴛʟᴀʀ", callback_data="tag3")
            ],
            [
                InlineKeyboardButton("➡️ ɢᴇʀɪ̇ ᴅᴏ̈ɴ", callback_data="start")
            ]
        ]
    )
)
	
@app.on_callback_query(filters.regex("tag1"))
async def tag1(_, query: CallbackQuery):
    etikett = "**🔹 ᴇᴛɪ‌ᴋᴇᴛ ᴋᴏᴍᴜᴛʟᴀʀɪ  :\n\n/cagir - ᴜ‌ʏᴇʟᴇʀɪ‌ ᴛᴏᴘʟᴜ ᴄ‌ᴀɢ‌ɪʀɪɴ .\n/atag - ʏᴏ‌ɴᴇᴛɪ‌ᴄɪ‌ʟᴇʀɪ‌ ᴇᴛɪ‌ᴋᴇᴛʟᴇʀ .\n/utag - ᴜ‌ʏᴇʟᴇʀɪ‌ ᴛᴏᴘʟᴜ ᴇᴛɪ‌ᴋᴇᴛʟᴇʀ .\n/tag - ᴜ‌ʏᴇʟᴇʀɪ‌ ᴛᴇᴋ ᴛᴇᴋ ᴇᴛɪ‌ᴋᴇᴛʟᴇʀ .\n/etag - ᴜ‌ʏᴇʟᴇʀɪ‌ ᴇᴍᴏᴊɪ‌ʟᴇʀʟᴇ ᴇᴛɪ‌ᴋᴇᴛʟᴇʀ .\n/vtag - ᴜ‌ʏᴇʟᴇʀɪ‌ sᴏʀᴜʟᴀʀʟᴀ ᴇᴛɪ‌ᴋᴇᴛʟᴇʀ .\n/stag - ᴜ‌ʏᴇʟᴇʀɪ‌ sᴏ‌ᴢʟᴇʀʟᴇ ᴇᴛɪ‌ᴋᴇᴛʟᴇʀ .\n/otag - ᴜ‌ʏᴇʟᴇʀɪ‌ ʀᴜ‌ᴛʙᴇʟᴇʀʟᴇ ᴇᴛɪ‌ᴋᴇᴛʟᴇʀ .\n/itag - ᴜ̈ʏᴇʟᴇʀɪ̇ ʜᴏş ᴋᴇʟɪ̇ᴍᴇʟᴇʀʟᴇ ᴇᴛɪ̇ᴋᴇᴛʟᴇʀ .\n/cancel - ᴇᴛɪ‌ᴋᴇᴛʟᴇᴍᴇʏɪ‌ ᴅᴜʀᴅᴜʀᴜʀ .**"
    await query.message.edit_text(etikett, reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("➡️ ɢᴇʀɪ̇ ᴅᴏ̈ɴ", callback_data="help")
            ]
        ]
    )
)

@app.on_callback_query(filters.regex("tag2"))
async def tag2(_, query: CallbackQuery):
    oyunn = "**🔹 ᴏʏᴜɴ ᴋᴏᴍᴜᴛʟᴀʀɪ  :\n\n/slap - ᴋᴜʟʟᴀɴɪᴄɪʟᴀʀɪ ᴛᴏᴋᴀᴛʟᴀʏɪɴ .\n/eros - ᴋᴜʟʟᴀɴɪᴄɪʟᴀʀɪ sʜɪ‌ᴘʟᴇʀ .\n/d - ᴅᴏɢ‌ʀᴜʟᴜᴋ sᴏʀᴜsᴜ ᴀᴛᴀʀ .\n/c - ᴄᴇsᴀʀᴇᴛ sᴏʀᴜsᴜ ᴀᴛᴀʀ .\n/soz - ʀᴀsᴛɢᴇʟᴇ sᴏ‌ᴢ ᴀᴛᴀʀ .\n/ok - ᴏᴋ ᴀᴛᴀʀ .\n/top - ᴛᴏᴘ ᴀᴛᴀʀ .\n/slot - sʟᴏᴛ ᴀᴛᴀʀ .\n/basket - ʙᴀsᴋᴇᴛ ᴀᴛᴀʀ .\n/bow - ʙᴏᴡʟɪ‌ɴɢ ᴀᴛᴀʀ .\n/zar - ᴢᴀʀ ᴀᴛᴀʀ .\n/sayi - sᴀʏɪ ᴛᴀʜᴍɪ‌ɴ ᴏʏᴜɴᴜ ᴀᴄ‌ᴀʀ .\n/turet - ᴋᴇʟɪ‌ᴍᴇ ᴛᴜ‌ʀᴇᴛ ᴏʏᴜɴᴜ ᴀᴄ‌ᴀʀ .\n/iptal - ᴏʏᴜɴᴜ ɪ‌ᴘᴛᴀʟ ᴇᴅᴇʀ .\n/werewolfrole - ᴡᴇʀᴇᴡᴏʟғ ʀᴏʟ ʙɪ‌ʟɢɪ‌ʟᴇʀɪ̇ .**"
    await query.message.edit_text(oyunn, reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("➡️ ɢᴇʀɪ̇ ᴅᴏ̈ɴ", callback_data="help")
            ]
        ]
    )
)

@app.on_callback_query(filters.regex("tag3"))
async def tag3(_, query: CallbackQuery):
    digerr = "**🔹 ᴅɪ‌ɢ‌ᴇʀ ᴋᴏᴍᴜᴛʟᴀʀ :\n\n/group - ɢʀᴜᴘ ʙɪ‌ʟɢɪ‌ᴇʀɪ‌ɴɪ‌ ɢᴏ‌sᴛᴇʀɪ‌ʀ .\n/adminlist - ʏᴏ‌ɴᴇᴛɪ‌ᴄɪ‌ʟᴇʀɪ‌ ɢᴏ‌sᴛᴇʀɪ‌ʀ .\n/botlist - ʙᴏᴛʟᴀʀɪ ɢᴏ‌sᴛᴇʀɪ‌ʀ .\n/id - ᴋᴜʟʟᴀɴɪᴄɪ ɪ‌ᴅ'sɪ‌ɴɪ‌ ɢᴏ‌sᴛᴇʀɪ‌ʀ .\n/reload - ʏᴏ‌ɴᴇᴛɪ‌ᴄɪ‌ ʟɪ‌sᴛᴇsɪ‌ɴɪ‌ ɢᴜ‌ɴᴄᴇʟʟᴇʀ .\n/chatbot - sᴏʜʙᴇᴛ ᴍᴏᴅᴜ ᴘᴀɴᴇʟɪ‌ .\n/ask - ʏᴀᴘᴀʏ ᴢᴇᴋᴀ ɪ‌ʟᴇ ᴋᴏɴᴜs‌ᴜɴ .**"
    await query.message.edit_text(digerr, reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("➡️ ɢᴇʀɪ̇ ᴅᴏ̈ɴ", callback_data="help")
            ]
        ]
    )
)

@app.on_callback_query(filters.regex("tag4"))
async def tag4(_, query: CallbackQuery):
    if query.from_user.id != OWNER_ID:
        await query.answer("ʙᴜɴᴀ ɪ̇ᴢɴɪ̇ɴ ʏᴏᴋ ᴋᴏᴄ̧ᴜᴍ .", show_alert=True)  # show_alert parametresini True olarak ayarlayarak yanıtın boyutunu büyütebilirsiniz
        return
    
    sudoo = "✦ Yakında !"
    await query.message.edit_text(sudoo, reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("➡️ ɢᴇʀɪ̇ ᴅᴏ̈ɴ", callback_data="help")
            ]
        ]
    ))

@app.on_message(filters.command(["slap"], prefixes=['/', '']))
async def slap(client: Client, message: Message):
    if message.chat.type == "private":
        return await message.reply(f"{nogroup}")

    if message.reply_to_message:
        reply_message = message.reply_to_message
        user = reply_message.from_user
        if user:
            user_name = f"{user.mention}"
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
            await message.reply(f"**{message.from_user.mention} ,  {slap_phrase}**")
        else:
            await message.reply("__**🔹 ʟᴀɴ, ᴋᴜʟʟᴀɴɪᴄɪʏɪ ʙᴜʟᴀᴍᴀᴅɪᴍ !**__")
    else:
        await message.reply("🔹 __**ʙɪ̇ʀ ᴍᴇsᴀᴊɪ ʏᴀɴɪᴛʟᴀ ʙᴇʙᴇɢ̆ɪ̇ᴍ !**__")
        
@app.on_message(filters.command(["eros", "ship"], prefixes=['/', '']))
async def handle_eros(client: Client, message: Message):
    if message.chat.type == "private":
        return await message.reply(f"{nogroup}")

    chat = await client.get_chat(message.chat.id)
    if message.reply_to_message:
        reply_msg = message.reply_to_message
        user1 = await client.get_chat_member(chat.id, reply_msg.from_user.id)
        user2 = await client.get_chat_member(chat.id, message.from_user.id)
        love_percentage = random.randint(0, 100)
        await message.reply_text(f"**🎈 ᴇʀᴏs'ᴜɴ ᴏᴋᴜɴᴜ ᴀᴛᴛɪᴍ !\n\n{user2.user.mention}  ❣️  {user1.user.mention}\n\n✦ sᴇᴠɢɪ ᴏʀᴀɴɪ : %{love_percentage}**")
    else:
        participants = await client.get_chat_members(chat.id)
        active_users = [user for user in participants if not user.user.is_bot and not user.user.is_deleted and not user.user.is_self]
        if len(active_users) < 2:
            await message.reply_text("**__🔹 ʏᴇᴛᴇʀʟɪ ᴀᴋᴛɪғ ᴋᴜʟʟᴀɴɪᴄɪ ʏᴏᴋ !__**")
        else:
            user1, user2 = random.sample(active_users, 2)
            love_percentage = random.randint(0, 100)
            await message.reply_text(f"**🎈 ᴇʀᴏs'ᴜɴ ᴏᴋᴜɴᴜ ᴀᴛᴛɪᴍ !\n\n{user1.user.mention}  ❣️  {user2.user.mention}\n\n✦ sᴇᴠɢɪ ᴏʀᴀɴɪ : %{love_percentage}**")

@app.on_message(filters.command('group', prefixes='/'))
async def grup_info(client: Client, message: Message):
    if message.chat.type == "private":
        return await message.reply(f"{nogroup}")
     
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
        special_status += f'sɪʟɪɴᴇɴ ʜᴇsᴀᴘʟᴀʀ : {deleted_count}\n'
    if bot_count > 0:
        special_status += f'ʙᴏᴛ sᴀʏɪsɪ : {bot_count}\n'

    if not special_status:
        special_status = "ʙᴜʟᴜɴᴀᴍᴀᴅɪ"

    response_text = (
        f'**ɢʀᴜᴘ ᴀᴅɪ : {group_name}**\n'
        f'**ɢʀᴜᴘ ɪᴅ :** `{group_id}`\n'
        f'**ᴜʏᴇ sᴀʏɪsɪ : {total_count}**\n'
        f'**ɢᴇʀᴄ̧ᴇᴋ ᴋᴜʟʟᴀɴɪᴄɪ : {active_count}**\n'
        f'**{special_status}**'
    )

    await message.reply_text(response_text)
	
@app.on_message(filters.command(["bots", "botlist"], prefixes="/"))
async def show_bots(client: Client, message: Message):
    if message.chat.type == "private":
        return await message.reply(f"{nogroup}")
	    
    all_users = await client.get_chat_members(message.chat.id)
    bot_list = []
    for user in all_users:
        if user.user.is_bot:
            bot_list.append(user.user.mention)
    if bot_list:
        await message.reply_text(f"**🔹 ɪ̇şᴛᴇ ɢʀᴜᴘᴛᴀᴋɪ̇ ʙᴏᴛʟᴀʀ :**\n\n➻  " + "\n➻  ".join(bot_list))
    else:
        await message.reply_text("**🔹 ʙᴜ ɢʀᴜᴘᴛᴀ ʜɪᴄ‌ ʙᴏᴛ ʏᴏᴋ .**")
	    
@app.on_message(filters.command(["admins", "adminlist"], prefixes="/"))
async def show_admins(client: Client, message: Message):
    if message.chat.type == "private":
        return await message.reply(f"{nogroup}")

    chat = message.chat
    admins = await client.get_chat_members(chat.id, filter="administrators")
    admin_list = ""
    for admin in admins:
        user = admin.user
        admin_list += f"\n➻  {user.mention}"
    await message.reply_text(f"**🔹 ɪ̇şᴛᴇ ɢʀᴜᴘᴛᴀᴋɪ̇ ᴀᴅᴍɪ̇ɴʟᴇʀ :\n{admin_list}**")
	
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
            status = "**ᴅᴜʀᴜᴍᴜ : ʏᴏ̈ɴᴇᴛɪ̇ᴄɪ̇**"
        else:
            status = "**ᴅᴜʀᴜᴍᴜ : ᴜ̈ʏᴇ**"
        info = f"**ᴋᴜʟʟᴀɴɪᴄɪ : {user.mention}**\n" \
               f"**ᴋᴜʟʟᴀɴɪᴄɪ ᴀᴅɪ : @{user.username}**\n" \
               f"**ᴋᴜʟʟᴀɴɪᴄɪ ɪᴅ : **`{user.id}`\n" \
               f"**ɢʀᴜᴘ ɪᴅ : **`{message.chat.id}`\n" \
               f"{status}"
        await message.reply_text(info)
    else:
        chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
        if chat_member.status == "administrator" or chat_member.status == "creator":
            status = "**ᴅᴜʀᴜᴍᴜ : ʏᴏ̈ɴᴇᴛɪ̇ᴄɪ̇**"
        else:
            status = "**ᴅᴜʀᴜᴍᴜ : ᴜ̈ʏᴇ**"
        info = f"**ᴋᴜʟʟᴀɴɪᴄɪ : {message.from_user.mention}**\n" \
               f"**ᴋᴜʟʟᴀɴɪᴄɪ ᴀᴅɪ : @{message.from_user.username}**\n" \
               f"**ᴋᴜʟʟᴀɴɪᴄɪ ɪᴅ : **`{message.from_user.id}`\n" \
               f"**ɢʀᴜᴘ ɪᴅ : **`{message.chat.id}`\n" \
               f"{status}"
        await message.reply_text(info)
	
@app.on_message(filters.command("reload", prefixes="/") & filters.group)
async def reload_command(client: Client, message: Message):
    if message.chat.type == "private":
        return await message.reply(f"{nogroup}")
	    
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status in ["creator", "administrator"]:
        await client.send_message(message.chat.id, "**🎈 ʙᴏᴛ ʏᴇɴɪᴅᴇɴ ʙᴀs‌ʟᴀᴅɪ !\n🎈 ᴀᴅᴍɪɴ ʟɪsᴛᴇsɪ ɢüɴᴄᴇʟʟᴇɴᴅɪ !**")
    else:
        await client.send_message(
            message.chat.id,
            "✨ __**ʟüᴛғᴇɴ ʙᴇɴɪ ʏöɴᴇᴛɪᴄɪ ʏᴀᴘɪɴ !**__"
	)
	    
@app.on_message(filters.new_chat_members, group=1)
async def welcomebot(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(BOT_ID):
            await msg.reply(
                f'''**✦  ʜᴇʏ  {msg.from_user.mention}\n\n✦  ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇᴅɪɢ‌ɪɴ ɪᴄ‌ɪɴ ᴛᴇs‌s‌ᴇᴋᴜ‌ʀ ᴇᴅᴇʀɪᴍ, ʙᴇɴɪ ʏᴏ‌ɴᴇᴛɪᴄɪ ʏᴀᴘᴍᴀʏɪ ᴜɴᴜᴛᴍᴀʏɪɴ !\n\n✦  ᴅᴀʜᴀ ғᴀᴢʟᴀ ʙɪʟɢɪ ɪᴄ‌ɪɴ ᴀs‌s‌ᴀɢ‌ɪᴅᴀᴋɪ ʙᴜᴛᴏɴᴜ ᴋᴜʟʟᴀɴɪɴ !**''', 
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔹 ʙᴜʀᴀʏᴀ ᴛɪᴋʟᴀʏɪɴ", url=f"https://t.me/{BOT_USERNAME}?start")]])
            )
            log_message = f"**🎂 ʙᴏᴛᴜ ɢʀᴜʙᴀ ᴇᴋʟᴇᴅɪ̇ !\n\nᴋᴜʟʟᴀɴɪᴄɪ : {msg.from_user.mention}\nᴋᴜʟʟᴀɴɪᴄɪ ᴀᴅɪ : @{msg.from_user.username}\nᴋᴜʟʟᴀɴɪᴄɪ ᴀᴅɪ : `{msg.from_user.id}`\n\nɢʀᴜᴘ ᴀᴅɪ : {msg.chat.title}\nɢʀᴜᴘ ʟɪ̇ɴᴋɪ̇ : @{msg.chat.username}\nɢʀᴜᴘ ᴀᴅɪ : `{msg.chat.id}`**"
            await bot.send_message(LOG_CHANNEL, log_message)
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

@app.on_message(filters.command(["slot"], ["/", ""]))
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
    await message.reply_text(f"**__🔹 ᴄᴇsᴀʀᴇᴛ sᴇᴄ̧ᴛɪɴ, sᴀɴɪʀɪᴍ ғᴀᴢʟᴀ ᴄᴇsᴀʀᴇᴛʟɪsɪɴ .__\n\n✦ ʏᴀᴘᴍᴀɴ ɢᴇʀᴇᴋᴇɴ : {random.choice(c)}**")

@app.on_message(filters.command(["d"], ["/", ""]))
async def dsor(client: Client, message: Message):
    await message.reply_text(f"**__🔹 ᴅᴏɢ̆ʀᴜʟᴜᴋ sᴇᴄ̧ᴛɪɴ, ᴄ̧ᴏᴋ ɢᴜ̈ᴢᴇʟ .__\n\n✦ sᴀɴᴀ sᴏʀᴜᴍ : {random.choice(d)}**")

@app.on_message(filters.command(["soz"], ["/", ""]))
async def dsor(client: Client, message: Message):
    await message.reply_text(f"**✦ ɢᴜ̈ᴢᴇʟ sᴏ̈ᴢ :\n\n{random.choice(guzelsoz)}**")

oyun = {}
rating = {}
@app.on_message(filters.command("turet") & ~filters.private & ~filters.channel)
async def kelimeoyun(c:Client, m:types.Message):

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

        text = f"""**{m.from_user.mention}  tarafından
💥 Oyun Başlatıldı !
        
🎯 Raund : {oyun[m.chat.id]['round']}/80
📖 Kelime :   <code>{kelime_list}</code>
💰 Kazandıracak Puan : 1
🔎 İpucu : 1. {oyun[m.chat.id]["kelime"][0]}
🌟 Uzunluk : {int(len(kelime_list)/2)} 

👁️‍🗨️ Karışık Harflerden Doğru Kelimeyi Bulun . . .
        **"""
        
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🔹 ᴋᴇʟɪ̇ᴍᴇʏɪ̇ ᴘᴀss ɢᴇᴄ̧", callback_data="pass")]
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
            await c.send_message(cb.message.chat.id,f"**{cb.from_user.mention}  tarafından \n🎂 Kelime pass geçildi .\n\n💥 Kalan Pass Hakkın : `{pass_hakki}`\n👀 Doğru Kelime : `{oyun[cb.message.chat.id]['kelime']}`**")
		
            oyun[cb.message.chat.id]["kelime"] = kelime_sec()
            oyun[cb.message.chat.id]["aktif"] = True
            
            kelime_list = ""
            kelime = list(oyun[cb.message.chat.id]['kelime'])
            shuffle(kelime)
            
            for harf in kelime:
                kelime_list+= harf + " "
            
            text = f"""**🎯 Raund : {oyun[cb.message.chat.id]['round']}/80
📖 Kelime :   <code>{kelime_list}</code>
💰 Kazandıracak Puan : 1
🔎 İpucu : 1. {oyun[cb.message.chat.id]["kelime"][0]}
🌟 Uzunluk : {int(len(kelime_list)/2)} 

👁️‍🗨️ Karışık Harflerden Doğru Kelimeyi Bulun . . .
            **"""

            keyboard = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🔹 ᴋᴇʟɪ̇ᴍᴇʏɪ̇ ᴘᴀss ɢᴇᴄ̧", callback_data="pass")]
                ]
            )
            
            await c.send_message(cb.message.chat.id, text, reply_markup=keyboard)
            
        else:
            await c.send_message(cb.message.chat.id, f"**✦ Pass Hakkın Tükendi .\n🔹 Oyunu Bitirmek için ➻ /iptal**")
     
@app.on_message(filters.command("iptal") & ~filters.private & ~filters.channel)
async def stop(c:Client, m:Message):
    global oyun
    
    if m.chat.id in oyun and "oyuncular" in oyun[m.chat.id]:
        siralama = []
        for i in oyun[m.chat.id]["oyuncular"]:
            siralama.append(f" {i}  :  {oyun[m.chat.id]['oyuncular'][i]}  Puan")
        siralama.sort(key=lambda x: x.split(":")[1].strip(), reverse=True)
        siralama_text = ""
        for i, sira in enumerate(siralama, start=1):
            siralama_text += f"{i}) {sira}\n"     
    
        await c.send_message(m.chat.id, f"**{m.from_user.mention}  tarafından\n💥 Oyun İptal Edildi !\n\n🎖️  Puan Tablosu  🎖️\n\n{siralama_text}**", reply_to_message_id=m.message_id)
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
                        [InlineKeyboardButton("🔹 ᴋᴇʟɪ̇ᴍᴇʏɪ̇ ᴘᴀss ɢᴇᴄ̧", callback_data="pass")]
                    ]
                )

                await c.send_message(m.chat.id, text, reply_markup=keyboard)
    except KeyError:
        pass   
	
@app.on_message(filters.command("sinfo") & filters.user(OWNER_ID))
async def ksayi(c:Client, m:Message):
    await m.reply(f"**🔹 Bot'ta kayıtlı {len(kelimeler)} kelime bulunmakta .**")

print("ALL.PY AKTİF !")
app.run()
