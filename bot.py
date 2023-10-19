import random
import shutil, psutil, traceback, os
import string
import time
import datetime
import motor.motor_asyncio
import shutil, psutil, traceback
import traceback
import aiofiles
import wget
import yt_dlp
import os, youtube_dl, requests, time
import random, os, logging, asyncio
import telethon
from mesaj.botmesaj import nogroup, startmesaj, startbutton, noadmin, tag1, tag2, tag3, tag4, emj, rutbe, sor, kapaksoz, romantiksoz, guzelsoz
from Config import Config
from telethon.tl import types
from telethon import Button
from telethon.tl import types
from telethon.tl import functions
from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch
from pyrogram.handlers import MessageHandler
from yt_dlp import YoutubeDL
from telethon import events
from telethon import errors
from telethon import TelegramClient
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
from pyrogram.types import Message
from pyrogram.types.messages_and_media import Message
from pyrogram import Client, filters
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
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
bot_token = os.environ.get("TOKEN","6559325433:AAF-G05bNjC-S5TwbmW222eY77SU8jM5GhY")
BOT_ID = int(os.environ.get("BOT_ID", "6559325433"))
DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://ok:ok@cluster0.uooya.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") # MongoDB veritabanınızın url'si. Nasıl alacağınızı bilmiyorsanız destek grubu @RepoHaneX'e gelin.
BOT_USERNAME = os.environ.get("BOT_USERNAME","AikoDenemeBot") # Botunuzun kullanıcı adı.
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL","-1001983841726")) # Botunuzun eylemleri kaydedeceği kayıt grubunun id'si.
GROUP_SUPPORT = os.environ.get("GROUP_SUPPORT", "BuketBilgi") # Botunuzdan yasaklanan kullanıcıların itiraz işlemleri için başvuracağı grup, kanal veya kullanıcı. Boş bırakırsanız otomatik olarak OWNER_ID kimliğine yönlendirecektir.
GONDERME_TURU = os.environ.get("GONDERME_TURU", False) # Botunuzun yanıtladığınız mesajı gönderme türü. Eğer direkt iletmek isterseniz False, kopyasını göndermek isterseniz True olarak ayarlayın.
OWNER_ID = int(os.environ.get("OWNER_ID","6540285284")) # Sahip hesabın id'si
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
gruplar = []
ozel_list = []
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
    if "Selam" in mesaj or "Selamün Aleyküm" in mesaj or "selamün aleyküm" in mesaj:
        await event.reply(f"**{random.choice(selam)}**")
	    
    if "Nasılsın" in mesaj or "nasılsın" in mesaj or "naber" in mesaj or "Naber" in mesaj:
        await event.reply(f"**{random.choice(nasilsin)}**")
	    
    if "Adam" in mesaj or "adam" in mesaj:
        await event.reply(f"**{random.choice(adam)}**")
	    
    if "iyiyim" in mesaj or "İyiyim" in mesaj:
        await event.reply(f"**{random.choice(iyiyim)}**")
	    
    if "Hoş Geldin" in mesaj or "hoş geldin" in mesaj:
        await event.reply(f"**{random.choice(hoş)}**")
	    
    if "Merhaba" in mesaj or "merhaba" in mesaj:
        await event.reply(f"**{random.choice(merhaba)}**")
	    
    if "Ban" in mesaj or "ban" in mesaj :
        await event.reply(f"**{random.choice(ban)}**")
	    
    if "Nabıyon" in mesaj or "nabıyon" in mesaj  or "Napıyorsun" in mesaj or "napıyorsun" in mesaj:
        await event.reply(f"**{random.choice(nabiyon)}**")
	    
    if "😔" in mesaj or "🥺" in mesaj  or "😥" in mesaj:
        await event.reply(f"**{random.choice(uzgun)}**")
	    
    if "valla" in mesaj or "Valla" in mesaj or "Vallahi" in mesaj or "vallahi" in mesaj:
        await event.reply(f"**{random.choice(valla)}**")
	    
    if "buket" in mesaj or "buket" in mesaj:
        await event.reply(f"**{random.choice(buket)}**")
	    
    if "sg" in mesaj or "Sg" in mesaj or "siktir" in mesaj or "Siktir" in mesaj:
        await event.reply(f"**{random.choice(sg)}**")
	    
    if "Mal" in mesaj or "gerizekalı" in mesaj or "Gerizekalı" in mesaj:
        await event.reply(f"**{random.choice(mal)}**")
	    
    if "Balım" in mesaj or "balım" in mesaj or "Bebeğim" in mesaj or "bebeğim" in mesaj:
        await event.reply(f"**{random.choice(balim)}**")
	    
    if "Canım" in mesaj or "canım" in mesaj or "Bitanem" in mesaj or "bitanem" in mesaj:
        await event.reply(f"**{random.choice(canim)}**")
	    
    if "gidiyorum" in mesaj or "Gidiyorum" in mesaj or "gittim" in mesaj or "Gittim" in mesaj or "Görüşürüz" in mesaj or "görüşürüz" in mesaj:
        await event.reply(f"**{random.choice(gidiyorum)}**")
	    
    if "Sinirlendim" in mesaj or "sinirlendim" in mesaj or "😡" in mesaj or "🤬" in mesaj:
        await event.reply(f"**{random.choice(sinirlendim)}**")
	    
    if "tanışalım mı" in mesaj or "Tanışalım mı" in mesaj:
        await event.reply(f"**{random.choice(tanis)}**")
	    
    if "İsmin ne" in mesaj or "ismin ne" in mesaj  or "Adın ne" in mesaj or "adın ne" in mesaj:
        await event.reply(f"**{random.choice(adne)}**")
	    
    if "iyi sen" in mesaj or "İyi sen" in mesaj  or "iyiyimm sen" in mesaj or "İyiyim sen" in mesaj:
        await event.reply(f"**{random.choice(iyisen)}**")
	    
    if "😅" in mesaj or "😂" in mesaj or "🤣" in mesaj:
        await event.reply(f"**{random.choice(gullu)}**")
	    
    if "Büyüğüm" in mesaj or "büyüğüm" in mesaj or "büyük" in mesaj  or "Büyük" in mesaj:
        await event.reply(f"**{random.choice(buyuk)}**")
	    
    if "Aiko" in mesaj or "aiko" in mesaj:
        await event.reply(f"**{random.choice(aiko)}**")
	    
    if "Merve" in mesaj or "merve" in mesaj:
        await event.reply(f"**{random.choice(merve)}**")
	    
    if "Günaydın" in mesaj or "günaydın" in mesaj:
        await event.reply(f"**{random.choice(gnyy)}**")
	    
    if "İyi geceler" in mesaj or "iyi geceler" in mesaj:
        await event.reply(f"**{random.choice(igece)}**")

    if "Kaç yaşındasın" in mesaj or "kaç yaşındasın" in mesaj:
        await event.reply(f"**{random.choice(kyas)}**")

    if "nerelisin" in mesaj or "Nerelisin" in mesaj:
        await event.reply(f"**{random.choice(nereli)}**")

    if "Konuşma" in mesaj or "konuşma" in mesaj or "sus" in mesaj or "Sus" in mesaj:
        await event.reply(f"**{random.choice(pms)}**")

    if "Kırdın" in mesaj or "kırdın" in mesaj or "kırıldım" in mesaj or "Kırıldım" in mesaj:
        await event.reply(f"**{random.choice(krdn)}**")

    if "kanka" in mesaj or "Kanka" in mesaj:
        await event.reply(f"**{random.choice(knks)}**")

    if "sıkıldım" in mesaj or "skldm" in mesaj or "Sıkıldım" in mesaj or "Skldm" in mesaj:
        await event.reply(f"**{random.choice(skdm)}**")

    if "hm" in mesaj or "Hm" in mesaj:
        await event.reply(f"**{random.choice(hms)}**")

    if "Geçmiş olsun" in mesaj or "geçmiş olsun" in mesaj:
        await event.reply(f"**{random.choice(bts)}**")

    if "oyun" in mesaj or "Oyun" in mesaj or "Game" in mesaj or "game" in mesaj:
        await event.reply(f"**{random.choice(trt)}**")

    if "Evet" in mesaj or "evet" in mesaj or "Evt" in mesaj or "evt" in mesaj:
        await event.reply(f"**{random.choice(evt)}**")

    if "hyr" in mesaj or "Hyr" in mesaj or "Hayır" in mesaj or "hayır" in mesaj:
        await event.reply(f"**{random.choice(hyrr)}**")

    if "🙄" in mesaj:
        await event.reply(f"**{random.choice(gzs)}**")

    if "Of" in mesaj:
        await event.reply(f"**{random.choice(ofs)}**")

    if "çikolata" in mesaj or "Çikolata" in mesaj:
        await event.reply(f"**{random.choice(cklta)}**")
	    
    if "Lan" in mesaj or "lann" in mesaj:
        await event.reply(f"**{random.choice(lna)}**")

    if "Dedim" in mesaj or "dedim" in mesaj:
        await event.reply(f"**{random.choice(dddm)}**")

    if "Yalan" in mesaj or "yalan" in mesaj:
        await event.reply(f"**{random.choice(ylna)}**")

    if "Sağol" in mesaj or "sağol" in mesaj:
        await event.reply(f"**{random.choice(sgll)}**")

    if "Çirkin" in mesaj or "çirkin" in mesaj:
        await event.reply(f"**{random.choice(crkn)}**")

    if "Pm" in mesaj or "Dm" in mesaj:
        await event.reply(f"**{random.choice(dmy)}**")

    if "Tatlı" in mesaj or "Yemek" in mesaj:
        await event.reply(f"**{random.choice(tymm)}**")

    if "Kes" in mesaj:
        await event.reply(f"**{random.choice(kmm)}**")


