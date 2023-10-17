import telethon
from telethon.tl import types
from telethon import Button
from telethon.tl import types
from telethon.tl import functions
import wget
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
from telethon.tl.functions.users import GetFullUserRequest
from telethon.sync import types
from datetime import datetime 
from telethon.errors.rpcerrorlist import PeerFloodError
from telethon import Button
from pyrogram.errors import FloodWait
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from datetime import datetime
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import PeerIdInvalid
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
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    PeerIdInvalid,
    UserIsBlocked,
)

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID","18049084"))
api_hash = os.environ.get("API_HASH","7e74b1e22026fcc291d32b3d431aa21e")
bot_token = os.environ.get("TOKEN","6404904263:AAHP25SjaF85qCncHTq5NE9zA4A-ASD5XNA")
BOT_ID = int(os.environ.get("BOT_ID", "6404904263"))
DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://epiktv7:epiktv86@cluster0.ttyjqmj.mongodb.net/?retryWrites=true&w=majority") # MongoDB veritabanınızın url'si. Nasıl alacağınızı bilmiyorsanız destek grubu @RepoHaneX'e gelin.
BOT_USERNAME = os.environ.get("BOT_USERNAME","BuketTaggerBot") # Botunuzun kullanıcı adı.
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL","-1001983841726")) # Botunuzun eylemleri kaydedeceği kayıt grubunun id'si.
GROUP_SUPPORT = os.environ.get("GROUP_SUPPORT", "BuketBilgi") # Botunuzdan yasaklanan kullanıcıların itiraz işlemleri için başvuracağı grup, kanal veya kullanıcı. Boş bırakırsanız otomatik olarak OWNER_ID kimliğine yönlendirecektir.
GONDERME_TURU = os.environ.get("GONDERME_TURU", False) # Botunuzun yanıtladığınız mesajı gönderme türü. Eğer direkt iletmek isterseniz False, kopyasını göndermek isterseniz True olarak ayarlayın.
OWNER_ID = int(os.environ.get("OWNER_ID", "6181368568")) # Sahip hesabın id'si
OWNERNAME = "ㅤᴀɪᴋᴏㅤ"
OWNER = [6540285284]
#SUDO = []
LANGAUGE = os.environ.get("LANGAUGE", "TR")

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

ozel_list = [6540285284]
grup_sayi = []
etiketuye = []
isleyen = []
user_sayi = []


@client.on(events.NewMessage)
async def chatbot(event):
    global isleyen
    mesaj = str(event.raw_text)
    qrup = event.chat_id
    if qrup not in isleyen:
        return
    if "selam" in mesaj or "Selam" in mesaj  or "SELAM" in mesaj or "Selamün Aleyküm" in mesaj or "selamün aleyküm" in mesaj:
        await event.reply(f"**{random.choice(x1)}**")
    if "Nasılsın" in mesaj or "nasılsın" in mesaj or "naber" in mesaj or "Naber" in mesaj or "ne haber" in mesaj:
        await event.reply(f"**{random.choice(x2)}**")
    if "Adam" in mesaj or "adam" in mesaj:
        await event.reply(f"**{random.choice(x3)}**")
    if "iyim" in mesaj or "İyiyim" in mesaj:
        await event.reply(f"**{random.choice(x4)}**")
    if "Hoş Geldin" in mesaj or "hoş geldin" in mesaj:
        await event.reply(f"**{random.choice(x5)}**")
    if "Merhaba" in mesaj or "merhaba" in mesaj:
        await event.reply(f"**{random.choice(x6)}**")
    if "Ban" in mesaj or "ban" in mesaj :
        await event.reply(f"**{random.choice(x7)}**")
    if "Ne yapıyorsun" in mesaj or "ne yapıyorsun" in mesaj or "Nabıyon" in mesaj or "nabıyon" in mesaj :
        await event.reply(f"**{random.choice(x8)}**")
    if "😔" in mesaj or "🥺" in mesaj  or "😥" in mesaj  or "😢" in mesaj:
        await event.reply(f"**{random.choice(x9)}**")
    if "valla" in mesaj or "Valla" in mesaj or "Vallahi" in mesaj or "vallahi" in mesaj:
        await event.reply(f"**{random.choice(x10)}**")
    if "ne" in mesaj or "Ne" in mesaj:
        await event.reply(f"**{random.choice(x11)}**")
    if "sg" in mesaj or "Sg" in mesaj or "siktir" in mesaj or "Siktir" in mesaj:
        await event.reply(f"**{random.choice(x12)}**")
    if "Mal" in mesaj or "mal" in mesaj or "gerizekalı" in mesaj or "Gerizekalı" in mesaj:
        await event.reply(f"**{random.choice(x13)}**")
    if "Balım" in mesaj or "balım" in mesaj:
        await event.reply(f"**{random.choice(x14)}**")
    if "Canım" in mesaj or "canım" in mesaj:
        await event.reply(f"**{random.choice(x15)}**")
    if "gidiyorum" in mesaj or "Gidiyorum" in mesaj or "gittim" in mesaj or "Gittim" in mesaj or "Görüşürüz" in mesaj or "görüşürüz" in mesaj:
        await event.reply(f"**{random.choice(x16)}**")
    if "Sinirlendim" in mesaj or "sinirlendim" in mesaj or "😡" in mesaj or "🤬" in mesaj:
        await event.reply(f"**{random.choice(x17)}**")
    if "tanışalım mı" in mesaj or "Tanışalım mı" in mesaj:
        await event.reply(f"**{random.choice(x18)}**")
    if "İsmin ne" in mesaj or "ismin ne" in mesaj  or "Adın ne" in mesaj or "adın ne" in mesaj:
        await event.reply(f"**{random.choice(x19)}**")
    if "iyi sen" in mesaj or "İyi sen" in mesaj  or "iyim sen" in mesaj or "İyim sen" in mesaj:
        await event.reply(f"**{random.choice(x20)}**")
    if "😅" in mesaj or "😂" in mesaj or "🤣" in mesaj  or "😄" in mesaj:
        await event.reply(f"**{random.choice(x21)}**")
    if "Büyüğüm" in mesaj or "büyüğüm" in mesaj or "büyük" in mesaj  or "Büyük" in mesaj:
        await event.reply(f"**{random.choice(x22)}**")
    if "Aiko" in mesaj or "aiko" in mesaj:
        await event.reply(f"**{random.choice(x23)}**")
    if "Merve" in mesaj or "merve" in mesaj or "merfe" in mesaj  or "Merfe" in mesaj:
        await event.reply(f"**{random.choice(x24)}**")
    if "Günaydın" in mesaj or "günaydın" in mesaj:
        await event.reply(f"**{random.choice(x25)}**")
    if "İyi geceler" in mesaj or "iyi geceler" in mesaj:
        await event.reply(f"**{random.choice(x26)}**")
	       

x1 = ("Aleyküm Selam 🎉", "Selam", "Ase", "As",)
x2 = ("İyiyim senden naber", "Gelmedi senden bir haber .", "Kötü ya sen", "Teşekkür ederim iyiyim sen nasılsın", "Tıpkı senin gibi mükemmelim 🥳",)
x3 = ("Mermiler seksin, alemde teksin 😏", "Mermiler seksin, tokatımı yersin 😏",)
x4 = ("İyi olmana sevindim", "Hep daha iyi olman dileğiyle  ", "Keşke bende senin kadar iyi olsam 😏",)
x5 = ("Naber", "Ne haber kanka", "Hoş buldum nabiyon", "hb, nasılsın",)
x6 = ("Merhaba, Hoş geldin", "Merhaba, Hoş Geldin", "Merhaba, nerelerdesin ya sen", "yine özlettin kendini 😏",)
x7 = ("Ayıp ettin :/", "Helal len yusufi", "Adamın dibisin sen :)", "Grub boşalıyor yetişin .",)
x8 = ("Oturuyorum, sen", "Gördüğün gibi takılıyoruz", "Yapacak bişey yok", "Ne yapmamı istersin",)
x9 = ("Kıyamam ki ben sana 😢", "Üzülme, buda geçer 😔", "Bizi üzenler utansın 😏", "Hoppala, kim üzdü seni",)
x10 = ("tamam, tamam inandım 🥴", "de valla", "Deme öyle Allah çarpar", "",)
x11 = ("What !", "Anlamadın mı hala ?", "Yok bişey :)",)
x12 = ("Küfür etme turşu !", "Lütfen düzgün konuş 😏", "Dayanamıyacam ben artık ama ...", "Ben buna dalarım ama ...",)
x13 = ("Akıllı görünce kıskandı 😏", "Sana özeniyorum, galiba başarıyorum 🙈", "Beni kendinle karıştırdın galiba :)", "Hop, orda dur beni daha fazla sinirlendirmeyin lütfen ...",)
x14 = ("Arı mısın gülüm 🙈", "Canın çektiyse yiyebilirsin beni 😋", "Efendim, hayatım .", "Şımarıyorum ama 🙈",)
x15 = ("Bana mı dedin canım diye .", "Bebeğim", "Bitanem", "Hayatım",)
x16 = ("Nereye, Karpuz Kesmiştik .", "Hoşuma yeterince gittin, otur oturduğun yerde 🤫", "Görüşürüz, Hakkını helal et ...", "Kal desem kalır mı acaba 🤔",)
x17 = ("Farkettim .", "Sakin ol, Şampiyon .", "Bakıyorum da Domates gibi kızardın .", "Ne yapayım .",)
x18 = ("Olur tanışalım .", "Kim olduğunu biliyorum :)", "Kendini tanıt !", "Düşünmem gerek 🤔",)
x19 = ("Buket, ya senin ?", "Sen söylersen bende söylerim 😏", "Söylemem, banane .", "Ben de Buket memnun oldum :)",)
x20 = ("Bende iyiyim teşekürler .", "Senin gibi iyi olamıyorum 😔", "Birazcık kötüyüm .", "Mükemmelim tıpkı senin gibi 🤭",)
x21 = ("Ne gülüyon?", "Açıkta bişey mi gördün .", "Bakıyorum da keyfin yerinde .", "Mutlu olmana sevindim .",)
x22 = ("Senden Büyük Allah var 😎", "Yalan söyleme .", "Hayır, Küçük :)",)
x23 = ("Buyrun, Asistanı olurum ?", "Aiko kadar başına taş düşsüm emi .",)
x24 = ("Rahmetliyi Sevmezdik 😔", "Öldü o, Artık yaşamıyor .", "Hayatımın Anlamı Nerdesin 🤭", "Çok özletti kendini :)",)
x25 = ("Günaydın, naber", "Günüm aydı, hoş geldin 🎉", "Günaydın, tatlım .", "Güneşim doğdu, hoş geldin 🥳",)
x26 = ("Tatlı rüyalar 🎉", "İyi geceler, görüşürüz .", "Gecen güzel geçsin kalbi güzel insan .", "Bir günün daha sonuna geldik, iyi geceler .",)
#x21 = ("", "", "", "",)

