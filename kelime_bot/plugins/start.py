from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕ Məni Qrubuna atila", url=f"http://t.me/SozTapBot?startgroup=new")
    ],
    [
        InlineKeyboardButton("🇦🇿 Sahibim", url="https://t.me/HupTelegram"),
        InlineKeyboardButton("💬 Chat", url="https://t.me/MinBirGece777"),
    ]
])


START = """
**🔮 Salam, Sözləri Tapma oyununa xoş geldin..**

➤ Məlumat üçün 👉 /help Basın. Ayarlar asand ve sadədir. 
"""

HELP = """
**✌️ Ayaralar Menüsünə Xoşgeldiniz.**
/oyun - Oyunu başlatmaq için..
/kec - Üç ədəd hakkınız var, oyunu keçmek üçün.. 
/reytinq - Oyuncular arasındaki rəqabət bilgisi..
/cancel - Oyundan çıxmaq üçün lazım olan komuttur.. 
"""

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://images.app.goo.gl/eKtuvcAF4cnMyenL8",caption=START,reply_markup=keyboard)

@Client.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://images.app.goo.gl/eKtuvcAF4cnMyenL8",caption=HELP) 

# Oyunu başlat. 
@Client.on_message(filters.command("oyun")) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**❗ Oyun onsuzda Qrubunuzda Davam Edir ✍🏻 \n Oyunu dayandırmaq üçün yazıb /cancel dayandırabilərsiz")
    else:
        await m.reply(f"**{m.from_user.mention}** Tərəfından! \nSözü Tapma Oyunu Başladı .\n\ Uğurlar !", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["kec"] = 3
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""


🎯 Raund : {oyun[m.chat.id]['round']}/60 
📝 Söz :   <code>{kelime_list}</code>
💰 Qazandığınız Rəqəm: 1
🔎 Yardım: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {int(len(kelime_list)/2)} 

✏️ Qarışıq hərflərdən doğru sözü tapın 
        """
        await c.send_message(m.chat.id, text)
        
