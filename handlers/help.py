from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("help") & filters.group & ~filters.channel)
async def start(_, message: Message):
      await message.reply_text("""_Perintah Untuk Semua Member_ :
┈──────────────────────┈
× /play <Judul>  : _Memutar Lagu Melalui Youtube._
× /dplay <Judul> : _Memutar Lagu Melalui Deezer._
× /reply <Link>  : _Memutar lagu lewat reply link YouTube atau file audio._
× /playlist : _Untuk Menampilkan Daftar Putar Lagu._
× /song <Judul>  : _Untuk Mendownload Lagu di YouTube._
× /vsong <Judul> : _Mendownload Video dari YouTube._
× /deezer <Judul> : _Mendownload Lagu Dari Deezer._
× /saavn <Judul>  : _Mendownload Lagu Dari Saavn._
× /search <Judul> : _Mencari Video di YouTube Secara Detail._
× /current : _Mengecek Antrian di Grup Kamu._
× /player  : _Mengelola Bot di Grup Kamu._

_Perintah Untuk Admin Group_ :
┈──────────────────────┈
× /pause  : _Menjeda Lagu._
× /resume : _Melanjutkan Lagu Yang Dipause._
× /skip : _Menloncati Lagu ke Lagu Berikutnya._
× /end  : _Memberhentikan Lagu._
× /joingroup  : _Mengundang Asisten ke VCG._
× /leavegroup : _Menendang Asisten Music dari VCG._
× /adminreset : _Memperbarui Admin List._
× /admincache : _Me-Refresh Cache Admin Pada Bot._""")
