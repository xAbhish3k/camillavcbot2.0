from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAItmWD3OC0m03OLIcpSzfiJMCDxm4xJAAKFAwACH8C5V-U9VextES_XIAQ")
    await message.reply_text(
        f"""**Hey, में 𝗖𝗿𝗲𝗽𝗮𝗻 हूं 👨‍💻
में आपके ɢʀᴏᴜᴩ में ᴍᴜsɪᴄ चला सकता हूं ।
मुझे आपके ɢʀᴏᴜᴩ में ᴀᴅᴅ करके ॲडमीन बनाये और साथ ही साथ @CrepanAssistant को आपके ɢʀᴏᴜᴩ में ᴀᴅᴅ करें और अपने मनपसंद गाने चलाकर मज़े ले 😊 
Pᴏᴡᴇʀᴇᴅ ʙʏ : [𝗖𝗥𝗘𝗔𝗧𝗢𝗥 𝗣𝗔𝗩𝗔𝗡](https://t.me/crepan) !**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👨‍💻 𝗢𝗪𝗡𝗘𝗥 👨‍💻", url="https://t.me/crepan")
                  ],[
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ", url="https://t.me/crepansupport"
                    ),
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ", url="https://t.me/crepansupport"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "➕ɢʀᴏᴜᴩ में ᴀᴅᴅ करें➕", url="https://t.me/crepanMusicbot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**online ही हूं 😄**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👨‍💻 𝗢𝗪𝗡𝗘𝗥 👨‍💻", url="https://t.me/crepan")
                ]
            ]
        )
   )
