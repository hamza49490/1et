import random
import shutil, psutil, traceback, os
import time
import datetime
import motor.motor_asyncio
import shutil, psutil, traceback
import traceback
import aiofiles
import os, requests, time
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
from asyncio import sleep
from time import time
from os import remove
from telethon.sync import types
from datetime import datetime 
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.sync import TelegramClient, events
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User
from pyrogram.types.messages_and_media import Message
from pyrogram import Client, filters
from random import randint


logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID","26573250"))
api_hash = os.environ.get("API_HASH","6306d2d23b1083a6f757f64f0b0c609c")
bot_token = os.environ.get("TOKEN","6923679994:AAGjngufj1dlquEiS5iKHThAj-IPtJl7XPc")
BOT_USERNAME = os.environ.get("BOT_USERNAME","EpicBetaBot")
CHANNELL = os.environ.get("CHANNELL", "AikoCall")
OWNER_ID = int(os.environ.get("OWNER_ID","6811941116"))
OWNERNAME = "ㅤᴀɪ‌ᴋᴏㅤ"
OWNER = [6811941116]

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

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
CHAT_BOTS_DATA = {}


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
	
    if "buket" in kelimeler:
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
	    
    if kelimeler[0] == "iyi" or kelimeler[0] == "kötü" or kelimeler[0] == "iyiyim":
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
	    
    if kelimeler[0] == "merve":
        cevap = random.choice(merve)
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

    if kelimeler[0] == "of":
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