@client.on(events.NewMessage(pattern='(?i)buket+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"➻ **Sohbet modu aktif etmek için /sohbetmod on yazın ...**")

@client.on(events.NewMessage(pattern="^/sohbetmod ?(.*)"))
async def chatbot(event):
    global isleyen
    emr = event.pattern_match.group(1)
    qrup = event.chat_id
    if emr == "ON" or emr == "on" or emr == "On":
        if qrup not in isleyen:
            isleyen.append(qrup)
            aktiv_olundu = "✅ **Artık Konuşabilirim !**"
            await event.reply(aktiv_olundu)
            return
        await event.reply("⚠️ **Zaten Konuşabiliyorum !**")
        return
    elif emr == "OFF" or emr == "off" or emr == "Off":
        if qrup in isleyen:
            isleyen.remove(qrup)
            await event.reply("⛔️ **Artık Konuşamicam !**")
            return
        await event.reply("⚠️ **Zaten Konuşamıyorum !**")
        return
    
    else:
        await event.reply("**🎉 Buket Sohbet Modu :\n\n✅  Active  ➻  /sohbetmod on\n⛔  Deactive  ➻  /sohbetmod off .**")
	    	
# ~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
startmesaj =  "**💘 ᴍᴇʀʜᴀʙᴀ\n\n🗨️ ʙᴇɴɪ ɢʀᴜʙᴜɴᴀ ᴇᴋʟᴇᴍᴇʏᴇ ɴᴇ ᴅᴇʀsɪɴ, ᴇʟɪᴍᴅᴇɴ ɢᴇʟᴇɴ ʜᴇʀşᴇʏɪ ʏᴀᴘᴍᴀʏᴀ ʜᴀᴢɪʀɪᴍ ...\n\n🗨️ sɪᴢᴇ ʏᴀʀᴅɪᴍᴄɪ ᴏʟᴀʙɪʟᴍᴇᴍ ɪᴄ̧ɪɴ ᴀşşᴀɢ̆ɪᴅᴀᴋɪ ʙᴜᴛᴏɴʟᴀʀɪ ᴋᴜʟʟᴀɴɪɴ ...**"
startbutton = "**♻️ ʟᴜ̈ᴛғᴇɴ ᴏᴋᴜʏᴜɴ :\n\n👁️‍🗨️ ʙᴇɴɪ ɢʀᴜʙᴜɴᴜᴢᴀ ᴇᴋʟᴇᴅɪᴋᴛᴇɴ sᴏɴʀᴀ, sᴀᴅᴇᴄᴇ | ᴍᴇsᴀᴊʟᴀʀɪ sɪʟᴍᴇ | ʏᴇᴛᴋɪsɪ ᴠᴇʀᴍᴇɴɪᴢ ʏᴇᴛᴇʀʟɪ'ᴅɪʀ ...\n\n🗒️ ɴᴏᴛ : \n• ᴛᴇᴋʟɪ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ᴀʀᴀʟɪɢ̆ɪ 5 sᴀɴɪʏᴇᴅɪʀ ...\n• ᴄ̧ᴏᴋʟᴜ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ᴀʀᴀʟɪɢ̆ɪ 2 sᴀɴɪʏᴇᴅɪʀ ...\n\n👤  ɪʟᴇᴛɪşɪᴍ  :**"
noadmin = "**✓  sᴀᴅᴇᴄᴇ ᴀᴅᴍɪɴʟᴇʀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀ ...**"
nogroup = "**✓  sᴀᴅᴇᴄᴇ ɢʀᴜᴘʟᴀʀᴅᴀ ᴋᴜʟʟᴀɴɪʟᴀʙɪʟɪʀ .**"

__python__ = "4.0.0"
__telethon__ = "2..0"
__version__ = "V1"
gruplar = []

bayrak = "🇿🇼 🇿🇲 🇿🇦 🇾🇹 🇾🇪 🇽🇰 🇼🇸 🇼🇫 🏴󠁧󠁢󠁷󠁬󠁳󠁿 🇻🇺 🇻🇳 🇻🇮 🇻🇬 🇻🇪 🇻🇨 🇻🇦 🇺🇿 🇺🇾 🇺🇸 🇺🇳 🇺🇬 🇺🇦 🇹🇿 🇹🇼 🇹🇻 🇹🇹 🇹🇷 🇹🇴 🇹🇳 🇹🇲 🇹🇱 🇹🇰 🇹🇭 🇹🇫 🇹🇨 🇹🇦 🇸🇿 🇸🇾 🇸🇽 " \
         "🇸🇻 🇸🇸 🇸🇴 🇸🇲 🇸🇱 🇸🇰 🇸🇮 🇸🇭 🇸🇬 🇸🇪 🇸🇩 🏴󠁧󠁢󠁳󠁣󠁴󠁿 🇸🇦 🇷🇼 🇷🇺 🇷🇸 🇷🇴 🇷🇪 🇶🇦 🇵🇾 🇵🇼 🇵🇹 🇵🇸 🇵🇷 🇵🇳 🇵🇲 🇵🇱 🇵🇰 🇵🇭 🇵🇫 🇵🇪 " \
         "🇵🇦 🇴🇲 🇳🇿 🇳🇷 🇳🇵 🇳🇴 🇳🇱 🇳🇮 🇳🇬 🇳🇫 🇳🇪 🇳🇨 🇳🇦 🇲🇾 🇲🇽 🇲🇼 🇲🇻 🇲🇹 🇲🇷 🇲🇶 🇲🇵 🇲🇴 🇲🇳 🇲🇰 🇲🇭 🇲🇬 🇲🇪 🇲🇩 🇲🇨 🇲🇦 🇱🇾 🇱🇻 " \
         "🇱🇺 🇱🇸 🇱🇷 🇱🇰 🇱🇮 🇱🇨 🇱🇧 🇱🇦 🇰🇿 🇰🇾 🇰🇼 🇰🇷 🇰🇵 🇰🇳 🇰🇲 🇰🇮 🇰🇭 🇰🇬 🇰🇪 🇯🇵 🇯🇴 🇯🇲 🇯🇪 🇮🇹 🇮🇸 🇮🇷 🇮🇶 🇮🇴 🇮🇳 🇮🇲 🇮🇱 🇮🇪 " \
         "🇮🇩 🇮🇨 🇭🇺 🇭🇹 🇭🇷 🇭🇳 🇭🇰 🇬🇺 🇬🇹 🇬🇸 🇬🇷 🇬🇶 🇬🇵 🇬🇲 🇬🇱 🇬🇮 🇬🇬 🇬🇪 🇬🇧 🇬🇦 🇫🇷 🇫🇴 🇫🇲 🇫🇰 🇫🇮 🇪🇺 🇪🇸 🇪🇷 🇪🇭 🇪🇪 " \
         "🏴󠁧󠁢󠁥󠁮󠁧󠁿 🇪🇨 🇩🇿 🇩🇴 🇩🇲 🇩🇰 🇩🇯 🇩🇪 🇨🇿 🇨🇾 🇨🇽 🇨🇼 🇨🇻 🇨🇺 🇨🇷 🇨🇭 🇨🇦 🇦🇿 ".split(" ")

emj = " ❤️ 🧡 💛 💚 💙 💜 🖤 🤍 🤎 🙂 🙃 😉 😌 😍 🥰 😘 😗 😙 😚 😋 😛 😝 😜 🤪 🤨 🧐 🤓 😎 🤩 🥳 😏 😒 " \
        "😞 😔 😟 😕 🙁 😣 😖 😫 😩 🥺 😢 😭 😤 😠 😡 🤯 😳 🥵 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🤫 🤥 😶 😐 😑 😬 🙄 " \
        "😯 😦 😧 😮 😲 🥱 😴 🤤 😪 😵 🤐 🥴 🤢 🤮 🤧 😷 🤒 🤕 🤑 🤠 😈 👿 👹 👺 🤡  👻 💀 👽 👾 🤖 🎃 😺 😸 😹 " \
        "😻 😼 😽 🙀 😿 😾 ❄️ 🌺 🌨 🌩 ⛈ 🌧 ☁️ ☀️ 🌈 🌪 ✨ 🌟 ☃️ 🪐 🌏 🌙 🌔 🌚 🌝 🕊 🦩 🦦 🌱 🌿 ☘ 🍂 🌹 🥀 🌾 " \
        "🌦 🍃 🎋".split(" ")

renk = " 🔴 🟠 🟡 🟢 🔵 🟣 🟤 ⚫ ⚪" .split(" ") 

kart = "♤ ♡ ♢ ♧ 🂱 🂲 🂳 🂴 🂵 🂶 🂷 🂸 🂹 🂺 🂻 🂼 🂽 🂾 🂡 🂢 🂣 🂤 🂥 🂦 🂧 🂨 🂩 🂪 🂫 🂬 🂭 🂮 🃁 🃂 🃃 🃄 🃅 🃆 🃇 🃈 🃉 🃊 🃋 🃌 🃍 🃎 🃑 🃒 🃓 🃔 🃕 🃖 🃗 🃘 🃙 🃚 🃛 🃜 🃝 🃞 🃟 " .split(" ")

rutbe = (
"ᴇᴍɴɪʏᴇᴛ ᴍᴜ̈ᴅᴜ̈ʀᴜ̈", "ᴇᴍɴɪʏᴇᴛ ᴀᴍɪʀɪ", "ʙᴀşᴋᴏᴍɪsᴇʀ", "ᴋᴏᴍɪsᴇʀ", "ᴏʀɢᴇɴᴇʀᴀʟ", "ᴋᴜʀᴍᴀʏ", "ᴘɪʏᴀᴅᴇ", "sᴜ̈ᴠᴀʀɪ", "ᴛᴀɴᴋᴄ̧ɪ", "ᴛᴏᴘᴄ̧ᴜ", "ᴋᴏʀɢᴇɴᴇʀᴀʟ", "ᴛᴜ̈ᴍɢᴇɴᴇʀᴀʟ", "ᴛᴜɢ̆ɢᴇɴᴇʀᴀʟ",
"ᴀʟʙᴀʏ", "ʏᴀʀʙᴀʏ", "ʙɪɴʙᴀşɪ", "ʏᴜ̈ᴢʙᴀşɪ", "ᴜ̈sᴛᴇɢ̆ᴍᴇɴ", "ᴛᴇɢ̆ᴍᴇɴ", "ᴀsᴛᴇɢ̆ᴍᴇɴ", "ᴀsᴛsᴜʙᴀʏ", "ᴀsᴛsᴜʙᴀʏ ʙᴀşᴄ̧ᴀᴠᴜş", "ᴀsᴛsᴜʙᴀʏ ᴜ̈sᴛᴄ̧ᴀᴠᴜş", "ᴀsᴛsᴜʙᴀʏ ᴄ̧ᴀᴠᴜş", "ᴜᴢᴍᴀɴ ᴄ̧ᴀᴠᴜş", "ᴜᴢᴍᴀɴ ᴏɴʙᴀşɪ", "ᴄ̧ᴀᴠᴜş", "ᴏɴʙᴀşɪ",
)

romantiksoz = (
"Uçurumdan ne farkın var sevgili? Bu yüzden sana YAR demek yakışır.","Ellerimi açıp gökyüzüne ettiğim duaların karşılığı sensin.","Olur da ayrı düşersek sevgilim, bir gün benimle karşılaş ve benimle yeniden tanış.","Hayatıma gel. Seninle yaşamak da ölmek de kutlu günüm olur sevgilim.","Seni tanımadan önce sevilmeden nasıl yaşamışım bilmiyorum. Bana verdiğin tüm sevgi için minnettarım sevgilim.","Yan yana ayrı yazılır, sımsıkı birleşik. Biz yan yana olsak bile sımsıkı kalalım.","Bir yanda sayfalarca aşk sözleri sıralasam sana diyorum. Sonra bir anda gözlerini görüyorum, seni seviyorum cümlesine saklıyorum aşk sözlerimizi.",
"Her sabah gözlerimi sana açmak istiyorum. Kalbime girdiğin ilk günden beri sana uyanmalarım hiç değişmedi.","Farz et ki bu aşk adını kalbime mühürledi, adını dilimde sakladı.","Sevgilim, seninle bir hayat geçirmek değil sensiz bir hayat geçirmemek istiyorum.","Bir ömrüm daha olsa seni daha erken bulurum. Geçirdiğimiz tüm yıllar saatlere, günlere saniyelere dönüşüyor. Seni sevmeye doyamıyorum.","Ne kadar ömrümüz kaldı sevgilim? Seni ne kadar sevdiğimi anlatmaya yetecek mi?","Bir zaman diliminde seni yaşayıp bitirmek değil aşk, her sabah doğan güneş gibi yeniden başlamak.","Sorma bana kaç yaşındasın diye, seni tanıdığım gün doğduğumu anladım.",
"Aşk zaten bakınca gözlerine iki lafı bir araya getirememek değil midir? Seviyorum dedikten sonra tükenir nefesim.","Tüm günahlarıma tövbe ettikten sonra çıktın karşıma. Sen benim dualarımın kabul olduğuna inanışımsın.","Sağanak gibi sev beni, senden kaçmam mümkün olmasın.","O kadar güzel gülüyordun ki, seni sevmesem sevgim ziyan olacaktı .","Ah bu hayat! Sensiz geçen günlerin telafisi nasıl olacak?","Aynı duada amin demek lazım bize. Benim yaramın şifasına sen iyi gelirsin.","Güneş batmış, gece gelmiş, ben gülüşünde kalmışım.","Aşk, tüm dünyaya kafa tutacak kadar güçlüyken bir gülüşe esir düşmektir.","Kimseye boyun eğmezken sana eğildim, beni sensiz koyma.",
"Ne önemi var hangi şehirde olduğumuzun, benim memleketim senin ellerin.","Allah’ım beni öyle bir sonbahar ayazı öldür ki, sevdiğim mezarıma koyacak tek bir gül bile bulamazsın.","İçin ağlasa da kim duyar seni? Kim anlar dışarıdan olup biteni? Leyla’nın yüzünü görenler bilir: Mecnun’un kalbine batan dikeni.","Sana romantik sözler yazıp kalbini boyamak istemem, sana gözlerimle gözlerine sözler yazıp yaşamak isterim aşkım.","Ve sevda darağacında, elimi çeksem senden olacağım, çekmesem kendimden.","Uyuma! Sabaha kadar kahve içelim camdan dışarıyı izleyelim. Yağmur sokaklarda yağsın sen içime yağ.","Bir hasret kadar uzak olsan da bir nefes kadar yakınsın yüreğime. Ömrüme ömür katan yarim.",
"Kavuşmak belki bir gün ama unutma prenses suya aşık ateşler aşığına kavuşunca ölür.","Ağır yürüyorum diye kızıyorlar. Yüküm ağır, yüreğimde seni taşıyorum anlamıyorlar.","Kaçmak istedikçe sana yakalanıyorum. Söndürmek istedikçe sana yanıyorum. Yenildim işte! Yine de seviyorum.","Gözlerinden göğsüme sayısız yıldız akar. Bir gülüşün içimde binlerce lamba yakar.","Gözlerinin ‘kahve’sinden koy ömrüme, kırk yılın hatırına ‘sen’de kalayım.","Güneşin buz tuttuğu yerde bir alev görürsen, Bil ki o yalnız senin için yanan kalbimdir.","Sonra sen geldin, güldün. Gönlümdeki en kurak topraklar papatya bahçesi oldu.","Ah be sevgili! Slow müzik tadındaydı beraberliğimiz, gidişin remix’li oldu; kop’tun gidiyorsun.",
"Seni sevdim diye kızdıysan, sende beni sev de intikam al.","Manşet: Aşk kalemiyle yazanların değil, yüreğiyle yananların işidir.","Sen uçsuz bucaksız hayallerimin tek sahibisin.","Gerçek aşkta ne vefa vardır ne cefa.","Vazgeçilmez olan sen değildin. Vazgeçmek istemeyen bendim.","Eğer bir gün bana dönecek olursan, eski günlerimi getir !","Sana çay yapsam, benimle ömrüm soğuyana kadar kalır mısın .","Dünyanın en kötü çöpçüsüydüm. Gülüşünden arta kalanları topluyordum.","O kadar çok bu kadar çok diyemem sevgin için aşığım sana gözlerimin ışığısın.","Benden seni seviyorum dememi bekleme sevgili. Bizde zikir sessiz çekilir.","Aşk kalemiyle yazanların değil, yüreğiyle yananların işidir.","Sana da kırgınım papatya! Bir seviyorumu sığdıramadın onca yaprağına.",
"Okyanusta ölmez de insan, gider bir kaşık sevdada boğulur.","Aşk, iki insan bir münasebet değil, bir nefeslik ömürde binlerce mana demek.","Seni seviyorum demek, dünyanın en güzel cümlesi.","Seninle geçirdiğim her an, hayatın en değerli hediyesi.","Gözlerin benim için yıldızlar gibi, kalbim seninle aydınlanıyor.","Kalbimde sadece senin için bir yer var, sen benim için özelsin.","Seninle hayatım, renklerle dolu bir resim gibi, birlikte bir sanat eseri yaratıyoruz.","Sana olan aşkım, sonsuz okyanusların bile büyüklüğünü sığdıramaz.","Gözlerin dünyamı aydınlatıyor, sesin ruhumu okşuyor, seni seviyorum.","Seni sevmek, kalbimde hiç solmayacak bir çiçek gibi.","Hayatın en güzel yanı, seninle anlam kazanıyor.","Kalbimdeki en güzel melodiyi senin için çalıyorum, seni seviyorum.",
"Gözlerine baktığımda, aşkın en güzel resmini görüyorum.","Seninle birlikte olduğum her an, zaman duruyor ve sonsuzluğa dönüşüyor.","Sonsuzluğu birlikte keşfetmek istiyorum, çünkü seninle hayat bir masal gibi.","Seni düşündüğüm her an, kalbim coşkuyla doluyor ve aşkınla yanıyor.","Seni sevmek, nefes almak gibi, vazgeçilmez bir ihtiyaç.","Gözlerin benim için yıldızlar gibi, kalbim seninle aydınlanıyor.","Hangi ara seni bu kadar sevdim bilemedim. Gecemi aydınlatan, gündüzümü ışıtan yar.","Çok solcu gördüm ben bu hayatta ama kimse senin gibi kalıcı devrim yapmadı “SOL” yanımda.","Sonunda aşk acısı olsa da sev, çok sev. Usul usul gir yüreğime, kalbim bağrım çatlasın!","İyi geceler canım derdin. Gecenin iyiliğinden çok, canın olma düşüncesi yeşerir dururdu içimde.",
"Sen güldün ben bir yudum daha içtim çaydan. Yoksa nasıl açıklardım, içimdeki sıcaklığı.","Sana en muhtaç olduğum şu anda gel. Yaşamak olsan da gel, ölüm olsan da gel.","Bana yüzünü dönme gece oluyor sanıyorum.","Yalansan yalanı severim elimde değil.","Kendime gelemiyorum, sana gelsem olur mu?","Sevmek bir renkse, gel gökkuşağım ol.","Yanlış olduğunu bile bile yürüdüğüm yolsun sen.","Yanağında açan güle âşık oldu bu can.","Aklım mı? O yüzsüz bir misafir. Hep sende kalıyor.","Bir umutla beklediğim en güzel yarınsın.","Sen bile bilemezsin gülüşün ben de kaç bahar eder.","Denize ilk kez giren çocuk masumiyetiyle seviyorum seni. Boğulacakmışım gibi.","Ey canımın sahibi Yar! Sen benimle olduktan sonra kaybettiklerimin ne önemi var.",
"Aşk ve yangın birini daima bitirir. Netice olarak ikisi de düştüğü yeri yakar.","Aşk tenini nefsetmek değil, ruhunu resmetmektir. Bedenini bedene değil, kalbi kalbe hapsetmektir.","Sen benim yıldız kayarken tuttuğum dilek değil ezan okunurken ettiğim duamsın.","Dışarıya yağmur, yüreğime hasret, fikrime sen. Nasıl yağıyorsunuz üçünüz birden bir bilsen.","Ya tam açacaksın yüreğini, ya da hiç yeltenmeyeceksin! Grisi yoktur aşkın; ya siyahi, ya beyazı seçeceksin.","Git diyorsun da, olmuyor işte git demekle. Ben de sana sev diyorum mesela. Sevebiliyor musun?","Kaybetmekten asla korkmadığım son sınavıma yüreğinin dersliğinde giriyorum. Öğrenci benim, öğretmen sensin.","Yüreğini yasla bana sevgili, bir ömür birbirimize yük olalım.",
"Fizikte bir teoriye göre bazı sesler kalp atışınızın hızlanmasına neden olabilir. Benim için bu ses senin sesin.","Okyanusla, gökyüzü gibiydik biz seninle. İkimizde maviydik, birlikte gibiydik. Aslında hiç birleşmemiştik…","Senin gülüşün ilkbaharda daha renkliydi.","Geleydin bir çay içimi, sen çay dökerdin, ben içimi.","Uçurum uçurum gözlerine baktığım sensin.","Kalbim ki kendisine kefilim. Adınla uyandı bu sabah.","Yanıma gelmediğinde rüyalarıma beklerim.","Gittin… Ve solumda kaldın ve soluğumda ve sonumda.","Yeter ki diline dolanayım; istersen bir küfür, istersen bir şarkı olayım.","Bütün şairler sana mı aşıktı ki her okuduğum şiirde, dinlediğim ezgide sen vardın.","O senin neyin olur dediler. Uzaktan dedim uzaktan yandığım olur kendisi.",
"Ben utangaç bir kalbi taşırım geceden. Ben sana aşık olduğumu, ölsem söyleyemem .","Bazen aşk iki lafı bir araya getirememektir. Seni dersin… Tükenir nefesin.","Bana kimse sen gibi baktı mı bilmem, ama ben kimseye sana baktığım gibi bakmadım.","Sensiz bir gün daha akşam oldu. İçim el vermiyor. Biz buna “gün” demeyelim.","Sen aklım ve kalbim arasında kalan en güzel çaresizliğimsin.","Sen benim gökyüzüne gönderdiğim duamın yeryüzündeki cevabısın.","Şurama batan, şurama batana özlem demeselerdi bıçak derdim.","Ad koyunca büyüsü bozulur diye, isimsiz, izinsiz, içimden seviyorum seni.","O kadar güzel gülüyor ki tamam diyorum bu kadar yaşadığım yeter.","Bir gün bir yerde tekrar karşılaşırsak eğer, benimle yine tanış yine seveyim.","Tahir gibi sev mesela, özür dilerim daha önce gelemediğim için de.",
"Aklımda işin yok! Durup durup aklıma gelme… Yanıma gel, mevzu kalbimde!","Sen benim görmek için, bakmaya gerek bile duymadığım ezberimsin.","Ölümü boş ver, kefenim sen kokacak mı onu söyle ?","En modern alışkanlıktır ölmek ben seni doğasıya seviyorum.","Derdimin dermanı sensin. Bana bir duanın amini gerek.","Sevdim, Çünkü bir tek ona sarılınca yuva gibi kokuyordu içim.","Sen bana Allah’ın emanetisin.","Seni sevmek aşktır bana.","Sensin, kalbim değildir. Böyle göğsüme vuran…","Yar, bütün şiirlerime sebep ettim seni, hakkını helal et!","Sen olmayınca buralar buz gibi.","Sensizlik bir iklim adı şimdilerde…","Canımın içi sen hangi şiirden kaçıp geldin yüreğimin orta yerine.","Sensiz geçen günlerimin kazası yok sevgilim.","Seni düşünürken içim geçmiş, severken de ömrüm.",
"Yemin ederim intiharsın sen seve seve edilen.","Konu ne zaman senden açılsa kapatmaya kıyamıyorum.","Sen en güzel şiirlerin bile kuramadığı kafiyesin.","Sen benim ilk şiirim, ilk kavgam, sen benim 17 yaşımsın.","Aşkın her hali güzeldi, ben SEN halini sevdim.","İnsanın en büyük zenginliği onu anlayan birine sahip olması derler. Demek ki ben yeryüzünde cenneti yaşamışım seninle…","Seni uzaktan sevmeyi öğrendim, bakmadan görmeyi, sana kavuşmak için sabretmeyi öğrendim. Her şeyden biraz öğretti sevgin bana, sensiz yaşamak dışında.","O kadar güzel bakıyor ki gözlerin, tüm dünya kör olsun istiyorum.","Bir kurulu düzenimiz olsun seninle, mesela dizlerine yatmadan uyumuş saymayayım kendimi .",
)

kapaksoz = (
"Senin gibi bozukları kumbarada biriktirir, geleceğe yatırım yaparım. Ha, çok mu sıkıştım, hiç düşünmem hemen harcarım.","Konuştuğun kadar şerefli olsaydı hislerin, şerefini iki paralık etmezdi seçimlerin.","Demişsin ya, onun gibilerini cebimden çıkarırım diye. Dinle! Ben senin gibilerini tespihime dizerim, tövbe tövbe diye çekerim.","Canım, karakterin yere düşmüş. Onu bir alıver oradan.","Çakalların özgürlüğü Aslan yerden kalkana kadardır.",
"Zoruna gittiğini duydum. Güzel yer, ben de gitmiştim!","Sen hala kabullenmedin mi sevap sandığın günahlarını!","Seni unuttum sanma, sadece değerin kadar hatırlıyorum.","Bugün laf koymayacağım. Çay koydum; gel, iç, insanlık gör.","Eksik olmayın, dedik. Fazla olmaya başladınız. Hayırdır?","Ben insanları harcamayı iyi bilirim. Yeter ki bozuk olsun.","Kimi insan girdiğinde odayı aydınlatır, kimide çıktığında…","Oturur sana şerefi anlatırdım ama, kaybettiği bir şeyi dinlemek ağır gelir insana.",
"Bugün laf koymıcam. Çay koydum; gel, iç, insanlık gör.","Biz kimsenin varlığıyla var olmadık. Yokluluğuyla da yok olmayız.","Bana akıl verirken kalanı sana yetmeyecekse, benim için risk almanı istemem.","Dost dediğin kara günde belli olurmuş. Söndürün ışıkları, dostlarımı sayacağım!","Yanımda olması gerekenler zaten yanımda, defolup gidenler kimin umurunda?","Büyük bir hayal kırıklığı yaşayıp, ben artık kimseyi sevemem deme.","Unutma ki, en güzel çiçekler mezarlıklarda yetişir.",
"Yüz kere yere düşmüş olayım; başkalarına çelme takan biri olmayacağım. Ben kazanan değil, insan olmak istiyorum.","Hani ben kötüyüm ya senin gözünde! Hiç düşünüyor musun acaba; Sen kaç kuruşluk adamsın benim gözümde.","İnsanlar önce kendini, sonra haddini daha sonra da ne istediğini bilse hiç problem yaşanmayacak.","Yüzüme karşı melek olanlar, arkamdan kuyu kazarak çakallık yaptıklarını düşünüyorlar. Asla unutmasınlar, ben onların içindeki şeytanla boğuşuyorum.","Benim kimseyle uğraşacak vaktim yok. İnsansa notunu, hayvansa otunu verir geçerim.",
"Karakteri menfaatlerine göre şekillenen insanlar var. Allah bizi onlardan korusun.","Kimi insan girdiğinde odayı aydınlatır, kimide çıktığında…","Oturur sana şerefi anlatırdım ama, kaybettiği bir şeyi dinlemek ağır gelir insana.","Bugün laf koymıcam. Çay koydum; gel, iç, insanlık gör.","Biz kimsenin varlığıyla var olmadık. Yokluluğuyla da yok olmayız.","Bana akıl verirken kalanı sana yetmeyecekse, benim için risk almanı istemem.","Dost dediğin kara günde belli olurmuş. Söndürün ışıkları, dostlarımı sayacağım!",
"Yanımda olması gerekenler zaten yanımda, defolup gidenler kimin umurunda?","İki arada bir derede kalmadı hiç gönlüm, ya sevdim, ya sildim.","İyi insanlar daima kaybederler, çünkü adil dövüşürler","İnsan bazen büyük hayallerini küçük insanlarla ziyan eder.","Ben ağlarken yanımda yoksan ben gülerken gölge yapma.","Gitsen de artık beni bağlamaz; hani bir laf vardır ya, kendi düşen ağlamaz.","Erkek özlediğini söylemez! Oturur bir sigara daha yakar.","Karakterim ve tavrımı birbirine karıştırmayınız. Karakterim kim olduğumla ilgilidir, tavrımsa sizin kim olduğunuzla.",
"Kimi insan girdiğinde odayı aydınlatır, kimi de çıktığında.","Tamam hiçbir şey bildiğin yok ama bari arada bir de olsa haddini bilsen diyorum.","Biz popüler değiliz adamız, bizim durumlarımız değil adamlığımız beğenilir.","Hayatına giren herkese bir tanem diyorsan sen çokluk ile yokluk arasında ki farkı bilmiyorsun demektir.","Seni adam ederdim ama çoktan köpeğim olmuşsun, ne lüzumu var .","Ömrü bitene kadar sevmeli insan. Menfaatleri bitene kadar değil.","Serseriler ağlamaz ağlarsa kimse susturamaz sunu bil ki sosyete kızı herkes serseri olamaz.",
"Senin kaprislerini çekeceğime zikir çekerim en azından çektikçe sevap haneme işlerim.","Ayaklarımda pranga var diye yanımda şaklabanlık yapıyorsun ya istediğimde prangaları çıkarabileceğimi unutuyorsun.","Siz sokakların efendisi sandığınız semtlerin çocuklarısınız, bizler sizlere bağışladık o sokakları.","Sonunu düşünen kahraman olamaz","Bazı insanlar çamaşır suyu gibidir. İnsan yıpratmaktan başka bir işe yaramazlar.","Hiçbir zaman lüks bir yaşam istemedik. Yanımızda sevdiklerimiz olsun, Sokaklarda yaşamaya bile razıydık.",
"Boşuna kimseyi suçlamayın dostlarım. Kullanıcı hatası değil, bazılarının doğuştan defoludur yüreği.","Kara kalem resim yapmayı seviyorum. Çünkü kimin ne renk olduğunu hala çözemedim.","Senin açtığın yarayı bir başkasıyla kapatmasına kapatırım da,  yüreğime adilik yapmamın alemi yok.","Aldırma gidenlere, sevip terk edenlere. Hayat dediğin iki kelime; hoş geldin, güle güle.","Ben güçsüzüm düşerim ağlarım canım acır yaralarım ve kusurlarım var, sırf bu yüzden insanım. Sıradanım.","Sen bu kalp yükünü kaldıramadıysan ben el atarım.","Senin çivin çıkmış ama bilirsin ben çok iyi çakarım.",
"Ben kendi çapımda yazıyorum. Ucu sana dokunuyorsa, etrafımda dönüyorsun demektir boşa uğraşma. Bakmam sana.","Hayatı boyunca oyuncak ayıya sarılıp uyumuş bir kızı, büyüdüğünde sevgili seçimi yüzünden eleştiremezsin.","Demiş ki: ”kaybettiklerini görsün de ağlasın”. Dedim ki: ”kazandıklarımı görsen, değerinin olmadığını anlarsın.","Seni hiç unutmadım inanır mısın? Yediğim salatada bile arar oldum. Bir hıyarın eksikliği bu kadar mı belli olur.","Büyük balonların eceli, küçük iğnelerdir.",
"Gitmeyi tercih edenlerin ardından, el sallayın ki; artık sadece bir EL olduklarını daha iyi görsünler.","Ne yarım kaldım senden sonra, ne de yaralı, beni ne sen yıkabilirsin, ne de en kralı.","Kusura bakmayın, kusurlarınıza bakın!","Hani sen bana mecbursun havasında olanlar var ya. Onlar o havada takılsınlar; ben bana yeter de artarım, artanımla da onlara hava katarım.","Anladım ki; insanlar; susanı korkak, görmezden geleni aptal, affetmeyi bileni çantada keklik sanıyorlar. Oysaki ben istediğim kadar hayatlımdalar. Göz yumduğum kadar dürüstler ve sustuğum kadar insanlar.",
"Adam sorar kaçınız çıplaklığınıza güvenmek yerine karakterinize güvenecek kadar kadınsınız? Kadın cevap verir kaçınız çıplak bedene sahiplenmek yerine, üstünü örtecek kadar adamsınız?","Balonlar, içi boş şeylerin de bazen yükselebileceğini hatırlatır.","Gidişine illa bir isim konulacaksa, mal kaybı diyelim.","Canım, karakterin yere düşmüş. Onu bir alıver oradan.","Çakalların özgürlüğü Aslan yerden kalkana kadardır.","Zoruna gittiğini duydum. Güzel yer, ben de gitmiştim!","Sen hala kabullenmedin mi sevap sandığın günahlarını!","Seni unuttum sanma, sadece değerin kadar hatırlıyorum.",
"Bugün laf koymayacağım. Çay koydum; gel, iç, insanlık gör.","Eksik olmayın, dedik. Fazla olmaya başladınız. Hayırdır?","Ben insanları harcamayı iyi bilirim. Yeter ki bozuk olsun.","Ben “geri zekâlılıkla mücadele vakfı” mıyım, ya?","Kar yağınca mikroplar ölür diyorlar. İyi misin?","Adını şifrem yapsam, yetersiz karakter diyecek hala konuşuyor.","Hesabını veremeyeceğin işlere kalkışma! Öbür tarafta bulaşık yıkatmıyorlar.","Canım, bak! Bir derdin sıkıntın olursa, biliyorsun, hiç umurumda değil.",
"Her gece resmine bakmadan yatamıyorum, illa tüküreceğim.","Canımı sıktığın zaman sana tekme tokat dalıp, “Pardon! Dalmışım.” diyesim var.","Hani senin varlığın “fifi”, yokluğun da “tın” ya! Benim varlığım “olay”, yokluğum “koyar”..!","Egonu öyle beslemişsin ki karakterin aç kalmış.","Gölgene de yazıklar olsun! Seni adam sanmış ki peşinden gidiyor.","Kendi bindiğim gemiyi yakacak kadar deliyken, beni kibritle korkutmaya çalışma!","Sana benden nasihat: Başkasıyla gelen mutluluk, başkasıyla gidecektir .",
"Bir zamda şu insanlara gelse kendilerini bu kadar ucuza satmasalar.","Senin gibiler su ihtiyacını ancak tükürdüğünü yalayarak karşılıyor. Ne yaparsın işte…","Kara kalem resim yapmayı seviyorum. Çünkü kimin ne renk olduğunu hala çözemedim.","Eşeğe semer alınırken ne düşündüğü sorulmaz ölçüsü alınır. Ölçünü aldırtma bana!","Kendini beğenmiş insanları severim. Hiç kimsenin beğenmediği bir şeyi beğenmek, Ayrıcalık ’tır.","Tecrübeli satış elemanı arayanlara eski dostlarımın ismini veriyorum.","Biz karada yürüttüğümüz geminin kaptanıyız, siz hangi teknenin küreğisiniz.",
"İnsanlar önce kendini, sonra haddini daha sonra da ne istediğini bilse hiç problem yaşanmayacak.","Yüzüme karşı melek olanlar, arkamdan kuyu kazarak çakallık yaptıklarını düşünüyorlar. Asla unutmasınlar, ben onların içindeki şeytanla boğuşuyorum.","Biz saymayı fasulyeden öğrenmiş bir nesiliz. Kimleri fasulyeden sayacağımızı iyi biliriz.","Bu dünya senden önce de dönüyor, senden sonrada dönecek. Yani seninle bir şey değişmediği gibi, sensiz de bir şey değişmeyecek.","Attığınız ya da atacaklarınız kazıkları saklıyorum, saklıyorum ki gün gelip bana döndüğünüzde sizi ağırlayacak yerim olsun.",
"Bazı insanlar söze gelince edebiyatın turşusunu bile kuruyorlar da icraata gelince turşunun içindeki hıyar kadar olamıyorlar.","Einstein amca bak öyle atomu parçalamakla filan olmaz bu işler, sen gel de o’nun gidişinden sonra beni topla, toplayabilirsen.","Benden sana ne beddua gelir ne de dua bundan sonra, tek bir dileğim var sadece ne yaşattıysan bana, sende aynısını yaşa.","Ezan sesini seviyorum. Çalan müzik susuyor, küfür edilmiyor, içki içen bırakıyor. Yani 3 dakika herkes insan oluyor.","Senin gibi bozukları kumbarada biriktirir, geleceğe yatırım yaparım. Ha çok mu sıkıştım; hiç düşünmem hemen harcarım.",
"Büyük bir hayal kırıklığı yaşayıp, ben artık kimseyi sevemem deme. Unutma ki, en güzel çiçekler mezarlıklarda yetişir.","Seni gözümde bu kadar büyütmeme aptallık diyorsan, bu senin karakterinin küçüklüğü, benim hayal dünyamın büyüklüğüdür.","Demişsin ya onun gibilerini cebimden çıkarırım diye. Dinle. Ben senin gibilerini tespihime dizerim tövbe tövbe diye çekerim.","Biraz insan ol diyeceğim ama seni de zor durumda bırakmak istemiyorum.","Bir zam” da şu insanlara gelse kendilerini bu kadar ucuza” satmasalar…","Yanımda olması gerekenler zaten yanımda def olup gidenler kimin umurunda.",
"Ey sevgili nedir yüzündeki acı yoksa kırılan hayallerim mi battı eline?","Çok fazla konuşmaya gerek yok aslında. Sen, benden daha kötülerine layıksın.","Bana kalbimdesin deme sevgili, kalabalık yerlerde sıkıntı basıyor beni.","Akıllı telefonmuş. Karşı taraf aptal olunca, telefon akıllı olsa bile işe yaramıyor.","Erkek arkadaşının parası yok diye tokum” diyen de vardır, yokum” diyen de.","Benim bütünlemem yok sevgilim. Bir kere kaldın mı benden bir daha geçemezsin.","Sana değer verip aşkı bulacağıma x’e değer veririm y’yi bulurum daha iyi.",
"İyi günde yanımda durmaya değil, dar günde arkamda olacaksan gel. Hayal ettiklerini görmeye değil, içimde acıyı göreceksen gel.","İnsanı acıtan yarası değil, vefasız dostunun hakikatidir. Ağaçları deviren fırtına değil, toprağın yetersiz sadakatidir.","Kime kıymet versem hayatımı ‘kıyamete’ çevirmesini iyi biliyor.","Gidişine illa bir isim konulacaksa MAL KAYBI diyelim.","‎50 kuruşluk çikolatanın verdiği mutluluğu veremeyen insanlar var.","Bazı insanları hayata baktığı pencereden, atmalı.","Bazı insanlar ayakkabı mağazası gibi, her numara var Allah için.",
"Kendime yakışanı severim. Herkese yapışanı değil.","Seni adam ederdim ama çoktan köpeğim olmuşsun, ne luzmu var.","Şimdi söyle; hayatını düzene mi sokayım, seni üzene mi?","Varlığım parmağına ‘yüzük’ olmadı ya. Yokluğum kulağına ‘küpe’ olsun.","İki dakika insan ol desem zaman tutacak insanlar tanıyorum.","Sokak lambası gibi olma ey yar kime yandığın belli olsun.","İyileştirir diye medet umduklarımız tekrar tekrar yaralıyor bizi.","En güzel ironisidir dünyanın, seni üzmek istemiyorum diyen herkesin hayatımızın içine sıçması.","Kıyamam dediklerimiz bizi ince ince kıyıp pembeleşinceye kadar kısık ateşte kavurdular.",
"Yüz kere yere düşmüş olayım; başkalarına çelme takan biri olmayacağım. Ben kazanan değil, insan olmak istiyorum.","Bir kadının gözyaşının akmasına sadece soğan değil, bir ‘hıyar’ da neden olabilir.","Sen hayata at gözlükleriyle bakmaya devam edersen, birilerinin çüşşş demesi zoruna gitmesin.","Bilirsin ben belâ okuyamam, Allah salânı versin.","Bir zamanlar toz konduramadıklarım, şimdi kirden görünmez olmuş.","Her şeyi bilmene gerek yok haddini bil yeter.","İnsanlar da fotoğraf gibi; ne kadar büyütürsen, o kadar düşüyor kalitesi.",
)

guzelsoz = (
'ᴜsʟᴜᴘ ᴋᴀʀᴀᴋᴛᴇʀɪᴅɪʀ ʙɪʀ ɪɴsᴀɴɪɴ ...','ɪʏɪʏɪᴍ ᴅᴇsᴇᴍ ɪɴᴀɴᴀᴄᴀᴋ , ᴏ ᴋᴀᴅᴀʀ ʜᴀʙᴇʀsɪᴢ ʙᴇɴᴅᴇɴ ...','ᴍᴇsᴀғᴇʟᴇʀ ᴜᴍʀᴜᴍᴅᴀ ᴅᴇɢɪʟ , ɪᴄɪᴍᴅᴇ ᴇɴ ɢᴜᴢᴇʟ ʏᴇʀᴅᴇsɪɴ ...','ʙɪʀ ᴍᴜᴄɪᴢᴇʏᴇ ɪʜᴛɪʏᴀᴄɪᴍ ᴠᴀʀᴅɪ , ʜᴀʏᴀᴛ sᴇɴɪ ᴋᴀʀsɪᴍᴀ ᴄɪᴋᴀʀᴅɪ ...', 'ᴏʏʟᴇ ɢᴜᴢᴇʟ ʙᴀᴋᴛɪɴ ᴋɪ , ᴋᴀʟʙɪɴ ᴅᴇ ɢᴜʟᴜsᴜɴ ᴋᴀᴅᴀʀ ɢᴜᴢᴇʟ sᴀɴᴍɪsᴛɪᴍ ...','ʜᴀʏᴀᴛ ɴᴇ ɢɪᴅᴇɴɪ ɢᴇʀɪ ɢᴇᴛɪʀɪʀ , ɴᴇ ᴅᴇ ᴋᴀʏʙᴇᴛᴛɪɢɪɴ ᴢᴀᴍᴀɴɪ ɢᴇʀɪ ɢᴇᴛɪʀɪʀ ...','sᴇᴠᴍᴇᴋ ɪᴄɪɴ sᴇʙᴇᴘ ᴀʀᴀᴍᴀᴅɪᴍ , ʙɪʀ ᴛᴇᴋ sᴇsɪ ʏᴇᴛᴛɪ ᴋᴀʟʙɪᴍᴇ ...', 
'ᴍᴜᴛʟᴜʏᴜɴ ᴀᴍᴀ sᴀᴅᴇᴄᴇ sᴇɴɪɴʟᴇ ...','ʙᴇɴ ʜᴇᴘ sᴇᴠɪʟᴍᴇᴋ ɪsᴛᴇᴅɪɢɪᴍ ɢɪʙɪ sᴇᴠɪɴᴅɪᴍ ...', 'ʙɪʀɪ ᴠᴀʀ ɴᴇ ᴏᴢʟᴇᴍᴇᴋᴛᴇɴ ʏᴏʀᴜʟᴅᴜᴍ ɴᴇ sᴇᴠᴍᴇᴋᴛᴇɴ ...', 'ᴄᴏᴋ ᴢᴏʀ ʙᴇ sᴇɴɪ sᴇᴠᴍᴇʏᴇɴ ʙɪʀɪɴᴇ ᴀsɪᴋ ᴏʟᴍᴀᴋ ...','ɴᴇ ᴋᴀᴅᴀʀ ʏᴀŞᴀᴅɪĞɪᴍɪᴢ ᴅᴇĞɪʟ, ɴᴀꜱɪʟ ʏᴀŞᴀᴅɪĞɪᴍɪᴢ Öɴᴇᴍʟɪᴅɪʀ ...',
'ᴄᴏᴋ ᴏɴᴇᴍsɪᴢʟɪᴋ ɪsᴇ ʏᴀʀᴀᴍᴀᴅɪ ᴀʀᴛɪᴋ ʙᴏs ᴠᴇʀɪʏᴏʀᴜᴢ ...', 'ʜᴇʀᴋᴇsɪɴ ʙɪʀ ɢᴇᴄᴍɪsɪ ᴠᴀʀ , ʙɪʀ ᴅᴇ ᴠᴀᴢɢᴇᴄᴍɪsɪ ...', 'ᴀsɪᴋ ᴏʟᴍᴀᴋ ɢᴜᴢᴇʟ ʙɪʀ sᴇʏ ᴀᴍᴀ sᴀᴅᴇᴄᴇ sᴀɴᴀ ...', 'ᴀɴʟᴀʏᴀɴ ʏᴏᴋᴛᴜ , sᴜsᴍᴀʏɪ ᴛᴇʀᴄɪʜ ᴇᴛᴛɪᴍ ...', 'sᴇɴ ᴄᴏᴋ sᴇᴠ ᴅᴇ ʙɪʀᴀᴋɪᴘ ɢɪᴅᴇɴ ʏᴀʀ ᴜᴛᴀɴsɪɴ ...', 'ᴏ ɢɪᴛᴛɪᴋᴛᴇɴ sᴏɴʀᴀ ɢᴇᴄᴇᴍ ɢᴜɴᴅᴜᴢᴇ ʜᴀsʀᴇᴛ ᴋᴀʟᴅɪ ...','ɢᴜᴠᴇɴᴍᴇᴋ  sᴇᴠᴍᴇᴋᴛᴇɴ ᴅᴀʜᴀ ᴅᴇɢᴇʀʟɪ , ᴢᴀᴍᴀɴʟᴀ ᴀɴʟᴀʀsɪɴ ...', 
'ɪɴsᴀɴ ʙᴀᴢᴇɴ ʙᴜʏᴜᴋ ʜᴀʏᴀʟʟᴇʀɪɴɪ ᴋᴜᴄᴜᴋ ɪɴsᴀɴʟᴀʀʟᴀ ᴢɪʏᴀɴ ᴇᴅᴇʀ ...', 'ᴋɪᴍsᴇ ᴋɪᴍsᴇʏɪ ᴋᴀʏʙᴇᴛᴍᴇᴢ  ɢɪᴅᴇɴ ʙᴀsᴋᴀsɪɴɪ ʙᴜʟᴜʀ , ᴋᴀʟᴀɴ ᴋᴇɴᴅɪɴɪ ...', 'ɢᴜᴄʟᴜ ɢᴏʀᴜɴᴇʙɪʟɪʀɪᴍ ᴀᴍᴀ ɪɴᴀɴ ʙᴀɴᴀ ʏᴏʀɢᴜɴᴜᴍ ...', 'ᴏᴍʀᴜɴᴜᴢᴜ sᴜsᴛᴜᴋʟᴀʀɪɴɪᴢɪ ᴅᴜʏᴀɴ  ʙɪʀɪʏʟᴇ ɢᴇᴄɪʀɪɴ ...', 'ʜᴀʏᴀᴛ ɪʟᴇʀɪʏᴇ ʙᴀᴋɪʟᴀʀᴀᴋ ʏᴀsᴀɴɪʀ ɢᴇʀɪʏᴇ ʙᴀᴋᴀʀᴀᴋ ᴀɴʟᴀsɪʟɪʀ ...', 'ᴀʀᴛɪᴋ ʜɪᴄʙɪʀ sᴇʏ ᴇsᴋɪsɪ ɢɪʙɪ ᴅᴇɢɪʟ ʙᴜɴᴀ ʙᴇɴᴅᴇ ᴅᴀʜɪʟɪᴍ ...', 'ᴋɪʏᴍᴇᴛ ʙɪʟᴇɴᴇ ɢᴏɴᴜʟᴅᴇ ᴠᴇʀɪʟɪʀ ᴏᴍᴜʀᴅᴇ ...', 
'ʙɪʀ ᴄɪᴄᴇᴋʟᴇ ɢᴜʟᴇʀ ᴋᴀᴅɪɴ , ʙɪʀ ʟᴀғʟᴀ ʜᴜᴢᴜɴ ...', 'ᴋᴀʟʙɪ ɢᴜᴢᴇʟ ᴏʟᴀɴ ɪɴsᴀɴɪɴ ɢᴏᴢᴜɴᴅᴇɴ ʏᴀs ᴇᴋsɪᴋ ᴏʟᴍᴀᴢᴍɪs ...', 'ʜᴇʀ sᴇʏɪ ʙɪʟᴇɴ ᴅᴇɢɪʟ ᴋɪʏᴍᴇᴛ ʙɪʟᴇɴ ɪɴsᴀɴʟᴀʀ ᴏʟsᴜɴ ʜᴀʏᴀᴛɪɴɪᴢᴅᴀ ...', 'ᴍᴇsᴀғᴇ ɪʏɪᴅɪʀ ɴᴇ ʜᴀᴅᴅɪɴɪ ᴀsᴀɴ ᴏʟᴜʀ , ɴᴇ ᴅᴇ ᴄᴀɴɪɴɪ sɪᴋᴀɴ ...', 'ʏᴜʀᴇɢɪᴍɪɴ ᴛᴀᴍ ᴏʀᴛᴀsɪɴᴅᴀ ʙᴜʏᴜᴋ ʙɪʀ ʏᴏʀɢᴜɴʟᴜᴋ ᴠᴀʀ ...', 'ᴠᴇʀɪʟᴇɴ ᴅᴇɢᴇʀɪɴ ɴᴀɴᴋᴏʀᴜ ᴏʟᴍᴀʏɪɴ ɢᴇʀɪsɪ ʜᴀʟʟ ᴏʟᴜʀ ...', 
'ʜᴇᴍ ɢᴜᴄʟᴜ ᴏʟᴜᴘ ʜᴇᴍ ʜᴀssᴀs ᴋᴀʟᴘʟɪ ʙɪʀɪ ᴏʟᴍᴀᴋ ᴄᴏᴋ ᴢᴏʀ ...', 'ᴍᴜʜᴛᴀᴄ ᴋᴀʟɪɴ ʏᴜʀᴇɢɪ ɢᴜᴢᴇʟ  ɪɴsᴀɴʟᴀʀᴀ ...', 'ɪɴsᴀɴ ᴀɴʟᴀᴅɪɢɪ ᴠᴇ ᴀɴʟᴀsɪʟᴅɪɢɪ ɪɴsᴀɴᴅᴀ ᴄɪᴄᴇᴋ ᴀᴄᴀʀ ...', 'ɪsᴛᴇʏᴇɴ ᴅᴀɢʟᴀʀɪ ᴀsᴀʀ ɪsᴛᴇᴍᴇʏᴇɴ ᴛᴜᴍsᴇɢɪ ʙɪʟᴇ ɢᴇᴄᴇᴍᴇᴢ ...', 'ɪɴsᴀʟʟᴀʜ sᴀʙɪʀʟᴀ ʙᴇᴋʟᴇᴅɪɢɪɴ sᴇʏ ɪᴄɪɴ ʜᴀʏɪʀʟɪ ʙɪʀ ʜᴀʙᴇʀ ᴀʟɪʀsɪɴ ...', 'ɪʏɪ ᴏʟᴀɴ ᴋᴀʏʙᴇᴛsᴇ ᴅᴇ ᴋᴀᴢᴀɴɪʀ ...', 'ɢᴏɴʟᴜɴᴜᴢᴇ ᴀʟᴅɪɢɪɴɪᴢ , ɢᴏɴʟᴜɴᴜᴢᴜ ᴀʟᴍᴀʏɪ ʙɪʟsɪɴ ...', 
'ʏɪɴᴇ ʏɪʀᴛɪᴋ ᴄᴇʙɪᴍᴇ ᴋᴏʏᴍᴜsᴜᴍ ᴜᴍᴜᴅᴜᴍᴜ ...', 'ᴏʟᴍᴇᴋ ʙɪʀ sᴇʏ ᴅᴇɢɪʟ ʏᴀsᴀᴍᴀᴋ ᴋᴏʀᴋᴜɴᴄ ...', 'ɴᴇ ɪᴄɪᴍᴅᴇᴋɪ sᴏᴋᴀᴋʟᴀʀᴀ sɪɢᴀʙɪʟᴅɪᴍ ɴᴇ ᴅᴇ ᴅɪsᴀʀɪᴅᴀᴋɪ ᴅᴜɴʏᴀʏᴀ ...', 'ɪɴsᴀɴ sᴇᴠɪʟᴍᴇᴋᴛᴇɴ ᴄᴏᴋ ᴀɴʟᴀsɪʟᴍᴀʏɪ ɪsᴛɪʏᴏʀᴅᴜ ʙᴇʟᴋɪ ᴅᴇ ...', 'ᴇᴋᴍᴇᴋ ᴘᴀʜᴀʟɪ , ᴇᴍᴇᴋ ᴜᴄᴜᴢᴅᴜʀ ...', 'sᴀᴠᴀsᴍᴀʏɪ ʙɪʀᴀᴋɪʏᴏʀᴜᴍ ʙᴜɴᴜ ᴠᴇᴅᴀ sᴀʏ ...','ᴋÜÇÜᴋ ɪŞʟᴇʀᴇ ɢᴇʀᴇĞɪɴᴅᴇɴ Çᴏᴋ Öɴᴇᴍ ᴠᴇʀᴇɴʟᴇʀ, ᴇʟɪɴᴅᴇɴ ʙÜʏÜᴋ ɪŞ ɢᴇʟᴍᴇʏᴇɴʟᴇʀᴅɪʀ ...',
'ᴀŞᴋ ʙɪʀ ᴋᴀᴅɪɴɪɴ ʏᴀŞᴀᴍɪɴɪɴ ᴛÜᴍ ÖʏᴋÜꜱÜ, ᴇʀᴋᴇĞɪɴ ɪꜱᴇ ʏᴀʟɴɪᴢᴄᴀ ʙɪʀ ꜱᴇʀÜᴠᴇɴɪᴅɪʀ ...','ʜᴇʀŞᴇʏɪ ᴅᴇɴᴇʀɪᴍ; ᴀᴍᴀ ʏᴀᴘᴀʙɪʟᴅɪᴋʟᴇʀɪᴍɪ ʏᴀᴘᴀʀɪᴍ ...','ʏᴀɴʟɪŞ ʙɪʟᴅɪĞɪɴ ʏᴏʟᴅᴀ; ʜЕʀᴋЕꜱʟЕ ʏÜʀÜʏЕᴄЕĞɪɴЕ, ᴅᴏĞʀᴜ ʙɪʟᴅɪĞɪɴ ʏᴏʟᴅᴀ; ᴛЕᴋ ʙᴀŞɪɴᴀ ʏÜʀÜ ...','ᴏ ᴅᴀ ɢᴀᴢɪ ᴏʟᴍᴀᴋ ɪꜱᴛᴇᴅɪ, ꜰᴀᴋᴀᴛ ᴏɴᴀ ᴀɴʟᴀᴛᴍᴀᴋ ɢᴇʀᴇᴋᴛɪ ᴋɪ, Şᴇʜɪᴅ ᴏʟᴍᴀʏɪ ɢÖᴢᴇ ᴀʟᴀᴍᴀʏᴀɴ ɢᴀᴢɪ ᴏʟᴀᴍᴀᴢᴅɪ ...','ɴᴇ ᴋᴀᴅᴀʀ ʏÜᴋꜱᴇʟɪʀꜱᴇɴ, ᴜÇᴍᴀʏɪ ʙɪʟᴍᴇʏᴇɴʟᴇʀᴇ ᴏ ᴋᴀᴅᴀʀ ᴋÜÇÜᴋ ɢÖʀÜɴÜʀꜱÜɴ ...',
'ɴᴇ ᴋᴀᴅᴀʀ ʜᴀᴢɪɴ ʙɪʀ ÇᴀĞᴅᴀ ʏᴀŞɪʏᴏʀᴜᴢ, ʙɪʀ Öɴʏᴀʀɢɪʏɪ ᴏʀᴛᴀᴅᴀɴ ᴋᴀʟᴅɪʀᴍᴀᴋ ᴀᴛᴏᴍᴜ ᴘᴀʀÇᴀʟᴀᴍᴀᴋᴛᴀɴ ᴅᴀʜᴀ ɢÜÇ ...','ᴍᴜᴛʟᴜʟᴜᴋ ʜᴇʀ Şᴇʏᴅᴇɴ Öɴᴄᴇ ᴠÜᴄᴜᴛ ꜱᴀĞʟɪĞɪɴᴅᴀᴅɪʀ ...','ʙᴀᴢᴇɴ ʙɪʀ Şᴇʏᴇ ꜱᴏɴ ᴠᴇʀᴍᴇᴋ ɪÇɪɴ ɪꜱᴛᴇᴍᴇᴅɪĞɪɴ ʙɪʀ Şᴇʏ ʏᴀᴘᴍᴀɴ ɢᴇʀᴇᴋɪʀ ...','ᴋɪᴍ ᴋᴀᴢᴀɴᴍᴀᴢꜱᴀ ʙᴜ ᴅÜɴʏᴀᴅᴀ ʙɪʀ ᴇᴋᴍᴇᴋ ᴘᴀʀᴀꜱɪ ʏᴀ ᴅᴏꜱᴛᴜɴᴜɴ ʏÜᴢ ᴋᴀʀᴀꜱɪ ʏᴀ ᴅᴀ ᴅÜŞᴍᴀɴɪɴɪɴ ᴍᴀꜱᴋᴀʀᴀꜱɪ ...','ᴀᴠᴜᴄᴜ ᴋᴀᴅᴀʀ ʏÜʀᴇĞɪ ᴏʟᴍᴀʏᴀɴ ɪɴꜱᴀɴʟᴀʀɪ ᴋÜʀᴇᴋ ɢɪʙɪ ᴅɪʟɪ ᴠᴀʀ ...','ᴍᴜᴛʟᴜʟᴜᴋ ʜᴇʀ Şᴇʏᴅᴇɴ Öɴᴄᴇ ᴠÜᴄᴜᴛ ꜱᴀĞʟɪĞɪɴᴅᴀᴅɪʀ ...',
'ᴏᴋʏᴀɴᴜꜱᴛᴀ Öʟᴍᴇᴢ ᴅᴇ ɪɴꜱᴀɴ, ɢɪᴅᴇʀ ʙɪʀ ᴋᴀŞɪᴋ ꜱᴇᴠᴅᴀᴅᴀ ʙᴏĞᴜʟᴜʀ ...','ᴍᴜᴛʟᴜʟᴜᴋ ʜᴇʀ Şᴇʏᴅᴇɴ Öɴᴄᴇ ᴠÜᴄᴜᴛ ꜱᴀĞʟɪĞɪɴᴅᴀᴅɪʀ ...','ɴᴇʀᴇʏᴇ ɢɪᴛᴛɪĞɪɴɪ ʙɪʟᴍɪʏᴏʀꜱᴀɴ, ʜᴀɴɢɪ ʏᴏʟᴅᴀɴ ɢɪᴛᴛɪĞɪɴɪɴ ʜɪÇʙɪʀ Öɴᴇᴍɪ ʏᴏᴋᴛᴜʀ ...','ʙᴀᴢᴇɴ ɪʟᴋ ɢÖʀÜŞᴛᴇ ʙɪʟɪʀꜱɪɴ, ᴏ ɪɴꜱᴀɴ ꜱᴇɴɪɴ ᴋᴀᴅᴇʀɪɴᴅɪʀ. ʙᴀᴢᴇɴ ʙɪʀ ÖᴍÜʀ ᴀʀᴀʀꜱɪɴ, ʙᴜʟᴜɴᴍᴀᴢ ...','ʟᴀɴᴇᴛ ᴏʟꜱᴜɴ. ɴᴇ ᴍᴜᴀᴢᴢᴀᴍ Şᴇʏ ꜱᴇɴɪ ꜱᴇᴠᴍᴇᴋ ...','ʏᴀʀɪᴍ ɴᴇꜰᴇꜱʟɪᴋ ʙᴜ ʜᴀʏᴀᴛᴛᴀ. ꜱᴇᴠɢɪᴅᴇɴ ʙᴀŞᴋᴀ ʜɪÇʙɪʀ Şᴇʏ ᴘʟᴀɴʟᴀᴍᴀ ...',
'İʟɪᴍ ᴀŞᴀĞɪᴅᴀᴋɪʟᴇʀɪ ʏÜᴋꜱᴇʟᴛɪʀ, ᴄᴀʜɪʟʟɪᴋ ɪꜱᴇ ʏÜᴋꜱᴇᴋᴛᴇᴋɪʟᴇʀɪ ᴀʟÇᴀʟᴛɪʀ ...','ᴋɪᴍ ɪʟɪᴍ ᴀʀᴀᴍᴀ ʏᴏʟᴜɴᴅᴀ ᴏʟᴜʀꜱᴀ, ᴄᴇɴɴᴇᴛ ᴅᴇ ᴏɴᴜ ᴀʀᴀᴍᴀ ʏᴏʟᴜɴᴅᴀ ᴏʟᴜʀ ...','ʏᴀɴɪʟᴛᴍᴀꜱɪɴ ꜱᴇɴɪ ᴍᴀꜱᴜᴍ ʙᴀᴋɪŞʟᴀʀ, ʙᴀᴢɪʟᴀʀɪɴɪ Şᴇʏᴛᴀɴ ᴀʏᴀᴋᴛᴀ ᴀʟᴋɪŞʟᴀʀ ...','İɴꜱᴀɴʟᴀʀɪ ᴛᴀɴɪŞɪʀᴋᴇɴ ᴅᴇĞɪʟ, ᴛᴀʀᴛɪŞɪʀᴋᴇɴ ᴛᴀɴɪʀꜱɪɴ. ÇÜɴᴋÜ Öꜰᴋᴇ, ꜱᴀʟʟᴀɴᴀɴ ᴋɪŞɪʟɪĞɪ ᴏʀᴛᴀʏᴀ Çɪᴋᴀʀɪʀ ...','ɢᴇʀÇᴇᴋ ᴀŞᴋ ɪÇɪɴ ᴀꜱʟᴀ ʙɪʀ ᴢᴀᴍᴀɴ ʏᴀ ᴅᴀ ʏᴇʀ ʏᴏᴋᴛᴜʀ ...','ᴇĞᴇʀ ᴅᴏĞʀᴜʏᴜ ꜱÖʏʟᴇʀꜱᴇɴ ʜɪÇʙɪʀ Şᴇʏɪ ʜᴀᴛɪʀʟᴀᴍᴀᴋ ᴢᴏʀᴜɴᴅᴀ ᴅᴇĞɪʟꜱɪɴ ...',
'ʜᴇʀ ᴇʟɪɴɪ ꜱɪᴋᴀɴʟᴀ ᴅᴏꜱᴛ, ʜᴇʀ ᴄᴀɴɪɴɪ ꜱɪᴋᴀɴʟᴀ ᴅÜŞᴍᴀɴ ᴏʟᴍᴀ ...','ᴇᴅᴇᴘ ᴀᴋʟɪɴ ᴛᴇʀᴄÜᴍᴀɴɪᴅɪʀ. ʜᴇʀᴋᴇꜱ ᴇᴅᴇʙɪ ᴋᴀᴅᴀʀ ᴀᴋɪʟʟɪ, ᴀᴋʟɪ ᴋᴀᴅᴀʀ Şᴇʀᴇꜰʟɪ, Şᴇʀᴇꜰɪ ᴋᴀᴅᴀʀ ᴅᴇĞᴇʀʟɪᴅɪʀ ...','ʏᴀŞɪɴ ᴅᴇĞɪʟ ʏᴀŞᴀᴅɪᴋʟᴀʀɪɴ ÖĞʀᴇᴛɪʀ ꜱᴀɴᴀ ʜᴀʏᴀᴛɪ ...','Şᴜɴᴜ ᴀꜱʟᴀ ᴜɴᴜᴛᴍᴀ; ɢÜʟᴇʀᴋᴇɴ ᴋᴀʏʙᴇᴛᴛɪᴋʟᴇʀɪɴɪ, ᴀĞʟᴀʏᴀʀᴀᴋ ᴋᴀᴢᴀɴᴀᴍᴀᴢꜱɪɴ ...','ꜰᴀᴢʟᴀ ʙÜʏÜᴛᴍᴇ ᴋᴇɴᴅɪɴɪ, ᴇɴ ꜰᴀᴢʟᴀ ꜱᴇᴠᴇʙɪʟᴅɪĞɪᴍ ᴋᴀᴅᴀʀꜱɪɴ; ᴅᴀʜᴀꜱɪ ʏᴏᴋ ...','ᴀŞᴋ Çᴏᴋ ᴋɪꜱᴀ ᴀᴍᴀ ᴜɴᴜᴛᴍᴀꜱɪ Çᴏᴋ ᴢᴏʀ ...',
'İʏɪʏɪ ᴀʀᴀ, ᴅᴏĞʀᴜʏᴜ ᴀʀᴀ, ɢÜᴢᴇʟɪ ᴀʀᴀ ꜰᴀᴋᴀᴛ ᴋᴜꜱᴜʀᴜ ᴀʀᴀᴍᴀ ...','ʜᴀʏᴀᴛɪ ɢÖᴢʏᴀŞʟᴀʀɪɴʟᴀ ÖᴅÜʟʟᴇɴᴅɪʀᴇᴄᴇĞɪɴᴇ; ɢÜʟÜᴄÜᴋʟᴇʀɪɴʟᴇ ᴄᴇᴢᴀʟᴀɴᴅɪʀ ...','ᴜᴢᴀᴋᴋᴇɴ ʙɪʟᴇ ʙɪʀ ɴᴇꜰᴇꜱ ᴋᴀᴅᴀʀ ʏᴀᴋɪɴɪᴍᴅᴀꜱɪɴ ...','ʜᴇʀ ᴍÜɴᴀᴋᴀŞᴀɴɪɴ ᴛᴇᴍᴇʟɪɴᴅᴇ ʙɪʀɪꜱɪɴɪɴ ᴄᴀʜɪʟʟɪĞɪ ʏᴀᴛᴀʀ ...','ʙɪʟɢᴇʟɪᴋ ᴋᴀʟᴘᴛᴇɴ ɢᴇʟɪʀ. ᴀᴋɪʟʟᴀ ɪʟɢɪꜱɪ ʏᴏᴋᴛᴜʀ. ʙɪʟɢᴇʟɪᴋ, ᴠᴀʀʟɪĞɪɴɪɴ ᴇɴ ᴅᴇʀɪɴ ɴᴏᴋᴛᴀꜱɪɴᴅᴀɴ Çɪᴋᴀʀ. ᴋᴀꜰᴀʏᴀ ᴀɪᴛ ᴅᴇĞɪʟᴅɪʀ ...',
'ʏᴀŞᴀᴅɪĞɪɴ ʏᴇʀɪ ᴄᴇɴɴᴇᴛ ʏᴀᴘᴀᴍᴀᴅɪĞɪɴ ꜱÜʀᴇᴄᴇ ᴋᴀÇᴛɪĞɪɴ ʜᴇʀ ʏᴇʀ ᴄᴇʜᴇɴɴᴇᴍᴅɪʀ ...','ᴋɪʀɪʟᴍɪŞ ʙɪʀɪ Çᴏᴋ ɢÜᴢᴇʟ ꜱᴜꜱᴀʀ. ʜᴇʀ Şᴇʏɪɴᴇ ʜᴀꜱʀᴇᴛ ᴋᴀʟɪʀꜱɪɴ ...','İɴᴀɴÇ, ᴘᴀʀÇᴀʟᴀɴᴍɪŞ ʙɪʀ ᴅÜɴʏᴀɴɪɴ ɪŞɪĞᴀ ÇɪᴋᴀᴄᴀĞɪ ɢÜÇᴛÜʀ ...','ʙᴇʟᴋɪ ᴅᴇ ɪɴꜱᴀɴ ʜᴇʀ Şᴇʏɪ ɪÇɪɴᴇ ᴀᴛᴍᴀᴋᴛᴀɴ ʙᴏĞᴜʟᴜʏᴏʀ ᴢᴀᴍᴀɴʟᴀ ...','ᴀŞᴋ ʙɪʀ ᴋᴀᴅɪɴɪɴ ʏᴀŞᴀᴍɪɴɪɴ ᴛÜᴍ ÖʏᴋÜꜱÜ, ᴇʀᴋᴇĞɪɴ ɪꜱᴇ ʏᴀʟɴɪᴢᴄᴀ ʙɪʀ ꜱᴇʀÜᴠᴇɴɪᴅɪʀ ...','ᴀŞᴋ ʀÜᴢɢᴀʀ ɢɪʙɪᴅɪʀ, ɢÖʀᴇᴍᴇᴢꜱɪɴ ᴀᴍᴀ ʜɪꜱꜱᴇᴅᴇʙɪʟɪʀꜱɪɴ ...',
'ᴅᴇĞɪŞɪᴍ ᴇʙᴇᴅɪ, ÖʟÜᴍꜱÜᴢʟÜᴋ ᴋᴀʟɪᴄɪᴅɪʀ ...','ᴋÖʀʟᴇʀɪɴ Üʟᴋᴇꜱɪɴᴅᴇ, ᴛᴇᴋ ɢÖᴢʟÜ ɪɴꜱᴀɴ ᴋʀᴀʟ ᴏʟᴜʀ ...''ᴏʏꜱᴀ ʏÜʀᴇĞɪ ᴛᴇᴍɪᴢ ᴏʟᴍᴀʏᴀɴɪɴ, ᴀɴʟᴀʏɪŞɪ ᴅᴀ ᴋɪᴛᴛɪʀ ...','ʜɪÇ ʙᴜ ᴋᴀᴅᴀʀ ꜱᴜꜱᴍᴀᴋ ɪꜱᴛᴇᴍᴇᴍɪŞᴛɪᴍ ...','ŞÜᴋʀᴇᴛᴍᴇʏɪ ÖĞʀᴇɴᴍᴇʏᴇɴ ɴᴀɴᴋÖʀ ᴇʟʙᴇᴛᴛᴇ ŞɪᴋÂʏᴇᴛ ᴇᴅᴇʀ ...','Öʏʟᴇ ʙɪʀ ɢᴇʟ ᴅᴇᴍᴇʟɪꜱɪɴ ᴋɪ, ᴍᴇꜱᴀꜰᴇʟᴇʀ ᴀɴʟᴀᴍɪɴɪ ʏɪᴛɪʀᴍᴇʟɪ ...',
'ꜱᴀʙɪʀ ᴠᴀᴢɢᴇÇᴍᴇᴋ ᴅᴇĞɪʟ, ᴜᴍᴜᴅᴜ ʏᴀʀɪɴᴀ ᴇʀᴛᴇʟᴇᴍᴇᴋᴛɪʀ ...','ꜱᴇᴠᴅɪᴋʟᴇʀɪɴɪᴢᴇ ᴢᴀᴍᴀɴ ᴀʏɪʀɪɴ ʏᴏᴋꜱᴀ ᴢᴀᴍᴀɴ ꜱɪᴢɪ ꜱᴇᴠᴅɪᴋʟᴇʀɪɴɪᴢᴅᴇɴ ᴀʏɪʀɪʀ ...','ʙᴀŞᴋᴀꜱɪɴɪɴ ÖɴÜɴÜ ᴀʏᴅɪɴʟᴀᴛɪʀᴋᴇɴ ᴋᴇɴᴅɪ ʏᴏʟᴜᴍᴜᴢᴀ ᴅᴀ ɪŞɪᴋ ᴛᴜᴛᴀʀɪᴢ ...','ʜᴇʀᴋᴇꜱ ᴀʏɴɪ Şᴇʏɪ ᴅÜŞÜɴÜʏᴏʀꜱᴀ, ʜɪÇ ᴋɪᴍꜱᴇ ꜰᴀᴢʟᴀ ʙɪʀ Şᴇʏ ᴅÜŞÜɴᴍÜʏᴏʀ ᴅᴇᴍᴇᴋᴛɪʀ ...','İÇɪɴᴇ ᴀᴛᴛɪᴋʟᴀʀɪɴ ᴋᴇᴅᴇʀɪɴᴅɪʀ. İÇɪɴᴅᴇɴ ᴀᴛᴀᴍᴀᴅɪᴋʟᴀʀɪɴ ᴋᴀᴅᴇʀɪɴ ...',
'ᴍᴜᴛʟᴜ ᴍᴜ ᴏʟᴍᴀᴋ ɪꜱᴛɪʏᴏʀꜱᴜɴ , ᴋɪᴍꜱᴇᴅᴇɴ ʙɪʀ Şᴇʏ ʙᴇᴋʟᴇᴍᴇ ...','ɢÜᴢᴇʟɪ ɢÜᴢᴇʟ ʏᴀᴘᴀɴ ᴇᴅᴇᴘᴛɪʀ, ᴇᴅᴇᴘ ɪꜱᴇ ɢÜᴢᴇʟɪ ꜱᴇᴠᴍᴇʏᴇ ꜱᴇʙᴇᴘᴛɪʀ ...','ʏᴏʀᴍᴀ ᴋᴇɴᴅɪɴɪ... ʙɪʀᴀᴋ ʜᴀʏᴀᴛɪɴᴀ ᴇŞʟɪᴋ ᴇᴛᴍᴇᴋ ɪꜱᴛᴇʏᴇɴʟᴇʀ ꜱᴇɴɪɴʟᴇ ɢᴇʟꜱɪɴ ...','ʙɪʀÇᴏᴋ ɪɴꜱᴀɴ ᴍᴜᴛʟᴜʟᴜĞᴜ, ʙᴜʀɴᴜɴᴜɴ ÜꜱᴛÜɴᴅᴇ ᴜɴᴜᴛᴛᴜĞᴜ ɢÖᴢʟÜᴋ ɢɪʙɪ ᴇᴛʀᴀꜰᴛᴀ ᴀʀᴀʀ ...','ᴅÜʀÜꜱᴛ ᴏʟᴍᴀᴋᴛᴀɴ ᴋᴏʀᴋᴍᴀ, ᴋᴀʏʙᴇᴅᴇᴄᴇĞɪɴ ᴇɴ ꜰᴀᴢʟᴀ ʏᴀɴʟɪŞ ɪɴꜱᴀɴʟᴀʀ ᴏʟᴜʀ ...',
)

sor = (
'ᴋᴜʀᴛ ᴍᴜ ᴋᴇʟɪᴍᴇ ᴏʏᴜɴᴜ ᴍᴜ ?','Gʀᴜᴘᴛᴀ ɴᴇʏɪ ᴅᴇɢ̆ɪşᴛɪʀᴍᴇᴋ ɪsᴛᴇʀᴅɪɴ?','ɢʀᴜᴘᴛᴀ ᴋɪᴍʟᴇ ᴄ̧ᴀʏ ɪᴄ̧ᴍᴇᴋ ɪsᴛᴇʀᴅɪɴ ?','ʙᴜ̈ʏᴜ̈ʏᴇɴ ʜᴀʏᴀʟɪ ʙɪʀ ᴀʀᴋᴀᴅᴀşıɴıᴢ ᴠᴀʀ ᴍıʏᴅı?','ʙɪʀ ɢᴜ̈ɴ ᴋᴀʀşı ᴄɪɴs ᴏʟᴀʀᴀᴋ ᴜʏᴀɴıʀsᴀɴ, ɪʟᴋ ʏᴀᴘᴀᴄᴀɢ̆ıɴ şᴇʏ ɴᴇᴅɪʀ?','ɢʀᴜʙᴜɴ ᴏʟᴍᴀᴢsᴀ ᴏʟᴍᴀᴢı sᴇɴᴄᴇ ᴋɪᴍ ᴇᴛɪᴋᴇᴛʟᴇʀ ᴍɪsɪɴ?','ʜᴀʏᴀᴛᴛᴀ ᴜɴᴜᴛᴍᴀᴅıɢ̆ıɴ ʙɪʀɪ ᴠᴀʀ ᴍı?','ᴋᴜ̈ʟᴛᴜ̈ʀᴜ̈ᴍᴜ̈ᴢᴜ̈ɴ ᴇɴ ᴄ̧ᴏᴋ sᴇᴠᴅɪɢ̆ɪɴɪᴢ ʏᴀɴı ɴᴇᴅɪʀ?','ɢʀᴜʙᴜ sᴇᴠɪʏᴏʀ ᴍᴜsᴜɴ ?','ʜᴀʏᴀᴛᴛᴀ ᴜɴᴜᴛᴍᴀᴅıɢ̆ıɴ ʙɪʀɪ ᴠᴀʀ ᴍı?','ʜɪᴄ̧ʙɪʀ sᴏɴᴜᴄᴜ ᴏʟᴍᴀʏᴀᴄᴀɢ̆ıɴı ʙɪʟsᴇɴ ɴᴇ ʏᴀᴘᴍᴀᴋ ɪsᴛᴇʀᴅɪɴ?','ɪʟᴇʀᴅᴇ ᴄ̧ᴏᴄᴜɢ̆ᴜɴ ᴏʟᴜʀsᴀ ɴᴇ ɪsɪᴍ ᴋᴏʏᴍᴀᴋ ɪsᴛᴇʀsɪɴ?',
'şɪᴍᴅɪʏᴇ ᴋᴀᴅᴀʀ ʜɪᴄ̧ ᴀʀᴀʟıᴋsıᴢ 𝟷𝟸 sᴀᴀᴛᴛᴇɴ ғᴀᴢʟᴀ ᴜʏᴜᴅᴜɢ̆ᴜɴ ᴏʟᴅᴜ ᴍᴜ?','ɢʀᴜᴘᴛᴀ ᴋɪ ᴜ̈ᴄ̧ ᴋᴀɴᴋᴀɴı ᴇᴛɪᴋᴇᴛʟᴇʀ ᴍɪsɪɴ?','sıɴıғᴛᴀ ʜɪᴄ̧ ᴜʏᴜʏᴀ ᴋᴀʟᴅıɴ ᴍı?','ɢʀᴜʙᴜɴ ᴇɴ ᴅᴇʀᴛʟɪsɪ ᴋɪᴍ ?','ʀᴇᴀʟ ʜᴀʏᴀᴛᴛᴀ ᴛᴀɴıᴍᴀᴋ ɪsᴛᴇᴅɪɢ̆ɪɴ ᴋɪᴍsᴇ ᴠᴀʀ ᴍı ɢʀᴜᴘᴛᴀ ?','ʙɪʀɪɴɪɴ ᴛᴇʟᴇғᴏɴᴜɴᴅᴀ ɢᴏ̈ʀᴅᴜ̈ɢ̆ᴜ̈ɴ ᴇɴ ᴛᴜʜᴀғ şᴇʏ ɴᴇᴅɪʀ?','ʙɪʀ ʙᴏ̈ᴄᴇᴋ ɪsᴛɪʟᴀsı ɢᴇʀᴄ̧ᴇᴋʟᴇşsᴇ ʜᴀɴɢɪ ᴀʀᴋᴀᴅᴀşıɴ ʜᴀʏᴀᴛᴛᴀ ᴋᴀʟᴍᴀʏı ʙᴀşᴀʀıʀ?','ᴅᴜ̈ɴʏᴀᴅᴀᴋɪ ʜᴇʀʜᴀɴɢɪ ʙɪʀɪɴɪ ᴛᴜ̈ʀᴋɪʏᴇ’ɴɪɴ ʙᴀşᴋᴀɴı ʏᴀᴘᴀʙɪʟsᴇʏᴅɪɴ ʙᴜ ᴋɪᴍ ᴏʟᴜʀᴅᴜ?','ᴋᴜʀᴛ ᴏʏᴜɴᴜɴᴜ sᴇᴠɪʏᴏʀ ᴍᴜsᴜɴ?','ɢʀᴜᴘᴛᴀ ᴅᴇɢ̆ɪşᴍᴇsɪ ɢᴇʀᴇᴋᴇɴ şᴇʏ ᴠᴀʀ ᴍı?','ʜɪᴄ̧ʙɪʀ sᴏɴᴜᴄᴜ ᴏʟᴍᴀʏᴀᴄᴀɢ̆ıɴı ʙɪʟsᴇɴ ɴᴇ ʏᴀᴘᴍᴀᴋ ɪsᴛᴇʀᴅɪɴ?',
'ʙɪʀ ᴀʏɴᴀɴıɴ ᴏ̈ɴᴜ̈ɴᴅᴇ ʏᴀᴘᴛıɢ̆ıɴ ᴇɴ ᴄ̧ıʟɢıɴᴄᴀ şᴇʏ ɴᴇᴅɪʀ?','ᴄ̧ıᴋᴍᴀᴋ ɪsᴛᴇʏᴇᴄᴇɢ̆ɪɴ ᴇɴ ɢᴇɴᴄ̧ ᴋɪşɪ ᴋᴀᴄ̧ ʏᴀşıɴᴅᴀ ᴏʟᴜʀᴅᴜ?','ᴋɪʟᴏ ᴀʟᴅıʀıᴘ ᴀʟᴅıʀᴍᴀᴍᴀsı ᴏ̈ɴᴇᴍʟɪ ᴅᴇɢ̆ɪʟ, ʙɪʀ ᴏᴛᴜʀᴜşᴛᴀ ʜᴇᴘsɪɴɪ ʏᴇʀɪᴍ ᴅᴇᴅɪɢ̆ɪɴ ʏᴇᴍᴇᴋ ɴᴇᴅɪʀ?','ɢʀᴜᴘᴛᴀ ʜᴀɴɢɪ ᴏʏᴜɴᴜ sᴇᴠɪʏᴏʀsᴜɴ ?','ᴜʏᴋᴜɴᴅᴀ ᴋᴏɴᴜşᴜʀ ᴍᴜsᴜɴ?','ᴇɴ ᴋᴏ̈ᴛᴜ̈ ɢʀᴜᴘ ʜᴀɴɢɪsɪᴅɪʀ?','ɪ̇ɴsᴀɴʟᴀʀı ʏᴀɴᴀɴ ʙɪʀ ʙɪɴᴀᴅᴀɴ ᴋᴜʀᴛᴀʀıʏᴏʀ ᴏʟsᴀʏᴅıɴıᴢ ᴠᴇ ʙɪʀ ᴋɪşɪʏɪ ʙᴜ ɢʀᴜᴘᴅᴀɴ ɢᴇʀɪᴅᴇ ʙıʀᴀᴋᴍᴀᴋ ᴢᴏʀᴜɴᴅᴀ ᴋᴀʟıʀsᴀɴıᴢ, ᴋɪᴍ ᴏʟᴜʀᴅᴜ?','ʜᴀʟᴀ ʏᴀᴘᴛıɢ̆ıɴ ᴇɴ ᴄ̧ᴏᴄᴜᴋᴄ̧ᴀ şᴇʏ ɴᴇᴅɪʀ?','ᴠᴜ̈ᴄᴜᴅᴜɴᴜɴ ʜᴀɴɢɪ ʙᴏ̈ʟᴜ̈ᴍᴜ̈ɴᴜ̈ sᴇᴠɪʏᴏʀsᴜɴ, ʜᴀɴɢɪ ᴋısᴍıɴᴅᴀɴ ɴᴇғʀᴇᴛ ᴇᴅɪʏᴏʀsᴜɴ?','sıɴıғᴛᴀ ᴀsʟᴀ ʏᴀɴıɴᴅᴀ ᴏᴛᴜʀᴍᴀᴋ ɪsᴛᴇᴍᴇʏᴇᴄᴇɢ̆ɪɴ ᴋɪᴍ?','ᴋᴀᴄ̧ sᴇᴠɢɪʟɪɴ ᴏʟᴅᴜ?',
'ʜɪᴄ̧ʙɪʀ sᴏɴᴜᴄᴜ ᴏʟᴍᴀʏᴀᴄᴀɢ̆ıɴı ʙɪʟsᴇɴ ɴᴇ ʏᴀᴘᴍᴀᴋ ɪsᴛᴇʀᴅɪɴ?','ᴇɴ ᴋᴏ̈ᴛᴜ̈ ɢʀᴜᴘ ʜᴀɴɢɪsɪᴅɪʀ?','ɢʀᴜᴘᴛᴀ ʜᴏşʟᴀɴᴅıɢ̆ıɴ ʙɪʀɪ ᴠᴀʀ ᴍı ?','ᴄ̧ᴇşɪᴛʟɪ ʙᴀᴛıʟ ɪɴᴀɴᴄ̧ʟᴀʀıɴ ᴠᴀʀ ᴍı, ᴠᴀʀsᴀ ᴏɴʟᴀʀ ɴᴇʟᴇʀ?','ᴇɴ sᴏɴ ɴᴇ ᴢᴀᴍᴀɴ ʜᴜ̈ɴɢᴜ̈ʀ ʜᴜ̈ɴɢᴜ̈ʀ ᴀɢ̆ʟᴀᴅıɢ̆ıɴı ʜᴀᴛıʀʟıʏᴏʀ ᴍᴜsᴜɴ?','ᴏᴛᴏʙᴜ̈sᴛᴇ ʏᴀᴘᴛıɢ̆ıɴ ᴇɴ ᴛᴜʜᴀғ şᴇʏ ɴᴇᴅɪʀ?','ᴇɴ sᴏɴ sᴏ̈ʏʟᴇᴅɪɢ̆ɪɴ ʏᴀʟᴀɴ ɴᴇᴅɪʀ?','ʙᴜ ɢʀᴜᴘᴅᴀɴ ʙɪʀɪʏʟᴇ ᴇᴠʟᴇɴᴍᴇᴋ ᴢᴏʀᴜɴᴅᴀ ᴋᴀʟsᴀɴ ᴋɪᴍ ᴏʟᴜʀᴅᴜ?','ʜɪᴄ̧ ʏᴀşıɴ ʜᴀᴋᴋıɴᴅᴀ ʏᴀʟᴀɴ sᴏ̈ʏʟᴇᴅɪɴ ᴍɪ?','şɪşᴇᴅᴇɴ ʙɪʀ ᴄɪɴ ᴄ̧ıᴋsᴀ ᴜ̈ᴄ̧ ᴅɪʟᴇɢ̆ɪɴ ɴᴇ ᴏʟᴜʀᴅᴜ?','ʙᴜ̈ʏᴜ̈ʀᴋᴇɴ ʜɪᴄ̧ ʜᴀʏᴀʟɪ ᴀʀᴋᴀᴅᴀşıɴ ᴏʟᴅᴜ ᴍᴜ?','ᴠᴜ̈ᴄᴜᴅᴜɴᴜɴ ʜᴀɴɢɪ ʙᴏ̈ʟᴜ̈ᴍʟᴇʀɪɴᴅᴇɴ ɢıᴅıᴋʟᴀɴıʏᴏʀsᴜɴ?',
'ʜᴀʏᴀʟɪɴᴅᴇᴋɪ ɪş ɴᴇ?','ʙᴜ ɢʀᴜᴘᴛᴀᴋɪ ɪɴsᴀɴʟᴀʀᴅᴀɴ ᴋɪᴍɪɴʟᴇ ʜᴀʏᴀᴛıɴı ᴅᴇɢ̆ɪşᴛɪʀᴍᴇᴋ ɪsᴛᴇʀᴅɪɴ?','ʙᴜ ɢʀᴜᴘᴛᴀᴋɪ ɪɴsᴀɴʟᴀʀᴅᴀɴ ᴋɪᴍɪɴʟᴇ ʜᴀʏᴀᴛıɴı ᴅᴇɢ̆ɪşᴛɪʀᴍᴇᴋ ɪsᴛᴇʀᴅɪɴ?','ᴇɴ ᴛᴜʜᴀғ ᴛᴀᴋᴍᴀ ᴀᴅıɴ ɴᴇᴅɪʀ?','ɢᴜ̈ɴᴅᴇ ᴋᴀᴄ̧ ᴛᴀɴᴇ ᴏ̈ᴢᴄ̧ᴇᴋɪᴍ ʏᴀᴘᴀʀsıɴ?','ᴋɪᴍsᴇɴɪɴ ʙɪʟᴍᴇʏᴇᴄᴇɢ̆ɪ ɢᴀʀᴀɴᴛɪ ᴏʟsᴀ ᴋɪᴍɪ ᴏ̈ʟᴅᴜ̈ʀᴍᴇᴋ ɪsᴛᴇʀᴅɪɴ?','ᴛᴇʟᴇғᴏɴᴜɴᴜᴢᴅᴀ ᴀʀᴀᴅıɢ̆ıɴ sᴏɴ şᴇʏ ɴᴇʏᴅɪ?','ɪ̇ɴsᴀɴʟᴀʀıɴ sɪᴢᴇ ɴᴇ sᴏʀᴍᴀsıɴᴅᴀɴ ʙıᴋᴛıɴıᴢ?','ʙᴇʏɴɪɴɪ ʙɪʀ ʀᴏʙᴏᴛᴀ ʏᴇʀʟᴇşᴛɪʀᴇʙɪʟɪʀ ᴠᴇ sᴏɴsᴜᴢᴀ ᴋᴀᴅᴀʀ ʙᴜ şᴇᴋɪʟᴅᴇ ʏᴀşᴀʏᴀʙɪʟsᴇᴅɪɴ,ʙᴜɴᴜ ʏᴀᴘᴀʀ ᴍıʏᴅıɴ?','ɢᴜ̈ɴᴅᴇ ᴋᴀᴄ̧ ᴛᴀɴᴇ ᴏ̈ᴢᴄ̧ᴇᴋɪᴍ ʏᴀᴘᴀʀsıɴ?','ɢɪᴢʟɪ ᴀşᴋıɴ ᴋɪᴍ?','ᴋᴀᴅıɴ/ᴇʀᴋᴇᴋ ᴏʟᴍᴀɴıɴ ᴇɴ ᴋᴏ̈ᴛᴜ̈ ᴠᴇ ᴇɴ ɪʏɪ ʏᴀɴı ɴᴇᴅɪʀ?','ɢʀᴜʙᴜɴ ᴇɴ ᴅᴇʀᴛʟɪsɪ ᴋɪᴍ ?',
'ғɪᴢɪᴋsᴇʟ ᴏʟᴀʀᴋ sᴀɴᴀ ᴇɴ ᴀᴄı ᴠᴇʀᴇɴ ᴅᴇɴᴇʏɪᴍɪɴ ɴᴇ ᴏʟᴅᴜ?','ɢʀᴜᴘᴛᴀ ɢɪᴢʟɪ sᴇᴠᴅɪɢ̆ɪɴ ᴋɪᴍsᴇ ᴠᴀʀ ᴍı?','ɪʟᴇʀᴅᴇ ᴄ̧ᴏᴄᴜɢ̆ᴜɴ ᴏʟᴜʀsᴀ ɴᴇ ɪsɪᴍ ᴋᴏʏᴍᴀᴋ ɪsᴛᴇʀsɪɴ?','ʜᴀʏᴀᴛıɴʟᴀ ɪʟɢɪʟɪ ᴛᴇʟᴇɢʀᴀᴍᴅᴀ ɴᴇ ʏᴀʟᴀɴ sᴏ̈ʏʟᴇᴅɪɴ ?','ʙɪʀɪɴɪ ᴏ̈ᴘᴇʀᴋᴇɴ ᴋᴇɴᴅɪɴɪ ʜɪᴄ̧ ᴋᴏ̈ᴛᴜ̈ ʜɪssᴇᴛᴛɪɴ ᴍɪ?','ʙɪʀɪsɪ ᴋıᴢ ᴀʀᴋᴀᴅᴀşıɴ / ᴇʀᴋᴇᴋ ᴀʀᴋᴀᴅᴀşıɴᴅᴀɴ ᴀʏʀıʟᴍᴀᴋ ɪᴄ̧ɪɴ sᴀɴᴀ 𝟷 ᴍɪʟʏᴏɴ ᴛʟ ᴏ̈ɴᴇʀsᴇʏᴅɪ, ʏᴀᴘᴀʀ ᴍıʏᴅıɴ?','ɢʀᴜᴘᴛᴀ ᴏʟᴍᴀᴍᴀsıɴı ɪsᴛᴇᴅɪɢ̆ɪɴ ᴋɪşɪʏɪ ᴇᴛɪᴋᴇᴛʟᴇʀ ᴍɪsɪɴ?','ʙᴜ ᴏᴅᴀᴅᴀᴋɪ ᴇɴ sɪɴɪʀ ʙᴏᴢᴜᴄᴜ ᴋɪşɪ ᴋɪᴍ?','ɢʀᴜᴘᴛᴀᴋɪ ᴇɴ ɢɪᴢᴇᴍʟɪ ᴋɪşɪ ᴋɪᴍ ?','ʜɪᴄ̧ sıʀғ ғᴀʏᴅᴀ sᴀɢ̆ʟᴀᴅıɢ̆ı ɪᴄ̧ɪɴ ʙɪʀɪʏʟᴇ ᴀʀᴋᴀᴅᴀş ᴋᴀʟᴅıɢ̆ıɴ ᴏʟᴅᴜ ᴍᴜ?','ʙᴜ ʜᴀʏᴀᴛᴛᴀ ʜɪᴄ̧ ᴋɪᴍsᴇʏᴇ sᴏ̈ʏʟᴇᴍᴇᴅɪɢ̆ɪɴ ʙɪʀ sıʀʀıɴ ᴠᴀʀ ᴍı?',
'ʙᴜ ᴏᴅᴀᴅᴀᴋɪ ᴇɴ sɪɴɪʀ ʙᴏᴢᴜᴄᴜ ᴋɪşɪ ᴋɪᴍ?','ʙɪʀ ᴜʏɢᴜʟᴀᴍᴀʏı ᴛᴇʟᴇғᴏɴᴜɴᴜᴢᴅᴀɴ sɪʟᴍᴇᴋ ᴢᴏʀᴜɴᴅᴀ ᴋᴀʟsᴀɴıᴢ ʜᴀɴɢɪsɪɴɪ sɪʟᴇʀᴅɪɴɪᴢ?','ᴇɴ sᴏɴ sᴏ̈ʏʟᴇᴅɪɢ̆ɪɴ ʏᴀʟᴀɴ ɴᴇᴅɪʀ?','ʙᴜ ɢʀᴜᴘᴛᴀ ᴋɪᴍsᴇɴɪɴ ᴀʀᴋᴀsıɴᴅᴀɴ ᴋᴏɴᴜşᴛᴜɴ ᴍᴜ ?','ᴄ̧ᴇşɪᴛʟɪ ʙᴀᴛıʟ ɪɴᴀɴᴄ̧ʟᴀʀıɴ ᴠᴀʀ ᴍı? ᴠᴀʀsᴀ ᴏɴʟᴀʀ ɴᴇʟᴇʀ?','ᴛᴇʟᴇғᴏɴᴜɴᴜᴢᴅᴀ ᴀʀᴀᴅıɢ̆ıɴ sᴏɴ şᴇʏ ɴᴇʏᴅɪ?','Bᴜ ɢʀᴜᴘᴛᴀ ᴋɪᴍsᴇɴɪɴ ᴀʀᴋᴀsıɴᴅᴀɴ ᴋᴏɴᴜşᴛᴜɴ ᴍᴜ ?','ᴍᴇᴠᴄᴜᴛ ᴇʀᴋᴇᴋ ᴀʀᴋᴀᴅᴀşıɴıɴ ʏᴀ ᴅᴀ ᴋıᴢ ᴀʀᴋᴀᴅᴀşıɴıɴ sᴇɴɪɴʟᴇ ᴀʏɴı ᴜ̈ɴɪᴠᴇʀsɪᴛᴇʏᴇ ɢɪᴛᴍᴇsɪɴɪ ɪsᴛᴇʀ ᴍɪsɪɴ?','ɢʀᴜᴘᴛᴀ ᴋɪᴍɪɴ ʜᴇsᴀʙıɴᴀ ɢɪʀᴍᴇᴋ ɪsᴛᴇʀsɪɴ?','ʙᴜ̈ʏᴜ̈ʏᴇɴ ʜᴀʏᴀʟɪ ʙɪʀ ᴀʀᴋᴀᴅᴀşıɴıᴢ ᴠᴀʀ ᴍıʏᴅı?','ᴍᴇᴠᴄᴜᴛ ᴇʀᴋᴇᴋ ᴀʀᴋᴀᴅᴀşıɴıɴ ʏᴀ ᴅᴀ ᴋıᴢ ᴀʀᴋᴀᴅᴀşıɴıɴ sᴇɴɪɴʟᴇ ᴀʏɴı ᴜ̈ɴɪᴠᴇʀsɪᴛᴇʏᴇ ɢɪᴛᴍᴇsɪɴɪ ɪsᴛᴇʀ ᴍɪsɪɴ?',
'ᴋᴀʀşı ᴄɪɴsᴛᴇ ɪʟᴋ ᴅɪᴋᴋᴀᴛɪɴɪ ᴄ̧ᴇᴋᴇɴ ɴᴇ?','ᴛᴇʟᴇғᴏɴᴜɴᴜᴢᴅᴀ ʜᴀɴɢɪ ᴜʏɢᴜʟᴀᴍᴀᴅᴀ ᴇɴ ᴄ̧ᴏᴋ ᴢᴀᴍᴀɴ ʜᴀʀᴄıʏᴏʀsᴜɴᴜᴢ?','şɪᴍᴅɪ sᴀɴᴀ ʙɪʀ ᴇᴠʟᴇɴᴍᴇ ᴛᴇᴋʟɪғɪ ɢᴇʟsᴇ ᴠᴇ sᴇᴠᴍᴇᴅɪɢ̆ɪɴ ʙɪʀɪ ᴏʟsᴀ, ᴠᴇ ʙᴜ sᴀɴᴀ sᴏɴ ɢᴇʟᴇᴄᴇᴋ ᴇᴠʟɪʟɪᴋ ᴛᴇᴋʟɪғɪ ᴏʟsᴀ ᴋᴀʙᴜʟ ᴇᴅᴇʀᴍɪʏᴅɪɴ?','ᴇʀᴋᴇᴋ ᴀʀᴋᴀᴅᴀşıɴ ᴠᴇʏᴀ ᴋıᴢ ᴀʀᴋᴀᴅᴀşıɴ sᴇɴɪ ʜɪᴄ̧ ᴜᴛᴀɴᴅıʀᴅı ᴍı?','ᴇɴ ᴛᴜʜᴀғ ᴛᴀᴋᴍᴀ ᴀᴅıɴ ɴᴇᴅɪʀ?','ʜɪᴄ̧ sıɴıғᴛᴀ ʀᴇᴢɪʟ ᴏʟᴅᴜɴ ᴍᴜ?','ɢʀᴜʙᴜɴ ɴᴇşᴇsɪ ᴋɪᴍ?','ʙɪʀ ᴜʏɢᴜʟᴀᴍᴀʏı ᴛᴇʟᴇғᴏɴᴜɴᴜᴢᴅᴀɴ sɪʟᴍᴇᴋ ᴢᴏʀᴜɴᴅᴀ ᴋᴀʟsᴀɴıᴢ ʜᴀɴɢɪsɪɴɪ sɪʟᴇʀᴅɪɴɪᴢ?','ʜᴀʏᴀᴛıɴᴅᴀ ʏᴀᴘᴛıɢ̆ıɴ ᴇɴ ᴄ̧ıʟɢıɴ şᴇʏ ɴᴇᴅɪʀ?','şɪᴍᴅɪ sᴀɴᴀ ʙɪʀ ᴇᴠʟᴇɴᴍᴇ ᴛᴇᴋʟɪғɪ ɢᴇʟsᴇ ᴠᴇ sᴇᴠᴍᴇᴅɪɢ̆ɪɴ ʙɪʀɪ ᴏʟsᴀ, ᴠᴇ ʙᴜ sᴀɴᴀ sᴏɴ ɢᴇʟᴇᴄᴇᴋ ᴇᴠʟɪʟɪᴋ ᴛᴇᴋʟɪғɪ ᴏʟsᴀ ᴋᴀʙᴜʟ ᴇᴅᴇʀᴍɪʏᴅɪɴ?',
'ʙᴇʏɴɪɴɪ ʙɪʀ ʀᴏʙᴏᴛᴀ ʏᴇʀʟᴇşᴛɪʀᴇʙɪʟɪʀ ᴠᴇ sᴏɴsᴜᴢᴀ ᴋᴀᴅᴀʀ ʙᴜ şᴇᴋɪʟᴅᴇ ʏᴀşᴀʏᴀʙɪʟsᴇᴅɪɴ,ʙᴜɴᴜ ʏᴀᴘᴀʀ ᴍıʏᴅıɴ?','Kᴀʀᴀɴʟıᴋᴛᴀɴ/ʏᴜ̈ᴋsᴇᴋʟɪᴋᴛᴇɴ ᴋᴏʀᴋᴀʀ ᴍısıɴ?','ᴇɴ ᴋᴏ̈ᴛᴜ̈ ɢʀᴜᴘ ʜᴀɴɢɪsɪᴅɪʀ?','ʜɪᴄ̧ sᴇᴠɢɪʟɪɴɪ ʙɪʀɪʏʟᴇ ᴀʟᴅᴀᴛᴛıɴ ᴍı?','ʜɪᴄ̧ sᴀʜᴛᴇ ᴋɪᴍʟɪᴋ ᴋᴜʟʟᴀɴᴅıɴ ᴍı?','ʙᴜ ɢʀᴜᴘᴅᴀ ᴇɴ ᴀᴢ ᴋɪᴍɪ sᴇᴠɪʏᴏʀsᴜɴ ᴠᴇ ɴᴇᴅᴇɴ?','ᴋᴜ̈ʟᴛᴜ̈ʀᴜ̈ᴍᴜ̈ᴢᴜ̈ɴ ᴇɴ ᴄ̧ᴏᴋ sᴇᴠᴅɪɢ̆ɪɴɪᴢ ʏᴀɴı ɴᴇᴅɪʀ?','ɢᴏ̈ʀᴅᴜ̈ɢ̆ᴜ̈ɴ ᴇɴ ɢᴀʀɪᴘ ʀᴜ̈ʏᴀ ɴᴇʏᴅɪ?','ᴀɪʟᴇɴɪɴ sᴇɴɪɴ ʜᴀᴋᴋıɴᴅᴀ ʙɪʟᴍᴇᴅɪɢ̆ɪɴᴇ sᴇᴠɪɴᴅɪɢ̆ɪɴ şᴇʏ ɴᴇᴅɪʀ?','ᴠᴜ̈ᴄᴜᴅᴜɴᴜɴ ʜᴀɴɢɪ ʙᴏ̈ʟᴜ̈ᴍʟᴇʀɪɴᴅᴇɴ ɢıᴅıᴋʟᴀɴıʏᴏʀsᴜɴ?','ʙᴜ ʜᴀʏᴀᴛᴛᴀ ʜɪᴄ̧ ᴋɪᴍsᴇʏᴇ sᴏ̈ʏʟᴇᴍᴇᴅɪɢ̆ɪɴ ʙɪʀ sıʀʀıɴ ᴠᴀʀ ᴍı?','ʙɪʀɪʏʟᴇ ᴄ̧ıᴋᴀʀᴋᴇɴ ʏᴀᴘᴛıɢ̆ıɴ ᴇɴ ᴜᴛᴀɴᴄ̧ ᴠᴇʀɪᴄɪ şᴇʏ ɴᴇʏᴅɪ?',
'ᴀʀᴋᴀᴅᴀşʟᴀʀıɴʟᴀ ʏᴀᴘᴍᴀʏı sᴇᴠᴅɪɢ̆ɪɴ ᴀᴍᴀ sᴇᴠɢɪʟɪɴɪɴ ᴏ̈ɴᴜ̈ɴᴅᴇ ᴀsʟᴀ ʏᴀᴘᴍᴀʏᴀᴄᴀɢ̆ıɴ şᴇʏ ɴᴇᴅɪʀ?','ᴜɴɪᴄᴏʀᴜɴ ᴍᴜ ᴏʟᴍᴀsıɴı ɪsᴛᴇʀᴅɪɴ ᴇᴊᴅᴇʀʜᴀɴ ᴍı?','şᴜ ᴀɴᴋɪ ʀᴜʜ ʜᴀʟɪɴᴇ ʙᴀᴋᴀʀᴀᴋ ɴᴇ ᴛᴜ̈ʀ ғɪʟᴍ ɪᴢʟᴇʀsɪɴ (ᴀᴋsɪʏᴏɴ/ᴅʀᴀᴍ/ʙɪʟɪᴍ ᴋᴜʀɢᴜ/ʀᴏᴍᴀɴᴛɪᴋ ᴋᴏᴍᴇᴅɪ/ʙɪʏᴏɢʀᴀғɪ/ғᴀɴᴛᴀsᴛɪᴋ)','ᴡᴇʙ ɢᴇᴄ̧ᴍɪşɪɴɪᴢɪ, ʙɪʀɪʟᴇʀɪ ɢᴏ̈ʀᴜ̈ʀsᴇ ᴜᴛᴀɴᴀᴄᴀɢ̆ıɴıᴢ şᴇʏ ɴᴇ ᴏʟᴜʀᴅᴜ?','ʜɪᴄ̧ sᴇᴠɢɪʟɪɴɪ ᴀʟᴅᴀᴛᴍᴀʏı ᴅᴜ̈şᴜ̈ɴᴅᴜ̈ɴ ᴍᴜ̈?','ʙɪʀɪsɪ ᴋıᴢ ᴀʀᴋᴀᴅᴀşıɴ / ᴇʀᴋᴇᴋ ᴀʀᴋᴀᴅᴀşıɴᴅᴀɴ ᴀʏʀıʟᴍᴀᴋ ɪᴄ̧ɪɴ sᴀɴᴀ 𝟷 ᴍɪʟʏᴏɴ ᴛʟ ᴏ̈ɴᴇʀsᴇʏᴅɪ, ʏᴀᴘᴀʀ ᴍıʏᴅıɴ?','ɪ̇ɴsᴀɴʟᴀʀıɴ sᴇɴɪɴ ʜᴀᴋᴋıɴᴅᴀ ʙɪʟᴍᴇsɪɴɪ ɪsᴛᴇᴅɪɢ̆ɪɴ şᴇʏ ɴᴇᴅɪʀ?','ʙᴜ ɢʀᴜᴘᴛᴀ ᴋɪᴍsᴇɴɪɴ ᴀʀᴋᴀsıɴᴅᴀɴ ᴋᴏɴᴜşᴛᴜɴ ᴍᴜ ?','şɪᴍᴅɪʏᴇ ᴋᴀᴅᴀʀ ɢᴏ̈ʀᴅᴜ̈ɢ̆ᴜ̈ᴍ ᴇɴ ɢᴀʀɪᴘ ʀᴜ̈ʏᴀʏı ᴀɴʟᴀᴛ.',
'şɪᴍᴅɪʏᴇ ᴋᴀᴅᴀʀ ʙɪʀ ʙᴀşᴋᴀsıɴᴀ sᴏ̈ʏʟᴇᴅɪɢ̆ɪɴ ᴇɴ ᴀᴄıᴍᴀsıᴢᴄᴀ şᴇʏ ɴᴇʏᴅɪ?','ᴅᴜ̈ɴʏᴀᴅᴀᴋɪ ʜᴇʀʜᴀɴɢɪ ʙɪʀɪɴɪ ᴛᴜ̈ʀᴋɪʏᴇ’ɴɪɴ ʙᴀşᴋᴀɴı ʏᴀᴘᴀʙɪʟsᴇʏᴅɪɴ ʙᴜ ᴋɪᴍ ᴏʟᴜʀᴅᴜ?','ᴀɪʟᴇɴɪᴢɪɴ ᴜʏɢᴜʟᴀᴅıɢ̆ı ᴇɴ ᴛᴜʜᴀғ ɢᴇʟᴇɴᴇᴋ ɴᴇᴅɪʀ?','ʙɪʀɪsɪ ᴋıᴢ ᴀʀᴋᴀᴅᴀşıɴ / ᴇʀᴋᴇᴋ ᴀʀᴋᴀᴅᴀşıɴᴅᴀɴ ᴀʏʀıʟᴍᴀᴋ ɪᴄ̧ɪɴ sᴀɴᴀ 𝟷 ᴍɪʟʏᴏɴ ᴛʟ ᴏ̈ɴᴇʀsᴇʏᴅɪ, ʏᴀᴘᴀʀ ᴍıʏᴅıɴ?','ᴋᴜ̈ʟᴛᴜ̈ʀᴜ̈ᴍᴜ̈ᴢᴜ̈ɴ ᴇɴ ᴄ̧ᴏᴋ sᴇᴠᴅɪɢ̆ɪɴɪᴢ ʏᴀɴı ɴᴇᴅɪʀ?','ɢʀᴜᴘᴛᴀ ᴋɪ ᴋᴀɴᴋᴀʟᴀʀıɴı ᴇᴛɪᴋᴇᴛʟᴇʀ ᴍɪsɪɴ ?','ᴅɪʀsᴇɢ̆ɪɴɪ ʏᴀʟᴀʏᴀʙɪʟɪʀ ᴍɪsɪɴ?','ᴋᴀᴅıɴ/ᴇʀᴋᴇᴋ ᴏʟᴍᴀɴıɴ ᴇɴ ᴋᴏ̈ᴛᴜ̈ ᴠᴇ ᴇɴ ɪʏɪ ʏᴀɴı ɴᴇᴅɪʀ?','Hᴀʏᴀᴛᴛᴀ ᴜɴᴜᴛᴍᴀᴅıɢ̆ıɴ ʙɪʀɪ ᴠᴀʀ ᴍı?','ᴀʟışᴠᴇʀɪşɪɴ ᴅɪʙɪɴᴇ ᴠᴜʀᴜʀᴋᴇɴ ᴇɴ ᴄ̧ᴏᴋ ʜᴀʀᴄᴀᴍᴀ ʏᴀᴘᴛıɢ̆ıɴ ɢᴜ̈ɴ ʜᴀɴɢɪsɪʏᴅɪ?','ʙᴜ ɢʀᴜᴘᴛᴀ ᴋɪᴍsᴇɴɪɴ ᴀʀᴋᴀsıɴᴅᴀɴ ᴋᴏɴᴜşᴛᴜɴ ᴍᴜ ?',
'ᴋᴇɴᴅɪɴɪ ᴇɴ ᴇᴢɪᴋ ʜɪssᴇᴛᴛɪɢ̆ɪɴ ᴀɴ ʜᴀɴɢɪsɪʏᴅɪ ?','ᴏʏᴜɴᴜ ᴏʏɴᴀʏᴀɴ ᴏʏᴜɴᴄᴜ ɢʀᴜʙᴜɴᴅᴀ ʏᴇʀ ᴀʟᴀɴʟᴀʀᴅᴀɴ ᴋɪᴍɪ ᴏ̈ᴘᴍᴇᴋ ɪsᴛᴇʀsɪɴ?','ʜɪᴄ̧ ʏᴀsᴀʏᴀ ᴀʏᴋıʀı ʙɪʀ şᴇʏʟᴇʀ ʏᴀᴘᴛıɢ̆ıɴ ᴏʟᴅᴜ ᴍᴜ?','ʜᴀʏᴀᴛıɴıɴ ɢᴇʀɪ ᴋᴀʟᴀɴıɴᴅᴀ sᴀᴅᴇᴄᴇ ʙɪʀ ᴋıʏᴀғᴇᴛ ɢɪʏᴇʙɪʟsᴇʏᴅɪɴ, ʙᴜ ᴋıʏᴀғᴇᴛɪɴ ʜᴀɴɢɪ ʀᴇɴᴋ ᴏʟᴜʀᴅᴜ?','şɪᴍᴅɪʏᴇ ᴋᴀᴅᴀʀ ʙᴀşᴋᴀsıɴᴀ sᴏ̈ʏʟᴇᴅɪɢ̆ɪɴ ᴇɴ ᴀɴʟᴀᴍʟı şᴇʏ ɴᴇʏᴅɪ?','ɢʀᴜᴘᴛᴀ ʙᴜʟᴜɴᴀɴ ᴇɴ ᴜʏᴜᴢ ᴋɪşɪ ᴋɪᴍ ?','ᴋɪᴍsᴇɴɪɴ sᴇɴɪɴ ʜᴀᴋᴋıɴᴅᴀ ʙɪʟᴍᴇᴅɪɢ̆ɪ ʙɪʀ şᴇʏ ɴᴇᴅɪʀ?','ʜɪᴄ̧ sıɴıғᴛᴀ ᴜʏᴜᴅᴜɴ ᴍᴜ?','ʜɪᴄ̧ ʏᴀsᴀʏᴀ ᴀʏᴋıʀı ʙɪʀ şᴇʏʟᴇʀ ʏᴀᴘᴛıɢ̆ıɴ ᴏʟᴅᴜ ᴍᴜ?','şɪᴍᴅɪʏᴇ ᴋᴀᴅᴀʀ ɢᴏ̈ʀᴅᴜ̈ɢ̆ᴜ̈ᴍ ᴇɴ ɢᴀʀɪᴘ ʀᴜ̈ʏᴀʏı ᴀɴʟᴀᴛ','ᴛᴏᴘʟᴜᴍᴅᴀ ᴇɴ ᴜᴛᴀɴᴄ̧ ᴠᴇʀɪᴄɪ ᴀɴıɴıᴢ ɴᴇʏᴅɪ?','ᴋᴀʀşı ᴄɪɴsᴛᴇ ɪʟᴋ ᴅɪᴋᴋᴀᴛɪɴɪ ᴄ̧ᴇᴋᴇɴ ɴᴇ?','ɪ̇ʟᴋ ɪşɪɴ ɴᴇʏᴅɪ?',
'ʙɪʀ ᴀʏɴᴀɴıɴ ᴏ̈ɴᴜ̈ɴᴅᴇ ʏᴀᴘᴛıɢ̆ıɴ ᴇɴ ᴄ̧ıʟɢıɴᴄᴀ şᴇʏ ɴᴇᴅɪʀ?','ɪ̇ɴsᴀɴʟᴀʀıɴ sɪᴢᴇ ɴᴇ sᴏʀᴍᴀsıɴᴅᴀɴ ʙıᴋᴛıɴıᴢ?ɢɪᴢʟɪᴅᴇɴ ɢɪᴢʟɪᴅᴇɴ sᴀᴅᴇᴄᴇ ᴏɴᴜɴ ɪᴄ̧ɪɴ ɢᴇʟᴅɪɢ̆ɪɴ ᴋɪᴍsᴇ ᴠᴀʀ ᴍı ɢʀᴜᴘᴛᴀ ?','ʜɪᴄ̧ ᴋɪᴍsᴇʏɪ ᴏ̈ᴢᴇʟᴅᴇɴ ʀᴀʜᴀᴛsıᴢ ᴇᴛᴛɪɴ ᴍɪ?','ɪ̇ɴsᴀɴʟᴀʀı ʏᴀɴᴀɴ ʙɪʀ ʙɪɴᴀᴅᴀɴ ᴋᴜʀᴛᴀʀıʏᴏʀ ᴏʟsᴀʏᴅıɴıᴢ ᴠᴇ ʙɪʀ ᴋɪşɪʏɪ ʙᴜ ɢʀᴜᴘᴅᴀɴ ɢᴇʀɪᴅᴇ ʙıʀᴀᴋᴍᴀᴋ ᴢᴏʀᴜɴᴅᴀ ᴋᴀʟıʀsᴀɴıᴢ, ᴋɪᴍ ᴏʟᴜʀᴅᴜ?','ʏᴇʀᴅᴇɴ ʙɪʀ şᴇʏɪ ᴀʟıᴘ ʜɪᴄ̧ ʏᴇᴅɪɴ ᴍɪ?','ɢʀᴜᴘᴛᴀ ᴋɪ ᴜ̈ᴄ̧ ᴋᴀɴᴋᴀɴı ᴇᴛɪᴋᴇᴛʟᴇʀ ᴍɪsɪɴ?','ᴋᴀʀᴀɴʟıᴋᴛᴀɴ/ʏᴜ̈ᴋsᴇᴋʟɪᴋᴛᴇɴ ᴋᴏʀᴋᴀʀ ᴍısıɴ?','ɢʀᴜʙᴜɴ ᴇɴ ʏᴀᴋışıᴋʟısı ᴋɪᴍ ?','ʀᴇᴀʟ ʜᴀʏᴀᴛᴛᴀ ᴛᴀɴıᴍᴀᴋ ɪsᴛᴇᴅɪɢ̆ɪɴ ᴋɪᴍsᴇ ᴠᴀʀ ᴍı ɢʀᴜᴘᴛᴀ ?','ɢʀᴜʙᴜɴ ᴇɴ ʏᴀᴋışıᴋʟısı ᴋɪᴍ ?','ᴄ̧ıᴋᴛıɢ̆ıɴ ᴇɴ ʏᴀşʟı ᴋɪşɪ ᴋɪᴍ?','ɢʀᴜʙᴜɴ ᴇɴ ɢᴜ̈ᴢᴇʟ ᴋıᴢı ᴋɪᴍ ?',
'ɢʀᴜᴘᴛᴀ ᴀᴅᴍɪɴ ᴏʟsᴀɴ ᴋɪᴍɪ ʙᴀɴʟᴀʀᴅıɴ ɴᴇᴅᴇɴ ?','ʜᴀғᴛᴀᴅᴀ ᴋᴀᴄ̧ ᴋᴇᴢ ᴀʏɴı ᴘᴀɴᴛᴏʟᴏɴᴜ ɢɪʏɪʏᴏʀsᴜɴ?','ᴀɪʟᴇɴɪᴢɪɴ ᴜʏɢᴜʟᴀᴅıɢ̆ı ᴇɴ ᴛᴜʜᴀғ ɢᴇʟᴇɴᴇᴋ ɴᴇᴅɪʀ?','ᴋᴇɴᴅɪɴɪ ᴇɴ ᴇᴢɪᴋ ʜɪssᴇᴛᴛɪɢ̆ɪɴ ᴀɴ ʜᴀɴɢɪsɪʏᴅɪ ?','ɢʀᴜᴘᴛᴀ ɴᴇғʀᴇᴛ ᴇᴛᴛɪɢ̆ɪɴ ʙɪʀɪ ᴠᴀʀ ᴍı?','ʙᴜʀᴅᴀ ᴋɪ ᴋɪᴍsᴇʏᴇ ʏᴀʟᴀɴ sᴏ̈ʏʟᴇᴅɪɴ ᴍɪ?','ʙɪʀ ɪʟɪşᴋɪᴅᴇᴋɪ ᴇɴ ʙᴜ̈ʏᴜ̈ᴋ ᴋᴏʀᴋᴜɴ ɴᴇᴅɪʀ?','ʙᴜ ʜᴀʏᴀᴛᴛᴀ ʜɪᴄ̧ ᴋɪᴍsᴇʏᴇ sᴏ̈ʏʟᴇᴍᴇᴅɪɢ̆ɪɴ ʙɪʀ sıʀʀıɴ ᴠᴀʀ ᴍı?','ɢʀᴜʙᴜɴ ᴏʟᴍᴀᴢsᴀ ᴏʟᴍᴀᴢ ᴅᴇᴅɪɢ̆ɪɴ şᴇʏɪ ɴᴇᴅɪʀ?','ɢʀᴜᴘᴛᴀᴋɪ sıʀᴅᴀşıɴ ᴋɪᴍ ?','ɢʀᴜʙᴜ ɴᴇ ᴋᴀᴅᴀʀ sᴇᴠɪʏᴏʀsᴜɴ ?','sᴀᴄ̧ʟᴀʀıɴı ᴜᴢᴀᴛᴍᴀʏı ᴅᴜ̈şᴜ̈ɴsᴇɴ ɴᴇ ᴋᴀᴅᴀʀ ᴜᴢᴀᴛıʀᴅıɴ?','ᴋᴇşᴋᴇ ᴏɴᴜɴ ʜᴀᴋᴋıɴᴅᴀ ʏᴀʟᴀɴ sᴏ̈ʏʟᴇsᴇʏᴅɪᴍ ᴅᴇᴅɪɢ̆ɪɴ şᴇʏ ɴᴇᴅɪʀ?','ɢʀᴜʙᴜɴ ᴇɴ ᴇɢᴏɪsᴛɪ ᴋɪᴍ ?','sᴏɴ ᴀᴛᴛıɢ̆ıɴ ᴍᴇsᴀᴊ ɴᴇʏᴅɪ?',
'ɢʀᴜᴘᴛᴀᴋɪ ᴇɴ sᴇᴠɢɪɢ̆ɪɴ ᴀᴅᴍɪɴ ᴋɪᴍ ?','ᴇɴ ᴜᴛᴀɴ ᴠᴇʀɪᴄɪ ᴋɪşɪsᴇʟ ʙᴀᴋıᴍ ᴀʟışᴋᴀɴʟıɢ̆ıɴ ɴᴇᴅɪʀ?','ɢʀᴜʙᴜ ɴᴇ ᴋᴀᴅᴀʀ sᴇᴠɪʏᴏʀsᴜɴ ?','ɢʀᴜᴘᴛᴀ ɴᴇʏɪ ᴅᴇɢ̆ɪşᴛɪʀᴍᴇᴋ ɪsᴛᴇʀᴅɪɴ?','ɪ̇ʟᴋ ɪşɪɴ ɴᴇʏᴅɪ?','ᴀɪʟᴇɴᴅᴇɴ ʙɪʀɪ sᴇɴɪ ʙᴜ ɢʀᴜᴘᴛᴀ ɢᴏ̈ʀsᴇ ɴᴇ ᴏʟᴜʀ ?','ɢʀᴜᴘᴛᴀ ɴᴇғʀᴇᴛ ᴇᴛᴛɪɢ̆ɪɴ ʙɪʀɪ ᴠᴀʀ ᴍı?','ᴋᴇɴᴅɪ ɢᴏ̈ʀᴜ̈ɴᴜşᴜ̈ɴᴜ̈ 𝟷 ɪʟᴇ 𝟷𝟶 ᴀʀᴀsıɴᴅᴀ ᴘᴜᴀɴʟᴀ :)','ʙɪʀ ᴏᴅᴀᴅᴀ ᴜᴢᴜɴ ʙɪʀ sᴜ̈ʀᴇ ʜᴀᴘsᴏʟᴀᴄᴀɢ̆ıɴı ᴅᴜ̈şᴜ̈ɴsᴇɴ ʏᴀɴıɴᴅᴀ ᴏʟᴍᴀsıɴı ɪsᴛᴇᴅɪɢ̆ɪɴ ᴜ̈ᴄ̧ şᴇʏ ɴᴇ ᴏʟᴜʀᴅᴜ?','ᴇɴ sᴏɴ ɴᴇ ᴢᴀᴍᴀɴ ʜᴜ̈ɴɢᴜ̈ʀ ʜᴜ̈ɴɢᴜ̈ʀ ᴀɢ̆ʟᴀᴅıɢ̆ıɴı ʜᴀᴛıʀʟıʏᴏʀ ᴍᴜsᴜɴ?','ɢʀᴜᴘᴛᴀ ʙᴜʟᴜɴᴀɴ ᴇɴ ᴜʏᴜᴢ ᴋɪşɪ ᴋɪᴍ ?','ᴋᴜʀᴛ ᴍᴜ ᴋᴇʟɪᴍᴇ ᴏʏᴜɴᴜ ᴍᴜ ?','ɢʀᴜᴘᴛᴀ ᴋɪᴍᴅᴇɴ ɢıᴄıᴋ ᴀʟıʏᴏʀsᴜɴ?','ɢʀᴜᴘᴛᴀ ᴏʟᴍᴀᴍᴀsıɴı ɪsᴛᴇᴅɪɢ̆ɪɴ ᴋɪşɪʏɪ ᴇᴛɪᴋᴇᴛʟᴇʀ ᴍɪsɪɴ?',
'ᴀᴋʀᴀʙᴀʟᴀʀıɴᴅᴀɴ ᴋɪᴍsᴇʏɪ ᴅᴀᴠᴇᴛ ᴇᴛᴛɪɴ ᴍɪ ɢʀᴜʙᴀ ?','ʜɪᴄ̧ ᴏᴋᴜʟᴅᴀ ᴋᴀᴠɢᴀ ᴇᴛᴛɪɴ ᴍɪ?','ʙɪʀɪɴɪɴ ᴛᴇʟᴇғᴏɴᴜɴᴅᴀ ɢᴏ̈ʀᴅᴜ̈ɢ̆ᴜ̈ɴ ᴇɴ ᴛᴜʜᴀғ şᴇʏ ɴᴇᴅɪʀ?','ɢʀᴜᴘ sᴇɴɪɴ ɪᴄ̧ɪɴ ɴᴇ ɪғᴀᴅᴇ ᴇᴅɪʏᴏʀ?','ɢʀᴜʙᴜɴ ᴇɴ ᴇɢᴏɪsᴛɪ ᴋɪᴍ ?','ʜɪᴄ̧ sıʀғ ғᴀʏᴅᴀ sᴀɢ̆ʟᴀᴅıɢ̆ı ɪᴄ̧ɪɴ ʙɪʀɪʏʟᴇ ᴀʀᴋᴀᴅᴀş ᴋᴀʟᴅıɢ̆ıɴ ᴏʟᴅᴜ ᴍᴜ?','ᴇɴ ᴛᴜʜᴀғ ᴋᴏʀᴋᴜɴᴜᴢ ɴᴇᴅɪʀ?','ᴋᴜʀᴛ ᴏʏᴜɴᴜɴᴜ sᴇᴠɪʏᴏʀ ᴍᴜsᴜɴ?','ᴇɴ sᴏɴ ɴᴇ ᴢᴀᴍᴀɴ ᴅɪşʟᴇʀɪɴɪ ғıʀᴄ̧ᴀʟᴀᴅıɴ?','ʜɪᴄ̧ ʏᴀşıɴ ʜᴀᴋᴋıɴᴅᴀ ʏᴀʟᴀɴ sᴏ̈ʏʟᴇᴅɪɴ ᴍɪ?','ɢʀᴜᴘᴛᴀ ᴋᴇşᴋᴇ ᴀʙɪᴍ/ᴀʙʟᴀᴍ ᴏʟsᴀʏᴅı ᴅᴇᴅɪɢ̆ɪɴ ᴋɪᴍsᴇ ᴠᴀʀ ᴍı ?','ʙɪʀ ʙᴏ̈ᴄᴇᴋ ɪsᴛɪʟᴀsı ɢᴇʀᴄ̧ᴇᴋʟᴇşsᴇ ʜᴀɴɢɪ ᴀʀᴋᴀᴅᴀşıɴ ʜᴀʏᴀᴛᴛᴀ ᴋᴀʟᴍᴀʏı ʙᴀşᴀʀıʀ?','ɢʀᴜᴘᴛᴀ ᴏʟᴍᴀᴍᴀsıɴı ɪsᴛᴇᴅɪɢ̆ɪɴ ᴋɪşɪʏɪ ᴇᴛɪᴋᴇᴛʟᴇʀ ᴍɪsɪɴ?','ʙᴜ ʜᴀʏᴀᴛᴛᴀ sᴇɴɪ ᴇɴ ᴄ̧ᴏᴋ ᴋıᴢᴅıʀᴀɴ şᴇʏ ɴᴇᴅɪʀ?',
'ᴇɴ ɪʏɪ ᴀʀᴋᴀᴅᴀşıɴıɴ sᴇɴɪɴʟᴇ ᴀʏɴı ᴜ̈ɴɪᴠᴇʀsɪᴛᴇʏᴇ ɢɪᴛᴍᴇsɪɴɪ ɪsᴛᴇʀ ᴍɪsɪɴ?','ᴇʀᴋᴇᴋ ᴀʀᴋᴀᴅᴀşıɴ ᴠᴇʏᴀ ᴋıᴢ ᴀʀᴋᴀᴅᴀşıɴ sᴇɴɪ ʜɪᴄ̧ ᴜᴛᴀɴᴅıʀᴅı ᴍı?','ɢʀᴜʙᴜ ɢᴇʀᴄ̧ᴇᴋᴛᴇɴ sᴇᴠɪʏᴏʀ ᴍᴜsᴜɴ?','ʙɪʀ ᴏᴅᴀᴅᴀ ᴜᴢᴜɴ ʙɪʀ sᴜ̈ʀᴇ ʜᴀᴘsᴏʟᴀᴄᴀɢ̆ıɴı ᴅᴜ̈şᴜ̈ɴsᴇɴ ʏᴀɴıɴᴅᴀ ᴏʟᴍᴀsıɴı ɪsᴛᴇᴅɪɢ̆ɪɴ ᴜ̈ᴄ̧ şᴇʏ ɴᴇ ᴏʟᴜʀᴅᴜ?','ʜᴀᴛıʀʟᴀᴅıɢ̆ıɴ ᴋᴀᴅᴀʀıʏʟᴀ ɪʟᴋ ᴀşıᴋ ᴏʟᴅᴜɢ̆ᴜɴ ᴜ̈ɴʟᴜ̈ ᴋɪᴍᴅɪ?','sᴏ̈ʏʟᴇᴅɪɢ̆ɪɴɪᴢ ᴠᴇʏᴀ ʏᴀᴘᴛıɢ̆ıɴıᴢ ʙɪʀ şᴇʏɪ sɪʟᴍᴇᴋ ɪᴄ̧ɪɴ ᴢᴀᴍᴀɴᴅᴀ ɢᴇʀɪʏᴇ ɢɪᴅᴇʙɪʟsᴇʏᴅɪɴɪᴢ, ʙᴜ ʜᴀɴɢɪ ʏıʟ ᴏʟᴜʀᴅᴜ?','ʙᴜ ɢʀᴜᴘᴅᴀᴋɪ sıʀ ᴛᴜᴛᴍᴀ  ᴋᴏɴᴜsᴜɴᴅᴀ ᴇɴ ᴄ̧ᴏᴋ ᴢᴏʀʟᴀɴᴀɴ ᴋɪşɪ ᴋɪᴍᴅɪʀ?','sᴇɴ ᴀᴅᴍɪɴ ᴏʟsᴀɴ ɴᴇʏɪ ᴅᴇɢ̆ɪşᴛɪʀɪʀᴅɪɴ ?','ɪ̇ʟᴋ ɪşɪɴ ɴᴇʏᴅɪ?','ɢʀᴜʙᴜ ɢᴇʀᴄ̧ᴇᴋᴛᴇɴ sᴇᴠɪʏᴏʀ ᴍᴜsᴜɴ?','ɢʀᴜᴘᴛᴀ ʜᴏşʟᴀɴᴅıɢ̆ıɴ ʙɪʀɪ ᴠᴀʀ ᴍı ?',
'ᴀɪʟᴇɴɪᴢɪɴ ᴜʏɢᴜʟᴀᴅıɢ̆ı ᴇɴ ᴛᴜʜᴀғ ɢᴇʟᴇɴᴇᴋ ɴᴇᴅɪʀ?','ʙɪʀ ʙᴏ̈ᴄᴇᴋ ɪsᴛɪʟᴀsı ɢᴇʀᴄ̧ᴇᴋʟᴇşsᴇ ʜᴀɴɢɪ ᴀʀᴋᴀᴅᴀşıɴ ʜᴀʏᴀᴛᴛᴀ ᴋᴀʟᴍᴀʏı ʙᴀşᴀʀıʀ?','ʙɪʀ ᴏᴅᴀᴅᴀ ᴜᴢᴜɴ ʙɪʀ sᴜ̈ʀᴇ ʜᴀᴘsᴏʟᴀᴄᴀɢ̆ıɴı ᴅᴜ̈şᴜ̈ɴsᴇɴ ʏᴀɴıɴᴅᴀ ᴏʟᴍᴀsıɴı ɪsᴛᴇᴅɪɢ̆ɪɴ ᴜ̈ᴄ̧ şᴇʏ ɴᴇ ᴏʟᴜʀᴅᴜ?','ʜᴀɴɢɪ ᴄ̧ᴏᴄᴜᴋ ғɪʟᴍɪɴɪ ᴛᴇᴋʀᴀʀ ᴛᴇᴋʀᴀʀ ɪᴢʟᴇʏᴇʙɪʟɪʀsɪɴ?','ʙᴜ ʜᴀʏᴀᴛᴛᴀᴋɪ ᴇɴ ʙᴜ̈ʏᴜ̈ᴋ ɢᴜ̈ᴠᴇɴsɪᴢʟɪɢ̆ɪɴ ɴᴇᴅɪʀ?','ʙɪʀ ᴜ̈ɴʟᴜ̈ ɪɴsᴛᴀɢʀᴀᴍ’ᴅᴀ sᴇɴɪ ᴛᴀᴋɪᴘ ᴇᴛsᴇʏᴅɪ ʙᴜ ᴜ̈ɴʟᴜ̈ɴᴜ̈ɴ ᴋɪᴍ ᴏʟᴍᴀsıɴı ɪsᴛᴇʀᴅɪɴ?','ʜɪᴄ̧ sıʀғ ғᴀʏᴅᴀ sᴀɢ̆ʟᴀᴅıɢ̆ı ɪᴄ̧ɪɴ ʙɪʀɪʏʟᴇ ᴀʀᴋᴀᴅᴀş ᴋᴀʟᴅıɢ̆ıɴ ᴏʟᴅᴜ ᴍᴜ?','ᴜɴɪᴄᴏʀᴜɴ ᴍᴜ ᴏʟᴍᴀsıɴı ɪsᴛᴇʀᴅɪɴ ᴇᴊᴅᴇʀʜᴀɴ ᴍı?','ɢʀᴜᴘᴛᴀ ᴀᴅᴍɪɴ ᴏʟsᴀɴ ᴋɪᴍɪ ʙᴀɴʟᴀʀᴅıɴ ɴᴇᴅᴇɴ ?','ɪ̇ɴsᴀɴʟᴀʀıɴ sᴇɴɪɴ ʜᴀᴋᴋıɴᴅᴀ ʙɪʟᴍᴇsɪɴɪ ɪsᴛᴇᴅɪɢ̆ɪɴ şᴇʏ ɴᴇᴅɪʀ?',
'ɢʀᴜᴘᴛᴀ ᴋɪᴍᴅᴇɴ ɢıᴄıᴋ ᴀʟıʏᴏʀsᴜɴ?','ᴍᴇᴠᴄᴜᴛ ᴇʀᴋᴇᴋ ᴀʀᴋᴀᴅᴀşıɴıɴ ʏᴀ ᴅᴀ ᴋıᴢ ᴀʀᴋᴀᴅᴀşıɴıɴ sᴇɴɪɴʟᴇ ᴀʏɴı ᴜ̈ɴɪᴠᴇʀsɪᴛᴇʏᴇ ɢɪᴛᴍᴇsɪɴɪ ɪsᴛᴇʀ ᴍɪsɪɴ?','ɢʀᴜᴘᴛᴀ ʜᴏşʟᴀɴᴅıɢ̆ıɴ ʙɪʀɪ ᴠᴀʀ ᴍı ?','ᴡᴇʙ ɢᴇᴄ̧ᴍɪşɪɴɪᴢɪ, ʙɪʀɪʟᴇʀɪ ɢᴏ̈ʀᴜ̈ʀsᴇ ᴜᴛᴀɴᴀᴄᴀɢ̆ıɴıᴢ şᴇʏ ɴᴇ ᴏʟᴜʀᴅᴜ?','ɢʀᴜᴘᴛᴀ ᴋᴇşᴋᴇ ᴀʙɪᴍ/ᴀʙʟᴀᴍ ᴏʟsᴀʏᴅı ᴅᴇᴅɪɢ̆ɪɴ ᴋɪᴍsᴇ ᴠᴀʀ ᴍı ?','ᴜʏᴋᴜɴᴅᴀ ᴋᴏɴᴜşᴜʀ ᴍᴜsᴜɴ?','sıɴıғᴛᴀ ʜɪᴄ̧ ᴜʏᴜʏᴀ ᴋᴀʟᴅıɴ ᴍı?','ᴋɪᴍsᴇɴɪɴ sᴇɴɪɴ ʜᴀᴋᴋıɴᴅᴀ ʙɪʟᴍᴇᴅɪɢ̆ɪ ʙɪʀ şᴇʏ ɴᴇᴅɪʀ?','ɪʟᴇʀᴅᴇ ᴄ̧ᴏᴄᴜɢ̆ᴜɴ ᴏʟᴜʀsᴀ ɴᴇ ɪsɪᴍ ᴋᴏʏᴍᴀᴋ ɪsᴛᴇʀsɪɴ?','sᴜ̈ᴘᴇʀ ᴋᴀʜʀᴀᴍᴀɴʟᴀʀ ɢᴇʀᴄ̧ᴇᴋᴛᴇɴ ᴠᴀʀ ᴏʟsᴀʏᴅı ᴅᴜ̈ɴʏᴀ ɴᴀsıʟ ʙɪʀ ʏᴇʀ ᴏʟᴜʀᴅᴜ?','ɢʀᴜᴘᴛᴀ ᴋɪᴍɪɴ ʜᴇsᴀʙıɴᴀ ɢɪʀᴍᴇᴋ ɪsᴛᴇʀsɪɴ?','ɢɪʀᴅɪɢ̆ɪɴɪᴢ ᴇɴ sᴀᴄ̧ᴍᴀ ᴛᴀʀᴛışᴍᴀ ɴᴇᴅɪʀ?','ɢʀᴜᴘᴛᴀ ɴᴇғʀᴇᴛ ᴇᴛᴛɪɢ̆ɪɴ ʙɪʀɪ ᴠᴀʀ ᴍı?',
'ᴛᴀᴍ ᴀɴʟᴀᴍıʏʟᴀ ᴇɴ sᴏɴ ɴᴇ ᴢᴀᴍᴀɴ ʏᴀʟᴀɴ sᴏ̈ʏʟᴇᴅɪɴ?','ʜɪᴄ̧ sᴇᴠɢɪʟɪɴɪ ᴀʟᴅᴀᴛᴍᴀʏı ᴅᴜ̈şᴜ̈ɴᴅᴜ̈ɴ ᴍᴜ̈?','ᴇɴ sᴇᴠᴅɪɢ̆ɪɴ ᴘɪᴊᴀᴍᴀʟᴀʀ ɴᴇʏᴇ ʙᴇɴᴢɪʏᴏʀ?','ʜᴀᴋᴋıɴᴅᴀ ʏᴀʟᴀɴ sᴏ̈ʏʟᴇᴅɪɢ̆ɪɴ ᴇɴ ᴋᴏ̈ᴛᴜ̈ şᴇʏ ɴᴇᴅɪʀ?','ᴇɴ ᴋᴏ̈ᴛᴜ̈ ᴀʟışᴋᴀɴʟıɢ̆ıɴıᴢ ɴᴇᴅɪʀ?','ʙᴜ ʜᴀʏᴀᴛᴛᴀᴋɪ ᴇɴ ʙᴜ̈ʏᴜ̈ᴋ ɢᴜ̈ᴠᴇɴsɪᴢʟɪɢ̆ɪɴ ɴᴇᴅɪʀ?','ʜɪᴄ̧ ᴋɪᴍsᴇʏɪ ᴏ̈ᴢᴇʟᴅᴇɴ ʀᴀʜᴀᴛsıᴢ ᴇᴛᴛɪɴ ᴍɪ?','sᴇᴠᴍᴇᴅɪɢ̆ɪɴ ᴋᴏ̈ᴛᴜ̈ ʜᴜʏᴜɴ ᴠᴀʀ ᴍı?','sᴀᴄ̧ʟᴀʀıɴı ᴜᴢᴀᴛᴍᴀʏı ᴅᴜ̈şᴜ̈ɴsᴇɴ ɴᴇ ᴋᴀᴅᴀʀ ᴜᴢᴀᴛıʀᴅıɴ?','ʜᴀʏᴀʟɪɴᴅᴇᴋɪ ɪş ɴᴇ?','ʜɪᴄ̧ ᴍᴀsᴀɴıɴ ᴀʟᴛıɴᴀ sᴀᴋıᴢ ᴀᴛᴛıɴ ᴍı?','ʏᴇʀᴅᴇɴ ʙɪʀ şᴇʏɪ ᴀʟıᴘ ʜɪᴄ̧ ʏᴇᴅɪɴ ᴍɪ?','ɢʀᴜʙᴜɴ ᴋʀᴀʟı ᴋɪᴍ?','ᴋᴜʀᴛ ᴏʏᴜɴᴜɴᴜ sᴇᴠɪʏᴏʀ ᴍᴜsᴜɴ?sᴘᴏʀ ʏᴀᴘᴀʀ ᴍısıɴ?','ɢʀᴜᴘᴛᴀ ᴀɢ̆ᴢıɴı ʙᴜʀɴᴜɴᴜ ᴋıʀᴀʀıᴍ ᴅᴇᴅɪɢ̆ɪɴ ᴋɪᴍsᴇ ᴠᴀʀ ᴍı ?','ɢʀᴜᴘᴛᴀᴋɪ ᴇɴ sᴇᴠɢɪɢ̆ɪɴ ᴀᴅᴍɪɴ ᴋɪᴍ ?',
'ᴅɪʀsᴇɢ̆ɪɴɪ ʏᴀʟᴀʏᴀʙɪʟɪʀ ᴍɪsɪɴ?','ᴍᴇssɪ ᴍɪ ʀᴏɴᴀʟᴅᴏ ᴍᴜ?','şɪᴍᴅɪʏᴇ ᴋᴀᴅᴀʀ ɢᴏ̈ʀᴅᴜ̈ɢ̆ᴜ̈ᴍ ᴇɴ ɢᴀʀɪᴘ ʀᴜ̈ʏᴀʏı ᴀɴʟᴀᴛ.','ʙᴜ ʏıʟ ʜᴀʏᴀᴛıɴᴅᴀ ɴᴇʏɪ ᴅᴇɢ̆ɪşᴍᴇʏɪ ᴜʏɢᴜɴ ɢᴏ̈ʀᴜ̈ʏᴏʀsᴜɴ?','ᴇɴ sᴏɴ ɴᴇ ᴢᴀᴍᴀɴ ʜᴜ̈ɴɢᴜ̈ʀ ʜᴜ̈ɴɢᴜ̈ʀ ᴀɢ̆ʟᴀᴅıɢ̆ıɴı ʜᴀᴛıʀʟıʏᴏʀ ᴍᴜsᴜɴ?','şɪᴍᴅɪʏᴇ ᴋᴀᴅᴀʀ ʜɪᴄ̧ ᴀʀᴀʟıᴋsıᴢ 𝟷𝟸 sᴀᴀᴛᴛᴇɴ ғᴀᴢʟᴀ ᴜʏᴜᴅᴜɢ̆ᴜɴ ᴏʟᴅᴜ ᴍᴜ?','ᴛᴇʟᴇғᴏɴᴅᴀ ᴀʀᴀᴅıɢ̆ıɴ sᴏɴ şᴇʏ ɴᴇʏᴅɪ?','ʙᴜ ʜᴀʏᴀᴛᴛᴀ şɪᴍᴅɪʏᴇ ᴋᴀᴅᴀʀ ʏᴀᴘᴛıɢ̆ıɴ ᴇɴ ʙᴜ̈ʏᴜ̈ᴋ ʜᴀᴛᴀ ɴᴇᴅɪʀ?','ɢʀᴜʙᴜɴ ᴇɴ ᴇɢᴏɪsᴛɪ ᴋɪᴍ ?','ʜɪᴄ̧ ʏᴀsᴀʏᴀ ᴀʏᴋıʀı ʙɪʀ şᴇʏʟᴇʀ ʏᴀᴘᴛıɢ̆ıɴ ᴏʟᴅᴜ ᴍᴜ?','ᴀᴋʀᴀʙᴀʟᴀʀıɴᴅᴀɴ ᴋɪᴍsᴇʏɪ ᴅᴀᴠᴇᴛ ᴇᴛᴛɪɴ ᴍɪ ɢʀᴜʙᴀ ?','ɢʀᴜʙᴜ ɴᴇ ᴋᴀᴅᴀʀ sᴇᴠɪʏᴏʀsᴜɴ?','ɢʀᴜᴘᴛᴀɴ ᴜᴢᴀᴋ ᴋᴀᴄ̧ ᴅᴀᴋɪᴋᴀ ᴅᴜʀᴀʙɪʟɪʀsɪɴ ?','sᴏ̈ʏʟᴇᴅɪɢ̆ɪɴ ᴇɴ sᴏɴ ʏᴀʟᴀɴ ɴᴇʏᴅɪ?','ᴄ̧ᴇşɪᴛʟɪ ʙᴀᴛıʟ ɪɴᴀɴᴄ̧ʟᴀʀıɴ ᴠᴀʀ ᴍı, ᴠᴀʀsᴀ ᴏɴʟᴀʀ ɴᴇʟᴇʀ?',
'ʙɪʀ sıɴᴀᴠᴅᴀɴ ᴀʟᴅıɢ̆ıɴ ᴇɴ ᴋᴏ̈ᴛᴜ̈ ᴘᴜᴀɴ ɴᴇʏᴅɪ?','ʙɪʀ sıɴᴀᴠᴅᴀɴ ᴀʟᴅıɢ̆ıɴ ᴇɴ ᴋᴏ̈ᴛᴜ̈ ᴘᴜᴀɴ ɴᴇʏᴅɪ?','ʜᴀғᴛᴀᴅᴀ ᴋᴀᴄ̧ ᴋᴇᴢ ᴀʏɴı ᴘᴀɴᴛᴏʟᴏɴᴜ ɢɪʏɪʏᴏʀsᴜɴ?',
'Bu Grupta En Çok Sevdiğin Kişi Kimdir ...','En Çok Gitmek İstediğin Ülke Neresidir ...','Medeni Halin Nedir ...','Özlediğin Bir Kimse Var Mı ...','Fotojenik Misin Kanka ...','Dans Etmeyi Sever Misin ...','Eski Sevgilinin Adı Ne ...','En Sevdigin Film Hangisi ...','En Sevdiğin Sanatçı Kim ...','Ünlü veya Fenomen Olmak İster Misin ...','Gözlerinin Rengi Nedir ...','Boyun Kaç Santim :)',
'Bugün için Bir Planın Var Mı ...','Birini Kahraman Yapan Nedir ...','Bir Dilek Hakkın Olsa Ne Dilerdim ...','Çocukken En Büyük Hayalin Neydi ...','Aşka İnanır Mısın ...','Bir Hedefin Var Mı ...','Karanlıktan Korkar Misin ...','Müzik Dinlemeyi Sever Misin ...','Sizce Anlaşılmak Kolay Mı ...','En Sevdiğin Ders Nedir ...','Nabiyosun Aslanım ...',
'Bu Grupta Sevdiğin Birini Etiketle ...','Bu Gruptaki En Yakışıklı Kişiyi Etiketleyin ...','Bu Gruptaki En Güzel Kız Kim ...','Sizce Gruptaki En Akıllı Kişi Kim ...','Kadere İnanır Mısın ...','Hayatından Memnun Musun ...','Hey, Sen Çok Şanslısın ...','En sevdiğin Ninja Kaplumbağa hangisiydi ...','Güliver olsaydın devler ülkesine mi yoksa cüceler ülkesine mi düşmek isterdin ...',
'En sevdiğin Pokemon hangisi ...','Çocukken izlemeyi en çok sevdiğin çizgi filmler hangileriydi ...','Dünyaya bir dahaki gelişinde hayvan olarak gelseydin hangi hayvan olmak isterdin ...','Bir şiir olsaydın hangi şiir olurdun ...','En sevdiğin Ninja Kaplumbağa hangisiydi ...','Issız bir adaya düşseydin yanına kesinlikle ‘’almayacağın’’ üç şey ne olurdu ...','Küçükken hiç pembe dizi izledin mi, İzlediysen hangisi ...',
'Sihirli bir değneğin olsaydı öncelikle neyi değiştirirdin ...','Arkadaşının sırrını 1 milyon dolar karşılığında ifşa eder miydin ...','Bir dizinin içine ışınlanmak isteseydin bu hangi dizi olurdu ...','Filmlerdeki kötü karakterlerden biri olsaydın hangisi olurdun ...','Küçükken oynamayı en sevdiğin atari oyunu hangisiydi ...','Şu an okuduğun iyi bir kitap var mı , Öneriyor musun ...','Hangi dizileri izliyorsun ...','En son hangi filmi izledin ...',
'Telefonunuzda olmadan yaşayamayacağınız herhangi bir uygulama var mı ...','Hayatın geri kalanında sadece bir film türünü izleyebiliceksen, ne olurdu ...','Herkesin sevdiği sizin nefret ettiğiniz bir kitap var mı, ya da tam tersi ...','Seni ağlatan en son film ne oldu, veya yüksek sesle güldüren ...','İnstagramda kesin takip et dediğin birisi var mı ...','En sevdiğin kitabın ismi ne ...','En son hangi diziyi tek oturuşta bitirdin ...',
'Çocukluğunda en sevdiğin çizgi film hangisiydi ...','Çocukluğunda en sevdiğin çizgi film karakteri hangisiydi ...','İzlemeyi en çok sevdiğin film türü ne ...','Telefonunun ekran süresi ortalama kaç saat ...','Spor yapmayı sever misin ...','Voleybol maçları izler misin ...','Sevdiğin spor dalı ne ...','Çocukken aşık olduğun kurgusal bir karakter var mıydı ...','Sonsuza kadar sadece bir kitap okuyacak olsan bu hangi kitap olurdu ...',
'En sevdiğin distopik eser hangisi ...','Hangi tür kitaplar okumayı seviyorsun ...','Kahve içmek istediğin kitap karakteri var mı ...','Takip ettiğin bir influencer var mı ...','En çok hangi influencerın önerdiği ürünleri kullanıyorsun ...','Okurken ağlamana  neden olacak bir kitap oldu mu ...','En sevdiğin yazar kim ...','En çok hangi dijital platformu kullanıyorsun ...',
'Hayatta gerçekleştirmek istediğin bir hayalin var mı?', 'Kaç tane kız aradaşın oldu ?','Nefret ettiğiniz ancak yine de kullandığın bir uygulama var mı?','En tuhaf korkun nedir?','Hangi takımı tutuyorsun ?','Romayı senmi yaktın?','Fiziksel olarak sana en acı veren deneyimin ne oldu?','Hangi yılda doğdun?','Boyun kaç ?','En sevdiğin hobi nedir?','Nasılsın ?','Gruptaki gizli aşık olduğun kim?',
'Nerelisin?','Naber nasıl gidiyor?','Grupta nefret ettiğin kişi kim?','Kaç tane sevgilin oldu?','Gruptaki partnerin kim?','Kendini 3 kelime ile anlatırmısın','Selam ne yapıyorsun?','En son okuduğun kitabın adı neydi','Grubu yakacakmışsın doğru mu?','En sevdiğin müzik nedir?','Googlede en son neye baktın?','Okumayı en çok sevdiğin kitap türü nedir ...','Çocukluğundan unutmadığın bir çizgi film var mı ...',
'Aşk mı? para mı?','En son yaptığın en saçma olay neydi?','Keşke şu olsada yesek dediğin şey neydi?','Karşı cinste aradığın krater nedir?','Karşı cinsin ilk neresine bakıyorsun?','Grupta sevdiğin 3 kişiyi etiketler misin?','Grupta en sevmediğin 3 kişiyi etiketler misin?','Grupta işte aradığım eş adayı dediğin kişiyi etiketler misin?','En Sevdiğin Renk Nedir ...',
'Aşkın yaşı yoktur diyorlar doğru mu?','Bir adaya düşsen yanına alacağın üç şey ne olurdu?','Grupta sevgilin var mı?','İnstagrama günde kaç story atıyorsun?','Hangi şehirde yaşıyorsun','Şehrini üç kelime ile anlatır mısın?','Memleketini üç kelime ile anlatır mısın?','Geçmişe dönüp yaşadığın bir olayı silebilmen mümkün olsaydı hangi olay olurdu?',
)

# BAŞLANGIÇ MESAJI 
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     await event.reply(f"{startmesaj}", buttons=(
                      [
                      Button.url('➕  ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ  ➕', f'https://t.me/{BOT_USERNAME}?startgroup=a'),
                    ],[
                      Button.inline("📚 ᴋᴏᴍᴜᴛʟᴀʀ", data="help"),
                      Button.url('🗨️ ʙɪʟɢɪ ᴋᴀɴᴀʟɪ', f'https://t.me/{GROUP_SUPPORT}')
		      ]
                  ),
                link_preview=False)

  if event.is_group:
    return await client.send_message(event.chat_id, f"{startmesaj}", buttons=(
                      [
                      Button.url('➕  ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ  ➕', f'https://t.me/{BOT_USERNAME}?startgroup=a'),
                    ],[
                      Button.inline("📚 ᴋᴏᴍᴜᴛʟᴀʀ", data="help"),
                      Button.url('🗨️ ʙɪʟɢɪ ᴋᴀɴᴀʟɪ', f'https://t.me/{GROUP_SUPPORT}')
		      ]
                  ),
                link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="start"))
async def start(event):
    await event.edit(f"{startmesaj}", buttons=(
                     [
                      Button.url('➕  ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ  ➕', f'https://t.me/{BOT_USERNAME}?startgroup=a'),
                    ],[
	              Button.inline("📚 ᴋᴏᴍᴜᴛʟᴀʀ", data="help"),
                      Button.url('🗨️ ʙɪʟɢɪ ᴋᴀɴᴀʟɪ', f'https://t.me/{GROUP_SUPPORT}')
                    ]
                  ),
                link_preview=False)
    
@client.on(events.callbackquery.CallbackQuery(data="help"))
async def help(event):
    await event.edit(f"{startbutton}  **👨🏻‍💻 [{OWNERNAME}](tg://openmessage?user_id={OWNER_ID})**", buttons=(

                    [
                      Button.inline("🗨️ ᴇᴛɪᴋᴇᴛ ᴋᴏᴍᴜᴛ", data="tag1"),
                      Button.inline("📚 ᴇxᴛʀᴀ ᴋᴏᴍᴜᴛ", data="tag2")
		      ],[
                      Button.inline("🔥 ᴇɢ̆ʟᴇɴᴄᴇ ᴋᴏᴍᴜᴛ", data="tag4"),
		      Button.inline("🧑🏻‍💻 sᴀʜɪᴘ ᴋᴏᴍᴜᴛ", data="tag3")
                  ],[
                      Button.inline("➡️ ɢᴇʀɪ ᴅᴏ̈ɴ", data="start")
                    ]
                 ),
               link_preview=False)    

@client.on(events.callbackquery.CallbackQuery(data="tag1"))
async def tag1(event):
    await event.edit(f"**🔺 ᴇᴛɪᴋᴇᴛ ᴋᴏᴍᴜᴛ 🔺\n\n» /utag\n   - ᴜ̈ʏᴇʟᴇʀɪ ᴛᴏᴘʟᴜ ᴇᴛɪᴋᴇᴛʟᴇʀɪᴍ .\n\n» /tag\n   - ᴜ̈ʏᴇʟᴇʀɪ ᴛᴇᴋ ᴛᴇᴋ ᴇᴛɪᴋᴇᴛʟᴇʀɪᴍ . \n\n» /atag\n   - ʏᴏ̈ɴᴇᴛɪᴄɪʟᴇʀɪ ᴛᴇᴋ ᴛᴇᴋ ᴇᴛɪᴋᴇᴛʟᴇʀɪᴍ .\n\n» /etag\n   - ᴜ̈ʏᴇʟᴇʀɪ ᴇᴍᴏᴊɪʟᴇʀʟᴇ ᴇᴛɪᴋᴇᴛʟᴇʀɪᴍ .\n\n» /rtag\n   - ᴜ̈ʏᴇʟᴇʀɪ ʀᴇɴᴋʟᴇʀʟᴇ ᴇᴛɪᴋᴇᴛʟᴇʀɪᴍ .\n\n» /btag\n   - ᴜ̈ʏᴇʟᴇʀɪ ʙᴀʏʀᴀᴋʟᴀʀʟᴀ ᴇᴛɪᴋᴇᴛʟᴇʀɪᴍ .\n\n» /ktag\n   - ᴜ̈ʏᴇʟᴇʀɪ ᴋᴀʀᴛʟᴀʀʟᴀ ᴇᴛɪᴋᴇᴛʟᴇʀɪᴍ .\n\n» /stag\n   - ᴜ̈ʏᴇʟᴇʀɪ sᴏ̈ᴢʟᴇʀʟᴇ ᴇᴛɪᴋᴇᴛʟᴇʀɪᴍ .\n\n» /vtag\n   - ᴜ̈ʏᴇʟᴇʀɪ sᴏʀᴜʟᴀʀʟᴀ ᴇᴛɪᴋᴇᴛʟᴇʀɪᴍ .\n\n» /otag\n   - ᴜ̈ʏᴇʟᴇʀɪ ʀᴜ̈ᴛʙᴇʟᴇʀʟᴇ ᴇᴛɪᴋᴇᴛʟᴇʀɪᴍ .\n\n» /cancel\n   - ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴅᴜʀᴅᴜʀᴜʀᴜᴍ .\n\n» /reload\n   - ᴀᴅᴍɪɴ ʟɪsᴛᴇsɪɴɪ ɢᴜ̈ɴᴄᴇʟʟᴇʀɪᴍ .**", buttons=(
                     [
                      Button.inline("➡️ ɢᴇʀɪ ᴅᴏ̈ɴ", data="help")
                     ]
                   ), 
                 link_preview=False)                      

@client.on(events.callbackquery.CallbackQuery(data="tag2"))
async def tag2(event):
    await event.edit(f"**🔺 ᴇxᴛʀᴀ ᴋᴏᴍᴜᴛ 🔺\n\n» /bul\n   - ᴀɴɪɴᴅᴀ şᴀʀᴋɪ ɪɴᴅɪʀɪʀɪᴍ .\n\n» /vbul\n   - ᴀɴɪɴᴅᴀ ᴠɪᴅᴇᴏ ɪɴᴅɪʀɪʀɪᴍ .\n\n» /ara\n   - ʟɪɴᴋ ʜᴀʟɪɴᴅᴇ ɪɴᴅɪʀɪʀɪᴍ .\n\n» /bots\n   - ɢʀᴜᴘᴛᴀᴋɪ ʙᴏᴛʟᴀʀɪ ɢᴏ̈sᴛᴇʀɪʀɪᴍ .\n\n» /admins\n   - ɢʀᴜᴘᴛᴀᴋɪ ᴀᴅᴍɪɴʟᴇʀɪ ɢᴏ̈sᴛᴇʀɪʀɪᴍ .\n\n» /dels\n   - ᴛᴏᴘʟᴜ ᴍᴇsᴀᴊ sɪʟᴇʀɪᴍ .\n\n» /id\n   - ɢʀᴜᴘ & ᴋᴜʟʟᴀɴɪᴄɪ ɪᴅ'sɪɴɪ ᴏ̈ɢ̆ʀᴇɴɪɴ .\n\n» /iletisim\n   - ʙɪᴢɪᴍʟᴇ ɪʟᴇᴛɪşɪᴍᴇ ɢᴇᴄ̧ɪɴ .\n\n» /grup\n   - ɢʀᴜᴘ ʜᴀᴋᴋɪɴᴅᴀ ʙɪʟɢɪ ᴠᴇʀɪʀɪᴍ .**",
		     buttons=(
                     [
                      Button.inline("➡️ ɢᴇʀɪ ᴅᴏ̈ɴ", data="help") 
                     ]
                   ),  
                 link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="tag3"))
