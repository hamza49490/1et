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
TOKEN = "6404904263:AAHP25SjaF85qCncHTq5NE9zA4A-ASD5XNA"
USERNAME = "BuketTaggerBot"

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