smesajs = ["Hoş Geldin 💕", "Nasılsın 😌",]
bottst = ["Bana mı dedin bot diye ?", "Ben bot değilim bi kere 🙄", "Bi daha bot dersen 🤬", "Hala bot diyor ya 😡", "Adamı hasta edersin 🙄", "Olm dayak yersin ama 😬",]
bkt = ["Efendim tatlım 💞", "Bana mı seslendin 🙄", "Yaw ne ne aaaa", "Seni dinliyorum gülüm 🥰", "Al sana harçlık 💰", "Başımın etini yedin 🙄", "Seni tokatlarım 😏", "Buyrun benim ?", "Offff 🙄", "Vay arkadaş bu çocuk abayı yakmış 😅", "Sus artik Sus !", "Dost elinden yaralıyam 😔", "Kırık kalbimi onarır mısın ?", "Seni seviyorum bitanem 💕", "Gel seni öpim 😘", "Dile benden ne dilersen", "Benim başım ağrıyor 🥺", "Yar beni sevmez !", "Şarkı söyleyelim mi ✨", "Efendim hocam ?",]
selam = ["ve aleyküm selam hoş geldin yahu", "Aleyküm Selam Naber 🎉", "Selam Hoş Geldin", "Ase, Hoş Geldin 💕",]
nasilsin = ["Senle iyi, Sen ?", "İyiyim senden naber", "İyiyim sen", "İyim fıstık, ya sen 💕", "Teşekkür ederim iyiyim sen nasılsın", "Tıpkı senin gibi mükemmelim 🥳",]
adam = ["Mermiler seksin, alemde teksin 😏", "Mermiler seksin, tokatımı yersin 😏",]
iyiyim = ["İyi olmana sevindim", "Hep daha iyi olman dileğiyle  ", "Keşke bende senin kadar iyi olsam 😏",]
hoş = ["Naber", "Hoş buldum nabıyon", "Nasılsın",]
merhaba = ["Merhaba, Hoş geldin", "Merhabalar Hoş geldiniz efem 🥳", "Merhaba, nerelerdesin ya sen", "yine özlettin kendini 😏",]
ban = ["İmdatttt, grup boşalıyor 😱", "Grupta üye kalmadı mübarek 🙄", "Ayıp ettin !", "Bak sen 🤔", "Adamın dibisin sen :)", "Grub boşalıyor yetişin .",]
nabiyon = ["Oturuyorum, sen", "Gördüğün gibi takılıyoruz", "Yapacak bişey yok", "Ne yapmamı istersin",]
uzgun = ["Kıyamam ki ben sana 😢", "Üzülme, buda geçer 😔", "Bizi üzenler utansın 😏", "Hoppala, kim üzdü seni",]
valla = ["tamam, tamam inandım 🥴", "de valla", "Deme öyle Allah çarpar", "Sus çarpılırsin .",]
sg = ["Küfür etme turşu !", "Lütfen düzgün konuş 😏", "Dayanamıyacam ben artık ama ...", "Ben buna dalarım ama ...",]
mal = ["Akıllı görünce kıskandı 😏", "Sana özeniyorum, galiba başarıyorum 🙈", "Beni birine benzettin galiba 🙄", "Hop, orda dur beni daha fazla sinirlendirmeyin lütfen ...",]
balim = ["Arı mısın gülüm 🙈", "Canın çektiyse yiyebilirsin beni 😋", "Efendim, hayatım .", "Şımarıyorum ama 🙈",]
canim = ["Gülüm 💕", "Bebeğim 💕", "Bitanem 💕", "Hayatım 💕", "Turşu suratlım 💕",]
gidiyorum = ["Nereye, Karpuz Kesmiştik .", "Hoşuma yeterince gittin, otur oturduğun yerde 🤫", "Görüşürüz, Hakkını helal et ...", "Kal desem kalır mı acaba 🤔",]
sinirlendim = ["Farkettim .", "Sakin ol, Şampiyon .", "Bakıyorum da Domates gibi kızardın .", "Ne yapayım .",]
tanis = ["Olur tanışalım .", "Kim olduğunu biliyorum :)", "Kendini tanıt !", "Düşünmem gerek 🤔",]
adne = ["Buket, ya senin ?", "Sen söylersen bende söylerim 😏", "Söylemem, banane .", "Ben de Buket memnun oldum ❣️",]
iyisen = ["Bende iyiyim teşekürler .", "Senin gibi iyi olamıyorum 😔", "Birazcık kötüyüm .", "Mükemmelim tıpkı senin gibi 🤭",]
gullu = ["Ne gülüyon?", "Açıkta bişey mi gördün .", "Bakıyorum da keyfin yerinde .", "Mutlu olmana sevindim 💕",]
buyuk = ["Senden Büyük Allah var 😎", "Yalan söyleme .", "Hayır, Küçük ✓",]
aiko = ["Buyrun, Asistanı olurum ?", "Aiko kadar başına taş düşsün emi .", "Öldü artık yok 🙄",] 
merve = ["Rahmetliyi Sevmezdik 😔", "Öldü o, Artık yaşamıyor .", "Hayatımın Anlamı Nerdesin 🤭",]
gnyy = ["Günaydın, naber", "Günüm aydı, hoş geldin 🎉", "Günaydın, tatlım .", "Güneşim doğdu, hoş geldin 🥳",]
igece = ["Tatlı rüyalar 🎉", "İyi geceler, görüşürüz .", "Gecen güzel geçsin kalbi güzel insan .", "Bir günün daha sonuna geldik, iyi geceler .",]
kyas = ["Yaşın bi önemi var mı ?", "Tahmin et kaç yaşındayım .", "Senden büyük olduğum kessin .",]
nereli = ["Dünyalı, ya sen", "Ben bir yerli değilim 😔", "Galiba Dünyanın bir yerindenim .",]
pms = ["Susmasam ne olur 😳", "Lan sus 🙄", "Sen konuşma 🤭", "Hayır, Konuşacam 🙄",]
krdn = ["Ya kıyamam 😔", "Gel sarılalım .", "Oh iyi oldu .",]
skdm = ["Bende, ne yapalım ?", "Benden sıkıldın mı ?", "Hadi uyuyalım .", "Oyun oynayalım mı ?",]
hms = ["hmmmm 🙄", "Yeter ama aaaa 🙄", "Kafana sıkarım senin 🙄",]
bts = ["Sağolun 😔", "Eyvallah Ciğerim .",]
trt = ["Oyun mu istiyorsun /turet yaz .", "/d mi /c mi !", "aaaa oyun oynamayı unuttuk 😬 derhal /sayi yaz .",]
evt = ["Bi sus ya", "Hayır", "Hayır dedim", "yioooooooo",]
hyrr = ["la havle vela kuvvete", "Ne demek hayır 🙄", "Evet", "Evet dedim",]
gzs = ["Gözler ömre bedel 😂", "Yukarıda ne var 🤔",]
ofs = ["pffffff", "of deme oh de 🤪", "Bakıyorum da oflamaya başladın 🙄",]
cklta = ["Aaaaa çok severim 💕", "Bana Çikolata Alsana 🥺", "Çikolatam olur musun 😋",]
lna = ["Lan mı, memleket bize Ana diyor 🙄", "Ne var lan 🙄", "Bana mı dedin 😠", "Lannnnn sus 🙄",]
dddm = ["Duymadım 😜", "Ne dedin ?", "Anlamadım ?", "Neden öyle dedin ?",]
ylna = ["Yalan söyleyen kim 🙄", "Yalan konuşmayın çarparım 🙄", "Terbiyesiz 😠",]
sgll = ["Sende sağol 💕", "Başımız sağolsun .",]
crkn = ["Kimmiş çirkin olan 🙄", "Ben çok güzelim 🙈", "Sus artık 🙄",]
dmy = ["Banın hayırlı olsun 🙄", "Şşşş, yasak ...", "Seni döverim bak 🙄",]
tymm = ["Midemden tuhaf bir ses geliyor 😸", "Galiba acıktım 😋", "Olsa da yesek 🥺",]
kmm= ["Olm sinirleniyorum ama 😬", "Bana bak 🙄", "Seni yollarım 😁", "Acımam ama 😁", "Sen şimdi hapı yuttun 😳",]
kankas = ["Efendim canım 💕", "Kanka diyen ağzını 😁", "Bana mı dedin lan 😳", "Bi daha dersen, fena olur 🙄",]
opsss = ["Muahhhhhhh 😘", "Utandırma beni 🤭", "Yanaş bakim 😲",]
sgne = ["Nasıl sanane 🙄", "Asıl sanane 😏", "Seni alakadar etmez 😏",]
bgne = ["Yok öyle yama 😏", "Asıl banane 😏", "Şşşş bidaha duymim 🙄",]

