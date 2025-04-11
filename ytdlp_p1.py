import yt_dlp

link = input("put link: ")

folder = r"\%(title)s.%(ext)s"

ydl_opts = {
    'format': 'best',
    'outtmpl': folder
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
    print("done dowload")
    