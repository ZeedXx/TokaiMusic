# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgIAAxkBAAEKL_1gt842-B5SnR5eHrlBsfTviEt2GwACrAsAAt_YUUnNC_qAE0qWKR8E")
    await message.reply_text(
        f"""__Hello!! Aku Adalah__ **HoneyMusic**!!\n__Aku di Rancang Untuk Mengunduh Maupun Memutar Musik di Obrolan Suara Grup Telegram.\n┈──────────────────────┈\n➠ __Invite__ [Assistance](https://t.me/HoneyAssistant) __Masuk ke Dalam Grup Anda__\n➠ __Untuk Info, Update, dan Panduan Selengkapnya Tekan Tombol Channel di Bawah, Terima kasih! Have Fun!!__""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                     InlineKeyboardButton(
                                text="➕️ Tambah Aku Kedalam Group ➕️", url="t.me/HoneyMusic_bot?startgroup=true"),
                ],
                [
                     InlineKeyboardButton(text="Channel", url=f"https://t.me/ZeedGoodBoys"),
                     InlineKeyboardButton(text="Group", url=f"https://t.me/AmazonVirtual"),
                ],
                [
                     InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/enjouecollectifxx"),
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Honey Music** __Telah Online, Tekan Tombol di Bawah Untuk Melihat Panduan!!__""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group", url="https://t.me/AmazonVirtual"),
                    InlineKeyboardButton(
                        "Panduan 📜", url="https://t.me/ZeedGoodBoys/14")
                ]
            ]
        )
   )