selam = ( "Aleyküm Selam Naber 🎉", "Selam Hoş Geldin", "Ase, Hoş Geldin .", )

nasilsin = ( "İyiyim senden naber", "İyiyim sen", "İyim fıstık, ya sen 💕", "Teşekkür ederim iyiyim sen nasılsın", "Tıpkı senin gibi mükemmelim 🥳", )

adam = ( "Mermiler seksin, alemde teksin 😏", "Mermiler seksin, tokatımı yersin 😏", )

iyiyim = ( "İyi olmana sevindim", "Hep daha iyi olman dileğiyle  ", "Keşke bende senin kadar iyi olsam 😏", )

hoş = ( "Naber", "Hoş buldum nabıyon", "nasılsın", )

merhaba = ( "Merhaba, Hoş geldin", "Merhaba, Hoş Geldin", "Merhaba, nerelerdesin ya sen", "yine özlettin kendini 😏", )

ban = ( "Ayıp ettin :/", "Bak sen 🤔", "Adamın dibisin sen :)", "Grub boşalıyor yetişin .", )

nabiyon = ( "Oturuyorum, sen", "Gördüğün gibi takılıyoruz", "Yapacak bişey yok", "Ne yapmamı istersin", )

uzgun = ( "Kıyamam ki ben sana 😢", "Üzülme, buda geçer 😔", "Bizi üzenler utansın 😏", "Hoppala, kim üzdü seni", )

