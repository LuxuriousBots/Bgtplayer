from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Bikash import config
from Bikash import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="» ᴄᴏᴍᴍᴀɴᴅs «",
                url=f"https://t.me/{BOT_USERNAME}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙ Bot settings ⚙", callback_data="settings_helper"
            )
        ],
        [           
            InlineKeyboardButton(
                text="» ʏᴏᴜᴛᴜʙᴇ «", url=f"https://youtube.com/@LuxuriousNetwork?si=YfF9vtMSWYNy3MY2"
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="« ᴀᴅᴅ ʏᴏᴜʀ ɢʀᴏᴜᴘ »",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="« ʜᴇʟᴘ »", callback_data="settings_back_helper"
            )
        ],
        [           
            InlineKeyboardButton(
                text="» ʏᴏᴜᴛᴜʙᴇ «", url=f"https://youtube.com/@LuxuriousNetwork?si=YfF9vtMSWYNy3MY2"
            )
        ],
        [
            InlineKeyboardButton(
                text="♕ Owner ♕", user_id=OWNER
            )
        ]
     ]
    return buttons
