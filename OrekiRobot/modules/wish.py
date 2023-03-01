import random

from telethon import events

from OrekiRobot import tbot as oreki


@oreki.on(events.NewMessage(pattern="/wish ?(.*)"))
async def wish(e):
quew = event.pattern_match.group(1)
    if event.sender_id != OWNER_ID and not quew:
        await event.reply(
            "ahh, Give me some text to say how much chance it have!\nExample `/wish Oreki `"
        )
        return
    if e.is_reply:
        mm = random.randint(1, 100)
        lol = await e.get_reply_message()
        fire = "https://te.legra.ph/file/38892f30c27ca7de35d08.jpg"
        await oreki.send_file(
            e.chat_id,
            fire,
            caption=f"**Hey, [{e.sender.first_name}](tg://user?id={e.sender.id}), Your wish has been cast.🖤**\n\n__chance of success {mm}%__",
            reply_to=lol,
        )
    if not e.is_reply:
        mm = random.randint(1, 100)
        fire = "https://te.legra.ph/file/38892f30c27ca7de35d08.jpg"
        await oreki.send_file(
            e.chat_id,
            fire,
            caption=f"**Hey, [{e.sender.first_name}](tg://user?id={e.sender.id}), Your wish has been cast.🖤**\n\n__chance of success {mm}%__",
            reply_to=e,
        )
