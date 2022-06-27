from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton

keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("✅  𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾  ✅", url=f"http://t.me/StarOyunBot?startgroup=new")
    ],
    [
        InlineKeyboardButton("📮 𝖵𝖨𝖯 𝖦𝗋𝗎𝖻 ", url="t.me/kostantinniyesohbet"),
        InlineKeyboardButton("📢 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋 ", url="t.me/Starbotkanal/7"),
    ],
    [
        InlineKeyboardButton("🏆 𝖤𝗇 𝗂𝗒𝗂 20 𝖮𝗒𝗎𝗇𝖼𝗎 ", url="t.me/HariboTube/6"),
    ]
])



START = """
• **Merhaba** 🇹🇷\n\n• **Ben Bir Oyun Botuyum** 🎮 \n\n• **Çeşitli oyunlar oynamak ve eğlenceli vakit geçirmek için benimle oynayabilirsin** ✍🏻 \n\n• **Benimle oynamak için beni bir gruba ekleyip yönetici yapman lazim** . 💭
"""

    
    
    
    
    
    
"""
PRIVATE /start MESSAGE
"""
@Client.on_message(filters.command("start") & filters.private)
async def priv_start(c:Client, m:Message):
    await c.send_message(m.chat.id, START, reply_markup=keyboard)
