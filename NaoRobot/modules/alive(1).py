import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from NaoRobot.events import register as MEMEK
from NaoRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/9357e7420a924d4581903.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  KEYZIO = "**Holla I'm Keyzio!** \n\n"
  KEYZIO += "⚡ **I'm Working Properly** \n\n"
  KEYZIO += "⚡ **My Master : [ꜱᴇᴛʜ★](https://t.me/xyzseth)** \n\n"
  KEYZIO += f"⚡ **Telethon Version : {tlhver}** \n\n"
  KEYZIO += f"⚡ **Pyrogram Version : {pyrover}** \n\n"
  KEYZIO += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/Keyziarobot_bot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/sethproject")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=KEYZIO,  buttons=BUTTON)
