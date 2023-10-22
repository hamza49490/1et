from pyrogram import Client, filters
import requests

# API anahtarını buraya girin
API_KEY = "bc5ca147175e26ed57581b6b"

# Komutları işlemek için bir filtre oluşturun
@filters.command(["dolar"])
def get_dolar(_, message):
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/USD")
    data = response.json()
    dolar_kuru = data["rates"]["TRY"]
    message.reply_text(f"1 USD = {dolar_kuru} TRY")

@filters.command(["euro"])
def get_euro(_, message):
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/EUR")
    data = response.json()
    euro_kuru = data["rates"]["TRY"]
    message.reply_text(f"1 EUR = {euro_kuru} TRY")

@filters.command(["altın"])
def get_altin(_, message):
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/XAU")
    data = response.json()
    altin_kuru = data["rates"]["TRY"]
    message.reply_text(f"1 XAU = {altin_kuru} TRY")
