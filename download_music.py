#!/usr/bin/env python

import yt_dlp

links = 'https://www.youtube.com/watch?v=69lO08ar-mI'

def get_video_title(ydl, url):
    info_dict = ydl.extract_info(url, download=False)
    return info_dict.get('title', None)

ydl_opts = {
    'writesubtitles': False,
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',  # Calidad del audio MP3 (ajusta según sea necesario).
    }],
    'outtmpl': '/home/luis/Desktop/%(title)s.%(ext)s',  # Incluye el título y la extensión en el nombre del archivo.
    'get-filename': get_video_title,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([links])