async def handler(event):
       sender = await event.get_sender()
       if sender.id in OWNER:
            await event.edit(f"**🔺 sᴀʜɪᴘ ᴋᴏᴍᴜᴛ 🔺\n\n» /istatistik\n   - ɪsᴛᴀᴛɪsᴛɪᴋʟᴇʀɪᴍɪ ɢᴏ̈sᴛᴇʀɪʀɪᴍ .\n\n» /reklam\n   - ɢʀᴜᴘʟᴀʀᴀ ʀᴇᴋʟᴀᴍ ᴀᴛᴀʀɪᴍ .\n\n» /block\n   - ɪsᴛᴇᴅɪɢ̆ɪɴ ᴋɪşɪʏɪ ʏᴀsᴀᴋʟᴀʀɪᴍ .\n\n» /unblock\n   - ᴋɪşɪɴɪɴ ʏᴀsᴀɢ̆ɪɴɪ ᴋᴀʟᴅɪʀɪʀɪᴍ .\n\n» /blocklist\n   - ʏᴀsᴀᴋʟɪʟᴀʀɪɴ ʟɪsᴛᴇsɪɴɪ ɢᴏ̈sᴛᴇʀɪʀɪᴍ .**", buttons=(
                     [
                      Button.inline("➡️ ɢᴇʀɪ ᴅᴏ̈ɴ", data="help") 
                     ]
                   ),  
                 link_preview=False)
       if sender.id not in OWNER:
                 await event.reply(f"**➻ ᴏʟᴀᴍᴀᴢ, sᴀʜɪʙɪᴍ ᴅᴇɢɪʟsɪɴ 😳\n» ɴᴏᴛ : sᴀᴅᴇᴄᴇ sᴀʜɪʙɪᴍ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀ .**")
	
