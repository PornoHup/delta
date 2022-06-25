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
API_ID = "5249642922"
API_HASH = "0f9159afc920f9c592df555e4b1cb73b"
TOKEN = "5554338413:AAHZC7BgMdYCsMa1z1_kGs8I8VP2kKG93S8" 
USERNAME = "5249642922"




# BOT CLIENTİ
bot = Client
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="soztapbot/plugins/"),
    workers=16



# Oyun Verileri
oyun = {}


# rating
rating = {}





# !!!!!!!!!!!!!! DEĞİŞTİR KESİNLİKLE !!!!!!!!!!!!!!!!
#      SAHİBİN USER ID'Sİ
OWNER_ID = 5249642922

