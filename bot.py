import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

from pyrogram.types.messages_and_media import Message
from pyrogram import Client, filters
import time


logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

app = Client("GUNC",
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token
             )

anlik_calisan = []

ozel_list = [1983444555]
anlik_calisan = []
grup_sayi = []
etiketuye = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"❌ Eᴛiᴋᴇᴛ İşʟᴇᴍiɴi İᴘᴛᴀʟ Eᴛᴛiᴍ.\n\nSᴀᴅᴇᴄᴇ 👥 {rxyzdev_tagTot[event.chat_id]} Kᴜʟʟᴀɴıᴄıʏı Eᴛɪᴋᴇᴛʟᴇᴅɪᴍ")


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("🇬🇧 Hi I'm @UserTaggertrbot I was created to search all contacts in chat.\nMᴇʀʜᴀʙᴀ! Gʀᴜʙᴜɴᴜᴢᴅᴀᴋɪ Kᴜʟʟᴀɴıᴄıʟᴀʀı Eᴛɪᴋᴇᴛʟᴇᴍᴇᴋ Bᴜʀᴀᴅᴀʏıᴍ.",
                    buttons=(
                      [
                         Button.url('➕ 𝐁𝐞𝐧𝐢 𝐆𝐫𝐮𝐛𝐚 𝐄𝐤𝐥𝐞 ➕ ', 'http://t.me/UserTaggertrbot?startgroup=a')
                      ],
                      [
                         Button.url('📣 𝐊𝐚𝐧𝐚𝐥', 'https://t.me/RulingClassChannel'),
                         Button.url('💬 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐮𝐩', 'https://t.me/RulingClassSupport')
                      ],
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**Nᴀꜱıʟ Çᴀʟışıʀıᴍ:\n\n/utag <Mesajınız> - Kᴜʟʟᴀɴıᴄıʟᴀʀı Eᴛɪᴋᴇᴛʟᴇʀɪᴍ.\n/atag <Mesajınız> - Sᴀᴅᴇᴄᴇ Yöɴᴇᴛɪᴄɪʟᴇʀɪ Eᴛɪᴋᴇᴛʟᴇʀɪᴍ.\n/cancel@UserTaggertrbot - Eᴛɪᴋᴇᴛ İşʟᴇᴍɪɴɪ İᴘᴛᴀʟ Eᴅᴇʀɪᴍ.\n❕ Yᴀʟɴıᴢᴄᴀ Yöɴᴇᴛɪᴄɪʟᴇʀɪ Bᴜ Kᴏᴍᴜᴛʟᴀʀı Kᴜʟʟᴀɴᴀʙɪʟɪʀ."
  await event.reply(helptext)

@client.on(events.NewMessage())
async def mentionalladmin(event):
  global etiketuye
  if event.is_group:
    if event.chat_id in etiketuye:
      pass
    else:
      etiketuye.append(event.chat_id)

@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("Bu komutu gruplar ve kanallar için geçerli❗️**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadace yoneticiler kullana bilir〽️**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Önceki Mesajlara Cevab Vermeyin")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Başlatmak için sebeb yok❗️")
  else:
    return await event.respond("Işleme başlamak için sebeb yok")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👥 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Işlem Başarıyla Durduruldu\n\n**Buda sizin reklamınız ola bilir @RulingClassChannel**❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👥 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("işlem başarıyla durduruldu❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern="^/atag ?(.*)"))
async def mentionalladmin(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__Bᴜ Kᴏᴍᴜᴛ Gʀᴜᴘʟᴀʀᴅᴀ Vᴇ Kᴀɴᴀʟʟᴀʀᴅᴀ Kᴜʟʟᴀɴıʟᴀʙɪʟɪʀ.!__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("__Yᴀʟɴıᴢᴄᴀ Yöɴᴇᴛɪᴄɪʟᴇʀ Eᴛɪᴋᴇᴛ İşʟᴇᴍɪ Yᴀᴘᴀʙɪʟɪʀ!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eꜱᴋɪ Mᴇꜱᴀᴊʟᴀʀ İçɪɴ Üʏᴇʟᴇʀᴅᴇɴ Bᴀʜꜱᴇᴅᴇᴍᴇᴍ! (Gʀᴜʙᴀ Eᴋʟᴇᴍᴇᴅᴇɴ Öɴᴄᴇ Göɴᴅᴇʀɪʟᴇɴ Mᴇꜱᴀᴊʟᴀʀ)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Bᴀɴᴀ Bɪʀ Mᴇᴛɪɴ Vᴇʀ!__")
  else:
    return await event.respond("__Bɪʀ Mᴇꜱᴀᴊı Yᴀɴıᴛʟᴀʏıɴ Vᴇʏᴀ Eᴛɪᴋᴇᴛ Aᴛᴍᴀᴍ İçɪɴ Bᴀɴᴀ Bɪʀ Mᴇᴛɪɴ Vᴇʀɪɴ!__")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("Eᴛɪᴋᴇᴛ İşʟᴇᴍɪ Bᴀşʟᴀᴛıʟᴅı.İşʟᴇᴍɪ İᴘᴛᴀʟ Eᴛᴍᴇᴋ İçɪɴ\n /cancel@usertaggertrbot Kᴏᴍᴜᴛᴜɴᴜ\n Kᴜʟʟᴀɴıɴıᴢ")
  
    async for usr in client.iter_participants(event.chat_id,filter=ChannelParticipantsAdmins):
      usrnum += 1
      usrtxt += f"\n➢ [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Eᴛɪᴋᴇʟᴇᴛᴍᴇ İşʟᴇᴍɪ Biᴛᴛi 🤗")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n\n{usrtxt}")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id,filter=ChannelParticipantsAdmins):
      usrnum += 1
      usrtxt += f"\n➢ [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("İşʟᴇᴍ Dᴜʀᴅᴜʀᴜʟᴅᴜ ❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""

    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅ Eᴛiᴋᴇᴛʟᴇᴍᴇ İşʟᴇᴍi Tᴀᴍᴀᴍʟᴀɴᴅı !.\n\n👥 Eᴛiᴋᴇᴛʟᴇɴᴇɴ Kᴜʟʟᴀɴıᴄı Sᴀʏıꜱı: {rxyzdev_tagTot[event.chat_id]}\n🗣 Eᴛiᴋᴇᴛ İşʟᴇᴍiɴi Bᴀşʟᴀᴛᴀɴ: {rxyzdev_initT}")





@client.on(events.NewMessage())
async def mentionalladmin(event):
  global grup_sayi
  if event.is_group:
    if event.chat_id in grup_sayi:
      pass
    else:
      grup_sayi.append(event.chat_id)

@client.on(events.NewMessage(pattern='^/botstatik ?(.*)'))
async def son_durum(event):
    global anlik_calisan,grup_sayi,ozel_list
    sender = await event.get_sender()
    if sender.id not in ozel_list:
      return
    await event.respond(f"**Tagger İstatistikleri 🤖**\n\nToplam Grup: `{len(grup_sayi)}`\nAnlık Çalışan Grup: `{len(anlik_calisan)}`")


@client.on(events.NewMessage(pattern='^/botreklam ?(.*)'))
async def duyuru(event):
 
  global grup_sayi,ozel_list
  sender = await event.get_sender()
  if sender.id not in ozel_list:
    return
  reply = await event.get_reply_message()
  await event.respond(f"Toplam {len(grup_sayi)} Gruba'a mesaj gönderiliyor...")
  for x in grup_sayi:
    try:
      await client.send_message(x,f"**📣 Sponsor**\n\n{reply.message}")
    except:
      pass
  await event.respond(f"Gönderildi.")

@app.on_message(filters.user(1983444555) & filters.command(["botcum"], ["."]))
def admin(_, message: Message):
    message.reply(f"__Biricik Sahibim Gelmiş Hoşgeldin Efendim 💋 Muck__")


app.run()
print(">> Bot çalışıyor <<")
client.run_until_disconnected()
