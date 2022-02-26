import tinytuya

bedroomDeviceID = '01041015807d3a62cb72'
bedroomIPaddress = '192.168.0.193'
bedroomLocalKey = 'e8f315bd8f0fb7e9'

livingRoomDeviceID = '2505828184f3eb37102b'
livingroomIPaddress = '192.168.0.172'
livingRoomLocalKey = '9dec8bcf335b73f4'


# Define devices using constructors from tinytuya

# lightbulb = tinytuya.BulbDevice(DEVICE_ID, IP_ADDRESS, )

br = tinytuya.BulbDevice(bedroomDeviceID,bedroomIPaddress,bedroomLocalKey)
lr = tinytuya.BulbDevice(livingRoomDeviceID,livingroomIPaddress,livingRoomLocalKey)

#br.set_version(3.1)
#lr.set_version(3.1)