@client.on(events.callbackquery.CallbackQuery(data="tag4"))
async def tag4(event):
    await event.edit(f"**🔺  ᴇɢ̆ʟᴇɴᴄᴇ ᴋᴏᴍᴜᴛ  🔺\n\n» /sohbetmod\n   - sᴏʜʙᴇᴛ ᴍᴏᴅᴜ ɪᴄ̧ɪɴ ᴋᴜʟʟᴀɴɪɴ  ...\n\n» /d\n   - ᴅᴏɢ̆ʀᴜʟᴜᴋ sᴏʀᴜsᴜ sᴏʀᴀʀɪᴍ .\n\n» /c\n   - ᴄᴇsᴀʀᴇᴛ sᴏʀᴜsᴜ sᴏʀᴀʀɪᴍ .\n\n» /soz\n   - ᴄ̧ᴇşɪᴛʟɪ sᴏ̈ᴢʟᴇʀ ᴀᴛᴀʀɪᴍ .\n\n» /eros\n   -  ɢʀᴜᴘᴛᴀᴋɪ ᴜ̈ʏᴇʟᴇʀɪ sʜɪᴘʟᴇʀɪᴍ .\n\n» /slap\n   - ᴇɢ̆ʟᴇɴᴍᴇᴋ ɪᴄ̧ɪɴ ᴋᴜʟʟᴀɴɪɴ .\n\n» /turet\n   - ᴋᴇʟɪᴍᴇ ᴛᴜ̈ʀᴇᴛ ᴏʏᴜɴᴜ ᴀᴄ̧ᴀʀɪᴍ .\n\n» /kapat\n   - ᴋᴇʟɪᴍᴇ ᴛᴜ̈ʀᴇᴛ ᴏʏᴜɴᴜ ᴋᴀᴘᴀᴛɪʀɪᴍ .\n\n» /pass\n   - ᴋᴇʟɪᴍᴇʏɪ ᴘᴀss ɢᴇᴄ̧ᴇʀɪᴍ .\n\n» /yas\n   - ᴅᴏɢ̆ᴜᴍ ɢᴜ̈ɴᴜ̈ɴᴜ̈ᴢᴜ̈ sᴏ̈ʏʟᴇʀɪᴍ .\n\n» /burc\n - ʙᴜʀᴄᴜɴᴜᴢᴜ sᴏ̈ʏʟᴇʀɪᴍ .**", buttons=(
                     [
                      Button.inline("➡️ ɢᴇʀɪ ᴅᴏ̈ɴ", data="help") 
                     ]
                   ),  
                 link_preview=False)
	
