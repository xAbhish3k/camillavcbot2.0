from pyrogram import Client, filters
from pyrogram.types import Message



@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""Cᴏᴍᴍᴀɴᴅs ᴏғ Bᴇsᴛɪᴇs Vᴄ Bᴏᴛ 🔥🛠
**For all in group**

Commands of Besties Vc Bot 🔥🛠

- /play <song name> - play song you requested 

- /song <song name> - download songs you want quickly 

**Admins only✅**


-  /pause - pause song play

- /resume - resume song play

- /skip - play the next song

- /end - stop music play


