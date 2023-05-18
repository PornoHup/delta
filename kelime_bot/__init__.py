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
TOKEN = "6216629694:AAF6o8kAIBQWjNUzG7b8lAoa_klCOLm6dNU" 
USERNAME = "5939626310"




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
OWNER_ID = 5939626310

