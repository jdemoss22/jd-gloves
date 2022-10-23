<h2>Setup for IDE</h2>

install "script" for atom

install anaconda for python
	conda create -n gloves python=3.7 anaconda
	activate gloves
	add tinytuya and window (tkinter)
		pip install tinytuya
		pip install tk
		pip list

point atom-script to virtual python executable created by anaconda
	ctrl-shift-alt-o
	input path to .exe in "command" box
	ex. C:\Users\Joe\anaconda3\envs\gloves\python.exe

to get device info, run "python -m tinytuya wizard"
	will ask for Access ID/Client ID, Client Secret, Device ID registered to account, and which data center (us)
	Will create devices.json with all device info

"PyInstaller" can convert Python files to standalone executables


<h2>Support Documents</h2>

[tkinter](https://tkdocs.com/shipman/)
[tinytuya](https://pythonrepo.com/repo/jasonacox-tinytuya-python-networking-programming)
[pyduino](https://www.arduino.cc/reference/en/libraries/pyduinobridge/)

Device Commands from tinytuya:

	 status()                           # Fetch status of device (json payload)
	                                    ##Returns dict array, which means example['key']['key2'] returns value

	 detect_available_dps()             # Return list of DPS available from device
	 set_status(on, switch=1)           # Control status of the device to 'on' or 'off' (bool)
	 set_value(index, value)            # Send and set value of any DPS/index on device.
	 heartbeat()                        # Send heartbeat to device
	 updatedps(index=[1])               # Send updatedps command to device to refresh DPS values
	 turn_on(switch=1)                  # Turn on device / switch #
	 turn_off(switch=1)                 # Turn off device
	 set_timer(num_secs)                # Set timer for num_secs on devices (if supported)
	 generate_payload(command, data)    # Generate TuyaMessage payload for command with data
	 send(payload)                      # Send payload to device (do not wait for response)
	 receive()                          # Receive payload from device

BulbDevice Commands
   set_colour(r, g, b):
   set_hsv(h, s, v):
   set_white(brightness, colourtemp):
   set_white_percentage(brightness=100, colourtemp=0):
   set_brightness(brightness):
   set_brightness_percentage(brightness=100):
   set_colourtemp(colourtemp):
   set_colourtemp_percentage(colourtemp=100):
   set_scene(scene):             # 1=nature, 3=rave, 4=rainbow
   set_mode(mode='white'):       # white, colour, scene, music
   result = brightness():
   result = colourtemp():
   (r, g, b) = colour_rgb():
   (h,s,v) = colour_hsv():
   result = state():

 Status #5 is brightness
