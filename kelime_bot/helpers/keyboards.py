from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup

kanal = InlineKeyboardMarkup([
    [
    InlineKeyboardButton("💡 ᴛᴜ̈ᴍ ᴋᴏᴍᴜᴛʟᴀʀ " , url= "t.me/KelimeTR/6"),
    ]

])

destek = InlineKeyboardMarkup([
    [
    InlineKeyboardButton("💭 ᴅᴜʏᴜʀᴜ ᴋᴀɴᴀʟɪ " , url= "t.me/KelimeTR"),
    ]

])

baslat = InlineKeyboardMarkup([
    [
    InlineKeyboardButton("Yeniden Başla" , callback_data="turet"),
    ]

])
