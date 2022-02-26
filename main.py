import tkinter
from tuyadevices import *
import tinytuya
import time

window=tkinter.Tk()
window.title("Glove Companion Window")
window.configure(width=500, height=300)
window.configure(bg='lightgray')

#Bedroom Light is br and Living Room Light is lr

#Begin Main Code

lrStatus = lr.status()

def lrLightSwitch():
    if lrStatus['dps']['1']==True:
        lr.turn_off(switch=1)
    else:
        lr.turn_on(switch=1)

#window.geometry("200x100")
button = tkinter.Button(window,text = "haley rocks", command=lrLightSwitch)
button.pack()

T = tkinter.Text()
T.pack()

while True:
    lrStatus = lr.status()
    window.update()
    #lrLightSwitch()
