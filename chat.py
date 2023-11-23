import logging
import asyncio
import random
import string
import aiohttp
import random

import config
from config import *

from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters, types
from time import sleep
from random import shuffle
from mesaj.botmesaj import *
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

app = Client(
    "Chat-Bot",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN
)


isleyen = []
@app.on_message(filters.command("chatbot", prefixes="/"))
async def chatbot(client, message):
    if message.chat.type == "private":
        await message.reply("🔹 __**ʙᴜ ᴋᴏᴍᴜᴛᴜ ɢʀᴜᴘʟᴀʀᴅᴀ ᴋᴜʟʟᴀɴ !**__", parse_mode='markdown')
        return
     
    admins = []
    async for admin in client.iter_chat_members(message.chat.id, filter="administrators"):
        admins.append(admin.user.id)
    if message.from_user.id not in admins:
        return await message.reply(f"😏 __**ʏᴏ̈ɴᴇᴛɪ̇ᴄɪ̇ ᴅᴇɢ̆ɪ̇ʟsɪ̇ɴ ʙᴇʙᴇɢ̆ɪ̇ᴍ !**__")
    
    global isleyen
    if message.chat.id in isleyen:
        status = " ᴀᴋᴛɪ̇ғ"
    else:
        status = " ᴋᴀᴘᴀʟɪ"
    
    await message.reply(f"__**✦ ᴀşᴀɢ̆ɪᴅᴀɴ sᴇᴄ̧ɪ̇ᴍ ʏᴀᴘɪɴ ! \n\n✦ ᴅᴜʀᴜᴍ : {status}**__", reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("✅ ᴀᴋᴛɪ̇ғ ᴇᴛ", callback_data="sohbetmod_on")],
            [InlineKeyboardButton("⛔ ᴋᴀᴘᴀᴛ", callback_data="sohbetmod_off")]
        ]
    ))

@app.on_callback_query()
async def callback_sohbetmod(client, callback_query):
    qrup = callback_query.message.chat.id
    if callback_query.data == "sohbetmod_on":
        if qrup not in isleyen:
            isleyen.append(qrup)
            aktiv_olundu = "__**✦ ʙᴀs‌ᴀʀɪʏʟᴀ ᴀᴋᴛɪғ ᴇᴅɪʟᴅɪ .\n\n✦ ᴀʀᴛıᴋ ᴋᴏɴᴜs‌ᴀʙɪʟɪʀɪᴍ !**__"
            await callback_query.edit_message_text(aktiv_olundu)
            return
        await callback_query.edit_message_text("__**✦ ᴄʜᴀᴛ ʙᴏᴛ ᴢᴀᴛᴇɴ ᴀᴋᴛɪ‌ғ .**__")
    elif callback_query.data == "sohbetmod_off":
        if qrup in isleyen:
            isleyen.remove(qrup)
            await callback_query.edit_message_text("__**✦ ʙᴀs‌ᴀʀɪʏʟᴀ ᴋᴀᴘᴀᴛɪʟᴅɪ .\n\n✦ ᴀʀᴛıᴋ ᴋᴏɴᴜs‌ᴀᴍᴀᴍ !**__")
            return
        await callback_query.edit_message_text("__**✦ ᴄʜᴀᴛ ʙᴏᴛ ᴢᴀᴛᴇɴ ᴋᴀᴘᴀʟɪ !**__")

