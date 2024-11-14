from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=R3GfuzLMPkA"
options = {
    'format': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',  # Best 4K or lower
    'outtmpl': 'E:\Codeing\Python Language\Projects\Project_22_4K_Videos/4kfile.%(ext)s',
}

with YoutubeDL(options) as ydl:
    ydl.download([url])

