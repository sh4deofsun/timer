from __future__ import barry_as_FLUFL
import time
import tkinter as tk
import random

from streamlit import stop

rootWindow = tk.Tk()
rootWindow.title("Timer")
# rootWindow.geometry("500x300")
rootWindow.resizable(width=False,height=False)

timerMin = tk.StringVar()
timerMin.set("00")
timerSec = tk.StringVar()
timerSec.set("00")
stopSign = tk.BooleanVar()
stopSign.set(True)

def timerStart():
    stopSign.set(True)
    totalSec = int(timerMin.get())*60 + int(timerSec.get())
    while(totalSec > -1 and stopSign.get()):
        tmpMin,tmpSec = divmod(totalSec,60)
        timerMin.set("{0:2d}".format(tmpMin))
        timerSec.set("{0:2d}".format(tmpSec))
        rootWindow.update()
        time.sleep(1)
        totalSec -= 1
        if(tmpSec==0 or totalSec==0):
            refreshAd()

def timerStop():
    stopSign.set(False)
    timerMin.set("{0:2d}".format(0))
    timerSec.set("{0:2d}".format(0))
    rootWindow.update()

def rndAds():
    adList = ["TDM is so cool tool!",
    "QAA is the best departmant!",
    "Batuhan is the best Tech-Support!",
    "Don't talk too much Nigar!",
    "Ahmet DAL is the best!",
    "Robot Framework v5.0 is out!",
    "Please update your Board",
    "Jenkins: This is how we do automation",
    "This is the way!",
    "Oh! You finally awake",
    "Batuhan not recommend to use RF v3.2.2",
    "Did you know? TDM built with Django",
    "Did you know what are these? BDD, KDD, DDD",
    "We have best Scrum master and her name is Esra",
    "This is the way I test it",
    "Hold my beer, I got this bug",
    "Coffee! You can sleep when you're dead!",
    "Let's talk about when we gonna do Happy Hour",
    "Happy hours is blesed times"]
    return random.choice(adList)

def refreshAd():
    lbl_ads["text"] = rndAds()
    lbl_ads.update()

# Clocks
frm_clock = tk.Frame(master=rootWindow)
ent_clockMin = tk.Entry(master=frm_clock,width=6,textvariable=timerMin,font=('Times New Roman', 40))
ent_clockMin.grid(row=0,column=0)
# timerMin = ent_clockMin.get()
ent_clockSec = tk.Entry(master=frm_clock,width=6,textvariable=timerSec,font=('Times New Roman', 40))
ent_clockSec.grid(row=0,column=1)
# timerSec = ent_clockSec.get()
# frm_clock.grid(row=0,column=0)
frm_clock.grid(row=0,column=0)

# Start - Stop buttons
frm_buttons = tk.Frame(master=rootWindow)
btn_start = tk.Button(master=frm_buttons,text="Start",command=timerStart)
btn_start.grid(row=0,column=0)
btn_stop = tk.Button(master=frm_buttons,text="Stop",command=timerStop)
btn_stop.grid(row=1,column=0)
frm_buttons.grid(row=0,column=1)

# Ads
frm_ads = tk.Frame(master=rootWindow,height=False)
# txt_ads = tk.Text(master=frm_ads,)
lbl_ads = tk.Label(master=frm_ads,text=rndAds())
lbl_ads.pack()
frm_ads.grid(row=1,column=0)


rootWindow.mainloop()