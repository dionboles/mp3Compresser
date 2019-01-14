#!/usr/local/bin/python
# This Python file uses the following encoding: utf-8
import os,sys,shutil

if os.path.isdir("mp3Compress") is False:
    print("Making folder")
    os.mkdir("mp3Compress")
    print("Moving to folder")
else:
    print("Folder already created")
    print("Moving to folder")
   
def getText(s):
    return os.path.splitext(s)[1]

for root, dirs, files in os.walk("."):
    for name in files:
        file_extension = str(os.path.splitext(name)[1])
        if os.path.isfile(name) is True:
            if file_extension == ".mp3":
                newName =str(os.path.splitext(name)[0]+"_compress");
                os.system("ffmpeg -i "+name+"  -acodec libmp3lame -ac 2 -ab 64k -ar 44100  "+newName+".mp3");
                shutil.copy2("./"+newName+".mp3","./mp3Compress/"+newName+".mp3")
                os.remove(newName+".mp3");