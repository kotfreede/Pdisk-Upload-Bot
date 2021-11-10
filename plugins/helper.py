# (c) HeimanPictures
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



START = """
𝗛𝗜 {}!
        
 𝗜 𝗔𝗠 𝗔 𝗣𝗗𝗜𝗦𝗞 𝗨𝗣𝗟𝗢𝗔𝗗𝗘𝗥 𝗕𝗢𝗧 𝘃𝟮  ©@KOT_BOTS😇
𝗥𝗘𝗔𝗗 /help 𝗖𝗮𝗿𝗲𝗳𝘂𝗹𝗹𝘆 & 𝗗𝗼 𝗙𝗼𝗹𝗹𝗼𝘄 𝗔𝗹𝗹 𝗚𝗶𝘃𝗲𝗻 𝗜𝗻𝘀𝘁𝗿𝘂𝗰𝘁𝗶𝗼𝗻𝘀...

𝗙𝗢𝗥 𝗠𝗢𝗥𝗘 𝗕𝗢𝗧𝗦 𝗝𝗢𝗜𝗡 : @KOT_BOTS 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 : @KOT_REPORS
"""

HELP = """
**Send Me Direct Download Link Like Mirror.

Send As This Format**

`link | Title`

**Or**

`Video link | Title | Thumbnail link`

**NOTE:
➢ Do Not Spam, Send Link One By One
➢ To Know Status Just Go To cofilink.com/home**
"""

# NON_OWNER = "You Can't Use Me Ask My [Owner](tg://user?id={})"


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📮 Update 📮', url='https://telegram.dog/KOT_BOTS/'),
        InlineKeyboardButton('🛠️ Support 🛠️', url='https://telegram.dog/KOT_REPORS/'),
        ],[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )



@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=START.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )


@Client.on_message(filters.command('help') & filters.private)
async def help(bot, message):
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=HELP,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )


@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    else:
        await update.message.delete()
