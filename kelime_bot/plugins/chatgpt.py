from pyrogram import Client, filters,enums,idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
from pyrogram.types import CallbackQuery
from random import choice
from datetime import datetime
from kelime_bot import OPENAI_KEY
import logging
import openai
import os,sys,re,requests
import asyncio,time

StartTime = time.time()
   
openai.api_key = OPENAI_KEY
@Client.on_message(filters.command(["buket"],  prefixes=["", "/"]))
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
