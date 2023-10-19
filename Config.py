import os

class Config:

API_ID = int(os.environ.get("API_ID","18049084"))
API_HASH = os.environ.get("API_HASH","7e74b1e22026fcc291d32b3d431aa21e")
BOT_TOKEN = os.environ.get("TOKEN","6559325433:AAF-G05bNjC-S5TwbmW222eY77SU8jM5GhY")
BOT_ID = int(os.environ.get("BOT_ID", "6559325433"))
DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://ok:ok@cluster0.uooya.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") # MongoDB veritabanınızın url'si. Nasıl alacağınızı bilmiyorsanız destek grubu @RepoHaneX'e gelin.
BOT_USERNAME = os.environ.get("BOT_USERNAME","AikoDenemeBot") # Botunuzun kullanıcı adı.
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL","-1001983841726")) # Botunuzun eylemleri kaydedeceği kayıt grubunun id'si.
GROUP_SUPPORT = os.environ.get("GROUP_SUPPORT", "BuketBilgi") # Botunuzdan yasaklanan kullanıcıların itiraz işlemleri için başvuracağı grup, kanal veya kullanıcı. Boş bırakırsanız otomatik olarak OWNER_ID kimliğine yönlendirecektir.
GONDERME_TURU = os.environ.get("GONDERME_TURU", False) # Botunuzun yanıtladığınız mesajı gönderme türü. Eğer direkt iletmek isterseniz False, kopyasını göndermek isterseniz True olarak ayarlayın.
OWNER_ID = int(os.environ.get("OWNER_ID","6540285284")) # Sahip hesabın id'si
OWNERNAME = "ㅤᴀɪᴋᴏㅤ"
OWNER = [6540285284]

LANGAUGE = os.environ.get("LANGAUGE", "TR")