@client.on(events.NewMessage(pattern="(?i)/chatbot"))
async def chatbot(event):
    if event.is_private:
        await event.respond(f"{nogroup}", parse_mode='markdown')
        return

    if not await is_group_admin(event):
        await event.respond(f"{noadmin}", parse_mode='markdown')
        return
     
    global isleyen
    await event.reply(f"**__✦  sᴇᴄ‌ɪᴍ ʏᴀᴘɪɴ  ✦__**", buttons=[
        [Button.inline("✅ ᴀᴋᴛɪ̇ғ ᴇᴛ", data="sohbetmod_on")],
        [Button.inline("⛔ ᴅᴇᴠʀᴇ ᴅɪşɪ", data="sohbetmod_off")]
    ])


@client.on(events.CallbackQuery(pattern=b"sohbetmod_on"))
async def callback_sohbetmod_on(event):
    qrup = event.chat_id
    if qrup not in isleyen:
        isleyen.append(qrup)
        aktiv_olundu = "**__💕 sᴏʜʙᴇᴛ ᴍᴏᴅ ᴏ‌ᴢᴇʟʟɪɢ‌ɪ ᴀᴋᴛɪғ ᴇᴅɪʟᴅɪ .\n\n✦ ᴀʀᴛıᴋ ᴋᴏɴᴜs‌ᴀʙɪʟɪʀɪᴍ !__**"
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
    await event.edit("**__✦ ᴢᴀᴛᴇɴ ᴋᴏɴᴜs‌ᴀʙɪʟɪʏᴏʀᴜᴍ .__**")
		

@client.on(events.CallbackQuery(pattern=b"sohbetmod_off"))
async def callback_sohbetmod_off(event):
    qrup = event.chat_id
    if qrup in isleyen:
        isleyen.remove(qrup)
        await event.edit("**__💕 sᴏʜʙᴇᴛ ᴍᴏᴅ ᴏ‌ᴢᴇʟʟɪɢ‌ɪ ᴅᴇᴠʀᴇ ᴅɪs‌ɪ .\n\n✦ ᴀʀᴛıᴋ ᴋᴏɴᴜs‌ᴀᴍᴀᴍ !__**")
        return
    await event.edit("**__✦ ᴢᴀᴛᴇɴ ᴋᴏɴᴜs‌ᴀᴍɪʏᴏʀᴜᴍ !__**")

