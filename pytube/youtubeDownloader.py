from pytube import YouTube
from pytube import Playlist
import urllib.request
import re
from collections import OrderedDict

contents = urllib.request.urlopen("https://www.youtube.com/playlist?list=PLCzY05S6TohrOKp_hCvCDKg2m_-GsG5ct").read().decode("utf-8")

pattern = re.compile(r'{"videoId":"([^\"]+)"')
# re.match( r'{"videoId":"([^\"]+)"', contents)
result1 = pattern.findall(contents)
res = list(OrderedDict.fromkeys(result1))

for url in res:
    print("start download:", 'https://youtube.com/watch?v='+url)
    obj = YouTube('https://youtube.com/watch?v='+url)
    obj1080p = obj.streams.filter(res='1080p').first();
    print(obj1080p)
    obj1080p.download("C:/self/mp4")
    # YouTube('https://youtube.com/watch?v='+url).streams.first().download("C:/self/mp4")
# pl = Playlist("https://www.youtube.com/watch?v=Edpy1szoG80&list=PL153hDY-y1E00uQtCVCVC8xJ25TYX8yPU")
# print(pl)
# for video in pl.videos:
#     video.streams.first().download()
# lists = pl.videos
# print(pl)
# print(lists)
# print("===")
# for url in lists:
#     print(url)
# y = YouTube('https://youtu.be/9bZkp7q19f0').streams.first()
# y.download()
