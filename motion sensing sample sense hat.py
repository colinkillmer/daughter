from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.clear()
o = sense.get_orientation()
pitch = o["pitch"]
roll = o["roll"]
yaw = o["yaw"]