@app.on_message()
async def chatbot(client, message):
    global isleyen
    mesaj = str(message.text)
    qrup = message.chat.id
    if qrup not in isleyen:
        if "derya" in mesaj.lower().split(" "):
            await message.reply("__**✦ ᴄʜᴀᴛ ʙᴏᴛ s‌ᴜᴀɴ ᴋᴀᴘᴀʟɪ !\n✦ ᴀᴄ‌ᴍᴀᴋ ɪ‌ᴄ‌ɪɴ ➻ /chatbot**__")
        return
    
    me = await client.get_me()
    if message.from_user.id == me.id:
        return
    
    kelimeler = mesaj.lower().split(" ")  # Mesajı küçük harfe çevirip kelimelere ayır

    if "derya" in kelimeler:
        cevap = random.choice(bkt)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
        return
  
    if kelimeler[0] in ["bot"]:
        cevap = random.choice(bottst)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
        return

    if "selamün aleyküm" in mesaj.lower() or kelimeler[0] in ["slm", "selam", "sa", "sea"]:
        cevap = random.choice(selam)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
        return
	
    if "ne haber" in mesaj.lower() or kelimeler[0] in ["nasılsın", "naber", "nbr"]:
        cevap = random.choice(nasilsin)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["erkek", "adam"]:
        cevap = random.choice(adam)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["iyiyim", "mükemmel", "harika"]:
        cevap = random.choice(iyiyim)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if "hoş geldin" in mesaj.lower() or kelimeler[0] in ["hg"]:
        cevap = random.choice(hoş)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["merhaba", "mrb"]:
        cevap = random.choice(merhaba)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["ban", "/ban", "banned", "banla"]:
        cevap = random.choice(ban)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if "ne yapıyorsun" in mesaj.lower() or kelimeler[0] in ["nabiyon", "napıyorsun"]:
        cevap = random.choice(nabiyon)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["😔", "🥺", "😢"]:
        cevap = random.choice(uzgun)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["valla", "vallahi", "yemin"]:
        cevap = random.choice(valla)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    	    
    if kelimeler[0] in ["sg", "siktir"]:
        cevap = random.choice(sg)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["mal", "gerizekalı", "it", "şrfsz", "şerefsiz"]:
        cevap = random.choice(mal)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["balım", "bebeğim", "aşkım"]:
        cevap = random.choice(balim)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["canım", "bitanem", "yavrum"]:
        cevap = random.choice(canim)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["gidiyorum", "gittim", "görüşürüz"]:
        cevap = random.choice(gidiyorum)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["sinirlendim", "sinirliyim", "sinirleniyorum", "😡", "😤"]:
        cevap = random.choice(sinirlendim)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if "tanışabilir miyiz" in mesaj.lower() or "tanışalım mı" in mesaj.lower():
        cevap = random.choice(tanis)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if "adın ne" in mesaj.lower() or "ismin ne" in mesaj.lower():
        cevap = random.choice(adne)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if "idare eder" in mesaj.lower() or kelimeler[0] in ["kötü", "iyi"]:
        cevap = random.choice(iyisen)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["😅", "😂", "🤣"]:
        cevap = random.choice(gullu)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["büyüğüm", "büyük"]:
        cevap = random.choice(buyuk)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	
    if kelimeler[0] in ["aiko"]:
        cevap = random.choice(aiko)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["günaydın", "günaydınnn", "gny", "rojbaş"]:
        cevap = random.choice(gnyy)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if "iyi akşamlar" in mesaj.lower() or "iyi geceler" in mesaj.lower():
        cevap = random.choice(igece)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if "kaç yaşındasın" in mesaj.lower() or "yaşın kaç" in mesaj.lower():
        cevap = random.choice(kyas)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["nerelisin"]:
        cevap = random.choice(nereli)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["konuşma", "sus", "knşma"]:
        cevap = random.choice(pms)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["kırdı", "krldm", "kırıcı", "kırıldım"]:
        cevap = random.choice(krdn)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["skldm", "sıkıldım"]:
        cevap = random.choice(skdm)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["hm", "hmmm"]:
        cevap = random.choice(hms)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if "geçmiş olsun" in mesaj.lower():
        cevap = random.choice(bts)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["oyun", "game"]:
        cevap = random.choice(trt)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["evt", "evet"]:
        cevap = random.choice(evt)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["hyr", "hayır"]:
        cevap = random.choice(hyrr)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["🙄"]:
        cevap = random.choice(gzs)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["of", "offf"]:
        cevap = random.choice(ofs)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["çikolata"]:
        cevap = random.choice(cklta)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["lan", "ln"]:
        cevap = random.choice(lna)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["dedim"]:
        cevap = random.choice(dddm)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["yalan", "yalancı"]:
        cevap = random.choice(ylna)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["sağol"]:
        cevap = random.choice(sgll)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["çirkin"]:
        cevap = random.choice(crkn)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["dm", "pm"]:
        cevap = random.choice(dmy)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["tatlı", "yemek"]:
        cevap = random.choice(tymm)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["kes", "kesss"]:
        cevap = random.choice(kmm)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["kanka", "knk", "kanki"]:
        cevap = random.choice(kankas)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["öp"]:
        cevap = random.choice(opsss)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["sanane", "sağne", "sanne"]:
        cevap = random.choice(sgne)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')
	    
    if kelimeler[0] in ["banne", "banane", "bağne"]:
        cevap = random.choice(bgne)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["ben", "bennn"]:
        cevap = random.choice(bnen)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')

    if kelimeler[0] in ["sen", "sennn"]:
        cevap = random.choice(snen)
        bold_cevap = f"<b>{cevap}</b>"
        await message.reply(bold_cevap, parse_mode='html')


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
        else:
            await db.add_user(chat_id)
            chat = bot.get_chat(chat_id)
            if str(chat_id).startswith("-100"):
                new_chat_id = str(chat_id)[4:]
            else:
                new_chat_id = str(chat_id)[1:]

    ban_status = await db.get_ban_status(chat_id) # Yasaklı Kullanıcı Kontrolü
    if ban_status["is_banned"]:
        if int((datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])).days) > int(ban_status["ban_duration"]):
            await db.remove_ban(chat_id)
        else:
            if SUPPORT:
                msj = f"@{SUPPORT}"
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
@app.on_message(filters.command("stats") & filters.user(OWNER_ID))
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

        SAHIBIME = "sahibime"
        NOT_ONLINE = "Aktif değil"
        BOT_BLOCKED = "Botu engellemiş"
        USER_ID_FALSE = "**Kullanıcı ID Yanlış .**"
        BROADCAST_STARTED = "**✓ Reklam başlatıldı!**"
        BROADCAST_STOPPED = "**✓ Reklam ( {} )  tamamlandı .\n\n👤 Kayıtlı Kullanıcı : {}\n♻️ Gönderme Denemesi : {}\n✅ Başarılı : {}\n⛔ Başarısız : {}**"
        STATS_STARTED = "{} **Veriler Toplanıyor !**"
        STATS = """**@{} Kullanıcıları :\n\n» Toplam Sohbetler : {}\n» Grup Sayısı : {}\n» PM Sayısı : {}**"""

print("chat.py çalışıyor !")
app.run()  
