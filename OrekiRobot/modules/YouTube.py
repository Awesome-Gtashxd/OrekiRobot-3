import aiohttp
from pyrogram import filters
from OrekiRobot import pgram
from OrekiRobot.utils.errors import capture_err


@pgram.on_message(filters.command(["instagram", "insta", f"insta@OrekiRobot"]))
@capture_err
async def instagram(_, message):
    if len(message.command) != 2:
        await message.reply_text("/insta Username")
        return
    username = message.text.split(None, 1)[1]
    URL = f"https://api.instagram.com/users/{username}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()
            try:
                url = result["html_url"]
                name = result["name"]
                username = result["username"]
                bio = result["bio"]
                avatar_url = result["avatar_url"]
                created_at = result["created_at"]
                subscribers = result["subscribers"]
                youtube = f"""
Info Of {name}

Username ~ {username}
Bio ~ {bio}
Created on ~ {created_at}
URL ~ {url}
Subscribers ~ {subscribers}
"""
            except Exception as e:
                print(str(e))
                pass
    await message.reply_photo(photo=avatar_url, caption=youtube)
    
__mod_name__ = "YouTube"