valla = ( "tamam, tamam inandım 🥴", "de valla", "Deme öyle Allah çarpar", "Sus çarpılırsin .", )

buket = ( "What dedin gülüm !", "Efendim Canım ", "Burdayım Bitanem", "Bana mı seslendin .", )

sg = ( "Küfür etme turşu !", "Lütfen düzgün konuş 😏", "Dayanamıyacam ben artık ama ...", "Ben buna dalarım ama ...", )

mal = ( "Akıllı görünce kıskandı 😏", "Sana özeniyorum, galiba başarıyorum 🙈", "Beni birine benzettin galiba 🙄", "Hop, orda dur beni daha fazla sinirlendirmeyin lütfen ...", )

balim = ( "Arı mısın gülüm 🙈", "Canın çektiyse yiyebilirsin beni 😋", "Efendim, hayatım .", "Şımarıyorum ama 🙈", )

canim = ( "Gülüm 💕", "Bebeğim 💕", "Bitanem 💕", "Hayatım 💕", "Turşu suratlım 💕", )

gidiyorum = ( "Nereye, Karpuz Kesmiştik .", "Hoşuma yeterince gittin, otur oturduğun yerde 🤫", "Görüşürüz, Hakkını helal et ...", "Kal desem kalır mı acaba 🤔", )

sinirlendim = ( "Farkettim .", "Sakin ol, Şampiyon .", "Bakıyorum da Domates gibi kızardın .", "Ne yapayım .", )

tanis = ( "Olur tanışalım .", "Kim olduğunu biliyorum :)", "Kendini tanıt !", "Düşünmem gerek 🤔", )

adne = ( "Buket, ya senin ?", "Sen söylersen bende söylerim 😏", "Söylemem, banane .", "Ben de Buket memnun oldum ❣️", )

