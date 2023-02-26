from OrekiRobot import tbot as oreki
from OrekiRobot.events import register

PHOTO = "https://te.legra.ph/file/c4b3a0fb319744a2e41fd.jpg"


@register(pattern=("/updates"))
async def awake(event):
    OREKI = """
    ⊛ New Fonts Module Added✅ ⊛
    ⊛ New Google Module Added✅ ⊛
    ⊛ Image Searching Module Added✅ ⊛
    * Running On New Repo✅ *
    * Almost All Errors Fixed ✅ *
    * UI Changed ✅ *
    * You can Rename Files ✅ *
"""
    await oreki.send_file(event.chat_id, PHOTO, caption=OREKI)
