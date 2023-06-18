from OrekiRobot import tbot as oreki
from OrekiRobot.events import register

GN_PIC = "https://graph.org/file/02555c466460361fc6145.mp4"
GM_PIC = "https://graph.org/file/2c5bc262e79b8797b651d.mp4"
HI_PIC = "https://graph.org/file/aa541a4f1ff8af37386c7.mp4"
HELLO_PIC = "https://graph.org/file/5b41b66247b2f6cdb876e.mp4"

@register(pattern=("Good night"))
async def awake(event):
    GN = f"Good night I hope tomorrow is a Lucky day for you... {event.sender.first_name}"
    await oreki.send_file(GN_PIC, caption=GN)

@register(pattern=("Good morning"))
async def awake(event):
    GM = f"Good morning I hope today is a Lucky day for you... {event.sender.first_name}"
    await oreki.send_file(GM_PIC, caption=GM)

@register(pattern=("Hi"))
async def awake(event):
    HI = f"Hey How are you?. {event.sender.first_name}"
    await oreki.send_file(HI_PIC, caption=HI)

@register(pattern=("Good morning"))
async def awake(event):
    HELLO = f"Hellallo.. {event.sender.first_name}"
    await oreki.send_file(HELLO_PIC, caption=HELLO)
