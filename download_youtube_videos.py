from pytube import YouTube

url = 'https://www.youtube.com/watch?v=nq4Klb3zzS4&list=LL&index=7'
my_video = YouTube(url)
my_video = my_video.streams.get_highest_resolution()
my_video.download()