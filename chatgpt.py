from pyrogram import Client, filters,enums,idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
import openai
from pyrogram.types import CallbackQuery
import os,sys,re,requests
import asyncio,time
from random import choice
from datetime import datetime
import logging

FORMAT = "[LEGEND-MUKESH] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

API_ID = int(os.environ.get("API_ID", "26573250"))
API_HASH = os.environ.get("API_HASH", "6306d2d23b1083a6f757f64f0b0c609c") 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6559325433:AAHRdRuS7agUSYXIYpQPfS7gYvLO5tXNPyY") 
OPENAI_KEY = os.environ.get("OPENAI_KEY", "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")

StartTime = time.time()
aiko = Client(
    "chat-gpt" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)
   
openai.api_key = OPENAI_KEY
@aiko.on_message(filters.command(["buket"],  prefixes=["", "/"]))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "**💕 Sorunuz Nedir ?**")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            end_time = time.time()
            await message.reply_text(f"**📑 {x}**", parse_mode=ParseMode.MARKDOWN)     
    except Exception as e:
        await message.reply_text(f"** Hata **")


if __name__ == "__main__":
    print(f"""Bot Aktif !""")
    try:
        aiko.start()

    
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("API_ID/API_HASH'ınız geçerli değil.")
    except AccessTokenInvalid:
        raise Exception("BOT_TOKEN'iniz geçerli değil.")
    print(f"""REPO'YA KATILIN !""")
    idle()
    aiko.stop()
    print("Bot Durdu !")
