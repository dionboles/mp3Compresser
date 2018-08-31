import os 
if os.path.isdir("mp3Compress") is False:
    os.mkdir("mp3Compress")
    os.chdir("mp3Compress")
else:
    os.chdir("mp3Compress")

if os.path.isdir(".") is True:
   for i in os.listdir('.'):
       extension = os.path.splitext(i)[1][1:]
       print(extension)
       if extension == "mp3":
           name = str(os.path.splitext(i)[0]+"_compress");
           print(name)
           os.system("ffmpeg -i "+i+"  -acodec libmp3lame -ac 2 -ab 64k -ar 44100  "+name+".mp3");
