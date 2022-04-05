import time
import tkinter as tk

def timerStart():

    timerMin = ent_clockMin.get()
    timerSec = ent_clockSec.get()
    print(f"{timerMin} : {timerSec}")
    btn_start.configure()

def timerStop():
    ent_clockMin.delete()
    ent_clockMin.insert(0,"00")
    ent_clockSec.delete()
    ent_clockSec.insert(0,"00")

rootWindow = tk.Tk()
rootWindow.title("Timer")
# rootWindow.geometry("300x200")
rootWindow.resizable(width=False,height=False)

# Clocks
frm_clock = tk.Frame(master=rootWindow)
ent_clockMin = tk.Entry(master=frm_clock,width=6,textvariable=tk.StringVar(master=frm_clock,value="03"))
ent_clockMin.grid(row=0,column=0)
# timerMin = ent_clockMin.get()
ent_clockSec = tk.Entry(master=frm_clock,width=6,textvariable=tk.StringVar(master=frm_clock,value="00"))
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




rootWindow.mainloop()