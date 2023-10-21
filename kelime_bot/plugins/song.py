import wget
import os, youtube_dl, requests, time
import yt_dlp
import random, os, logging, asyncio
import random
import shutil, psutil, traceback, os
import string
import time
import datetime
import aiofiles
import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch
from random import randint
from asyncio import sleep
from time import time
from os import remove
from datetime import datetime
from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User
from pyrogram import Client, filters
from kelime_bot import BOT_ID, BOT_USERNAME, OWNER_ID

# "/lyrics" komutunu işleyen bir filtre oluşturun
@filters.command("lyrics")
def get_lyrics(_, message):
    # Mesajdaki şarkı adını alın
    song_name = message.text.split("/lyrics", maxsplit=1)[1].strip()
    
    # Şarkı sözlerini almak için bir API isteği yapın
    response = requests.get(f"https://api.lyrics.ovh/v1/{song_name}")
    
    # İstek başarılı ise şarkı sözlerini gönderin
    if response.status_code == 200:
        lyrics = response.json()["lyrics"]
        message.reply_text(lyrics)
    else:
        message.reply_text("Şarkı sözleri bulunamadı.")

# Mesajları filtreleyin ve "/lyrics" komutunu işleyin
app.add_handler(get_lyrics)

##############################
@Client.on_message(filters.command(["bul", "song"]) & ~filters.edited)
async def bul(_, message):
    try:
        await message.delete()
    except:
        pass
    query = " ".join(message.command[1:])
    m = await message.reply("➻  **şᴀʀᴋɪ ᴀʀᴀɴɪʏᴏʀ !**")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]
    
    except Exception as e:
        await m.edit("➻  **şᴀʀᴋɪ ʙᴜʟᴜɴᴀᴍᴀᴅɪ !**")
        print(str(e))
        return
    await m.edit("➻  **şᴀʀᴋɪ ɪɴᴅɪʀɪʟɪʏᴏʀ !**")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"**➻ ᴘᴀʀᴄ̧ᴀ : {title[:35]}\n➻ sᴜ̈ʀᴇ : {duration}\n\n➻ ɪsᴛᴇʏᴇɴ : {message.from_user.first_name}**"
        res = f"**➻ ᴘᴀʀᴄ̧ᴀ : {title[:35]}\n➻ sᴜ̈ʀᴇ : {duration}\n\n➻ ɪsᴛᴇʏᴇɴ : {message.from_user.first_name}**"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        await m.edit("➻ **şᴀʀᴋɪ ʏᴜ̈ᴋʟᴇɴɪʏᴏʀ !**")
        await message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name, performer="♫︎ 𝐌𝐮̈𝐳𝐢𝐤 𝐈𝐧𝐝𝐢𝐫𝐢𝐜𝐢 ♫︎")
        await m.delete()
        await _.send_audio(chat_id=PLAYLIST_ID, audio=audio_file, caption=res, performer="♫︎ 𝐌𝐮̈𝐳𝐢𝐤 𝐈𝐧𝐝𝐢𝐫𝐢𝐜𝐢 ♫︎", parse_mode='md', title=title, duration=dur, thumb=thumb_name)
    except Exception as e:
        await m.edit("🗨️ **ʙᴇɴɪ ʏᴏɴᴇᴛɪᴄɪ ʏᴀᴘɪɴ !**")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

@Client.on_message(filters.command(["vbul", "vsong"]) & ~filters.edited)
async def vsong(client, message):
    try:
        await message.delete()
    except:
        pass
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]
        message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("➻  **ᴠɪᴅᴇᴏ ᴀʀᴀɴɪʏᴏʀ !**")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"➻  **ᴠɪᴅᴇᴏ ʙᴜʟᴜɴᴀᴍᴀᴅɪ !**")
    preview = wget.download(thumbnail)
    await msg.edit("➻  **ᴠɪᴅᴇᴏ ɪɴᴅɪʀɪʟɪʏᴏʀ !**")
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=ytdl_data["title"],
    )
    try:
        os.remove(file_name)
        await msg.delete()
    except Exception as e:
        print(e)