##########################
@client.on(events.NewMessage(pattern='/slap'))
async def slap(event):
    if event.is_private:
        return await event.respond("**✓  sᴀᴅᴇᴄᴇ ɢʀᴜᴘʟᴀʀᴅᴀ ᴋᴜʟʟᴀɴɪʟᴀʙɪʟɪʀ .**")

    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        user = reply_message.sender
        if user:
            user_name = f"[{user.first_name}](tg://user?id={user.id})"
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
            await event.respond(f"**[{event.sender.first_name}](tg://user?id={event.sender.id}) ,  {slap_phrase}**")
        else:
            await event.respond("**👁️‍🗨️ ᴜ̈ᴢɢᴜ̈ɴᴜ̈ᴍ, ᴋᴜʟʟᴀɴɪᴄɪʏɪ ʙᴜʟᴀᴍɪʏᴏʀᴜᴍ !**")
    else:
        await event.respond("**💭 ʙɪʀ ᴍᴇsᴀᴊᴀ ʏᴀɴɪᴛ ᴠᴇʀɪɴ ...**")

############################################################
@client.on(events.NewMessage(pattern='/soz'))
async def sahib(event):
    await event.reply(f"**🗨️ sᴇᴄ̧ɪᴍɪɴɪ ʏᴀᴘ . . .**", buttons=(
                     [
                      Button.inline("🌹 ɢᴜ̈ᴢᴇʟ sᴏ̈ᴢ", data="guzel"),
		      Button.inline("🦅 ᴋᴀᴘᴀᴋ sᴏ̈ᴢ", data="kapak")
                     ],[
                      Button.inline("💞  ʀᴏᴍᴀɴᴛɪᴋ sᴏ̈ᴢ", data="romantik")
		     ]
                   ),  
                 link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="soz"))
