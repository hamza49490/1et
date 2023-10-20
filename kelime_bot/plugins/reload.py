import asyncio
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, Message


@Client.on_message(filters.command(["r"]))
async def update_admin(client: Client, message: Message):
    global admins
    if message.chat.type == "private":
        return
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text("**🎄 ʙᴏᴛ ʏᴇɴɪᴅᴇɴ ʙᴀşʟᴀᴅɪ .\n🎄 ᴀᴅᴍɪɴ ʟɪsᴛᴇsɪ ɢᴜ̈ɴᴄᴇʟʟᴇɴᴅɪ .**")
