import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import OrekiRobot.modules.movies.movie_strings.py as movie_strings
from OrekiRobot.modules.helper_funcs.chat_status import (is_user_admin)
from OrekiRobot.modules.helper_funcs.extraction import extract_user



@run_async
def thunivu(update: Update, context: CallbackContext):
    update.effective_message.reply_text(movie_strings.THUNIVU_STRINGS)
