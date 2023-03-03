import random

from OrekiRobot.events import register



Text1 = (
    "Do you have Lover?", "Which Game You long time played?", "Are you played Game With Big youtuber?", "Any girls Seen your dick?", "Any time you shared Your Browing History To Others?",
    "Are you Changed Tv Channel In Your dad/mother watching TV?", "Do you have any Ex?", "Any girl shared her number to you?", "Do you like girls?", "Are you Sigma?",
    "Do you have Any brothers?", "Are you Pokemon fan?", "Doremon best or his devices best?", "What Is Your Favourite Anime?", "If any girls love you are you accept her love?",
    "What is your Dad income?", "Are you Completed college Are Not?", "How many crushes You have?", "Any scamer scamed You?", "What type of YouTube videos you like?",
    "Any time you helped poor peoples?", "You Know Python?", "You Like Me?", "Your favourite Command in my Modules?", "You Boy or Girl?",
)


@register(pattern=("/truth"))
async def awake(event):
  turn1 = random.choice(Text1)
  await event.reply(turn1)
  


Text2 = (
    "Share Your Browsing History to others", "Buy briyani And Show Me", "Play minecraft java in your phone", "Give me your Telegram GF ID", "Go to park Propose Any one",
    "Switch off your phone for 10 mins", "Help any Poor peoples", "Go to tea shop Drink tea for free", "give me 1rs", "Join @Gtash_Association",
    "Go and exchange your Lover phone", "Just Start me in dm", "Go and swim for 30 mins", "Off your Phone And study", "Share Me",
    "Send Me your GF Pic", "Send Me Hi", 
)


@register(pattern=("/dare"))
async def awake(event):
  turn2 = random.choice(Text2)
  await event.reply(turn2)



Text3 = (
    "You Don't Have GF", "You Don't have Dick", "You're Not Boy", "You're Not Girl", "You Like Games",
    "You Like Me", "You Like Foods much", "You Have Baby", "You Have Own House", "You Don't Have House",
    "You Idiot", "You're Crush Hate You",
)


@register(pattern=("/fact"))
async def awake(event):
  turn3 = random.choice(Text3)
  await event.reply(turn3)
    


Text4 = (
    "Question: In One Place Big Brother and Small Brother Are there Big Brother saw a Place and Big Brother Only Goes the Place Answer: Course That Place Only For Big Brothers",
)


@register(pattern=("/joke"))
async def awake(event):
  turn4 = random.choice(Text4)
  await event.reply(turn4)

__mod_name__ = "OrekiFun"
__help__ = """
 🔹 `/truth`*:* Tell the Truth
 🔹 `/dare`*:* Do that
 🔹 `/fact`*:* Some Real
 🔹 `/joke`*:* Some Jokes you like that
"""
