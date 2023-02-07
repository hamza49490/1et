from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup

kanal = InlineKeyboardMarkup([
    [
    InlineKeyboardButton("💡 Komutlar 💡" , url= "t.me/KelimeTR/6"),
    ]

])

destek = InlineKeyboardMarkup([
    [
    InlineKeyboardButton("♻️ Küresel Skor ♻️" , url= "t.me/KelimeTR/7"),
    ]

])

baslat = InlineKeyboardMarkup([
    [
    InlineKeyboardButton("Yeniden Başla" , data="turet"),
    ]

])