@client.on(events.NewMessage(pattern=r"(?i)(/|)buket", incoming=True))
async def buket_handler(event):
    if event.is_private:
        return
    chat_id = event.chat_id
    if chat_id in isleyen:
        return
    await event.respond("**__💞 şᴜᴀɴ sᴏʜʙᴇᴛ ᴍᴏᴅᴜ ᴋᴀᴘᴀʟɪ !\n✦ ᴀᴄ̧ᴍᴀᴋ ɪ̇ᴄ̧ɪ̇ɴ ➻ /chatbot __**")
	
##################################################
##################################################
##################################################
@client.on(events.NewMessage(pattern='(?i)(/|)ship'))
@client.on(events.NewMessage(pattern='(?i)(/|)eros'))
async def handle_eros(event):
    chat = await event.get_chat()
    if event.is_reply:
        reply_msg = await event.get_reply_message()
        user1 = await event.client.get_entity(reply_msg.from_id)
        user2 = await event.client.get_entity(event.sender_id)
        love_percentage = random.randint(0, 100)
        await event.reply(f"**💘 ᴇʀᴏs'ᴜɴ ᴏᴋᴜɴᴜ ᴀᴛᴛɪᴍ .\n✦  ɢɪᴢʟɪ ᴀşɪᴋʟᴀʀ :\n\n[{user2.first_name}](tg://user?id={user2.id})  💕  [{user1.first_name}](tg://user?id={user1.id}) \n\n💞 sᴇᴠɢɪ ᴏʀᴀɴɪ : %{love_percentage}**")
    else:
        participants = await event.client.get_participants(chat)
        active_users = [user for user in participants if not user.bot and not user.deleted and not user.is_self]
        if len(active_users) < 2:
            await event.reply("**__⛔ Yᴇᴛᴇʀʟɪ Aᴋᴛɪғ Kᴜʟʟᴀɴɪᴄɪ Yᴏᴋ !__**")
        else:
            user1, user2 = random.sample(active_users, 2)
            love_percentage = random.randint(0, 100)
            await event.reply(f"**__💘 ᴇʀᴏs'ᴜɴ ᴏᴋᴜɴᴜ ᴀᴛᴛɪᴍ .\n✦  ɢɪᴢʟɪ ᴀşɪᴋʟᴀʀ :__\n\n[{user1.first_name}](tg://user?id={user1.id})  💕  [{user2.first_name}](tg://user?id={user2.id}) \n\n__💞 sᴇᴠɢɪ ᴏʀᴀɴɪ : %{love_percentage}__**")

@client.on(events.NewMessage(pattern='(?i)(/|)slap'))
async def slap(event):
    if event.is_private:
        return await event.respond(f"{nogroup}")

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
            await event.respond("**__👁️‍🗨️ ᴜ̈ᴢɢᴜ̈ɴᴜ̈ᴍ, ᴋᴜʟʟᴀɴɪᴄɪʏɪ ʙᴜʟᴀᴍɪʏᴏʀᴜᴍ !__**")
    else:
        await event.respond("**__💭 ʙɪʀ ᴍᴇsᴀᴊᴀ ʏᴀɴɪᴛ ᴠᴇʀɪɴ !__**")

