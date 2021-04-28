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
    await message.reply_sticker("CAACAgQAAx0CVij2LgABECN1YHtruZ8lqFS_yvdqHwkUpjdPUwEAAiMNAALjHT4PZNM7QRBdiYwfBA")
    await message.reply_text(
        f"""Hello!! Aku Adalah Bot Musik Telegram Dengan Banyak Sekali Fitur!\n\n➥ Tolong Baca Manual Dibawah Agar Tau Cara Menggunakanku.\n\n➥ [Assistance](https://t.me/TokaiMusicAssistance) Juga Harus Berada Di Dalam Grup Kamu.\n\nProvided By @Insaynn 🇲🇨""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/musikalitassID"
                    ),
                    InlineKeyboardButton(
                        "Group", url="https://t.me/musikalitasID"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Instagram", url="https://instagram.com/sndykaa/"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Tokai Music Telah Online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/Insaynn"
                    ),
                    InlineKeyboardButton(
                        "Panduan", url="https://telegra.ph/Music-Bot-Command-04-15")
                ]
            ]
        )
   )

