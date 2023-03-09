import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import OrekiRobot.modules.game_strings as game_strings
from OrekiRobot import OREKI_MOD
from OrekiRobot.modules.disable import DisableAbleCommandHandler
from OrekiRobot.modules.helper_funcs.chat_status import (is_user_admin)
from OrekiRobot.modules.helper_funcs.extraction import extract_user


@run_async
def truth(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(game_strings.TRUTH_STRINGS))


@run_async
def dare(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(game_strings.DARE_STRINGS))

    
__help__ = """
 • `/truth`*:* asks you a question
 • `/dare`*:* gives you a dare
"""

TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)

OREKI_MOD.add_handler(TRUTH_HANDLER)
OREKI_MOD.add_handler(DARE_HANDLER)

__mod_name__ = "Games"
__command_list__ = [
   "truth",
   "dare",
]

__handlers__ = [
    TRUTH_HANDLER,
    DARE_HANDLER,
]
