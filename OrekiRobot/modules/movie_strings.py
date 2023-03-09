from OrekiRobot.events import register
from OrekiRobot import tbot as oreki

THUNIVU_STRINGS = (
POSTER = "https://t.me/OrekiMovies/7"

@register(pattern=("Thunivu"))
async def awake(event):
    CAPTION = """
 THUNIVU

Year : 2023
Language : Tamil
Quality : HDRip
Size : 250MB-1.4GB

Powered By : @Gtash_Association
"""
await oreki.send_file(event.chat_id, POSTER, caption=CAPTION)

file1 = "https://t.me/OrekiMovies/8"

F1_CAP = """
@Gtash_Association Thinuvu (2023) 320p HQ HDRip - x264 - Tamil - 250MB
"""
await oreki.send_file(event.chat_id, file1, caption=F1_CAP)

file2 = "https://t.me/OrekiMovies/9"

F2_CAP = """
@Gtash_Association Thinuvu (2023) 480p HQ HDRip - x264 - Tamil - 400MB
"""
await oreki.send_file(event.chat_id, file2, caption=F2_CAP)

file3 = "https://t.me/OrekiMovies/10"

F3_CAP = """
@Gtash_Association Thinuvu (2023) 720p HQ HDRip - x264 - Tamil - 700MB
"""
await oreki.send_file(event.chat_id, file3, caption=F3_CAP)

file4 = "https://t.me/OrekiMovies/11"

F4_CAP = """
@Gtash_Association Thunivu (2023) 1080p HQ HDRip - x264 - Tamil - 1.4GB
"""
await oreki.send_file(event.chat_id, file4, caption=F4_CAP)
)
