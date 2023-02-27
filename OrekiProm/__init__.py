import logging
import pymongo
from pyrogram import Client


FORMAT = "[OrekiProm] %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)


OWNER_ID = 5534661034
PREFIX = ["/","!","*","$","#","?",">",]

mongo = pymongo.MongoClient("")
db = mongo["OrekiProm"]

ND = Client("OrekiProm",
     api_id=int(""),
     api_hash="",
     bot_token="",
     plugins=dict(root="OrekiProm"),)
