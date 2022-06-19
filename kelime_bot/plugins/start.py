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
        InlineKeyboardButton("➕ Grubuna Ekle", url=f"http://t.me/TapmacaOyunBot?startgroup=new")
    ],
    [
        InlineKeyboardButton("🇦🇿 Sahibim", url="https://t.me/Thagiyevvvv"),
        InlineKeyboardButton("💬 Chat", url="https://t.me/karabakhteamm"),
    ]
])


START = """
**🔮 Salam, Sözləri Tapma oyununa xoş geldin..**

➤ Bilgi için 👉 /help Tıklayın. Komutlar asand ve sadədir. 
"""

HELP = """
**✌️ Komutlar Menüsüne Hoşgeldiniz.**
/oyun - Oyunu başlatmaq için..
/kec - Üç ədəd hakkınız var, oyunu keçmek üçün.. 
/reytinq - Oyuncular arasındaki rəqabət bilgisi..
/cancel - Oyundan çıxmaq üçün lazım olan komuttur.. 
"""

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://images.app.goo.gl/Dys4v3hgKMr4YVmx9",caption=START,reply_markup=keyboard)

@Client.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://images.app.goo.gl/Dys4v3hgKMr4YVmx9",caption=HELP) 

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
        await m.reply("**❗ Oyun onsuzda Qrubunuzda Davam Edir ✍🏻 \n Oyunu dayandırmaq üçün yazıp /cancel dayandırabilərsiz")
    else:
        await m.reply(f"**{m.from_user.mention}** Tarafından! \nSözü Tapma Oyunu Başladı .\n\nİyi Şanslar !", reply_markup=kanal)
        
        oyun[m.chat.id] = {"söz":söz_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["kec"] = 0
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
        