##################################################
##################################################
##################################################
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     await event.reply_photo(
	     photo="https://telegra.ph/file/9898d0f8006cf4dd47245.jpg",
	     caption=f"{startmesaj}", buttons=(
                      [
                      Button.url('➕  𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾  ➕', f'https://t.me/{BOT_USERNAME}?startgroup=a'),
                    ],[
                      Button.inline("📚 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋", data="help"),
                      Button.url('🗨️ 𝖡𝗂𝗅𝗀𝗂 𝖪𝖺𝗇𝖺𝗅ı', f'https://t.me/{CHANNELL}')
                    ],[
                      Button.url('✦  𝖮𝗐𝗇𝖾𝗋  ✦', f'tg://openmessage?user_id={OWNER_ID}')
                    ]
                  ),
                link_preview=False)

  if event.is_group:
    return await client.send_message(event.chat_id, f"{startmesaj}", buttons=(
                      [
                      Button.url('➕  𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾  ➕', f'https://t.me/{BOT_USERNAME}?startgroup=a'),
                    ],[
                      Button.inline("📚 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋", data="help"),
                      Button.url('🗨️ 𝖡𝗂𝗅𝗀𝗂 𝖪𝖺𝗇𝖺𝗅ı', f'https://t.me/{CHANNELL}')
		    ],[
		      Button.url('✦  𝖮𝗐𝗇𝖾𝗋  ✦', f'tg://openmessage?user_id={OWNER_ID}')
		      ]
                  ),
                link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="start"))
async def start(event):
    await event.edit(f"{startmesaj}", buttons=(
                      [
                      Button.url('➕  𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾  ➕', f'https://t.me/{BOT_USERNAME}?startgroup=a'),
                    ],[
                      Button.inline("📚 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋", data="help"),
                      Button.url('🗨️ 𝖡𝗂𝗅𝗀𝗂 𝖪𝖺𝗇𝖺𝗅ı', f'https://t.me/{CHANNELL}')
		    ],[
		      Button.url('✦  𝖮𝗐𝗇𝖾𝗋  ✦', f'tg://openmessage?user_id={OWNER_ID}')
		      ]
                  ),
                link_preview=False)
    
@client.on(events.callbackquery.CallbackQuery(data="help"))
async def help(event):
    await event.edit(f"{startbutton}", buttons=(
                      [
                      Button.inline("📇 𝖤𝗍𝗂𝗄𝖾𝗍 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋ı", data="tag1"),
		    ],[
		      Button.inline("🗒️ 𝖤𝗄 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋", data="tag2")
		    ],[
                      Button.inline("🎯 𝖮𝗒𝗎𝗇 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋ı", data="tag4"),
                    ],[
                      Button.inline("➡️ 𝖦𝖾𝗋𝗂 𝖣𝗈̈𝗇", data="start")
                    ]
                 ),
               link_preview=False)    

@client.on(events.callbackquery.CallbackQuery(data="tag1"))
async def tag1(event):
    await event.edit(f"{etikett}", buttons=(
                     [
                      Button.inline("➡️ 𝖦𝖾𝗋𝗂 𝖣𝗈̈𝗇", data="help")
                     ]
                   ), 
                 link_preview=False)                      

@client.on(events.callbackquery.CallbackQuery(data="tag2"))
async def tag2(event):
    await event.edit(f"{extraa}",
		     buttons=(
                     [
                      Button.inline("➡️ 𝖦𝖾𝗋𝗂 𝖣𝗈̈𝗇", data="help") 
                     ]
                   ),  
                 link_preview=False)
	
@client.on(events.callbackquery.CallbackQuery(data="tag4"))
async def tag4(event):
    await event.edit(f"{oyunn}", buttons=(
                     [
                      Button.inline("➡️ 𝖦𝖾𝗋𝗂 𝖣𝗈̈𝗇", data="help") 
                     ]
                   ),  
                 link_preview=False)

@client.on(events.NewMessage(pattern='(?i)(/|)soz'))
async def sahib(event):
    await event.reply(f"**__✦ ʙɪʀ ᴛᴜ̈ʀ sᴇᴄ̧ɪɴ !__**", buttons=(
                     [
                      Button.inline("🌹 𝖦𝗎̈𝗓𝖾𝗅 𝖲𝗈̈𝗓", data="guzelsos"),
		      Button.inline("🦅 𝖪𝖺𝗉𝖺𝗄 𝖲𝗈̈𝗓", data="kapaksos")
                     ],[
                      Button.inline("💞  𝖱𝗈𝗆𝖺𝗇𝗍𝗂𝗄 𝖲𝗈̈𝗓", data="romantiksos")
		     ]
                   ),  
                 link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="soz"))
