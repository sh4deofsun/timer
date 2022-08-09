import time
import random
import tkinter as tk

rootWindow = tk.Tk()
rootWindow.title("Timer")
rootWindow.resizable(width=False,height=False)
rootWindow.attributes('-topmost', True)
rootWindow.focus()

timerMin = tk.StringVar()
timerMin.set("03")
timerSec = tk.StringVar()
timerSec.set("00")

stopSign = tk.BooleanVar()
stopSign.set(True)

timerLastMin = tk.StringVar()
timerLastSec = tk.StringVar()

def timerStart():
    stopSign.set(True)
    totalSec = int(timerMin.get())*60 + int(timerSec.get())
    timerLastMin.set(timerMin.get())
    timerLastSec.set(timerSec.get())
    while(totalSec > -1 and stopSign.get()):
        tmpMin,tmpSec = divmod(totalSec,60)
        timerMin.set("{0:2d}".format(tmpMin))
        timerSec.set("{0:2d}".format(tmpSec))
        rootWindow.update()
        time.sleep(1)
        totalSec -= 1
        if(tmpSec==0):
            refreshAd()

def timerStop():
    stopSign.set(False)
    timerMin.set("{0:2d}".format(0))
    timerSec.set("{0:2d}".format(0))
    rootWindow.update()

def timerReset():
    timerStop()
    timerMin.set("{0:2d}".format(int(timerLastMin.get())))
    timerSec.set("{0:2d}".format(int(timerLastSec.get())))
    rootWindow.update()

def rndAds():
    adList = ["TDM is so cool tool!",
    "QAA is the best departmant!",
    "Please update your Board",
    "Jenkins: This is how we do automation",
    "This is the way!",
    "Oh! You finally awake",
    "Did you know? TDM built with Django",
    "Did you know what are these? BDD, KDD, DDD",
    "This is the way I test it",
    "Hold my beer, I got this bug",
    "Coffee! You can sleep when you're dead!",
    "Let's talk about when we gonna do Happy Hour",
    "Happy hours is blesed times",
    "A QA Tester has no name",
    "If they don't fix their bug, Initiate Order 66",
    '"I think therefore I am." -Rene Descartes',
    '"Knowledge is power." -Sir Francis Bacon',
    "May the Force be with you.",
    '"Not all those who wander are lost." -J. R. R. Tolkein',
    '"You must be the change you wish to see in the world." -Mahatma Ghandi',
    '"I like criticism. It makes you strong." —LeBron James',
    '"There are no mistakes, only opportunities." —Tina Fey',
    '"Make each day your masterpiece." -John Wooden']
    return random.choice(adList)

def refreshAd():
    lbl_ads["text"] = rndAds()

# Clocks
frm_clock = tk.Frame(master=rootWindow)
ent_clockMin = tk.Entry(master=frm_clock,width=4,textvariable=timerMin,font=('Times New Roman', 65))
ent_clockMin.grid(row=0,column=0)
ent_clockSec = tk.Entry(master=frm_clock,width=4,textvariable=timerSec,font=('Times New Roman', 65))
ent_clockSec.grid(row=0,column=1)
frm_clock.grid(row=0,column=0)

# Start - Stop buttons
frm_buttons = tk.Frame(master=rootWindow)
btn_start = tk.Button(master=frm_buttons,text="Start",command=timerStart)
btn_start.grid(row=0,column=0,sticky="nsew")
btn_stop = tk.Button(master=frm_buttons,text="Stop",command=timerStop)
btn_stop.grid(row=1,column=0,sticky="nsew")
btn_reset = tk.Button(master=frm_buttons,text="Reset",command=timerReset)
btn_reset.grid(row=2,column=0,sticky="nsew")
frm_buttons.grid(row=0,column=1)

# Ads
frm_ads = tk.Frame(master=rootWindow,height=False,width=5)
lbl_ads = tk.Label(master=frm_ads,text=rndAds(),font=('Times New Roman', 15))
lbl_ads.pack()
frm_ads.grid(row=1,column=0)

# Members
MemberList = ["Member 1Member",
            "Member 2Member",
            "Member 3Member",
            "Member 4Member",
            "Member 5Member",
            "Member 6Member",
            "Member 7Member",
            "Me ber 8Member",
            "AMember 9Member",
            "Member 10Member",
            "Member 11Member",
            "Member 12Member",
            ]

frm_members = tk.Frame(master=rootWindow)
for number, member in enumerate(sorted(MemberList)):
    cbx_member = tk.Checkbutton(master=frm_members,text=member)
    cbx_member.grid(row=int(number/2),column=(number%2),sticky=tk.NSEW)

frm_members.grid(row=2,column=0)

rootWindow.mainloop()