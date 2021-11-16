import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from lunaBot.events import register as MEMEK
from lunaBot import telethn as tbot

PHOTO = "https://telegra.ph/file/9357e7420a924d4581903.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  seth = event.sender.first_name
  KEYZIO = "**Holla I'am Keyzio!** \n\n"
  KEYZIO += "⚡ **I'm Working Properly** \n\n"
  KEYZIO += "⚡ **My Master : [ꜱᴇᴛʜ★](https://t.me/xyzseth)** \n\n"
  KEYZIO += f"⚡ **Telethon Version : {tlhver}** \n\n"
  KEYZIO += f"⚡ **Pyrogram Version : {pyrover}** \n\n"
  KEYZIO += "**Thanks For Adding Me Here 😊🔪**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/lunatapibot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/sethproject")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=KEYZIO,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  seth = event.sender.first_name
  LUNA = "✅ **Keyzio berhasil di restart**\n\n• Admin list has been **updated**"
  BUTTON = [[Button.url("📡 ᴜᴘᴅᴀᴛᴇs", "https://t.me/sethproject")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)