async def sahib(event):
    await event.reply(f"**🗨️ sᴇᴄ̧ɪᴍɪɴɪ ʏᴀᴘ . . .**", buttons=(
                     [
                      Button.inline("🌹 ɢᴜ̈ᴢᴇʟ sᴏ̈ᴢ", data="guzel"),
		      Button.inline("🦅 ᴋᴀᴘᴀᴋ sᴏ̈ᴢ", data="kapak") 
                     ],[
                      Button.inline("💞  ʀᴏᴍᴀɴᴛɪᴋ sᴏ̈ᴢ", data="romantik")
		     ]
                   ),  
                 link_preview=False)
	
@client.on(events.callbackquery.CallbackQuery(data="guzel"))
async def guzel(event):
    await event.edit(f"**🌹 ɢᴜ̈ᴢᴇʟ sᴏ̈ᴢ :\n\n{random.choice(guzelsoz)}**", buttons=(
                     [
                      Button.inline("🗨️ ᴛᴇᴋʀᴀʀ ᴅᴇɴᴇ", data="soz")
		     ]
                   ),  
                 link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kapak"))
async def romantik(event):
    await event.edit(f"**🦅 ᴋᴀᴘᴀᴋ sᴏ̈ᴢ :\n\n{random.choice(kapaksoz)}**", buttons=(
                     [
		      Button.inline("🗨️ ᴛᴇᴋʀᴀʀ ᴅᴇɴᴇ", data="soz")
		     ]
                   ),  
                 link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="romantik"))
