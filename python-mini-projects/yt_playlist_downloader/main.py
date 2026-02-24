from pytubefix import Playlist

p=input("enter the url of the playlist: ")

plist=Playlist(p)

for video in plist.videos:
    video.streams.first().download()