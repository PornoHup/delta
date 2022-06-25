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
API_ID = "15283231"
API_HASH = "36e3686358ae38f722dce5c7d5b59902"
TOKEN = "5447017941:AAFLZQoXQqWaq2j0IBdTS6s1xFDxRf7vOj8" 
USERNAME = "5249642922"




# BOT CLIENTİ
bot = Client
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="soztap_bot/plugins/"),
    workers=16



# Oyun Verileri
oyun = {}


# rating
rating = {}





# !!!!!!!!!!!!!! DEĞİŞTİR KESİNLİKLE !!!!!!!!!!!!!!!!
#      SAHİBİN USER ID'Sİ
OWNER_ID = 5249642922

