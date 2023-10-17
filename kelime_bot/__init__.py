from time import sleep
from pyrogram import Client
import logging


# THE LOGGING
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


# Hesap
API_ID = "16347484"
API_HASH = "da52627a852e4d62633fd6ab72dee4c4"
TOKEN = "6559325433:AAF-G05bNjC-S5TwbmW222eY77SU8jM5GhY"
USERNAME = "AikoDenemeBot"
BOT_ID = "6404904263"

OWNER_ID = 6540285284

# BOT CLIENTİ
app = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="kelime_bot/plugins/"),
    workers=16
    )


# Oyun Verileri
oyun = {}


# rating
rating = {}