iyisen = ( "Bende iyiyim teşekürler .", "Senin gibi iyi olamıyorum 😔", "Birazcık kötüyüm .", "Mükemmelim tıpkı senin gibi 🤭", )

gullu = ( "Ne gülüyon?", "Açıkta bişey mi gördün .", "Bakıyorum da keyfin yerinde .", "Mutlu olmana sevindim 💕", )

buyuk = ( "Senden Büyük Allah var 😎", "Yalan söyleme .", "Hayır, Küçük :)", )

aiko = ( "Buyrun, Asistanı olurum ?", "Aiko kadar başına taş düşsün emi .", "Öldü artık yok 🙄", )

merve = ( "Rahmetliyi Sevmezdik 😔", "Öldü o, Artık yaşamıyor .", "Hayatımın Anlamı Nerdesin 🤭", "Çok özletti kendini :)", )

gnyy = ( "Günaydın, naber", "Günüm aydı, hoş geldin 🎉", "Günaydın, tatlım .", "Güneşim doğdu, hoş geldin 🥳", )

igece = ( "Tatlı rüyalar 🎉", "İyi geceler, görüşürüz .", "Gecen güzel geçsin kalbi güzel insan .", "Bir günün daha sonuna geldik, iyi geceler .", )

kyas = ( "Yaşın bi önemi var mı ?", "Tahmin et kaç yaşındayım .", "Senden büyük olduğum kessin .", )

nereli = ( "Dünyalı, ya sen", "Ben bir yerli değilim 😔", "Galiba Dünyanın bir yerindenim .", )

pms = ( "Sen konuşma 🤭", "Hayır, Konuşacam 🙄", )

krdn = ( "Ya kıyamam 😔", "Gel sarılalım .", "Oh iyi oldu .", )

knks = ( "Aaaa kankam gelmiş .", "Efendim Kanka 💕", )

skdm = ( "Bende, ne yapalım ?", "Benden sıkıldın mı ?", "Hadi uyuyalım .", "Oyun oynayalım mı ?", )

hms = ( "hmmmm 🙄", "Yeter ama aaaa 🙄", )

bts = ( "Sağolun 😔", "Eyvallah Ciğerim .", )

trt = ( "Oyun mu istiyorsun /turet yaz .", "Dc oynayalım mı, /d mi /c mi .", )

evt = ( "Hayır", "Hayır dedim", "yioooooooo", )

hyrr = ( "Ne demek hayır 🙄", "Evet", "Evet dedim", )

gzs = ( "Gözler ömre bedel 😂", "Yukarıda ne var 🤔", )

ofs = ( "of deme oh de 🤪", "Bakıyorum da oflamaya başladın 🙄", )

cklta = ( "Aaaaa çok severim 💕", "Bana Çikolata Alsana 🥺", "Çikolatam olur musun 😋", )

lna = ( " Ne var lan 🙄", "Bana mı dedin 😠", "Lannnnn sus 🙄", )

dddm = ( "Ne dedin ?", "Anlamadım ?", "Neden öyle dedin ?", )

ylna = ( "Yalan söyleyen kim 🙄", "Yalan konuşmayın çarparım 🙄", "Terbiyesiz 😠", )

sgll = ( "Sende sağol 💕", "Başımız sağolsun .", )

crkn = ( "Kimmiş çirkin olan 🙄", "Ben çok güzelim 🙈", "Sus artık 🙄", )

dmy = ( "Banın hayırlı olsun 🙄", "Şşşş, yasak ...", "Seni döverim bak 🙄", )

tymm = ( "Midemden tuhaf bir ses geliyor 😸", "Galiba acıktım 😋", "Olsa da yesek 🥺", )

kmm= ( "Bana bak 🙄", "Seni yollarım 😁", "Acımam ama 😁", "Sen şimdi hapı yuttun 😳", )

