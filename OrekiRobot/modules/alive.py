from pyrogram import __version__ as pyrover
from telethon import Button
from telegram import __version__ as ptb
from telethon import __version__ as tlhver

from OrekiRobot import tbot as oreki
from OrekiRobot.events import register

IMAGE = "https://te.legra.ph/file/344cdfc69c65647c10313.jpg"


@register(pattern=("/alive"))
async def awake(event):
    OREKI = """
**Hola I'm Prince Oreki 왕자 ~ 🖤!**
**Python-Telegram-Bot Version ~ 🖤 :** {ptb}
**Telethon Version ~ 🖤:** {tlhver}
**Pyrogram Version ~ 🖤:** {pyrover}
**My Master ~ 🖤 :** [THE GTASH](https://t.me/Awesome_Gtashxd)
"""

    BUTTON = [
        [
            Button.url(
                "Add Prince Oreki 왕자 To Your Group ✅", "https://t.me/{BOT_NAME}?startgroup=true"
            ),
    ],
    [
            Button.url(
                "Support🎯", "https://t.me/Gtash_Association"
         ),
     ],
  ]
    await oreki.send_file(event.chat_id, IMAGE, caption=OREKI, buttons=BUTTON)
