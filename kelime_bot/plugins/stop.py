from pyrogram import Client
from pyrogram import filters
from random import shuffle
from kelime_bot import USERNAME
from pyrogram.types import Message
from kelime_bot.helpers.keyboards import *
from kelime_bot.helpers.kelimeler import kelime_sec
from kelime_bot import *



@Client.on_message(filters.command("stop") & ~filters.private & ~filters.channel)
async def stop(c:Client, m:Message):
    global oyun
    
    siralama = []
    for i in oyun[m.chat.id]["oyuncular"]:
        siralama.append(f"{i}  :   {oyun[m.chat.id]['oyuncular'][i]} 𝖯𝗎𝖺𝗇")
    siralama.sort(reverse=True)
    siralama_text = ""
    for i in siralama:
        siralama_text += i + "\n"     
    
    await c.send_message(m.chat.id, f"**{m.from_user.mention}** 𝖳𝖺𝗋𝖺𝖿𝗂𝗇𝖽𝖺𝗇 ! \n•> 𝖪𝖾𝗅𝗂𝗆𝖾 𝖮𝗒𝗎𝗇𝗎 𝖡𝗂𝗍𝗍𝗂𝗋𝗂𝗅𝖽𝗂 ! \n\n•> 𝖸𝖾𝗇𝗂 𝖮𝗒𝗎𝗇 𝖡𝖺𝗌𝗅𝖺𝗍𝗆𝖺𝗄 𝗂𝖼𝗂𝗇 \n /game 𝖸𝖺𝗓𝖺𝖻𝗂𝗅𝗂𝗋𝗌𝗂𝗇𝗂𝗓 . . .\n\n 🏆  𝖯𝗎𝖺𝗇 𝖳𝖺𝖻𝗅𝗈𝗌𝗎  :\n\n{siralama_text}")
    oyun[m.chat.id] = {}
    