async def sahib(event):
    await event.reply(f"**__✦ ʙɪʀ ᴛᴜ̈ʀ sᴇᴄ̧ɪɴ !__**", buttons=(
                     [
                      Button.inline("🌹 𝖦𝗎̈𝗓𝖾𝗅 𝖲𝗈̈𝗓", data="guzelsos"),
		      Button.inline("🦅 𝖪𝖺𝗉𝖺𝗄 𝖲𝗈̈𝗓", data="kapaksos") 
                     ],[
                      Button.inline("💞  𝖱𝗈𝗆𝖺𝗇𝗍𝗂𝗄 𝖲𝗈̈𝗓", data="romantiksos")
		     ]
                   ),  
                 link_preview=False)
	
@client.on(events.callbackquery.CallbackQuery(data="guzelsos"))
async def guzel(event):
    await event.edit(f"**🌹 𝖦𝗎̈𝗓𝖾𝗅 𝖲𝗈̈𝗓 :\n\n{random.choice(guzelsoz)}**", buttons=(
                     [
                      Button.inline("🗨️ ᴛᴇᴋʀᴀʀ ᴅᴇɴᴇ", data="soz")
		     ]
                   ),  
                 link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="kapaksos"))
async def romantik(event):
    await event.edit(f"**🦅 𝖪𝖺𝗉𝖺𝗄 𝖲𝗈̈𝗓 :\n\n{random.choice(kapaksoz)}**", buttons=(
                     [
		      Button.inline("🗨️ ᴛᴇᴋʀᴀʀ ᴅᴇɴᴇ", data="soz")
		     ]
                   ),  
                 link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="romantiksos"))
async def romantik(event):
    await event.edit(f"**💞  𝖱𝗈𝗆𝖺𝗇𝗍𝗂𝗄 𝖲𝗈̈𝗓 :\n\n{random.choice(romantiksoz)}**", buttons=(
                     [
		      Button.inline("🗨️ ᴛᴇᴋʀᴀʀ ᴅᴇɴᴇ", data="soz")
		     ]
                   ),  
                 link_preview=False)

##################################################
##################################################
##################################################
@client.on(events.NewMessage(pattern='(?i)/id'))
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
		

@client.on(events.NewMessage(pattern='(?i)/dels'))
async def purge_messages(event):
    if event.is_private:
        await event.respond(f"{nogroup}", parse_mode='markdown')
        return

    if not await is_group_admin(event):
        await event.respond(f"{noadmin}", parse_mode='markdown')
        return

    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.respond("**✓  sɪʟᴍᴇᴍ ɪᴄ‌ɪɴ ʙɪʀ ᴍᴇsᴀᴊ ʏᴀɴɪᴛʟᴀ .**")
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
    text = f"✓  ᴛᴇᴍɪᴢʟᴇᴍᴇ {time_:0.2f} ᴛᴀᴍᴀᴍʟᴀɴᴅɪ ..."
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
	

@client.on(events.NewMessage(pattern='(?i)/grup'))
async def sahib(event):
    if event.is_private:
        await event.respond(f"{nogroup}", parse_mode='markdown')
        return

    if not await is_group_admin(event):
        await event.respond(f"{noadmin}", parse_mode='markdown')
        return
	    
    user = await event.get_sender()
    user_first_name = f"[{user.first_name}](tg://user?id={user.id})"
    response_text = f'** {user_first_name} __ʟᴜ̈ᴛғᴇɴ ʙᴇᴋʟᴇ ...__**'
    response = await event.respond(response_text)
    await asyncio.sleep(2)
    await response.delete()
	
    await event.reply(f"**__✦ ʟᴜ̈ᴛғᴇɴ ʙɪʀ sᴇᴄ̧ɪᴍ ʏᴀᴘ !__**", buttons=(
                     [
                      Button.inline("🤖  𝖦𝗋𝗎𝗉 𝖡𝗈𝗍𝗅𝖺𝗋ı", data="gbot"),
		      Button.inline("👤 𝖦𝗋𝗎𝗉 𝖠𝖽𝗆𝗂𝗇𝗅𝖾𝗋𝗂", data="gadmin")
		     ],[
                      Button.inline("⚙️ 𝖦𝗋𝗎𝗉 𝖧𝖺𝗄𝗄ı𝗇𝖽𝖺", data="gbilgi")
                     ]
                   ),  
                 link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="grup"))
