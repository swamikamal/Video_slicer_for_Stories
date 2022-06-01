from moviepy.editor import VideoFileClip
from tkinter import *
from tkinter import messagebox as box
import math 
import sys

# declaring path to the file/video in your machine 
path = r"F:\movie\Omerta 2018 Hindi 720p WEBRip x264 AAC - LOKiHD - Telly\Omerta 2018 Hindi 720p WEBRip x264 AAC - LOKiHD - Telly.mkv"
path = (input("PLEASE ENTER YOUR PATH WITH OUT (' ,"'""'", '' ,' ) \nENTER MOVIE PATH: ")) 
print("WELCOME TO THE ViDEO SPlITER BY KAMAL")
#print("please dont enter zero as prefix in time")
movie_finnal_start_hrs=int(input("ENTER STARTING HRS: "))
movie_finnal_start_min=int(input("ENTER STARTING MIN: "))
movie_finnal_start_sec=int(input("ENTER STARTING SEC: "))
#start=movie_finnal_start_min,movie_finnal_start_sec
# to calculate time

movie_finnal_end_hrs=int(input("ENTER ENDING HRS: "))
movie_finnal_end_min=int(input("ENTER ENDING MIN: "))
movie_finnal_end_sec=int(input("ENTER ENDING SEC: "))
#end=movie_finnal_end_hrs,movie_finnal_end_min,movie_finnal_end_sec





#super starting
sstart=(((movie_finnal_start_hrs*60)*60)+movie_finnal_start_min*60+movie_finnal_start_sec)
send=(((movie_finnal_end_hrs*60)*60)+movie_finnal_end_min*60+movie_finnal_end_sec)
# error box
if sstart==send or sstart>send:
    sys.exit(box.showerror("Wrong selection","PLEASE ENTER CORRECT STARTING AND ENDING TIME"))


# time frame
def frameasker():
    timeframe=int(input("ENTER THE DURATION OF TRIMED ClIP in sec: "))    
    return timeframe
timeframe=(frameasker())


if timeframe==send or timeframe>send:
     box.showerror("frame time selection"," TIME FRAME IS GREATeR then whole video \n PLEASE ENTER CORRECT frame TIME")
     timeframe=(frameasker())
# opening the file and storing it in 'file' variable
file = VideoFileClip(path)
turns=((send)/timeframe)

#return noramilse and finnal value of turns
#nutraler
def fllr(turns):
    turns=math.floor(turns)
    return(turns)

def cel(turns):
    turns=math.ceil(turns)
    return(turns)

def turner(turns):
    if turns>round(turns):
        return fllr(turns)
    else:
        return cel(turns)

auto_turn=turner(turns)
print("POSSIBLE SPLItING Turns for video is ,",auto_turn)
def tur(auto_turn):
    turns=(int (input("HOW MANY TuRNS YOU WANt from that clip \n if you want to trim whole video then Enter 0 as input:  ")))
    if turns==0:
        turns=auto_turn
        return turns
    elif turns>auto_turn:
        box.showerror("Wrong turn selection","turns are greater then possible turns \n PLEASE ENTER CORRECT STARTING AND ENDING TIME")
        tur(auto_turn)
        

    else:
        turns=turner(turns)
        return turns
turns=tur(auto_turn)


save=str(input("PLEASE ENTER YOUR PATH WITH OUT (' ,"'""'", '' ,' ) \nEnter THE PATH WHERE TO SAVE TRIMMED FILE: "))

snext=sstart+timeframe    
for i in range (turns):
    print(sstart,snext)
    #making a trimmed clip of original video    
    new = file.subclip(t_start=(sstart), t_end=(snext))
    # exporting the trimmed video to desired path 
    new.write_videofile(save+"\%d.mp4"%i)
    sstart=snext
    snext=timeframe+sstart

print("THANKS FOR USING HIS SOFTWARE \n | KAMAL SWAMI |")
