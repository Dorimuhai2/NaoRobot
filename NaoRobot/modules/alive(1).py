import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from NaoRobot.events import register as MEMEK
from NaoRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/93b07a50496c85afbdd51.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  KEYZIA = "**Holla I'm Keyzia!** \n\n"
  KEYZIA += "💎 **I'm Working Properly** \n\n"
  KEYZIA += "💎 **My Master : [ꜱᴇᴛʜ★](https://t.me/xyzseth)** \n\n"
  KEYZIA += f"💎 **Telethon Version : {tlhver}** \n\n"
  KEYZIA += f"💎 **Pyrogram Version : {pyrover}** \n\n"
  KEYZIA += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/Keyziarobot_bot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/sethproject")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=KEYZIA,  buttons=BUTTON)
