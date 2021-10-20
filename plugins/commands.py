import os
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
from script import Script
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    await update.reply_text(
        text=Script.START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=Script.START_BUTTONS
    )


@Client.on_message(filters.command(["help"]) & filters.private)
async def help(bot, update):
    await update.reply_text(
        text=Script.HELP_TEXT,
        disable_web_page_preview=True,
        reply_markup=Script.HELP_BUTTONS
    )

@Client.on_message(filters.command(["about"]) & filters.private)
async def about(bot, update):
    await update.reply_text(
        text=Script.ABOUT_TEXT,
        disable_web_page_preview=True,
        reply_markup=Script.ABOUT_BUTTONS
    )

