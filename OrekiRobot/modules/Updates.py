from OrekiRobot import tbot as oreki
from OrekiRobot.events import register

PHOTO = "https://te.legra.ph/file/c4b3a0fb319744a2e41fd.jpg"


@register(pattern=("/updates"))
async def awake(event):
    OREKI = """
    ⊛ New Fonts Module Added✅ ⊛
    ⊛ New Google Module Added✅ ⊛
    **⊛ New Image Searching Module Added✅ ⊛**
    **⊛ New Zip/Unzip Module Added✅ ⊛**
    ⊛ Almost All Errors Fixed✅ ⊛
    **⊛ New Url Uploader Module Added✅ ⊛**
    **⊛ Pm/Dm Start was Updated✅ ⊛**
    **⊛ New Waifu Module Added✅ ⊛**
    **⊛ Youtube Video & Song Uploader Module Added✅ ⊛**
    **⊛ Special Update: New Files Renamer Module Added✅ ⊛**

      **Next Update is Comming on 20th March**
"""
    await oreki.send_file(event.chat_id, PHOTO, caption=OREKI)
