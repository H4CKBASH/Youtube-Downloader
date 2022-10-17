import youtube_dl
from pytube import YouTube


class Download(object):
    # def __init__(self, path, url, quality, playlist = False):
    def __init__(self, path, url, quality):
        self.url = url
        self.qualities = {
            "Best": "1400",
            "Semi": "320",
            "Worst": "180"
        }
        self.quality = self.qualities[quality]
        # self.playlist = playlist
        self.path = path
        
    def download_mp3(self):
        opts = {
            'format': 'bestaudio/best',
            'fixup': 'detect_or_warn',
            'verbose': False,
            'extract-audio': 'mp3',
            'outtmpl': self.path + '\\%(title)s.%(ext)s',
            'postprocessors': [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3"
            }]
        }
        try:
            Download_obj = youtube_dl.YoutubeDL(opts)
            Download_obj.download([self.url])
        except:
            print("\nCheck FFmpeg Installation!!!")

    def download_mp4(self):
        link = self.url
        video = YouTube(link)
        download = video.streams.get_highest_resolution()
        download.download()