#x21 = ( "", "", "", "", )
#@client.on(events.NewMessage(pattern='(?i)buket+'))
#async def yeni_mesaj(event: events.NewMessage.Event):
#    await event.reply(f"➻ **Sohbet modu aktif etmek için /sohbetmod on yazın ...**")
@client.on(events.NewMessage(pattern="^/sohbetmod ?(.*)"))
async def chatbot(event):
    if event.is_private:
        await event.respond("**✓  sᴀᴅᴇᴄᴇ ɢʀᴜᴘʟᴀʀᴅᴀ ᴋᴜʟʟᴀɴɪʟᴀʙɪʟɪʀ .**", parse_mode='markdown')
        return

    if not await is_group_admin(event):
        await event.respond("**✓  sᴀᴅᴇᴄᴇ ᴀᴅᴍɪɴʟᴇʀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀ ...**", parse_mode='markdown')
        return
	    
    global isleyen
    emr = event.pattern_match.group(1)
    qrup = event.chat_id
    if emr == "on" or emr == "On":
        if qrup not in isleyen:
            isleyen.append(qrup)
            aktiv_olundu = "**✓ sᴏʜʙᴇᴛ ᴍᴏᴅ ᴏ̈ᴢᴇʟʟɪɢ̆ɪ ᴀᴋᴛɪғ ᴇᴅɪʟᴅɪ .\n\n💕 ᴀʀᴛıᴋ ᴋᴏɴᴜşᴀʙɪʟɪʀɪᴍ !**"
            await event.reply(aktiv_olundu)
            return
        await event.reply("**🗯️ ᴢᴀᴛᴇɴ ᴋᴏɴᴜşᴀʙɪʟɪʏᴏʀᴜᴍ .**")
        return
    elif emr == "off" or emr == "Off":
        if qrup in isleyen:
            isleyen.remove(qrup)
            await event.reply("**✓ sᴏʜʙᴇᴛ ᴍᴏᴅ ᴏ̈ᴢᴇʟʟɪɢ̆ɪ ᴅᴇᴠʀᴇ ᴅɪşɪ .\n\n💕 ᴀʀᴛıᴋ ᴋᴏɴᴜşᴀᴍᴀᴍ !**")
            return
        await event.reply("**🗯️ ᴢᴀᴛᴇɴ ᴋᴏɴᴜşᴀᴍɪʏᴏʀᴜᴍ !**")
        return
    
    else:
        await event.reply("**💕  ʙᴜᴋᴇᴛ sᴏʜʙᴇᴛ ᴍᴏᴅᴜ  :\n\n» /sohbetmod on\n   ➻ sᴏʜʙᴇᴛ ᴍᴏᴅᴜɴᴜ ᴀᴋᴛɪғ ᴇᴛ.\n» /sohbetmod off\n   ➻ sᴏʜʙᴇᴛ ᴍᴏᴅᴜɴᴜ ᴋᴀᴘᴀᴛ .**", buttons=(
                     [
	              Button.url('🎉  ʙɪʟɢɪ  ᴇᴅɪɴɪɴ ', f'https://t.me/{GROUP_SUPPORT}')
                    ]
                  ),
                link_preview=False)
	

# ~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
    await event.edit(f"{startbutton}", buttons=(

                    [
                      Button.inline("🗨️ ᴇᴛɪᴋᴇᴛ ᴋᴏᴍᴜᴛ", data="tag1"),
                      Button.inline("📚 ᴇxᴛʀᴀ ᴋᴏᴍᴜᴛ", data="tag2")
		      ],[
                      Button.inline("🎮 ᴏʏᴜɴ ᴋᴏᴍᴜᴛ", data="tag4"),
		      Button.inline("🧑🏻‍💻 sᴀʜɪᴘ ᴋᴏᴍᴜᴛ", data="tag3")
                  ],[
                      Button.inline("➡️ ɢᴇʀɪ ᴅᴏ̈ɴ", data="start")
                    ]
                 ),
               link_preview=False)    

@client.on(events.callbackquery.CallbackQuery(data="tag1"))
async def tag1(event):
    await event.edit(f"{tag1}", buttons=(
                     [
                      Button.inline("➡️ ɢᴇʀɪ ᴅᴏ̈ɴ", data="help")
                     ]
                   ), 
                 link_preview=False)                      

