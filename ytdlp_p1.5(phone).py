# ติดตั้ง yt-dlp
!pip install -q yt-dlp

link = input("Link: ")

import yt_dlp
from google.colab import files

# ตั้งค่าการโหลด
ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s'  
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(link, download=True)  # ดึงข้อมูล + ดาวน์โหลด
    filename = ydl.prepare_filename(info)         # สร้างชื่อไฟล์จาก info

print("Download complete!")


files.download(filename) # โหลดไฟล์ลงมือถือ
