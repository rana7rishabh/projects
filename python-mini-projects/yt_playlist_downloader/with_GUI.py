from tkinter import *
from pytubefix import Playlist
def submit():
    p=entry.get()
    plist=Playlist(p)

    for video in plist.videos:
        video.streams.first().download()

window=Tk()
entry=Entry(window
            ,font=("Inter",24))
button=Button(window,
              text="submit",font=("Inter",24),bg="red",
              command=submit)
button.pack(side=RIGHT)
entry.pack(side=LEFT)
window.mainloop()