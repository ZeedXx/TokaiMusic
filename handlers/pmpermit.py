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




from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Halo, Aku Official Assistance Dari @HoneyMusic_bot.\n\n ❗️ Rules:\n   - No Chatting Allowed\n   - No Spam Allowed\n\n 👉 **KIRIM LINK ATAU USERNAME GRUP KAMU DISINI JIKA ASISTEN TIDAK JOIN.**\n\n ⚠️ **Perhatian**!: Jika Anda Mengirim Pesan di Sini Berarti Admin Akan Melihat Pesan Anda dan Akan Segera Bergabung Dengan Grup Obrolan Anda.\n   - Jangan Bagikan Info Pribadi Di Sini!!\n   - [Managed by](https://www.instagram.com/enjouecollectifxx) : @ZeedGoodBoys")
  return                        
