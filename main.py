import tkinter
import tinytuya
import time


from tuyadevices import *
from funkylights import *

brChangingBrightness=False

def brAdjustBrightnessOn():
    global brChangingBrightness
    brChangingBrightness=not brChangingBrightness

def brAdjustBrightnessOff():
    global brChangingBrightness
    brChangingBrightness=False

#-----------------------------Here the window and its properties are defined-----------------------
window=tkinter.Tk()
window.title("Glove Companion Window")
window.configure(width=500, height=300)
window.configure(bg='lightgray')

window.geometry("800x500")

button = tkinter.Button(window,text = "Light Switch", command=brLightSwitch)
button.pack()

button2 = tkinter.Button(window,text = "Switch White/Color", command=brSwitchMode)
button2.pack()

button3 = tkinter.Button(window,text = "Enter Adjust Brightness", command=brAdjustBrightnessOn)
button3.pack()

button4 = tkinter.Button(window,text = "Exit Adjust Brightness", command=brAdjustBrightnessOff)
button4.pack()

r = tkinter.StringVar()
r.set('')

brightness_entry = tkinter.Entry(window, width=6, textvariable=r)
brightness_entry.pack()

#-----------------------------------------Begin Main Code loop----------------------------------------
while True:
    try:
        testInt = int(r.get())
    except:
        window.update()
    else:
        if brChangingBrightness==True and 0<int(r.get())<101:
            rInt=int(r.get())
            br.set_brightness_percentage(brightness=rInt)

    window.update()
