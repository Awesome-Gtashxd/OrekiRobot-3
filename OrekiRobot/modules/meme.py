import random 
from OrekiRobot.events import register
from OrekiRobot import tbot as oreki

Text1 = (
    "Do you have Lover?", "Which Game You long time played?", "Are you played Game With Big youtuber?", "Any girls Seen your dick?", "Any time you shared Your Browing History To Others?",
    "Are you Changed Tv Channel In Your dad/mother watching TV?", "Do you have any Ex?", "Any girl shared her number to you?", "Do you like girls?", "Are you Sigma?",
    "Do you have Any brothers?", "Are you Pokemon fan?", "Doremon best or his devices best?", "What Is Your Favourite Anime?", "If any girls love you are you accept her love?",
    "What is your Dad income?", "Are you Completed college Are Not?", "How many crushes You have?", "Any scamer scamed You?", "What type of YouTube videos you like?",
    "Any time you helped poor peoples?", "You Know Python?", "You Like Me?", "Your favourite Command in my Modules?", "You Boy or Girl?",
)



@register(pattern=("/truth"))
async def awake(event):
  gtash = random.choice(Text1)
  await event.reply(gtash)
  
  
Text2 = (
    "Share Your Browsing History to others", "Buy briyani And Show Me", "Play minecraft java in your phone", "Give me your Telegram GF ID", "Go to park Propose Any one", "Switch off your phone for 10 mins", "Help any Poor peoples", "Go to tea shop Drink tea for free", "give me 1rs", "Join @Gtash_Association", "Go and exchange your Lover phone", "Just Start me in dm", "Go and swim for 30 mins", "Off your Phone And study",
    "Share Me", "Send Me your GF Pic", "Send Me Hi", 
)



@register(pattern=("/dare"))
async def awake(event):
  meow = random.choice(Text2)
  await event.reply(meow)

@register(pattern="^/fact ?(.*)")
async def _(dr):
    try:
        resp = requests.get("https://api.safone.tech/fact").json()
        results = f"{resp['fact']}"
        return await dr.reply(results)
    except Exception:
        await dr.reply(f"Error Report @{SUPPORT_CHAT}")



@register(pattern="^/joke ?(.*)")
async def _(dr):
    try:
        resp = requests.get("https://api.safone.tech/joke").json()
        results = f"{resp['joke']}"
        return await dr.reply(results)
    except Exception:
        await dr.reply(f"Error Report @{SUPPORT_CHAT}")



@register(pattern="^/advice ?(.*)")
async def _(dr):
    try:
        resp = requests.get("https://api.safone.tech/advice").json()
        results = f"{resp['advice']}"
        return await dr.reply(results)
    except Exception:
        await dr.reply(f"Error Report @{SUPPORT_CHAT}")


__help__ = """
 🔹 `/truth`*:* Tell the Truth
 🔹 `/dare`*:* Do that
 🔹 `/fact`*:* Some Real
 🔹 `/joke`*:* Some Jokes you like that
 🔹 `/advice`*:* Some advices for you
"""