async def sahib(event):
    await event.edit(f"**__✦ ʟᴜ̈ᴛғᴇɴ ʙɪʀ sᴇᴄ̧ɪᴍ ʏᴀᴘ !__**", buttons=(
                     [
                      Button.inline("🤖  𝖦𝗋𝗎𝗉 𝖡𝗈𝗍𝗅𝖺𝗋ı", data="gbot"),
		      Button.inline("👤 𝖦𝗋𝗎𝗉 𝖠𝖽𝗆𝗂𝗇𝗅𝖾𝗋𝗂", data="gadmin")
		     ],[
                      Button.inline("⚙️ 𝖦𝗋𝗎𝗉 𝖧𝖺𝗄𝗄ı𝗇𝖽𝖺", data="gbilgi")
                     ]
                   ),  
                 link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="gadmin"))
async def show_admins(event):	    
    chat = await event.get_chat()
    admins = await event.client.get_participants(chat, filter=types.ChannelParticipantsAdmins)
    admin_list = ""
    for admin in admins:
        admin_list += f"\n➻  [{admin.first_name}](tg://user?id={admin.id})"
    await event.edit(f"**__🗨️  ɢʀᴜᴘᴛᴀᴋɪ ᴀᴅᴍɪɴʟᴇʀ :__ \n{admin_list}**", buttons=(
                     [
                      Button.inline("🗯️  𝖦𝖾𝗋𝗂", data="grup")
                     ]
                   ),  
                 link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="gbot"))
async def show_bots(event):
	    
    geri_button = Button.inline("🗯️  𝖦𝖾𝗋𝗂", data="grup")	
    all_users = await event.client.get_participants(event.chat_id)
    bot_list = []
    for user in all_users:
        if isinstance(user, types.User) and user.bot:
            bot_list.append(user.username)
    if bot_list:
        await event.edit(f"**__🤖 ɢʀᴜᴘᴛᴀᴋɪ ʙᴏᴛʟᴀʀ :__**\n\n➻  @" + "\n➻  @".join(bot_list), buttons=[[geri_button]])
    else:
        await event.edit("**__🤖 ʙᴜ ɢʀᴜᴘᴛᴀ ʜɪᴄ̧ ʙᴏᴛ ʏᴏᴋ .__**", buttons=(
                     [
                      Button.inline("🗯️  𝖦𝖾𝗋𝗂", data="grup")
                     ]
                   ),  
                 link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="gbilgi"))
async def grup_info(event):
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
        special_status += f'__➻ sɪʟɪɴᴇɴ ʜᴇsᴀᴘ sᴀʏɪsɪ __: {deleted_count}\n'
    if bot_count > 0:
        special_status += f'__➻ ɢʀᴜᴘ ʙᴏᴛ sᴀʏɪsɪ __: {bot_count}\n'

    if not special_status:
        special_status = "__ʙᴜʟᴜɴᴀᴍᴀᴅɪ__"

    geri_button = Button.inline("🗯️  𝖦𝖾𝗋𝗂", data="grup")

    response_text = (
        f'**__➻ ɢʀᴜᴘ ᴀᴅɪ __: {group_name}**\n'
        f'**__➻ ɢʀᴜᴘ ɪᴅ __:** `-100{group_id}`\n'
        f'**__➻ ᴜʏᴇ sᴀʏɪsɪ __: {total_count}**\n'
        f'**__➻ ᴀᴋᴛɪғ ᴜʏᴇ sᴀʏɪsɪ __: {active_count}**\n'
        f'**{special_status}**'
    )

    await event.edit(response_text, buttons=[[geri_button]])
			
