from kelime_bot import rating
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message


@Client.on_message(filters.command("rating"))
async def ratingsa(c:Client, m:Message):
    metin = """📝 𝖦𝗅𝗈𝖻𝖺𝗅 𝖳𝗈𝗉 10 𝖮𝗒𝗎𝗇𝖼𝗎 :

"""
    eklenen = 0
    s = sorted(rating.items(), key=lambda x: x[1], reverse=True)
    for kisi in s:
        metin +=  f"**{kisi[0]}** :  {kisi[1]}  𝖯𝗎𝖺𝗇\n"
        eklenen+=1
        if eklenen == 10:
            break
    await c.send_message(m.chat.id, metin)