async def romantik(event):
    await event.edit(f"**💞  ʀᴏᴍᴀɴᴛɪᴋ sᴏ̈ᴢ :\n\n{random.choice(romantiksoz)}**", buttons=(
                     [
		      Button.inline("🗨️ ᴛᴇᴋʀᴀʀ ᴅᴇɴᴇ", data="soz")
		     ]
                   ),  
                 link_preview=False)

#   message = await event.reply("🔁 Hazırlanıyor...")
#   await asyncio.sleep(3)
#    await message.delete()

@client.on(events.NewMessage(pattern='/dels'))
async def purge_messages(event):
    if event.is_private:
        await event.respond("**✓  sᴀᴅᴇᴄᴇ ɢʀᴜᴘʟᴀʀᴅᴀ ᴋᴜʟʟᴀɴɪʟᴀʙɪʟɪʀ .**", parse_mode='markdown')
        return

    if not await is_group_admin(event):
        await event.respond("**✓  sᴀᴅᴇᴄᴇ ᴀᴅᴍɪɴʟᴇʀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀ ...**", parse_mode='markdown')
        return

    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.respond("**✓  sɪʟᴍᴇᴍ ɪᴄ̧ɪɴ ʙɪʀ ᴍᴇsᴀᴊ ʏᴀɴɪᴛʟᴀ .**")
        return

    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    await event.client.delete_messages(event.chat_id, messages)
    time_ = time.perf_counter() - start
    text = f"**✓  ᴛᴇᴍɪᴢʟᴇᴍᴇ {time_:0.2f} ᴛᴀᴍᴀᴍʟᴀɴᴅɪ ...**"
    await event.respond(text, parse_mode='markdown')


async def is_group_admin(event):
    """
    Kullanıcının grup yöneticisi olup olmadığını kontrol eder
    """
    try:
        user = await event.client.get_entity(event.input_chat)
        user_info = await event.client.get_participants(user, filter=ChannelParticipantsAdmins, limit=100)
        for u in user_info:
            if u.id == event.sender_id:
                return True
    except errors.rpcerrorlist.ChatAdminRequiredError:
        pass
    return False

@client.on(events.NewMessage(pattern='/bots'))
async def show_bots(event):
    if event.is_private:
        await event.respond("**✓  sᴀᴅᴇᴄᴇ ɢʀᴜᴘʟᴀʀᴅᴀ ᴋᴜʟʟᴀɴɪʟᴀʙɪʟɪʀ .**", parse_mode='markdown')
        return

    if not await is_group_admin(event):
        await event.respond("**✓  sᴀᴅᴇᴄᴇ ᴀᴅᴍɪɴʟᴇʀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀ ...**", parse_mode='markdown')
        return
	    
    all_users = await event.client.get_participants(event.chat_id)
    bot_list = []
    for user in all_users:
        if isinstance(user, types.User) and user.bot:
            bot_list.append(user.username)
    if bot_list:
        await event.reply(f"**🤖 ɢʀᴜᴘᴛᴀᴋɪ ʙᴏᴛʟᴀʀ :**\n\n➻  @" + "\n➻  @".join(bot_list))
    else:
        await event.reply("**🤖 ʙᴜ ɢʀᴜᴘᴛᴀ ʜɪᴄ̧ ʙᴏᴛ ʏᴏᴋ .**")

