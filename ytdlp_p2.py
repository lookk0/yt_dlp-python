import yt_dlp

link = input("put link: ")
mode = input("inputmode [audio,video,both]: ").lower()
folder = r"\%(title)s.%(ext)s"
Issub = False
lang = None
Ismerge = False

if mode in ['audio','a','au','aud']:
    mode = 'bestaudio'
elif mode in ['video','vid','vi','v']:
    mode = 'bestvideo'
else:
    mode = 'bestvideo+bestaudio/best'

sub = input("Do u want sub? [y/n]: ").lower()
if sub in ['yes','ye','y']:
    Issub = True
    lang = input("which language do u want? [th,eng,both]: ").lower()
    if lang in ['th','tha','thai','t']:
        lang = 'th'
    elif lang in ['e','en','eng']:
        lang = 'en'
    else:
        lang = 'all'
    merge = input('Do u want to merge sub into vid? [y/n]: ').lower()
    if merge in ['yes','ye','y']:
        Ismerge = True
    else:
        Ismerge = False
else:
    Issub = False


ydl_opts = {
    'format': mode,
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4', 
    }],
    'write_subtitles': Issub, # เพิ่มซับอัตโนมัติจาก yt ไหม
    'writeautomaticsub': Issub, # เพิ่มซับอัตโนมัติจากเจ้าของ ไหม
    'subtitleslangs': [lang],  # ซับภาษาอะไร หรือ ['all'] เพื่อโหลดทุกภาษา
    'embedsubtitles': Ismerge, # รวมซับในคริปไหม
    'outtmpl': folder,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
    print("done dowload")
    
