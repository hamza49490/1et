import heroku3
import random, os, logging, asyncio
import time
import os
import heroku3
import logging
from mesaj.kurtmesaj import ...
from telethon import TelegramClient, events
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.events import StopPropagation
from pyrogram.types.messages_and_media import Message
from pyrogram import Client, filters
from Config import Config
from pyrogram import Client
from pyrogram import filters


api_id = int(os.environ.get("APP_ID","18049084"))
api_hash = os.environ.get("API_HASH","7e74b1e22026fcc291d32b3d431aa21e")
bot_token = os.environ.get("TOKEN","6559325433:AAF-G05bNjC-S5TwbmW222eY77SU8jM5GhY")

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)



@client.on(events.NewMessage(pattern="^/kurt$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     await event.reply(f"**💕 Bir rol takımı seçin .**", buttons=(
                      [
                       Button.inline('👱 Köylü Takımı', data='koylu')
                      ],
                      [
                       Button.inline('🐺 Kurtlar & Müttefikleri', data='kurt')
                      ],
                      [
                       Button.inline('👤 Diğer Düşmanlar', data='bireysel')
                      ],
                    ),
                    link_preview=False)

  if event.is_group:
    return await client.send_message(event.chat_id, f"**💕 Bir rol takımı seçin .**", buttons=(
                      [
                       Button.inline('👱 Köylü Takımı', data='koylu')
                      ],
                      [
                       Button.inline('🐺 Kurtlar & Müttefikleri', data='kurt')
                      ],
                      [
                       Button.inline('👤 Diğer Düşmanlar', data='bireysel')
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
                       Button.inline('🐺 Kurtlar & Müttefikleri', data='kurt')
                      ],
                      [
                       Button.inline('👤 Diğer Düşmanlar', data='bireysel')
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="koylu"))
async def handler(event):
    await event.edit(f"**💕 Hakkında bilgi almak istediğiniz rolü seçin .**", buttons=(
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
                      Button.inline("Lanetli 🙇", data="lanetli"),
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
                      Button.inline("Güzellik 💅", data="guzellik")
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
                      Button.inline("👈 Geri", data="grstart")
                      ]
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="bireysel"))
async def handler(event):
    await event.edit(f"**💕 Hakkında bilgi almak istediğiniz rolü seçin .**", buttons=(
                      [
                      Button.inline("İblis 👺", data="iblis"),
                      Button.inline("Tarikatçı 👤", data="tarikatci")
                      ],
                      [
                      Button.inline("Rahip ✝️", data="rahip"),
                      Button.inline("Hırsız 😈", data="hirsiz")
                      ],
                      [
                      Button.inline("Kukla ustası 🕴", data="kustasi"),
                      Button.inline("Seri Katil 🔪", data="skatil")
                      ],
                      [
                      Button.inline("Kundakçı 🔥", data="kundakci"),
                      Button.inline("Büyücü ⚰️", data="buyucu")
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