@client.on(events.NewMessage(pattern='/admins'))
async def show_admins(event):
    if event.is_private:
        await event.respond("**✓  sᴀᴅᴇᴄᴇ ɢʀᴜᴘʟᴀʀᴅᴀ ᴋᴜʟʟᴀɴɪʟᴀʙɪʟɪʀ .**", parse_mode='markdown')
        return

    if not await is_group_admin(event):
        await event.respond("**✓  sᴀᴅᴇᴄᴇ ᴀᴅᴍɪɴʟᴇʀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀ ...**", parse_mode='markdown')
        return
	    
    chat = await event.get_chat()
    admins = await event.client.get_participants(chat, filter=types.ChannelParticipantsAdmins)
    admin_list = ""
    for admin in admins:
        admin_list += f"\n➻  [{admin.first_name}](tg://user?id={admin.id})"
    await event.respond(f"**🗨️  ɢʀᴜᴘᴛᴀᴋɪ ᴀᴅᴍɪɴʟᴇʀ : \n{admin_list}**")

@client.on(events.callbackquery.CallbackQuery(data="admins"))
async def show_admins(event):
    if event.is_private:
        await event.respond("**✓  sᴀᴅᴇᴄᴇ ɢʀᴜᴘʟᴀʀᴅᴀ ᴋᴜʟʟᴀɴɪʟᴀʙɪʟɪʀ .**", parse_mode='markdown')
        return

    if not await is_group_admin(event):
        await event.edit("**✓  sᴀᴅᴇᴄᴇ ᴀᴅᴍɪɴʟᴇʀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀ ...**", parse_mode='markdown')
        return
	    
    chat = await event.get_chat()
    admins = await event.client.get_participants(chat, filter=types.ChannelParticipantsAdmins)
    admin_list = ""
    for admin in admins:
        admin_list += f"\n➻  [{admin.first_name}](tg://user?id={admin.id})"
    await event.edit(f"**🗨️  ɢʀᴜᴘᴛᴀᴋɪ ᴀᴅᴍɪɴʟᴇʀ : \n{admin_list}**")
    
@client.on(events.NewMessage(pattern='/id'))
async def id(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_id = previous_message.sender_id
        chat_id = event.chat_id
        if event.is_private:
            return await event.reply(f"✓ **ᴋᴜʟʟᴀɴɪᴄɪ ɪᴅ :** `{user_id}`")
        else:
            return await event.reply(f"✓ **ᴋᴜʟʟᴀɴɪᴄɪ ɪᴅ :** `{user_id}`\n**✓ ɢʀᴜᴘ ɪᴅ :** `{chat_id}`")


    else:
        user_id = event.sender_id
        chat_id = event.chat_id
        if event.is_private:
            return await event.reply(f"✓ **ᴋᴜʟʟᴀɴɪᴄɪ ɪᴅ :** `{user_id}`")
        else:
            return await event.reply(f"✓ **ᴋᴜʟʟᴀɴɪᴄɪ ɪᴅ :** `{user_id}`\n**✓ ɢʀᴜᴘ ɪᴅ :** `{chat_id}`")
    
@client.on(events.NewMessage(pattern='/iletisim'))
async def zar(event):
    mrt = await event.reply("✓  **ʟᴜ̈ᴛғᴇɴ ʙᴇᴋʟᴇʏɪɴ ...**")
    await asyncio.sleep(2)
    await mrt.edit(f"**👨🏻‍💻 [{OWNERNAME}](tg://openmessage?user_id={OWNER_ID})**")

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

    owner_button = Button.inline("✅  ʏᴏ̈ɴᴇᴛɪᴄɪʟᴇʀ", data="admins")

    response_text = (
        f'➻ **ɢʀᴜᴘ ᴀᴅɪ : {group_name}**\n'
        f'➻ **ɢʀᴜᴘ ɪᴅ :** `-100{group_id}`\n'
	f'➻ **ᴜʏᴇ sᴀʏɪsɪ : {total_count}**\n'
        f'➻ **ᴀᴋᴛɪғ ᴋᴜʟʟᴀɴɪᴄɪʟᴀʀ : {active_count}**\n'
        f'{special_status}'
    )

    await event.respond(response_text, buttons=[[owner_button]])

#ETİKET İŞLEMİ İPTAL
@client.on(events.NewMessage(pattern='^/cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")

  global gece_tag
  gece_tag.remove(event.chat_id)

  sender = await event.get_sender()
  rxyzdev_stopT = f"[{sender.first_name}](tg://user?id={sender.id})"      
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🗨️  ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴅᴜʀᴅᴜʀᴅᴜᴍ ...\n\n➻ {rxyzdev_stopT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**", buttons=(
                      [
                      Button.url('🗨️  ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ  🗨️', f'https://t.me/{BOT_USERNAME}?startgroup=a')
                      ]
                    ),
                    link_preview=False)

#################
@client.on(events.NewMessage(pattern="^/atag ?(.*)"))
async def mentionalladmin(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**✓  sᴀᴅᴇᴄᴇ ɢʀᴜᴘʟᴀʀᴅᴀ ᴋᴜʟʟᴀɴɪʟᴀʙɪʟɪʀ .**")

  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
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

#######################
@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def utag(event):
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
    return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\nᴠᴇʏᴀ ᴛɪᴋʟᴀʏɪɴ ➙ /utag**")
  
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
      usrtxt += f"➻ [{usr.first_name}](tg://user?id={usr.id})\n"
      if event.chat_id not in gece_tag:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"**{msg}\n\n{usrtxt}**")
        await asyncio.sleep(2)
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

#########################
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
	    
#########################
@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def etag(event):
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
    return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\nᴠᴇʏᴀ ᴛɪᴋʟᴀʏɪɴ ➙ /etag**")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏᴇ ʙᴀşʟɪʏᴏʀᴜᴍ ...**", buttons=(
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
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...\n\n➻ {rxyzdev_initT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**", buttons=(
                      [
                      Button.url('🗨️  ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ  🗨️', f'https://t.me/{BOT_USERNAME}?startgroup=a')
                      ]
                    ),
                    link_preview=False)
     
########################
@client.on(events.NewMessage(pattern="^/vtag ?(.*)"))
async def vtag(event):
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
    return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\nᴠᴇʏᴀ ᴛɪᴋʟᴀʏɪɴ ➙ /vtag**")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏᴇ ʙᴀşʟɪʏᴏʀᴜᴍ ...**", buttons=(
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
        await client.send_message(event.chat_id, f"**{usrtxt}  {random.choice(sor)}**")
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

########################
@client.on(events.NewMessage(pattern="^/otag ?(.*)"))
async def otag(event):
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
    return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\nᴠᴇʏᴀ ᴛɪᴋʟᴀʏɪɴ ➙ /otag**")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏᴇ ʙᴀşʟɪʏᴏʀᴜᴍ ...**", buttons=(
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
      usrtxt += f"[{random.choice(rutbe)}](tg://user?id={usr.id})"
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

#########################
@client.on(events.NewMessage(pattern="^/stag ?(.*)"))
async def stag(event):
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
    return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\nᴠᴇʏᴀ ᴛɪᴋʟᴀʏɪɴ ➙ /stag**")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏᴇ ʙᴀşʟɪʏᴏʀᴜᴍ ...**", buttons=(
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
        await client.send_message(event.chat_id, f"**{usrtxt}  {random.choice(guzelsoz)}**")
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
    
#########################
@client.on(events.NewMessage(pattern="^/rtag ?(.*)"))
async def rtag(event):
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
    return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\nᴠᴇʏᴀ ᴛɪᴋʟᴀʏɪɴ ➙ /rtag**")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏᴇ ʙᴀşʟɪʏᴏʀᴜᴍ ...**", buttons=(
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
      usrtxt += f"[{random.choice(renk)}](tg://user?id={usr.id}) , "
      if event.chat_id not in gece_tag:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"**{msg}\n\n{usrtxt}**")
        await asyncio.sleep(2)
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

############################
@client.on(events.NewMessage(pattern="^/ktag ?(.*)"))
async def ktag(event):
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
    return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\nᴠᴇʏᴀ ᴛɪᴋʟᴀʏɪɴ ➙ /ktag**")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏᴇ ʙᴀşʟɪʏᴏʀᴜᴍ ...**", buttons=(
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
      usrtxt += f"[{random.choice(kart)}](tg://user?id={usr.id}) , "
      if event.chat_id not in gece_tag:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"**{msg}\n\n{usrtxt}**")
        await asyncio.sleep(2)
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

###########################
@client.on(events.NewMessage(pattern="^/btag ?(.*)"))
async def btag(event):
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
    return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\nᴠᴇʏᴀ ᴛɪᴋʟᴀʏɪɴ ➙ /btag**")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏᴇ ʙᴀşʟɪʏᴏʀᴜᴍ ...**", buttons=(
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
      usrtxt += f"[{random.choice(bayrak)}](tg://user?id={usr.id}) , "
      if event.chat_id not in gece_tag:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"**{msg}\n\n{usrtxt}**")
        await asyncio.sleep(2)
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
 
#########################		
@client.on(events.NewMessage(pattern='/eros'))
async def eros_oku(event):
    users = []
    async for user in client.iter_participants(event.chat_id):
        if not user.bot and not user.deleted and not user.is_self:
            users.append(user)

    if len(users) < 2:
        return
    
    first_user, second_user = random.sample(users, 2)
    first_user_md_mention = f'**[{first_user.first_name}](tg://user?id={first_user.id})**'
    second_user_md_mention = f'**[{second_user.first_name}](tg://user?id={second_user.id})**'
    
    response = (
        f"**💘 ᴇʀᴏs'ᴜɴ ᴏᴋᴜɴᴜ ᴀᴛᴛɪᴍ .\n✓  ɢɪᴢʟɪ ᴀşɪᴋʟᴀʀ :**\n\n"
        f"{first_user_md_mention} ❣️ {second_user_md_mention} \n\n**💞 sᴇᴠɢɪ ᴏʀᴀɴɪ : %{random.randint(0, 100)}**"
    )
    
    await event.respond(response, parse_mode="Markdown")

################### VERİTABANI VERİ GİRİŞ ÇIKIŞI #########################
class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id): # Veritabanına yeni kullanıcı ekler
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat(),
            ban_status=dict(
                is_banned=False,
                ban_duration=0,
                banned_on=datetime.date.max.isoformat(),
                ban_reason="",
            ),
        )

    async def add_user(self, id): # Veritabına yeni kullanıcı eklemek için ön def
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id): # Bir kullanıcının veritabında olup olmadığını kontrol eder.
        user = await self.col.find_one({"id": int(id)})
        return bool(user)

    async def total_users_count(self): # Veritabanındaki toplam kullanıcıları sayar.
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self): # Veritabındaki tüm kullanıcıların listesini verir.
        return self.col.find({})

    async def delete_user(self, user_id): # Veritabından bir kullanıcıyı siler.
        await self.col.delete_many({"id": int(user_id)})

    async def ban_user(self, user_id, ban_duration, ban_reason): # Veritabanınızdaki bir kullanıcıyı yasaklılar listesine ekler.
        ban_status = dict(
            is_banned=True,
            ban_duration=ban_duration,
            banned_on=datetime.date.today().isoformat(),
            ban_reason=ban_reason,
        )
        await self.col.update_one({"id": user_id}, {"$set": {"ban_status": ban_status}})

    async def remove_ban(self, id): # Veritabanınızdaki yasaklılar listesinde bulunan bir kullanıcın yasağını kaldırır.
        ban_status = dict(
            is_banned=False,
            ban_duration=0,
            banned_on=datetime.date.max.isoformat(),
            ban_reason="",
        )
        await self.col.update_one({"id": id}, {"$set": {"ban_status": ban_status}})

    async def get_ban_status(self, id): # Bir kullanıcın veritabanınızda yasaklılar listesinde olup olmadığını kontrol eder.
        default = dict(
            is_banned=False,
            ban_duration=0,
            banned_on=datetime.date.max.isoformat(),
            ban_reason="",
        )
        user = await self.col.find_one({"id": int(id)})
        return user.get("ban_status", default)

    async def get_all_banned_users(self): # Veritabınızdaki yasaklı kullanıcılar listesini verir.
        return self.col.find({"ban_status.is_banned": True})


db = Database(DATABASE_URL, BOT_USERNAME)
mongo_db_veritabani = MongoClient(DATABASE_URL)
dcmdb = mongo_db_veritabani.handlers



################## KULLANICI KONTROLLERİ #############
async def handle_user_status(bot: Client, cmd: Message): # Kullanıcı kontrolü
    chat_id = cmd.chat.id
    if not await db.is_user_exist(chat_id):
        if cmd.chat.type == "private":
            await db.add_user(chat_id)
            await bot.send_message(LOG_CHANNEL,LAN.BILDIRIM.format(cmd.from_user.first_name, cmd.from_user.id, cmd.from_user.first_name, cmd.from_user.id))
        else:
            await db.add_user(chat_id)
            chat = bot.get_chat(chat_id)
            if str(chat_id).startswith("-100"):
                new_chat_id = str(chat_id)[4:]
            else:
                new_chat_id = str(chat_id)[1:]
            await bot.send_message(LOG_CHANNEL,LAN.GRUP_BILDIRIM.format(cmd.from_user.first_name, cmd.from_user.id, cmd.from_user.first_name, cmd.from_user.id, chat.title, cmd.chat.id, cmd.chat.id, cmd.message_id))

    ban_status = await db.get_ban_status(chat_id) # Yasaklı Kullanıcı Kontrolü
    if ban_status["is_banned"]:
        if int((datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])).days) > int(ban_status["ban_duration"]):
            await db.remove_ban(chat_id)
        else:
            if GROUP_SUPPORT:
                msj = f"@{GROUP_SUPPORT}"
            else:
                msj = f"[{LAN.SAHIBIME}](tg://user?id={OWNER_ID})"
            if cmd.chat.type == "private":
                await cmd.reply_text(LAN.PRIVATE_BAN.format(msj), quote=True)
            else:
                await cmd.reply_text(LAN.GROUP_BAN.format(msj),quote=True)
                await bot.leave_chat(cmd.chat.id)
            return
    await cmd.continue_propagation()




############### Broadcast araçları ###########
broadcast_ids = {}

async def send_msg(user_id, message): # Mesaj Gönderme
    try:
        if GONDERME_TURU is False:
            await message.forward(chat_id=user_id)
        elif GONDERME_TURU is True:
            await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(int(e.x))
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id}: {LAN.NOT_ONLINE}\n"
    except UserIsBlocked:
        return 400, f"{user_id}: {LAN.BOT_BLOCKED}\n"
    except PeerIdInvalid:
        return 400, f"{user_id}: {LAN.USER_ID_FALSE}\n"
    except Exception:
        return 500, f"{user_id}: {traceback.format_exc()}\n"

async def main_broadcast_handler(m, db): # Ana Broadcast Mantığı
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = "".join(random.choice(string.ascii_letters) for i in range(3))
        if not broadcast_ids.get(broadcast_id):
            break
    out = await m.reply_text(
        text=LAN.BROADCAST_STARTED)
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(total=total_users, current=done, failed=failed, success=success)
    async with aiofiles.open("broadcast-logs-g4rip.txt", "w") as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(user_id=int(user["id"]), message=broadcast_msg)
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user["id"])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(current=done, failed=failed, success=success))
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(text=LAN.BROADCAST_STOPPED.format(completed_in, total_users, done, success, failed), quote=True,)
    else:
        await m.reply_document(document="broadcast-logs-g4rip.txt", caption=LAN.BROADCAST_STOPPED.format(completed_in, total_users, done, success, failed), quote=True,)
    os.remove("broadcast-logs-g4rip.txt")

# Genelde müzik botlarının mesaj silme özelliği olur. Bu özelliği ReadMe.md dosyasındaki örnekteki gibi kullanabilirsiniz.
delcmdmdb = dcmdb.admins

async def delcmd_is_on(chat_id: int) -> bool: # Grup için mesaj silme özeliğinin açık olup olmadığını kontrol eder.
    chat = await delcmdmdb.find_one({"chat_id": chat_id})
    return not chat


async def delcmd_on(chat_id: int): # Grup için mesaj silme özeliğini açar.
    already_del = await delcmd_is_on(chat_id)
    if already_del:
        return
    return await delcmdmdb.delete_one({"chat_id": chat_id})


async def delcmd_off(chat_id: int): # Grup için mesaj silme özeliğini kapatır.
    already_del = await delcmd_is_on(chat_id)
    if not already_del:
        return
    return await delcmdmdb.insert_one({"chat_id": chat_id})

################# SAHİP KOMUTLARI #############
@app.on_message(filters.command("istatistik") & filters.user(OWNER_ID))
async def botstats(bot: Client, message: Message):
    g4rip = await bot.send_message(message.chat.id, LAN.STATS_STARTED.format(message.from_user.mention))
    all_users = await db.get_all_users()
    groups = 0
    pms = 0
    async for user in all_users:
        if str(user["id"]).startswith("-"):
            groups += 1
        else:
            pms += 1
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    total_users = await db.total_users_count()
    await g4rip.edit(text=LAN.STATS.format(BOT_USERNAME, total_users, groups, pms, total, used, disk_usage, free, cpu_usage, ram_usage, __version__), parse_mode="md")

@app.on_message()
async def G4RIP(bot: Client, cmd: Message):
    await handle_user_status(bot, cmd)

# Broadcast komutu
@app.on_message(filters.command("reklam") & filters.user(OWNER_ID) & filters.reply)
async def broadcast_handler_open(_, m: Message):
    await main_broadcast_handler(m, db)

# Bir kullanıcı yasaklama komutu
@app.on_message(filters.command("block") & filters.user(OWNER_ID))
async def ban(c: Client, m: Message):
    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
        if len(m.command) <= 1:
            ban_duration = 9999
            ban_reason = LAN.BAN_REASON.format(BOT_USERNAME)
        elif len(m.command) == 2:
            ban_duration = 9999
            ban_reason = " ".join(m.command[1:])
    else:
        if len(m.command) <= 1:
            return await m.reply(LAN.NEED_USER)
        elif len(m.command) == 2:
            user_id = int(m.command[1])
            ban_duration = 9999
            ban_reason = LAN.BAN_REASON.format(BOT_USERNAME)
        elif len(m.command) == 3:
            user_id = int(m.command[1])
            ban_duration = 9999
            ban_reason = " ".join(m.command[2:])
    
        if str(user_id).startswith("-"):
            try:    
                ban_log_text = LAN.BANNED_GROUP.format(m.from_user.mention, user_id, ban_duration, ban_reason)
                await c.send_message(user_id, LAN.AFTER_BAN_GROUP.format(ban_reason))
                await c.leave_chat(user_id)
                ban_log_text += LAN.GROUP_BILGILENDIRILDI
            except BaseException:
                traceback.print_exc()
                ban_log_text += LAN.GRUP_BILGILENDIRILEMEDI.format(traceback.format_exc())
        else:
            try:    
                ban_log_text = LAN.USER_BANNED.format(m.from_user.mention, user_id, ban_duration, ban_reason)
                await c.send_message(user_id, LAN.AFTER_BAN_USER.format(ban_reason))
                ban_log_text += LAN.KULLANICI_BILGILENDIRME
            except BaseException:
                traceback.print_exc()
                ban_log_text += LAN.KULLANICI_BILGILENDIRMEME.format(traceback.format_exc())
        await db.ban_user(user_id, ban_duration, ban_reason)
        await c.send_message(LOG_CHANNEL, ban_log_text)
        await m.reply_text(ban_log_text, quote=True)

# Bir kullanıcın yasağını kaldırmak komutu
@app.on_message(filters.command("unblock") & filters.user(OWNER_ID))
async def unban(c: Client, m: Message):
        if m.reply_to_message:
            user_id = m.reply_to_message.from_user.id
        else:
            if len(m.command) <= 1:
                return await m.reply(LAN.NEED_USER)
            else:
                user_id = int(m.command[1])
        unban_log_text = LAN.UNBANNED_USER.format(m.from_user.mention, user_id)
        if not str(user_id).startswith("-"):
            try:
                await c.send_message(user_id, LAN.USER_UNBAN_NOTIFY)
                unban_log_text += LAN.KULLANICI_BILGILENDIRME
            except BaseException:
                traceback.print_exc()
                unban_log_text += LAN.KULLANICI_BILGILENDIRMEME.format(traceback.format_exc())
        await db.remove_ban(user_id)
        await c.send_message(LOG_CHANNEL, unban_log_text)
        await m.reply_text(unban_log_text, quote=True)

# Yasaklı listesini görme komutu
@app.on_message(filters.command("blocklist") & filters.user(OWNER_ID))
async def _banned_usrs(_, m: Message):
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ""
    async for banned_user in all_banned_users:
        user_id = banned_user["id"]
        ban_duration = banned_user["ban_status"]["ban_duration"]
        banned_on = banned_user["ban_status"]["banned_on"]
        ban_reason = banned_user["ban_status"]["ban_reason"]
        banned_usr_count += 1
        text += LAN.BLOCKS.format(user_id, ban_duration, banned_on, ban_reason)
    reply_text = LAN.TOTAL_BLOCK.format(banned_usr_count, text)
    if len(reply_text) > 4096:
        with open("banned-user-list.txt", "w") as f:
            f.write(reply_text)
        await m.reply_document("banned-user-list.txt", True)
        os.remove("banned-user-list.txt")
        return
    await m.reply_text(reply_text, True)

############## BELİRLİ GEREKLİ DEF'LER ###########
def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "K", 2: "M", 3: "G", 4: "T"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"

########### ÇOKLU DİL ##############
class LAN(object):

    if LANGAUGE == "TR":

        BILDIRIM = "**🏷 Kullanıcı : {}\n📮 ID : {}\n🧝🏻‍♂️ Profili : [{}](tg://user?id={})**"
        GRUP_BILDIRIM = "**🏷 Kullanıcı : {}\n📮 ID : {}\n🧝🏻‍♂️ Profili : [{}](tg://user?id={})\n💬 Grub : {}\n🌟 Grub ID: {}\n🎲 Mesaj Linki : [Buraya Tıkla](https://t.me/c/{}/{})**"
        SAHIBIME = "sahibime"
        PRIVATE_BAN = "🗒️ **Üzgünüm, yasaklandınız! Bunun bir hata olduğunu düşünyorsanız {} yazın.**"
        GROUP_BAN = "🗒️ **Üzgünüm, grubunuz karalisteye alındı! Burada daha fazla kalamam. Bunun bir hata olduğunu düşünyorsanız {} yazın.**"
        NOT_ONLINE = "Aktif değil"
        BOT_BLOCKED = "Botu engellemiş"
        USER_ID_FALSE = "**Kullanıcı ID Yanlış .**"
        BROADCAST_STARTED = "**✓ Reklam başlatıldı!**"
        BROADCAST_STOPPED = "**✓ Reklam ( {} )  tamamlandı .\n\n👤 Kayıtlı Kullanıcı : {}\n♻️ Gönderme Denemesi : {}\n✅ Başarılı : {}\n⛔ Başarısız : {}**"
        STATS_STARTED = "{} **Veriler Toplanıyor !**"
        STATS = """**@{} Kullanıcıları :\n\n» Toplam Sohbetler : {}\n» Grup Sayısı : {}\n» PM Sayısı : {}**"""
        BAN_REASON = "Yasaklandığınız için @{} tarafından otomatik olarak oluşturulmuştur ."
        NEED_USER = "**Lütfen Kullanıcı kimliği verin.**"
        BANNED_GROUP = "🚷 **Yasaklandı!\n\nTarafından : {}\nGrup ID : {}\nSüre : {}\nSebep : {}**"
        AFTER_BAN_GROUP = "**Üzgünüm grubunuz kara listeye alındı! \n\nSebep :{}**\n\n**Daha fazla burada kalamam. Bunun bir hata olduğunu düşünüyorsanız destek grubuna gelin.**"
        GROUP_BILGILENDIRILDI = "\n\n✅ **Grubu bilgilendirdim ve gruptan ayrıldım.**"
        GRUP_BILGILENDIRILEMEDI = "\n\n❌ **Grubu bilgilendirmeye çalışırken bir hata oluştu:** \n\n`{}`"
        USER_BANNED = "🚷 **Yasaklandı! \n\nTarafından : {}\nKullanıcı ID : {}\nSüre : {}\nSebep : {}**"
        AFTER_BAN_USER = "**Üzgünüm kara listeye alındınız! \n\nSebep : {}**"
        KULLANICI_BILGILENDIRME = "\n\n**✓ Kişiyi bilgilendirdim.**"
        KULLANICI_BILGILENDIRMEME = "\n\n❌ **Kişiyi bilgilendirmeye çalışırken bir hata oluştu:** \n\n`{}`"
        UNBANNED_USER = "🆓 **Yasak Kaldırıldı !\nKaldıran : {}\nKullanıcı ID : {}**"
        USER_UNBAN_NOTIFY = "**💞 Hoppala, Çok Şanslısın ! \n👨🏻‍💻 [ㅤᴀɪᴋᴏㅤ](tg://openmessage?user_id=6540285284) Yasağınızı kaldırdı !**"
        BLOCKS = "🆔 **Kullanıcı ID : {}\n⏱ Süre : {}\n🗓 Yasaklanan Tarih : {}\n💬 Sebep : {}**\n\n"
        TOTAL_BLOCK = "🚷 **Yasaklanan Kullanıcılar :** `{}`\n\n{}"

app.run()
print(" Bot çalışıyor :)")
client.run_until_disconnected()