@client.on(events.callbackquery.CallbackQuery(data="tag2"))
async def tag2(event):
    await event.edit(f"{tag2}",
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
            await event.edit(f"{tag3}", buttons=(
                     [
                      Button.inline("➡️ ɢᴇʀɪ ᴅᴏ̈ɴ", data="help") 
                     ]
                   ),  
                 link_preview=False)
       if sender.id not in OWNER:
                 await event.reply(f"**➻ ᴏʟᴀᴍᴀᴢ, sᴀʜɪʙɪᴍ ᴅᴇɢɪʟsɪɴ 😳\n» ɴᴏᴛ : sᴀᴅᴇᴄᴇ sᴀʜɪʙɪᴍ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀ .**")
	
@client.on(events.callbackquery.CallbackQuery(data="tag4"))
async def tag4(event):
    await event.edit(f"{tag4}", buttons=(
                     [
                      Button.inline("➡️ ɢᴇʀɪ ᴅᴏ̈ɴ", data="help") 
                     ]
                   ),  
                 link_preview=False)
	
@client.on(events.NewMessage(pattern='/eros'))
async def eros_oku(event):
    if event.is_private:
        await event.respond("**✓  sᴀᴅᴇᴄᴇ ɢʀᴜᴘʟᴀʀᴅᴀ ᴋᴜʟʟᴀɴɪʟᴀʙɪʟɪʀ .**", parse_mode='markdown')
        return
	    
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
        f"{first_user_md_mention} 💕 {second_user_md_mention} \n\n**💞 sᴇᴠɢɪ ᴏʀᴀɴɪ : %{random.randint(0, 100)}**"
    )
    
    await event.respond(response, parse_mode="Markdown")


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
        await asyncio.sleep(4)
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
        await asyncio.sleep(4)
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
        await asyncio.sleep(4)
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
        await client.send_message(event.chat_id, f"**{usrtxt}**")
        await asyncio.sleep(4)
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
        await asyncio.sleep(4)
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

@app.on_message(filters.new_chat_members, group=1)
async def zar(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(BOT_ID):
            await msg.reply(
                f'''**💞 ᴍᴇʀʜᴀʙᴀ , {msg.from_user.mention}\n\n🗨️ ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇᴅɪɢ̆ɪɴ ɪᴄ̧ɪɴ ᴛᴇşşᴇᴋᴜ̈ʀ ᴇᴅᴇʀɪᴍ, ʙᴇɴɪ ʏᴏ̈ɴᴇᴛɪᴄɪ ʏᴀᴘᴍᴀʏɪ ᴜɴᴜᴛᴍᴀʏɪɴ ...\n\n🗯️ ᴅᴀʜᴀ ғᴀᴢʟᴀ ʙɪʟɢɪ ɪᴄ̧ɪɴ ᴀşşᴀɢ̆ɪᴅᴀᴋɪ ʙᴜᴛᴏɴᴜ ᴋᴜʟʟᴀɴɪɴ ...**''', 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💕  ʙᴜʀᴀʏᴀ ᴛɪᴋʟᴀ  ", url=f"https://t.me/{BOT_USERNAME}?start")]])
    )
        elif str(new_user.id) == str(OWNER_ID):
            await msg.reply('**🗯️ ᴅᴇɢ̆ᴇʀʟɪ sᴀʜɪʙɪᴍ [ㅤᴀɪᴋᴏㅤ](tg://openmessage?user_id=6540285284) ɢᴇʟᴅɪ, ʜᴏş ɢᴇʟᴅɪɴ ᴇғᴇɴᴅɪᴍ ...**')


@app.on_message(filters.command(["reload"], ["/"]) & ~filters.private & ~filters.channel)
async def reload(client: Client, message: Message):
    await message.reply_text("**♻️ ʙᴏᴛ ʏᴇɴɪᴅᴇɴ ʙᴀşʟᴀᴅɪ .\n♻️ ᴀᴅᴍɪɴ ʟɪsᴛᴇsɪ ɢᴜ̈ɴᴄᴇʟʟᴇɴᴅɪ .**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✅  ʏᴏ̈ɴᴇᴛɪᴄɪʟᴇʀ", callback_data="admins"),
                ],
            ],
        ),
			    )
	

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
# Verileri listeleme komutu
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



# Botu ilk başlatan kullanıcıların kontrolünü sağlar.
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
        USER_UNBAN_NOTIFY = "**💞 Hoppala, Çok Şanslısın ! \n👨🏻‍💻 Sahibim Yasağınızı kaldırdı !**"
        BLOCKS = "🆔 **Kullanıcı ID : {}\n⏱ Süre : {}\n🗓 Yasaklanan Tarih : {}\n💬 Sebep : {}**\n\n"
        TOTAL_BLOCK = "🚷 **Yasaklanan Kullanıcılar :** `{}`\n\n{}"
		
        
app.run()
print(" Bot çalışıyor :)")
client.run_until_disconnected()
