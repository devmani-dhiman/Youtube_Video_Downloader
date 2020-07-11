# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 13:56:19 2020

@author: user
"""

from pytube import YouTube



url = input("Enter the url of the video: ")


yt= YouTube(url)  ##Creating object of Youtube class



video= yt.streams.first()  ##Selecting the First streams from all the available streams


final= video.download(#address in string format)
##Downloading video with .download function to your preferred location
 
print('Done')