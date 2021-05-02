from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("help") & filters.private & ~filters.channel)
async def start(_, message: Message):
      await message.reply_text("""• Berikut Adalah Perintah Untuk Member Group :

/play <Judul Lagu>  - Untuk Memutar Lagu Yang Anda Minta Melalui Youtube.
/dplay <Judul Lagu>  - Untuk Memutar Lagu Yang Anda Minta Melalui Deezer.
/plays <Link Youtube / Direct> - Untuk Memutar lagu lewat link YouTube atau Lagu biasa (Sudah di Download)
/playlist - Untuk Menampilkan Daftar Putar Lagu.
/song <Judul Lagu> - Untuk Mendownload Lagu di YouTube.
/video atau /vsong <Judul Lagu> - Untuk Mendownload Video di YouTube Secara Detail.
/deezer <Judul Lagu> - Untuk Mendownload Lagu Dari Deezer.
/saavn <Judul Lagu> - Untuk Mendownload Lagu Dari Website Saavn.
/search <Judul Lagu> - Untuk Mencari Video di YouTube Secara Detail.
/current - Untuk Mengecek Antrian dan Juga Siapa yang Me-Request Lagu Tersebut.
/player - Untuk Memudahkan Anda Dalam Mengelola Robot.


• Berikut Adalah Perintah Untuk Admin Group :

/pause - Untuk Menjeda Pemutaran Lagu.
/resume - Untuk Melanjutkan Pemutaran Lagu Yang Telah Dipause.
/skip - Untuk Menloncati Pemutaran Lagu ke Lagu Berikutnya.
/end - Untuk Memberhentikan Pemutaran Lagu.
/joingroup - Untuk Mengundang Asisten Music ke Obrolan Suara.
/leavegroup - Untuk Menendang Asisten Music dari Obrolan Suara.
/adminreset - Untuk Memperbarui Admin List.
/admincache - Untuk Me-Refresh Cache Admin Pada Robot.""")
