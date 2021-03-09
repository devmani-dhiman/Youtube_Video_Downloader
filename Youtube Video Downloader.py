from tkinter import *
from pytube import YouTube

## Creating Display

display = Tk()
display.geometry('500x300')
display.resizable(0, 0)
display.title("Youtube Video Downloader")

## Labeling the input Box
Label(display,text = 'Youtube Video Downloader', font='Times 18 bold').pack()

link = StringVar()

Label(display, text = 'Paste Link Here:', font = 'Times 15 bold').place(x= 160 , y = 60)
link_enter = Entry(display, width = 70,textvariable = link).place(x = 32, y = 90)

##Downloading Video
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.get_by_resolution("720p")
    video.download()
    Label(display, text = 'DOWNLOADED', font = 'Times 15').place(x= 180 , y = 210)  

Button(display,text = 'DOWNLOAD', font = 'Times 15 bold' ,bg = 'violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

display.mainloop()
