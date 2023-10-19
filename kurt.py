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
                      Button.inline("Kahin Çırak 🙇", data="kahinc"),
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




@client.on(events.callbackquery.CallbackQuery(data="koylu"))
async def handler(event):
    await event.edit(f"{koyluu}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="sarhos"))
async def handler(event):
    await event.edit(f"{sarhoss}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="gozcu"))
async def handler(event):
    await event.edit(f"{gozcuu}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="yanci"))
async def handler(event):
    await event.edit(f"{yancii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="seyirci"))
async def handler(event):
    await event.edit(f"{seyircii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="silahsor"))
async def handler(event):
    await event.edit(f"{silahsorr}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kmelek"))
async def handler(event):
    await event.edit(f"{kmelekk}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="aptal"))
async def handler(event):
    await event.edit(f"{aptall}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="mason"))
async def handler(event):
    await event.edit(f"{masonn}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="dedektif"))
async def handler(event):
    await event.edit(f"{dedektiff}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kahinc"))
async def handler(event):
    await event.edit(f"{kahincc}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="tavci"))
async def handler(event):
    await event.edit(f"{tavcii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="eros"))
async def handler(event):
    await event.edit(f"{eross}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="avci"))
async def handler(event):
    await event.edit(f"{avcii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="beceriksiz"))
async def handler(event):
    await event.edit(f"{beceriksizz}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="demirci"))
async def handler(event):
    await event.edit(f"{demircii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="karak"))
async def handler(event):
    await event.edit(f"{karakk}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="prens"))
async def handler(event):
    await event.edit(f"{prenss}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="bbaskani"))
async def handler(event):
    await event.edit(f"{bbaskanii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kahin"))
async def handler(event):
    await event.edit(f"{kahinn}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="hukumdar"))
async def handler(event):
    await event.edit(f"{hukumdarr}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="bariscil"))
async def handler(event):
    await event.edit(f"{bariscill}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="ybilge"))
async def handler(event):
    await event.edit(f"{ybilgee}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="uyutucu"))
async def handler(event):
    await event.edit(f"{uyutucuu}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kurdumsu"))
async def handler(event):
    await event.edit(f"{kurdumsuu}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)
    
@client.on(events.callbackquery.CallbackQuery(data="sehit"))
async def handler(event):
    await event.edit(f"{sehitt}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="simyaci"))
async def handler(event):
    await event.edit(f"{simyacii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="efendi"))
async def handler(event):
    await event.edit(f"{efendii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="guzel"))
async def handler(event):
    await event.edit(f"{guzell}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="fgetiren"))
async def handler(event):
    await event.edit(f"{fgetirenn}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="hain"))
async def handler(event):
    await event.edit(f"{hainn}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)
    
@client.on(events.callbackquery.CallbackQuery(data="ycocuk"))
async def handler(event):
    await event.edit(f"{ycocukk}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="lanetli"))
async def handler(event):
    await event.edit(f"{lanetlii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

################################

@client.on(events.callbackquery.CallbackQuery(data="kurtadam"))
async def handler(event):
    await event.edit(f"{kurtadamm}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)
    
@client.on(events.callbackquery.CallbackQuery(data="alfakurt"))
async def handler(event):
    await event.edit(f"{alfakurtt}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="falci"))
async def handler(event):
    await event.edit(f"{falcii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="yavrukurt"))
async def handler(event):
    await event.edit(f"{yavrukurtt}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="lycan"))
async def handler(event):
    await event.edit(f"{lycann}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="haydut"))
async def handler(event):
    await event.edit(f"{haydutt}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="mistik"))
async def handler(event):
    await event.edit(f"{mistikk}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="duzenbaz"))
async def handler(event):
    await event.edit(f"{duzenbazz}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="karmelek"))
async def handler(event):
    await event.edit(f"{karmelekk}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

################################

@client.on(events.callbackquery.CallbackQuery(data="iblis"))
async def handler(event):
    await event.edit(f"{ibliss}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)
    
@client.on(events.callbackquery.CallbackQuery(data="tarikatci"))
async def handler(event):
    await event.edit(f"{tarikatcii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="rahip"))
async def handler(event):
    await event.edit(f"{rahipp}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="hirsiz"))
async def handler(event):
    await event.edit(f"{hirsizz}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kustasi"))
async def handler(event):
    await event.edit(f"{kustasii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="skatil"))
async def handler(event):
    await event.edit(f"{skatill}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kundakci"))
async def handler(event):
    await event.edit(f"{kundakcii}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="buyucu"))
async def handler(event):
    await event.edit(f"{buyucu}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ],
                    ),
                    link_preview=False)
    
client.run_until_disconnected()