##################################################
##################################################
##################################################
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

  if event.chat_id not in gece_tag:
    return await event.respond("**__• ᴀᴋᴛɪ̇ғ ʙɪ̇ʀ ɪ̇şʟᴇᴍ ʏᴏᴋ !__**")

  gece_tag.remove(event.chat_id)
  sender = await event.get_sender()
  rxyzdev_stopT = f"[{sender.first_name}](tg://user?id={sender.id})"      
  if event.chat_id in rxyzdev_tagTot:
    await event.respond(f"**⛔ ɪşʟᴇᴍɪ ɪᴘᴛᴀʟ ᴇᴛᴛɪᴍ ...\n\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**")


@client.on(events.NewMessage(pattern="^(?i)/atag ?(.*)"))
async def atag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /atag Merhaba**")
    msg = msg_list[1]
    if msg == "/atag":
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /atag Merhaba**")
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("____")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /atag Merhaba**")
    msg = msg_list[1]
  else:
      return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /atag Merhaba**")
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"{ibaslama}")

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
      await event.respond(f"**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...\n\n➻  {rxyzdev_initT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**")


@client.on(events.NewMessage(pattern="^(?i)/utag ?(.*)"))
async def utag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /utag Merhaba**")
    msg = msg_list[1]
    if msg == "/utag":
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /utag Merhaba**")
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("____")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /utag Merhaba**")
    msg = msg_list[1]
  else:
      return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /utag Merhaba**")
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"{ibaslama}")

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
        await client.send_message(event.chat_id, f"**➻ {msg}\n\n{usrtxt}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:
      await event.respond(f"**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...\n\n➻  {rxyzdev_initT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**")
	    

@client.on(events.NewMessage(pattern="^(?i)/tag ?(.*)"))
async def tag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /tag Merhaba**")
    msg = msg_list[1]
    if msg == "/tag":
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /tag Merhaba**")
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("____")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /tag Merhaba**")
    msg = msg_list[1]
  else:
      return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /tag Merhaba**")
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"{ibaslama}")

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
      await event.respond(f"**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...\n\n➻  {rxyzdev_initT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**")


@client.on(events.NewMessage(pattern="^(?i)/etag ?(.*)"))
async def etag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /etag Merhaba**")
    msg = msg_list[1]
    if msg == "/etag":
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /etag Merhaba**")
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("____")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /etag Merhaba**")
    msg = msg_list[1]
  else:
      return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /etag Merhaba**")
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"{ibaslama}")

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
        await client.send_message(event.chat_id, f"**➻ {msg}\n\n{usrtxt}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:
      await event.respond(f"**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...\n\n➻  {rxyzdev_initT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**")


@client.on(events.NewMessage(pattern="^(?i)/vtag ?(.*)"))
async def vtag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /vtag Merhaba**")
    msg = msg_list[1]
    if msg == "/vtag":
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /vtag Merhaba**")
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("____")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /vtag Merhaba**")
    msg = msg_list[1]
  else:
      return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /vtag Merhaba**")
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"{ibaslama}")

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
      await event.respond(f"**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...\n\n➻  {rxyzdev_initT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**")


@client.on(events.NewMessage(pattern="^(?i)/otag ?(.*)"))
async def otag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /otag Merhaba**")
    msg = msg_list[1]
    if msg == "/otag":
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /otag Merhaba**")
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("____")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /otag Merhaba**")
    msg = msg_list[1]
  else:
      return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /otag Merhaba**")
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"{ibaslama}")

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
      await event.respond(f"**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...\n\n➻  {rxyzdev_initT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**")


@client.on(events.NewMessage(pattern="^(?i)/stag ?(.*)"))
async def stag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /stag Merhaba**")
    msg = msg_list[1]
    if msg == "/stag":
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /stag Merhaba**")
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("____")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    mode = "text_on_cmd"
    msg_list = event.pattern_match.string.split(None, 1)
    if len(msg_list) < 2:
        return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /stag Merhaba**")
    msg = msg_list[1]
  else:
      return await event.respond(f"**💭 ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .\n💕 öʀɴᴇᴋ : /stag Merhaba**")
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"{ibaslama}")

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
      await event.respond(f"**🗨️ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇʏɪ ᴛᴀᴍᴀᴍʟᴀᴅɪᴍ ...\n\n➻  {rxyzdev_initT}\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**")
	
##################################################
##################################################
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
