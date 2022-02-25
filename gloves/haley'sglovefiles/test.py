import tinytuya
import time

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
# data = d.status()
# print('set_status() result %r' % data)

d.turn_off(switch=1)
time.sleep(0.5)
d.turn_on(switch=1)
d.set_mode(mode='white')
i = 1
while i <= 100:
  d.set_brightness_percentage(brightness=i)
  i += 5

while i >= 0:
  d.set_brightness_percentage(brightness=i)
  i -= 5
d.turn_off(switch=1)

print('Light Party')
