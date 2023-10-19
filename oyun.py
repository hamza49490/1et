import heroku3
import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.events import StopPropagation

from pyrogram.types.messages_and_media import Message
from pyrogram import Client, filters
import time
import os
import heroku3
from telethon import TelegramClient, events

from pyrogram import Client
from pyrogram import filters
import logging

api_id = int(os.environ.get("APP_ID","18049084"))
api_hash = os.environ.get("API_HASH","7e74b1e22026fcc291d32b3d431aa21e")
bot_token = os.environ.get("TOKEN","6686468684:AAEe2sSuc8ZkYBFL2jozDJ5AHUXYv4UqtpU")
 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

app = Client("GUNC",
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token
            )

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     await event.reply(f"**💕 Bir rol takımı seçin .**", buttons=(
                      [
                       Button.inline('👱 Köylü Takımı', data='koylu')
                      ],
                      [
                       Button.inline('🐺 Kurt Takımı', data='kurt'),
                       Button.inline('👤 Bireysel', data='bireysel')
                      ],
                    ),
                    link_preview=False)

@client.on(events.NewMessage(pattern="^/kurt$"))
async def start(event):
  if event.is_group:
    return await client.send_message(event.chat_id, f"**💕 Bir rol takımı seçin .**", buttons=(
                      [
                       Button.inline('👱 Köylü Takımı', data='koylu')
                      ],
                      [
                       Button.inline('🐺 Kurt Takımı', data='kurt'),
                       Button.inline('👤 Bireysel', data='bireysel')
                      ],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="grstart"))
async def start(event):
    async for usr in client.iter_participants(event.chat_id):
     await event.edit(f"**💕 Bir rol takımı seçin .**",
                    buttons=(
                      [
                       Button.inline('👱 Köylü Takımı', data='koylu')
                      ],
                      [
                       Button.inline('🐺 Kurt Takımı', data='kurt'),
                       Button.inline('👤 Bireysel', data='bireysel')
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="koylu"))
async def handler(event):
    await event.edit(f"**💕 Hakkında bilgi almak istediğiniz rolü seçin .**", buttons=(
                      [
                      Button.inline("Tarikat Avcısı 💂", data="tavci")
                      ],
                      [
                      Button.inline("Gözcü 👳", data="gozcu"),
                      Button.inline("Sarhoş 🍻", data="sarhos")
                      ],
                      [
                      Button.inline("Yancı 💋", data="yancı"),
                      Button.inline("Seyirci 👁", data="seyirci")
                      ],
                      [
                      Button.inline("Silahşör 🔫", data="silahsor"),
                      Button.inline("Koruyucu Melek 👼", data="kmelek")
                      ],
                      [
                      Button.inline("Mason 👷", data="mason"),
                      Button.inline("Dedektif 🕵️", data="dedektif")
                      ],
                      [
                      Button.inline("Lanetli 😾", data="lanetli"),
                      Button.inline("Avcı 🎯", data="avci")
                      ],
                      [
                      Button.inline("Eros 🏹", data="eros"),
                      Button.inline("Demirci ⚒️", data="demirci")
                      ],
                      [
                      Button.inline("Prens 💍", data="prens"),
                      Button.inline("Muhtar 🎖", data="muhtar")
                      ],
                      [
                      Button.inline("Kahin 🌀", data="kahin"),
                      Button.inline("Hükümdar 👑", data="hükümdar")
                      ],
                      [
                      Button.inline("Barışçıl ☮️", data="barışçıl"),
                      Button.inline("Yaşlı Bilge 📚", data="ybilge")
                      ],
                      [
                      Button.inline("Uyutucu 💤", data="uyutucu"),
                      Button.inline("Fedai 🔰", data="fedai")
                      ],
                      [
                      Button.inline("Simyacı 🍵", data="simyaci"),
                      Button.inline("Güzel 💅", data="guzel")
                      ],
                      [
                      Button.inline("Fırtına Getiren 🌩", data="fırtına"),
                      Button.inline("Yabanı Çocuk 👶", data="yabani")
                      ],
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ]
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kurt"))
async def handler(event):
    await event.edit(f"**💕 Hakkında bilgi almak istediğiniz rolü seçin .**", buttons=(
                      [
                      Button.inline("Kurtadam 🐺", data="kurtadam"),
                      Button.inline("Alfa Kurt ⚡️", data="alfakurt")
                      ],
                      [
                      Button.inline("Falcı 🔮", data="falci"),
                      Button.inline("Yavru Kurt 🐶", data="yavrukurt")
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
                      Button.inline("👈 Geri", data="grstart")
                      ]
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="tavci"))
async def handler(event):
    await event.edit(f"{tavci}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="gozcu"))
async def handler(event):
    await event.edit(f"{gozcu}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="yancı"))
async def handler(event):
    await event.edit(f"{yancı}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="seyirci"))
async def handler(event):
    await event.edit(f"{seyirci}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="silahsor"))
async def handler(event):
    await event.edit(f"{silahsor}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="kmelek"))
async def handler(event):
    await event.edit(f"{kmelek}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="mason"))
async def handler(event):
    await event.edit(f"{mason}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="dedektif"))
async def handler(event):
    await event.edit(f"{dedektif}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="eros"))
async def handler(event):
    await event.edit(f"{eros}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="avci"))
async def handler(event):
    await event.edit(f"{avci}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="demirci"))
async def handler(event):
    await event.edit(f"{demirci}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="prens"))
async def handler(event):
    await event.edit(f"{prens}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="muhtar"))
async def handler(event):
    await event.edit(f"{muhtar}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kahin"))
async def handler(event):
    await event.edit(f"{kahin}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="hükümdar"))
async def handler(event):
    await event.edit(f"{hükümdar}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="barışçıl"))
async def handler(event):
    await event.edit(f"{bariscil}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="ybilge"))
async def handler(event):
    await event.edit(f"{ybilge}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="uyutucu"))
async def handler(event):
    await event.edit(f"{uyutucu}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="fedai"))
async def handler(event):
    await event.edit(f"{fedai}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="simyaci"))
async def handler(event):
    await event.edit(f"{simyaci}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="guzel"))
async def handler(event):
    await event.edit(f"{guzel}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="fırtına"))
async def handler(event):
    await event.edit(f"{mason}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="yabani"))
async def handler(event):
    await event.edit(f"{dedektif}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="lanetli"))
async def handler(event):
    await event.edit(f"{lanetli}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kurtadam"))
async def handler(event):
    await event.edit(f"{kurtadam}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="alfakurt"))
async def handler(event):
    await event.edit(f"{alfakurt}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="karmelek"))
async def handler(event):
    await event.edit(f"{karmelek}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="mistik"))
async def handler(event):
    await event.edit(f"{mistik}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="haydut"))
async def handler(event):
    await event.edit(f"{haydut}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="duzenbaz"))
async def handler(event):
    await event.edit(f"{duzenbaz}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="falci"))
async def handler(event):
    await event.edit(f"{falci}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="yavrukurt"))
async def handler(event):
    await event.edit(f"{yavrukurt}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

client.run_until_disconnected()


pyrogram==1.4.8
beautifulsoup4
requests
feedparser==6.0.2
telethon
cryptg
requests
heroku3
pyrogram
TgCrypto

