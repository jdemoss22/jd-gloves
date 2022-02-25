import tinytuya
import tkinter
top = tkinter.Tk()
# Code to add widgets will go here...
#top.mainloop()
#print('hello world')

bedroomDeviceID = '01041015807d3a62cb72'
livingRoomDeviceID = '2505828184f3eb37102b'
bedroomIPaddress = '192.168.0.246'
livingroomIPaddress = '192.168.0.101'
bedroomLocalKey= 'e8f315bd8f0fb7e9'
livingRoomLocalKey = '97759bb0119792ad'



DEVICE_ID = bedroomDeviceID
IP_ADDRESS = bedroomIPaddress
LOCAL_KEY = bedroomLocalKey

d = tinytuya.BulbDevice(DEVICE_ID, IP_ADDRESS, LOCAL_KEY)

d.set_version(3.1)

def buttonFunction():
    d.set_brightness_percentage(brightness=50)


top.geometry("200x100")
button = tkinter.Button(top,text = "haley rocks", command=buttonFunction)
button.pack()

while True:
    top.update()
    print('test')
