import tkinter
import tinytuya
import time

from tuyadevices import *



#----------------------Declaring Global Variables Here--------------------
#Bedroom Light is br and Living Room Light is lr
#Put brStatus = br.status() at beginning of each function to update status of light



#----------------------Arduino Functions go Here--------------------------

def readGesture():
    return 0
#----------------------List of Functions----------------------------------
def brLightSwitch():
    brStatus = br.status()
    if brStatus['dps']['1']==True:
        br.turn_off(switch=1)
    else:
        br.turn_on(switch=1)

#brSwitchMode switches between color and white mode
def brSwitchMode():
    brStatus = br.status()
    if brStatus['dps']['2']=="colour":
        br.set_mode(mode='white')
    else:
        br.set_mode(mode='colour')

#brAdjustBrightnessOn creates a loop to allow for change of brightness until ended
