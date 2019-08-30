#!/usr/local/bin/python
# This Python file uses the following encoding: utf-8
import os,sys,shutil

if os.path.isdir("mp4Compress") is False:
    print("Making folder")
    os.mkdir("mp4Compress")
    print("Moving to folder")
else:
    print("Folder already created")
    print("Moving to folder")
   
def getText(s):
    return os.path.splitext(s)[1]
#video files are in the same dir as the python file 
for root, dirs, files in os.walk("."):
    for name in files:
        file_extension = str(os.path.splitext(name)[1])
        if os.path.isfile(name) is True:
            if file_extension == ".mp4":
                newName =str(os.path.splitext(name)[0]+"_compress");
                if os.path.isfile("./mp4Compress/"+newName+".mp4") is False:
                    os.system("ffmpeg -i "+name+"  -crf 20  "+newName+".mp4");
                    shutil.copy2("./"+newName+".mp4","./mp4Compress/"+newName+".mp4")
                    os.remove(newName+".mp4");
                else:
                    print("File {} already compressed".format(name))
