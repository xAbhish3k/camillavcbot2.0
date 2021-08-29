from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
      await message.reply_text(
        f"""**Hey, I'm {bn} 🎀
🤖 I am an advanced bot created for playing music in the voice chats of Telegram Groups & Channels. !**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔨Source Code🔨", url="https://github.com/War-Legend/camillavcbot2.0")
                  ],[
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ👿", url="https://t.me/warbotzsupport"
                    ),
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ", url="https://t.me/thewarbotz"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "➕ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ➕", url="https://t.me/camillamusicbot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Yes iᴍ online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊Uᴩᴅᴀᴛᴇs", url="https://t.me/thewarbotz")
                ]
            ]
        )
   )
