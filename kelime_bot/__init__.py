from time import sleep
from pyrogram import Client
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


API_ID = int(os.environ.get("API_ID", "26573250"))
API_HASH = os.environ.get("API_HASH", "6306d2d23b1083a6f757f64f0b0c609c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6404904263:AAHmC2JxmeN8wfODX-L8caONf8Y5GbozpjY")
BOT_ID = int(os.environ.get("BOT_ID", "6404904263"))
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://epiktv7:epiktv86@cluster0.ttyjqmj.mongodb.net/?retryWrites=true&w=majority")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "BuketTaggerBot")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001983841726"))
GROUP_SUPPORT = os.environ.get("GROUP_SUPPORT", "BuketBilgi")
GONDERME_TURU = os.environ.get("GONDERME_TURU", False)
OWNER_ID = int(os.environ.get("OWNER_ID", "6540285284"))
LANGAUGE = os.environ.get("LANGAUGE", "TR")

app = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="kelime_bot/plugins/"),
    workers=16
    )


oyun = {}
rating = {}
