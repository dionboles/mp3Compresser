#!/usr/local/bin/python
# This Python file uses the following encoding: utf-8
import os,sys,shutil,subprocess,threading,time,random

if os.path.isdir("mp4Compress") is False:
    print("Making folder")
    os.mkdir("mp4Compress")
    print("Moving to folder")
else:
    print("Folder already created")
    print("Moving to folder")
   
def getText(s):
    return os.path.splitext(s)[1]


def compress(name,wait_time):
    time.sleep(wait_time)
    file_extension = str(os.path.splitext(name)[1])
    if os.path.isfile(name) is True:
        if file_extension == ".mp4":
            newName =str(os.path.splitext(name)[0]+"_compress");
            if os.path.isfile("./mp4Compress/"+newName+".mp4") is False:
                child = subprocess.Popen("ffmpeg -i "+name+"  -crf 20  "+newName+".mp4 -y",shell=True).wait() 
                if child is not None:
                    print("Starting move")
                    shutil.copy2("./"+newName+".mp4","./mp4Compress/"+name+".mp4")
                    os.remove(newName+".mp4");
            else:
                print("File {} already compressed".format(name))
for root, dirs, files in os.walk("."):
    for name in files:
        thredName = "test"+str(len(name))
        thredName = threading.Thread(target=compress,args=[name,random.randint(0,5)])
        thredName.start()
        
