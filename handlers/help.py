from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("help") & filters.group & ~filters.channel)
async def start(_, message: Message):
      await message.reply_text("""_^Perintah Untuk Semua Member__ :
┈──────────────────────┈
× /play <Judul>  : __Memutar Lagu Melalui Youtube.__
× /dplay <Judul> : __Memutar Lagu Melalui Deezer.__
× /reply <Link>  : __Memutar Lagu Lewat Reply Link YouTube atau File Audio.__
× /playlist : __Untuk Menampilkan Daftar Putar Lagu.__
× /song <Judul>  : __Untuk Mendownload Lagu di YouTube.__
× /vsong <Judul> : __Mendownload Video dari YouTube.__
× /deezer <Judul> : __Mendownload Lagu Dari Deezer.__
× /saavn <Judul>  : __Mendownload Lagu Dari Saavn.__
× /search <Judul> : __Mencari Video di YouTube Secara Detail.__
× /current : __Mengecek Antrian di Grup Kamu.__
× /player  : __Mengelola Bot di Grup Kamu.__

__Perintah Untuk Admin Group__ :
┈──────────────────────┈
× /pause  : __Menjeda Lagu.__
× /resume : __Melanjutkan Lagu Yang Dipause.__
× /skip : __Menloncati Lagu ke Lagu Berikutnya.__
× /end  : __Memberhentikan Lagu.__
× /joingroup  : __Mengundang Asisten ke VCG.__
× /leavegroup : __Menendang Asisten Music dari VCG.__
× /adminreset : __Memperbarui Admin List.__
× /admincache : __Me-Refresh Cache Admin Pada Bot.__
• Dikelola Oleh [Honey Music](https://www.instagram.com/enjouecollectifxx)""")