@Client.on_message(filters.command(["ara", "search"]) & ~filters.edited)
async def ytsearch(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        if len(message.command) < 2:
            return await message.reply_text("**➻ sᴏɴᴜᴄ̧ ʙᴜʟᴜɴᴀᴍᴀᴅɪ !**")
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("**➻  ᴀʀɪʏᴏʀᴜᴍ !**")
        results = YoutubeSearch(query, max_results=6).to_dict()
        i = 0
        text = ""
        while i < 6:
            text += f"**💬 ᴘᴀʀᴄ̧ᴀ : {results[i]['title']}**\n"
            text += f"**⌚ sᴜ̈ʀᴇ : {results[i]['duration']}**\n"
            text += f"**🔗 ʟɪɴᴋ : [ ʏᴏᴜᴛᴜʙᴇ'ᴅᴇɴ ɪᴢʟᴇ ](https://youtube.com{results[i]['url_suffix']})**\n\n"
            i += 1
        await m.edit_text(
            text=text,
            disable_web_page_preview=True,
        )
    except Exception as e:
        await message.reply_text(str(e))

@Client.on_message(filters.new_chat_members, group=1)
async def zar(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(BOT_ID):
            await msg.reply(
                f'''**💞 ᴍᴇʀʜᴀʙᴀ , {msg.from_user.mention}\n\n🗨️ ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇᴅɪɢ̆ɪɴ ɪᴄ̧ɪɴ ᴛᴇşşᴇᴋᴜ̈ʀ ᴇᴅᴇʀɪᴍ, ʙᴇɴɪ ʏᴏ̈ɴᴇᴛɪᴄɪ ʏᴀᴘᴍᴀʏɪ ᴜɴᴜᴛᴍᴀʏɪɴ ...\n\n🗯️ ᴅᴀʜᴀ ғᴀᴢʟᴀ ʙɪʟɢɪ ɪᴄ̧ɪɴ ᴀşşᴀɢ̆ɪᴅᴀᴋɪ ʙᴜᴛᴏɴᴜ ᴋᴜʟʟᴀɴɪɴ ...**''', 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💕  ʙᴜʀᴀʏᴀ ᴛɪᴋʟᴀ  ", url=f"https://t.me/{BOT_USERNAME}?start")]])
    )
        elif str(new_user.id) == str(OWNER_ID):
            await msg.reply(f'**🗯️ ᴅᴇɢ̆ᴇʀʟɪ sᴀʜɪʙɪᴍ [ㅤᴀɪᴋᴏㅤ](tg://openmessage?user_id=6540285284) ɢᴇʟᴅɪ, ʜᴏş ɢᴇʟᴅɪɴ ᴇғᴇɴᴅɪᴍ ...**')


@Client.on_message(filters.command(["reload"], ["/"]) & ~filters.private & ~filters.channel)
async def reload(client: Client, message: Message):
    await message.reply_text(f"**🎄 ʙᴏᴛ ʏᴇɴɪᴅᴇɴ ʙᴀşʟᴀᴅɪ .\n🎄 ᴀᴅᴍɪɴ ʟɪsᴛᴇsɪ ɢᴜ̈ɴᴄᴇʟʟᴇɴᴅɪ .**")

@Client.on_message(filters.command(["c"], ["/", ""]))
async def csor(client: Client, message: Message):
    await message.reply_text(f"**🗨️ ᴄᴇsᴀʀᴇᴛ sᴇᴄ̧ᴛɪɴ, sᴀɴɪʀɪᴍ ғᴀᴢʟᴀ ᴄᴇsᴀʀᴇᴛʟɪsɪɴ .\n\n🗒️ ʏᴀᴘᴍᴀɴ ɢᴇʀᴇᴋᴇɴ : {random.choice(c)}**")


@Client.on_message(filters.command(["d"], ["/", ""]))
async def dsor(client: Client, message: Message):
    await message.reply_text(f"**🗨️ ᴅᴏɢ̆ʀᴜʟᴜᴋ sᴇᴄ̧ᴛɪɴ, ᴄ̧ᴏᴋ ɢᴜ̈ᴢᴇʟ .\n\n🗒️ sᴀɴᴀ sᴏʀᴜᴍ : {random.choice(d)}**")


d = (
"Telefonunda en son aradığın şey neydi?","Birisi kız arkadaşın / erkek arkadaşından ayrılmak için sana 1 milyon tl önerseydi, yapar mıydın?","Bu grupda en az kimi seviyorsun ve neden?","Hiç sınıfta yüksek sesle geğirdin mi?","Hiç sınıfta yüksek sesle geğirdin mi?","Yerden bir şeyi alıp hiç yedin mi?","Bir gün karşı cins olarak uyanırsan, ilk yapacağın şey nedir?","Hiç havuzda işedin mi?","Asansörde hiç gaz kaçırdın mı?",
"Tuvalette otururken aklınıza gelen şeyler nelerdir?","Büyüyen hayali bir arkadaşınız var mıydı?","En kötü alışkanlığınız nedir?","Burnunu karıştırır mısın?","Banyoda şarkı söyler misin?","Hiç üzerine işedin mi?","Toplumda en utanç verici anınız neydi?","Aynada kendinle hiç konuştun mu?",
"Web geçmişinizi, birileri görürse utanacağınız şey ne olurdu?","Uykunda konuşur musun?","Gizli aşkın kim?","Benim hakkımda neyi sevmiyorsun?","Şu an ne renk iç çamaşır giyiyorsun?","Son attığın mesaj neydi?","İnsanları yanan bir binadan kurtarıyor olsaydınız ve bir kişiyi bu grupdan geride bırakmak zorunda kalırsanız, kim olurdu?",
"İç çamaşırlarını ne sıklıkla yıkıyorsun?","Hiç kulak kiri tattın mı?","Hiç osurup başka birini suçladın mı?","Hiç terinin tadına baktın mı?","Bu odadaki kim bugüne kadarki en kötü insan olurdu? Neden?",
"Yeniden doğmuş olsaydın, hangi yüz yılda doğmak isterdin?","Söylediğiniz veya yaptığınız bir şeyi silmek için zamanda geriye gidebilseydiniz, bu hangi yıl olurdu?","Erkek arkadaşın veya kız arkadaşın seni hiç utandırdı mı?","Birdenbire görünmez olsaydın ne yapardın?",
"Banyoda kaldığınız en uzun süre nedir ve neden bu kadar uzun süre kaldınız?","Şimdiye kadar gördüğüm en garip rüyayı anlat.","Duşta işiyor musun?","Hala yaptığın en çocukça şey nedir?","Hangi çocuk filmini tekrar tekrar izleyebilirsin?",
"Ayak kokunuz kötü mü?","Saçma takma adların var mı?","Telefonunuzda hangi uygulamada en çok zaman harcıyorsunuz?","Tek bir oturuşta yediğin en çok yemek ne?","Tek başınayken dans ediyor musun?","Karanlıktan korkar mısın?",
"Bütün gün evdeysen ne yapardın?","Günde kaç öz çekim yapıyorsunuz?","En son ne zaman dişlerini fırçaladın?","En sevdiğin pijamalar neye benziyor?","Hiç yerden bir şey yedin mi?","Yapmaman gereken bir şeyi yaparken hiç yakalandın mı?","Vücudunun hangi bölümünü seviyorsun, hangi kısmından nefret ediyorsun?","Hiç bitlendin mi?","Pantolonunu hiç kestin mi?","Tabağını yalıyor musun?","Kimsenin senin hakkında bilmediği bir şey nedir?",
"Hiç tabağını yaladın mı?","Dirseğini yalayabilir misin?","Eğer buradaki herkesi yanan bir binadan kurtarmaya çalışıyor olsaydın ve birini geride bırakmak zorunda kalırsan, kimi geride bırakırdın?","Telefonda aradığın son şey neydi?","Bir uygulamayı telefonunuzdan silmek zorunda kalsanız hangisini silerdiniz?","Bir ilişkideki en büyük korkun nedir?",
"Odanın her bir kişi hakkında bir tane olumlu, bir tane olumsuz şey söyleyin.","Sevmediğin kötü huyun var mı?","Hayatında yaptığın en çılgın şey nedir?","Üç gün boyunca bir adada mahsur kalmış olsaydınız, bu grupdan kimleri seçerdiniz?","Bu odadaki en sinir bozucu kişi kim?","Bu grupdan biriyle evlenmek zorunda kalsan kim olurdu?","En uzun ilişkiniz ne kadar sürdü?",
"Bir ünlü Instagram’da seni takip etseydi bu ünlünün kim olmasını isterdin?","Instagram’da 5 kişiyi silmek zorunda olsan kimleri silerdin?","Kaç çocuk sahibi olmak istersin?","Hayallerinizdeki kişiyi tarif edin.","Messi mi Ronaldo mu?","Pes mi Fifa mı?",
"İlk işin neydi?","Üniversite hakkındaki en büyük korkun nedir?","En iyi arkadaşının seninle aynı üniversiteye gitmesini ister misin?","Mevcut erkek arkadaşının ya da kız arkadaşının seninle aynı üniversiteye gitmesini ister misin?","Hayalindeki iş ne?",
"Hiç bir dersten başarısız oldun mu?","Hiç kopya çektin mi?","Hiç sınıfta uyudun mu?","Sınıfta asla yanında oturmak istemeyeceğin kim?","Derse hiç geç kaldın mı?","Bir öğretmenin önünde yaptığın en utanç verici şey nedir?","Hiç masanın altına sakız attın mı?",
"Hiç okulda kavga ettin mi?","Bir sınavdan aldığın en kötü puan neydi?","Sınıfta hiç uyuya kaldın mı?","Hiç gözaltına alındın mı?","Eğer görünmez olsaydın hangi derse gizlice girerdin?","En kötü grup hangisidir?","Bu grupdaki sır tutma  konusunda en çok zorlanan kişi kimdir?",
"s‌ɪᴍᴅɪʏᴇ ᴋᴀᴅᴀʀ ʙɪʀ ʙᴀs‌ᴋᴀsıɴᴀ sᴏ‌ʏʟᴇᴅɪɢ‌ɪɴ ᴇɴ ᴀᴄıᴍᴀsıᴢᴄᴀ s‌ᴇʏ ɴᴇʏᴅɪ?","ᴄ‌ıᴋᴛıɢ‌ıɴ ᴇɴ ʏᴀs‌ʟı ᴋɪs‌ɪ ᴋɪᴍ?","ɢʀᴜᴘᴛᴀ ᴋɪ sᴇᴠᴍᴇᴅᴇɢ‌ɪɴ ᴋɪs‌ɪʏɪ ᴇᴛɪᴋᴇᴛʟᴇʀ ᴍɪsɪɴ ?","ᴇɴ sᴏɴ ɴᴇ ᴢᴀᴍᴀɴ ʜᴜ‌ɴɢᴜ‌ʀ ʜᴜ‌ɴɢᴜ‌ʀ ᴀɢ‌ʟᴀᴅıɢ‌ıɴı ʜᴀᴛıʀʟıʏᴏʀ ᴍᴜsᴜɴ?","ʙɪʀɪʏʟᴇ ᴄ‌ıᴋᴀʀᴋᴇɴ ʏᴀᴘᴛıɢ‌ıɴ ᴇɴ ᴜᴛᴀɴᴄ‌ ᴠᴇʀɪᴄɪ s‌ᴇʏ ɴᴇʏᴅɪ?","ᴜ‌ᴄ‌ ɢᴜ‌ɴ ʙᴏʏᴜɴᴄᴀ ʙɪʀ ᴀᴅᴀᴅᴀ ᴍᴀʜsᴜʀ ᴋᴀʟᴍıs‌ ᴏʟsᴀʏᴅıɴıᴢ, ʙᴜ ɢʀᴜᴘᴅᴀɴ ᴋɪᴍʟᴇʀɪ sᴇᴄ‌ᴇʀᴅɪɴɪᴢ?","ᴇɴ sᴏɴ ɴᴇ ᴢᴀᴍᴀɴ ᴅɪs‌ʟᴇʀɪɴɪ ғıʀᴄ‌ᴀʟᴀᴅıɴ?",
"ᴋᴜ‌ʟᴛᴜ‌ʀᴜ‌ᴍᴜ‌ᴢᴜ‌ɴ ᴇɴ ᴄ‌ᴏᴋ sᴇᴠᴅɪɢ‌ɪɴɪᴢ ʏᴀɴı ɴᴇᴅɪʀ?","ʙɪʀ ɪʟɪs‌ᴋɪᴅᴇᴋɪ ᴇɴ ʙᴜ‌ʏᴜ‌ᴋ ᴋᴏʀᴋᴜɴ ɴᴇᴅɪʀ?","ʙᴜʀᴅᴀ ᴋɪ ᴋɪᴍsᴇʏᴇ ʏᴀʟᴀɴ sᴏ‌ʏʟᴇᴅɪɴ ᴍɪ?","ᴀɪʟᴇɴɪɴ sᴇɴɪɴ ʜᴀᴋᴋıɴᴅᴀ ʙɪʟᴍᴇᴅɪɢ‌ɪɴᴇ sᴇᴠɪɴᴅɪɢ‌ɪɴ s‌ᴇʏ ɴᴇᴅɪʀ?","s‌ᴜ ᴀɴᴋɪ ʀᴜʜ ʜᴀʟɪɴᴇ ʙᴀᴋᴀʀᴀᴋ ɴᴇ ᴛᴜ‌ʀ ғɪʟᴍ ɪᴢʟᴇʀsɪɴ (ᴀᴋsɪʏᴏɴ/ᴅʀᴀᴍ/ʙɪʟɪᴍ ᴋᴜʀɢᴜ/ʀᴏᴍᴀɴᴛɪᴋ ᴋᴏᴍᴇᴅɪ/ʙɪʏᴏɢʀᴀғɪ/ғᴀɴᴛᴀsᴛɪᴋ)","ʙɪʀ ᴜ‌ɴʟᴜ‌ ɪɴsᴛᴀɢʀᴀᴍ’ᴅᴀ sᴇɴɪ ᴛᴀᴋɪᴘ ᴇᴛsᴇʏᴅɪ ʙᴜ ᴜ‌ɴʟᴜ‌ɴᴜ‌ɴ ᴋɪᴍ ᴏʟᴍᴀsıɴı ɪsᴛᴇʀᴅɪɴ?",
"sᴏ‌ʏʟᴇᴅɪɢ‌ɪɴɪᴢ ᴠᴇʏᴀ ʏᴀᴘᴛıɢ‌ıɴıᴢ ʙɪʀ s‌ᴇʏɪ sɪʟᴍᴇᴋ ɪᴄ‌ɪɴ ᴢᴀᴍᴀɴᴅᴀ ɢᴇʀɪʏᴇ ɢɪᴅᴇʙɪʟsᴇʏᴅɪɴɪᴢ, ʙᴜ ʜᴀɴɢɪ ʏıʟ ᴏʟᴜʀᴅᴜ?","ɢɪᴢʟɪ ᴀs‌ᴋıɴ ᴋɪᴍ?","ʜɪᴄ‌ ʏᴇʀᴅᴇɴ ʙɪʀ s‌ᴇʏ ʏᴇᴅɪɴ ᴍɪ?","ʜɪᴄ‌ sᴇᴠɢɪʟɪɴɪ ᴀʟᴅᴀᴛᴍᴀʏı ᴅᴜ‌s‌ᴜ‌ɴᴅᴜ‌ɴ ᴍᴜ‌?","ʜɪᴄ‌ ʏᴇʀᴅᴇɴ ʙɪʀ s‌ᴇʏ ʏᴇᴅɪɴ ᴍɪ?","ʙɪʀ sıɴᴀᴠᴅᴀɴ ᴀʟᴅıɢ‌ıɴ ᴇɴ ᴋᴏ‌ᴛᴜ‌ ᴘᴜᴀɴ ɴᴇʏᴅɪ?","ʙɪʀ ᴄɪɴ sᴀɴᴀ ᴜ‌ᴄ‌ ᴅɪʟᴇᴋ ʜᴀᴋᴋı sᴜɴsᴀʏᴅı ɴᴇʟᴇʀ ᴅɪʟᴇʀᴅɪɴ?","ɢʀᴜᴘᴛᴀɴ ᴜᴢᴀᴋ ᴋᴀᴄ‌ ᴅᴀᴋɪᴋᴀ ᴅᴜʀᴀʙɪʟɪʀsɪɴ ?",
"sɪᴢᴄᴇ ᴛᴜ‌ʀᴋɪʏᴇ’ɴɪɴ ᴇɢ‌ɪᴛɪᴍ sɪsᴛᴇᴍɪɴᴅᴇ ʏᴀᴘıʟᴍᴀsı ɢᴇʀᴇᴋᴇɴ ᴇɴ ᴏ‌ɴᴇᴍʟɪ ᴅᴇɢ‌ɪs‌ɪᴋʟɪᴋ ɴᴇᴅɪʀ?","ʜᴀʟᴀ ʏᴀᴘᴛıɢ‌ıɴ ᴇɴ ᴄ‌ᴏᴄᴜᴋᴄ‌ᴀ s‌ᴇʏ ɴᴇᴅɪʀ?","ɢʀᴜʙᴜɴ ᴇɴ ʏᴀᴋıs‌ıᴋʟısı ᴋɪᴍ ?","ʜᴀғᴛᴀᴅᴀ ᴋᴀᴄ‌ ᴋᴇᴢ ᴀʏɴı ᴘᴀɴᴛᴏʟᴏɴᴜ ɢɪʏɪʏᴏʀsᴜɴ?","sıɴıғᴛᴀ ᴀsʟᴀ ʏᴀɴıɴᴅᴀ ᴏᴛᴜʀᴍᴀᴋ ɪsᴛᴇᴍᴇʏᴇᴄᴇɢ‌ɪɴ ᴋɪᴍ?","sᴜ‌ᴘᴇʀ ᴋᴀʜʀᴀᴍᴀɴʟᴀʀ ɢᴇʀᴄ‌ᴇᴋᴛᴇɴ ᴠᴀʀ ᴏʟsᴀʏᴅı ᴅᴜ‌ɴʏᴀ ɴᴀsıʟ ʙɪʀ ʏᴇʀ ᴏʟᴜʀᴅᴜ?","sᴏ‌ᴢʟᴜ‌ ᴅᴇsᴛᴀɴʟᴀʀ ʜᴀᴋᴋıɴᴅᴀ ɴᴇ ᴅᴜ‌s‌ᴜ‌ɴᴜ‌ʏᴏʀsᴜɴ?","ʜᴀʏᴀʟʟᴇʀɪɴɪᴢᴅᴇᴋɪ ᴋɪs‌ɪʏɪ ᴛᴀʀɪғ ᴇᴅɪɴ.",
"ɢʀᴜʙᴜ sᴇᴠɪʏᴏʀ ᴍᴜsᴜɴ ?","ʙɪʀɪɴɪ ᴏ‌ᴘᴇʀᴋᴇɴ ᴋᴇɴᴅɪɴɪ ʜɪᴄ‌ ᴋᴏ‌ᴛᴜ‌ ʜɪssᴇᴛᴛɪɴ ᴍɪ?","ʙᴜ ʜᴀʏᴀᴛᴛᴀ sᴇɴɪ sᴇɴɪ ᴇɴ ᴄ‌ᴏᴋ ɴᴇ ɢıᴄıᴋ ᴇᴅᴇɴ ᴠᴇ ᴄ‌ɪʟᴇᴅᴇɴ ᴄ‌ıᴋᴀʀᴀɴ s‌ᴇʏ ɴᴇᴅɪʀ?","ʜɪᴄ‌ ᴋᴏᴘʏᴀ ᴄ‌ᴇᴋᴛɪɴ ᴍɪ?","ɪ‌ɴsᴀɴʟᴀʀıɴ sɪᴢᴇ ɴᴇ sᴏʀᴍᴀsıɴᴅᴀɴ ʙıᴋᴛıɴıᴢ?","ʜɪᴄ‌ sᴇᴠɢɪʟɪɴɪ ʙɪʀɪʏʟᴇ ᴀʟᴅᴀᴛᴛıɴ ᴍı?","ᴇɢ‌ᴇʀ ʙᴜʀᴀᴅᴀᴋɪ ʜᴇʀᴋᴇsɪ ʏᴀɴᴀɴ ʙɪʀ ʙɪɴᴀᴅᴀɴ ᴋᴜʀᴛᴀʀᴍᴀʏᴀ ᴄ‌ᴀʟıs‌ıʏᴏʀ ᴏʟsᴀʏᴅıɴ ᴠᴇ ʙɪʀɪɴɪ ɢᴇʀɪᴅᴇ ʙıʀᴀᴋᴍᴀᴋ ᴢᴏʀᴜɴᴅᴀ ᴋᴀʟıʀsᴀɴ, ᴋɪᴍɪ ɢᴇʀɪᴅᴇ ʙıʀᴀᴋıʀᴅıɴ?",
"ᴏʏᴜɴᴜ ᴏʏɴᴀʏᴀɴ ᴏʏᴜɴᴄᴜ ɢʀᴜʙᴜɴᴅᴀ ʏᴇʀ ᴀʟᴀɴʟᴀʀᴅᴀɴ ᴋɪᴍɪ ᴏ‌ᴘᴍᴇᴋ ɪsᴛᴇʀsɪɴ?","ɢʀᴜᴘᴛᴀ ᴋɪᴍɪɴ ʏᴇʀɪɴᴅᴇ ᴏʟᴍᴀᴋ ɪsᴛᴇʀᴅɪɴ ?","sᴇᴠᴅɪɢ‌ɪɴɪ ɪᴛɪʀᴀғ ᴇᴛᴍᴇᴋᴛᴇɴ ᴜᴛᴀɴᴅıɢ‌ıɴ ғɪʟᴍ ʜᴀɴɢɪsɪᴅɪʀ?","ʙᴜ ʜᴀʏᴀᴛᴛᴀ s‌ɪᴍᴅɪʏᴇ ᴋᴀᴅᴀʀ ʏᴀᴘᴛıɢ‌ıɴ ᴇɴ ʙᴜ‌ʏᴜ‌ᴋ ʜᴀᴛᴀ ɴᴇᴅɪʀ?","ʜɪᴄ‌ sıɴıғᴛᴀ ᴜʏᴜᴅᴜɴ ᴍᴜ?","ᴍᴇssɪ ᴍɪ ʀᴏɴᴀʟᴅᴏ ᴍᴜ?","ʜɪᴄ‌ ʙɪʀ ᴅᴇʀsᴛᴇɴ ʙᴀs‌ᴀʀısıᴢ ᴏʟᴅᴜɴ ᴍᴜ?","s‌ᴜ ᴀɴᴋɪ ʀᴜʜ ʜᴀʟɪɴᴇ ʙᴀᴋᴀʀᴀᴋ ɴᴇ ᴛᴜ‌ʀ ғɪʟᴍ ɪᴢʟᴇʀsɪɴ (ᴀᴋsɪʏᴏɴ/ᴅʀᴀᴍ/ʙɪʟɪᴍ ᴋᴜʀɢᴜ/ʀᴏᴍᴀɴᴛɪᴋ ᴋᴏᴍᴇᴅɪ/ʙɪʏᴏɢʀᴀғɪ/ғᴀɴᴛᴀsᴛɪᴋ)",
"ɪʟᴇʀᴅᴇ ᴄ‌ᴏᴄᴜɢ‌ᴜɴ ᴏʟᴜʀsᴀ ɴᴇ ɪsɪᴍ ᴋᴏʏᴍᴀᴋ ɪsᴛᴇʀsɪɴ?","ᴋıʀᴍıᴢı ʜᴀʟıᴅᴀ ʙᴇʀᴀʙᴇʀ ʏᴜ‌ʀᴜ‌ᴍᴇᴋ ɪsᴛᴇᴅɪɢ‌ɪɴ ᴜ‌ɴʟᴜ‌ ɪsɪᴍ ᴋɪᴍ .","ʙᴇʏɴɪɴɪ ʙɪʀ ʀᴏʙᴏᴛᴀ ʏᴇʀʟᴇs‌ᴛɪʀᴇʙɪʟɪʀ ᴠᴇ sᴏɴsᴜᴢᴀ ᴋᴀᴅᴀʀ ʙᴜ s‌ᴇᴋɪʟᴅᴇ ʏᴀs‌ᴀʏᴀʙɪʟsᴇᴅɪɴ,ʙᴜɴᴜ ʏᴀᴘᴀʀ ᴍıʏᴅıɴ?","ʜᴀʏᴀʟʟᴇʀɪɴɪᴢᴅᴇᴋɪ ᴋɪs‌ɪʏɪ ᴛᴀʀɪғ ᴇᴅɪɴ.","ᴀɪʟᴇɴɪᴢ ᴅıs‌ıɴᴅᴀ, ʏᴀs‌ᴀᴍıɴıᴢ ᴜ‌ᴢᴇʀɪɴᴅᴇ ᴇɴ ʙᴜ‌ʏᴜ‌ᴋ ᴇᴛᴋɪsɪ ᴏʟᴀɴ ᴋɪs‌ɪ ᴋɪᴍᴅɪʀ?","ᴇɴ ᴋᴏ‌ᴛᴜ‌ ᴀʟıs‌ᴋᴀɴʟıɢ‌ıɴıᴢ ɴᴇᴅɪʀ?","ɢʀᴜᴘ sᴇɴɪɴ ɪᴄ‌ɪɴ ɴᴇ ɪғᴀᴅᴇ ᴇᴅɪʏᴏʀ?","ʙɪʀ ɢᴜ‌ɴ ᴋᴀʀs‌ı ᴄɪɴs ᴏʟᴀʀᴀᴋ ᴜʏᴀɴıʀsᴀɴ, ɪʟᴋ ʏᴀᴘᴀᴄᴀɢ‌ıɴ s‌ᴇʏ ɴᴇᴅɪʀ?",
"ɢʀᴜᴘᴛᴀ ɢɪᴢʟɪ ᴀs‌ᴋıɴ ᴠᴀʀ ᴍı ?","ᴛᴇʟᴇғᴏɴᴅᴀ ᴀʀᴀᴅıɢ‌ıɴ sᴏɴ s‌ᴇʏ ɴᴇʏᴅɪ?","sᴜ‌ᴘᴇʀ ᴋᴀʜʀᴀᴍᴀɴʟᴀʀ ɢᴇʀᴄ‌ᴇᴋᴛᴇɴ ᴠᴀʀ ᴏʟsᴀʏᴅı ᴅᴜ‌ɴʏᴀ ɴᴀsıʟ ʙɪʀ ʏᴇʀ ᴏʟᴜʀᴅᴜ?","ᴋᴀʀᴀɴʟıᴋᴛᴀɴ/ʏᴜ‌ᴋsᴇᴋʟɪᴋᴛᴇɴ ᴋᴏʀᴋᴀʀ ᴍısıɴ?","ᴘᴀɴᴛᴏʟᴏɴᴜɴᴜ ʜɪᴄ‌ ᴋᴇsᴛɪɴ ᴍɪ?","ʜɪᴄ‌ sᴀʜᴛᴇ ᴋɪᴍʟɪᴋ ᴋᴜʟʟᴀɴᴅıɴ ᴍı?",
"Söylediğin en son yalan neydi?","Spor yapar mısın?","Hayatının geri kalanında sadece bir kıyafet giyebilseydin, bu kıyafetin hangi renk olurdu?","Sizce Türkiye’nin eğitim sisteminde yapılması gereken en önemli değişiklik nedir?","Karanlıktan/yükseklikten korkar mısın?",
"Kendi görünuşünü 1 ile 10 arasında puanla :)","Yaptıgın en yasadışı şey neydi?","Şimdi sana bir evlenme teklifi gelse ve sevmediğin biri olsa, ve bu sana son gelecek evlilik teklifi olsa kabul edermiydin?","Şu anki ruh haline bakarak ne tür film izlersin (aksiyon/dram/bilim kurgu/romantik komedi/biyografi/fantastik)","Kendini en ezik hissettiğin an hangisiydi ?","ilerde çocuğun olursa ne isim koymak istersin?",
"Unicorun mu olmasını isterdin ejderhan mı?","Kaç sevgilin oldu?","Hayatta unutmadığın biri var mı?","en sevdiğin şarkı?","Yapmaman gereken bir şeyi yaparken hiç yakalandın mı?","En sevdiğin sanatçı kim?","karşı cinste ilk dikkatini çeken ne?","bu yıl hayatında neyi değişmeyi uygun görüyorsun?",
"Birinin telefonunda gördüğün en tuhaf şey nedir?","Süper kahramanlar gerçekten var olsaydı Dünya nasıl bir yer olurdu?","Hayatın size öğrettiği en önemli ders nedir?","Kültürümüzün en çok sevdiğiniz yanı nedir?","Ailenizin uyguladığı en tuhaf gelenek nedir?",
"Aileniz dışında, yaşamınız üzerinde en büyük etkisi olan kişi kimdir?","Kadın/Erkek olmanın en kötü ve en iyi yanı nedir?","Beynini bir robota yerleştirebilir ve sonsuza kadar bu şekilde yaşayabilsedin,bunu yapar mıydın?","Evinizde ağırladığın en kötü misafir kimdi ve ne oldu?",
"İnsanların size ne sormasından bıktınız?","En tuhaf korkunuz nedir?","En sevdiğiniz TV programı hangisidir?","Girdiğiniz en saçma tartışma nedir?","En son söylediğin yalan nedir?", "Biriyle çıkarken yaptığın en utanç verici şey neydi?","Hiç arabanla (varsa) yanlışlıkla bir şeye birine çarptın mı?",
"Hoşuna gittiğini düşündüğün ama bir türlü açılamadığın biri oldu mu?","En tuhaf takma adın nedir?","Fiziksel olarak sana en acı veren deneyimin ne oldu?","Hangi köprüleri yakmak seni rahatlattı?","Toplu taşıma araçlarında yaptığın en çılgınca şey neydi?","Şişeden bir cin çıksa üç dileğin ne olurdu?","Dünyadaki herhangi birini Türkiye’nin başkanı yapabilseydin bu kim olurdu?",
"Şimdiye kadar bir başkasına söylediğin en acımasızca şey neydi?","Birini öperken kendini hiç kötü hissettin mi?","Hiçbir sonucu olmayacağını bilsen ne yapmak isterdin?","Bir aynanın önünde yaptığın en çılgınca şey nedir?","Şimdiye kadar başkasına söylediğin en anlamlı şey neydi?",
"Arkadaşlarınla yapmayı sevdiğin ama sevgilinin önünde asla yapmayacağın şey nedir?","Bu hayatta en çok kimi kıskanıyorsun?","En sevdiğin pijamaların neye benziyor?","Bir buluşmadan kaçmak için hiç hasta numarası yaptın mı?","Çıktığın en yaşlı kişi kim?",
"Günde kaç tane özçekim yaparsın?","Aşk için her şeyi yaparım ama “bunu” yapmam dediğin şey nedir?","Haftada kaç kez aynı pantolonu giyiyorsun?","Bugün şansın olsa lise aşkınla çıkar mısın?","Vücudunun hangi bölümlerinden gıdıklanıyorsun?",
"Çeşitli batıl inançların var mı? Varsa onlar neler?","Sevdiğini itiraf etmekten utandığın film hangisidir?","En utan verici kişisel bakım alışkanlığın nedir?","En son ne zaman ve ne için özür diledin?","Sözlü destanlar hakkında ne düşünüyorsun?",
"Utanç verici kokularınızın çoğu nereden geliyor?","Hiç sevgilini anlatmayı düşündün mü?","Hiç sevgilini biriyle aldattın mı?","Boxer mı yoksa külot mu?","Hiç havuza veya denize işedin mi?","Saçlarını uzatmayı düşünsen ne kadar uzatırdın?","Kimsenin bilmeyeceği garanti olsa kimi öldürmek isterdin?","Başkası için aldığın en ucuz hediye nedir?",
"Zamanının çoğunu en çok hangi uygulamada harcıyorsun?","Otobüste yaptığın en tuhaf şey nedir?","Hiç toplum içinde çıplak kaldın mı?","Günde ne kadar dedikodu yaparsın?","Çıkmak isteyeceğin en genç kişi kaç yaşında olurdu?","Hiç toplum içindeyken burnunu karıştırdın mı?",
"Hiç yaşın hakkında yalan söyledin mi?","Telefonundan bir uygulamayı silmek zorunda olsan bu hangisi olurdu?","Gece geç saatte yaptığın en utanç verici şey nedir?","Duş almadan en uzun süre ne kadar durdun ?","Hiç sahte kimlik kullandın mı?","Kırmızı halıda beraber yürümek istediğin ünlü isim kim?","Gizli aşkın kim?",
)

c = (
"Seçtiğiniz bir sosyal medya hesabınızdan çok çirkin bir fotoğrafınızı paylaşın.","Mesaj yazma bölümünüzü telefonunuzdan açın gözlerinizi kapatın ve rasgele bir kişiye körü körüne bir metin gönderin.","Telegramda son konuşmanı ss at.","🎀 ŞANSLI MESAJ🎊 Grupdan İstediğin Birinin Google/Youtube/İnstagram Arama Geçmişini İste","Galerinin En Alttan 7. Fotosunu gönder","Sonraki 3 tur boyunca şiveyle konuş. Farklı şivelere kayış olursa /zar Komutunu kullanarak 6 ya en cok yaklaşan oyuncu sana ceza verecek",
"Önümüzdeki 5 dakika boyunca söylediğin her şeyden sonra “mee” diyeceksin","Önümüzdeki 5 dakika içinde birinin hayvanı olun.","İnstagramını oyunculardan birine ver. 5 dk boyunca her yere bakmak serbest.","Oyundan bir kişiye serenat yap (kız ise erkeğe, erkek ise kıza)","Sonraki 3 tur boyunca şiveyle konuş.","3 dakika boyunca bebek taklidi yap!","Telefonunda ki en sevmediğin fotoğrafını at","En beğendiğin fotoğrafını at",
"Whatsapp’da 2 konuşmanı at","Özel mesajlarını ssi al ve gruba at","Whatsapp’da son konuşmanı at","Bir deftere 20 kez ben çatlağım yaz ve resmini at","Telegramda son konuşmanı ss at.","Biyografine +18 bir cümle yaz; 3 Saat duracak.!","Galerinin bir kısmını ss alıp at","Galerindeki 16. Fotoğrafı at.","Instagram yada telegramdan tanımadığın birine komik olmayan bir fıkra anlat.",
"Ninni Söyleyerek Ses At","Bugununle ilgili kısa bir hikaye uydur.","Grupta ki en çok hoşuna giden karşı cinse seni seviyorum diye mesaj at.","Galerindeki 16. Fotoğrafı at.","Galerindeki 30. Fotoğrafı at.","Whatsapp’da konuşduğun kişilerin ss ini at","Grubun üye listesine gir ve 7. kişiye anlık at. (Grup daha az kişiyse ya da aktif sayısı azsa üstten saymaya devam et)","En son konuştuğun kişiye \"Hayırlı Cumalar\" diye mesaj at.(platform farketmez)",
"Şuan ki halini fotoğraf çekip  atar mısın?","Grupta üyeler kısmına gir 11. kişiye \"Analar neler doğuruyor bee\" diye ses at ve cevabını grupla paylaş.","Profil fotoğrafına nefret ettiğin bir ünlünün resmini koy.","Kafanda yumurta kır ve fotosunu at","Gruptan sevdiğin bir kişinin fotoğrafını profil resmi yap","Balkona veya pencereye cık dısardakılerın duyacagı sekılde sarkı soyle videoya al gruba at.",
"İtiraf et: üye çalmak için kaç hesabın var?","Gruptaki 5 abazaya seni seviyorum de","İki dakika tavuk gibi davran.","Seçtiğiniz bir hayvanı taklit edin.","Seçtiğin bir nesneyi yalayın ve gruba fotosunu atın.","Gruba gerçekten utanç verici bir fotoğrafını göster.","Çirkin bir selfie çek ve sosyal medya uygulamalarından birinde yayınla 1.5 saat kalacak.","Bir kaşık un ye ve video ya al gruba at",
"Hiç tanımadığın birine Kurban Bayramınızı kutlarım deyin","Sevdiğin bir kişiye ( ben seni neden sevdim niçin sevdim niye sevdim bunların bi izahı yok gördün işte sevdim. Yaw sahi ben seni nidennn sevdim ) de. Cevap geldiğinde grupla paylaş biz de gülelim","Telegram'daki en kalabalık grubu aç ve \"`Benim adım turşu bidonu!`\" diyerek ses kaydedip en kalabalık gruba gönder.","Hemcinsin olan yakın bir arkadaşına ona aşık olduğunu söyle.","Sürahiden su iç ve fotoğraf at.","En çok konuştuğun karşı cinsten arkadaşına \" `Seni çok seviyorum galiba aşık oldum`\" yaz ve tepkisini bizimle paylaş",
"İsmini 1 saatliğine Abdül<ismin> yap. (örneğin adın Berk ise AbdülBerk yap)","İnstagram'da dm kutunu (mesajlar bölümü) ss al gruba at.","Tanımadığın birisine şu cümleyi atıp sohbet başlat: \"`Aşkımızın suya düşeceğini bilseydim , balık olurdum`\"","En komik fotoğrafını grupla paylaş.","Grupta üyeler kısmına gir 11. kişiye \"`Analar neler doğuruyor bee`\" diye ses at ve cevabını grupla paylaş.",
"Tanımadığın birine şu mesajı at sonra cevabını grupla paylaş ➡️\n  \"`Bu mesaj özel bir frekansla gönderilmiştir. Zekilerde hafıza kaybı, aptallarda kısa sureli körlük ibnelerde de bir anlık gülümseme yapar!`\"","@ yaz çıkan ilk kişiyi etiketle ve seni seviyorum yaz.","Tanımadığın birine \" `sanırım sana aşık oldum`\" diye mesaj at.","Telegram hakkında kısmına \"`Babasının Prensesi`\" yaz 1 saat boyunca dursun.","Birine Sesli Öpücük At Ve Etiketle",
"Üç çorba kaşığı acı salça (veya buna benzer bir şey) ye ve video ya al gruba at","5 dakika boyunca oyundaki birinin evcil hayvanı olmasını isteyebilirsin.","Yeri yala Ve fotoğraf/videosunu gruba at","/zar Komutunu kullanarak 6 ya en cok yaklaşan oyuncuya sosyal medya hesaplarından birini 5dk ver","3 dakika boyunca bir ünlüyü taklit et.", "Birisi taklit edilen sanatçıyı tahmin edene kadar bir sanatçıyı taklit et",
"Grubun ortaya koyduğu bir konu etrafında sekiz satır ve iki mısralık bir şiir yaz","Oyundaki kişilerin ortak kararıyla gruptan birini öp ses atarak (ortak karar verilemezse /zar komutundan 1 e en yakın oyuncuyu öp).","5 dakika boyunca oyundaki bir kişinin kölesi ol.", "Bir süpürgeyle veya paspas ile dans et ve videosunu at","Gerçek aşkının kim olduğunu ilan et","Ağzını hareket ettirmeden baştan sona alfabeyi oku okurken video at", "Aklına gelen ilk kelimeyi hemen söyle.",
"Oyundaki oyunculardan biri hakkında hikaye uydur", "15 saniye içerisinde sondan başa doğru alfabeyi oku okurken ses at", "Bir köpek gibi havla havlarken ses at","Bir şarkıyı baştan sona söyle söylerken ses at","Çıktığın en kötü ve en iyi kişiyi açıkla.","Bir dakika boyunca karşı cinsten biri gibi yürü.","Sevgiline atıp atabileceğin en acımasız mesajı gönder.","Oyunda yer alan her kişi hakkında bildiğin komik bir şey anlat.",
"Ünlü restoranlardan birini ara ve menülerini öğrenirken dalga geç.","Eski bir şarkıyı aç ve onu taklit ederek söylemeye çalış söylerken ses at","1 tur boyunca farklı bir dilde konuş.","Eski sevgiline mesaj at ve onu unutamadığını söyle.","2 tur boyunca “sen” kelimesini duyunca kuş gibi ses çıkart.","Telefondaki tarayıcı geçmişini herkese göster.","Odadan birisi için satın alacakmış gibi iç çamaşırı araştırması yap.",
)
                                           
#@app.on_message(filters.command(["eros"],["/", ""]))
#async def eros(c:Client, m:Message):
#    users = await c.get_chat_members(m.chat.id, limit=1000)
#    
#    users_l = []
#    for user in users:
#        if user.user.is_bot or user.user.is_deleted:
#            pass
#        else:
#            users_l.append(user.user)
#    count = len(users_l)
    
#    ilk = users_l[randint(0,count)]
#    iki = users_l[randint(0,count)]
    
#    if ilk.id==1550788256 or ilk.id==5576614947 or iki.id==5375589992 or iki.id==5576614947:
#        await m.reply(f"**💘 ᴇʀᴏs'ᴜɴ ᴏᴋᴜɴᴜ ᴀᴛᴛɪᴍ .\n✓  ɢɪᴢʟɪ ᴀşɪᴋʟᴀʀ :\n\n[ ✍🏻 ](tg://user?id=5053767281) ❤️ [ . ](tg://user?id=5533927130)**")
        
#    else:
#        await m.reply(f"**💘 ᴇʀᴏs'ᴜɴ ᴏᴋᴜɴᴜ ᴀᴛᴛɪᴍ .\n✓  ɢɪᴢʟɪ ᴀşɪᴋʟᴀʀ :\n\n{ilk.mention} ❣️ {iki.mention}\n\n💞 sᴇᴠɢɪ ᴏʀᴀɴɪ : %{random.choice(say)}**")

