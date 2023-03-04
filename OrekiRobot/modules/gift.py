import os
import asyncio
import time

from datetime import datetime

from OrekiRobot import tbot as oreki
from OrekiRobot.events import register
from OrekiRobot import OWNER_ID
from OrekiRobot import TEMP_DOWNLOAD_DIRECTORY as path

meow = './OrekiRobot/imagefiles/IMG_20211114_164239_236.jpg'
client = oreki

@register(pattern=r"^/gift ?(.*)")
async def Prof(event):
    if event.sender_id == OWNER_ID:
        pass
    else:
        return
    thumb = meow
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./OrekiRobot/modules/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
     message_id = event.message.id
     await event.client.send_file(
             event.chat_id,
             the_plugin_file,
             force_document=True,
             allow_cache=False,
             thumb=thumb,
             reply_to=message_id,
         )
    else:
        await event.reply("No File Found ⚠️")
