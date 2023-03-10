import aiohttp
from pyrogram import filters
from OrekiRobot import pgram
from OrekiRobot.utils.errors import capture_err


@pgram.on_message(filters.command(["instagram"]))
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
                name = result["name"]
                username = result["username"]
                bio = result["bio"]
                posts = result["posts"]
                avatar_url = result["avatar_url"]
                created_at = result["created_at"]
                followers = result["followers"]
                following = result["following"]
                instagram = f"""
Info Of {name}

Username ~ {username}
Bio ~ {bio}
Posts ~ {posts}
Created on ~ {created_at}
Followers ~ {followers}
Following ~ {following}
"""
            except Exception as e:
                print(str(e))
                pass
    await message.reply_photo(photo=avatar_url, caption=instagram)
    
__mod_name__ = "Instagram"
