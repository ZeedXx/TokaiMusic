# Calls Music 1 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest

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

from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice

from callsmusic import callsmusic, queues

import converter
from downloaders import youtube

from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.filters import command, other_filters
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(command("reply") & other_filters)
@errors
async def play(_, message: Message):

    lel = await message.reply("🔄 **Sedang Proses**...")
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
            [
                [
                   InlineKeyboardButton(
                       text="Manual",
                       url='https://telegra.ph/Music-Bot-Command-04-15')
                
                ],                     
                [
                    InlineKeyboardButton(
                        text="Channel",
                        url='https://t.me/TokaiMusik')
                   
                ]
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 240) > DURATION_LIMIT:
            raise DurationLimitError(
                f"❌ Video Dengan Durasi Melebihi {DURATION_LIMIT} minute(s) Tidak Diizinkan Untuk Diputar!"
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await lel.edit_text("Anda Tidak Memberi Saya Apapun Untuk Dimainkan, Silahkan Reply direct!")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await lel.edit(f"#⃣ Lagu Request Kamu **Queued** Di Posisi {position}!")
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_photo(
        photo="https://telegra.ph/file/d1adb5378a94e1a9a4daa.jpg",
        reply_markup=keyboard,
        caption = f"🏷 **Judul:** 404 Not Found\n🤖 **Player:** Tokai Music\n" \
               + f"🎧 **Request Dari:** {message.from_user.mention}"
        ),
        return await lel.delete()
