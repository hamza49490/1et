import random
import shutil, psutil, traceback
import aiofiles
import requests, time
import random, os, logging, asyncio
import telethon
from mesaj.kurtmesaj import *
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
from telethon.tl.types import User
from telethon.tl import types
from telethon.tl import functions
from pyrogram.handlers import MessageHandler
from telethon import errors
from time import time
from os import remove
from telethon.sync import types
from telethon import types
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.sync import TelegramClient, events
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User
from pyrogram import Client, filters
from random import randint


logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID","26573250"))
api_hash = os.environ.get("API_HASH","6306d2d23b1083a6f757f64f0b0c609c")
bot_token = os.environ.get("TOKEN","6865081184:AAFcDOrflr2l_tibi7tvQ3A9Sv288XxevLA")
BOT_USERNAME = os.environ.get("BOT_USERNAME","EpicTaggerBot")

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

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
        await event.respond(f"{nogroup}", parse_mode='markdown')
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
    message = f'**{tags}\n\n➻  {sender_username}\n✦ __sɪᴢɪ ᴏʏᴜɴᴀ ᴄ̧ᴀɢ̆ɪʀɪʏᴏʀ .__**'
    
    # Mesajı gönder
    await client.send_message(event.chat_id, message)

@client.on(events.NewMessage(pattern='/utag'))
async def utag(event):
    global gece_tag, rxyzdev_tagTot, anlik_calisan
    if event.is_private:
        return await event.respond("Bu komut yalnızca gruplarda kullanılabilir.")
    
    admins = []
    async for admin in client.iter_participants(event.chat_id, filter=types.ChannelParticipantsAdmins):
        admins.append(admin.id)
    if event.sender_id not in admins:
        return await event.respond("Bu komutu yalnızca yöneticiler kullanabilir.")
    
    if len(event.message.text.split()) > 1:
        mode = "text_on_cmd"
        msg_list = event.message.text.split(None, 1)
        if len(msg_list) < 2:
            return await event.respond("Bir mesaj verin.\nÖrnek: /utag Merhaba")
        msg = msg_list[1]
    elif event.message.reply_to_msg_id:
        mode = "text_on_reply"
        msg = event.message.reply_to_msg_id
        if msg == None:
            return await event.respond("Bir mesaj verin.")
    elif len(event.message.text.split()) > 1 and event.message.reply_to_msg_id:
        mode = "text_on_cmd"
        msg_list = event.message.text.split(None, 1)
        if len(msg_list) < 2:
            return await event.respond("Bir mesaj verin.\nÖrnek: /utag Merhaba")
        msg = msg_list[1]
    else:
        mode = "text_on_cmd"
        msg = ""
    
    if mode == "text_on_cmd":
        if event.chat_id in gece_tag:
            return await event.respond("Zaten aktif bir işlem var.")

    gece_tag.append(event.chat_id)  # Bu satırı ekledim
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("Etiketlemeye başlıyorum.")
    
    async for usr in client.iter_participants(event.chat_id):
        if usr.bot or usr.deleted:
            continue
        if event.chat_id not in rxyzdev_tagTot:
            rxyzdev_tagTot[event.chat_id] = 0
        rxyzdev_tagTot[event.chat_id] += 1
        usrnum += 1
        usrtxt += f"{usr.first_name} , "
        if usrnum == 1:  # Kullanıcı sayı
            await client.send_message(event.chat_id, f"{msg}\n\n{usrtxt}")
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    
    sender = await client.get_entity(event.sender_id)
    rxyzdev_initT = f"{sender.first_name}"      
    if event.chat_id in rxyzdev_tagTot:
        await event.respond(f"🗨️ Etiketleme tamamlandı.\n\n➻ {rxyzdev_initT}\n👤 Etiketlenenlerin sayısı: {rxyzdev_tagTot[event.chat_id]}")
    rxyzdev_tagTot[event.chat_id] = 0  # Etiketlenen kullanıcı sayısını sıfırla
    if event.chat_id in gece_tag:
        gece_tag.remove(event.chat_id)

@client.on(events.NewMessage(pattern='/cancel'))
async def cancel(event):
    global gece_tag
    if event.is_private:
        return await event.respond("Bu komut yalnızca gruplarda kullanılabilir.")
    
    admins = []
    async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
        admins.append(admin.id)
    if event.sender_id not in admins:
        return await event.respond("Bu komutu yalnızca yöneticiler kullanabilir.")
    
    if event.chat_id in gece_tag:
        gece_tag.remove(event.chat_id)
        return await event.respond("Etiketleme işlemi durduruldu. Toplam etiketlenen kullanıcı sayısı: {rxyzdev_tagTot[event.chat_id]}, Etiketlemeyi iptal eden kullanıcı: {event.sender_id}")
    else:
        return await event.respond("Aktif bir etiketleme işlemi bulunmamaktadır.")
	    
##################################################
@client.on(events.NewMessage(pattern='(?i)(/|)/kurt'))
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

@client.on(events.callbackquery.CallbackQuery(data="grstart"))
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
                      Button.inline("👈 Geri", data="grstart")
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
                      Button.inline("👈 Geri", data="grstart")
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
                      Button.inline("👈 Geri", data="grstart")
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

	
print("Telethon çalışıyor :)")
client.start()
client.run_until_disconnected()
