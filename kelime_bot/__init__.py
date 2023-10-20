from time import sleep
from pyrogram import Client
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

API_ID = "26573250"
API_HASH = "6306d2d23b1083a6f757f64f0b0c609c"
TOKEN = "6559325433:AAHRdRuS7agUSYXIYpQPfS7gYvLO5tXNPyY"
BOT_ID = "6559325433"
USERNAME = "AikoDenemeBot"
OWNER_ID = 6540285284
DATABASE_URL = "mongodb+srv://ok:ok@cluster0.uooya.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
BOT_USERNAME = "AikoDenemeBot"
LOG_CHANNEL = "-1001983841726"
GROUP_SUPPORT = "BuketBilgi"
GONDERME_TURU = "False"
LANGAUGE = "TR"

# BOT CLIENTİ
app = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="kelime_bot/plugins/"),
    workers=16
    )


oyun = {}
rating = {}
