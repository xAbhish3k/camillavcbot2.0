from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/37589911c048164588393.jpg")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎀
I Cᴀɴ Pʟᴀʏ Mᴜsɪᴄ Iɴ Yᴏᴜʀ Sᴇxʏ Gʀᴏᴜᴩ Vᴏɪᴄᴇ Cʜᴀᴛ. Dᴇᴠᴇʟᴏᴩᴇᴅ Bʏ [Bʟᴀᴢᴇ•Oᴩ](https://t.me/piroXpower).
Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴩ Aɴᴅ Pʟᴀʏ Mᴜsɪᴄ Fʀᴇᴇʟʏ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Oᴡɴᴇʀ😘", url="t.me/piroXpower")
                  ],[
                    InlineKeyboardButton(
                        "Sᴜᴩᴩᴏʀᴛ👿", url="https://t.me/patricia_Support"
                    ),
                    InlineKeyboardButton(
                        "Cʜᴀɴɴᴇʟ", url="https://t.me/patricia_updates"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Gʀᴏᴜᴩ Mᴇ ᴅᴀʟᴅᴏ➕", url="https://t.me/BITTU_MUSICBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Aᴍ Oɴʟɪɴᴇ ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊Uᴩᴅᴀᴛᴇs", url="https://t.me/patricia_updates")
                ]
            ]
        )
   )
