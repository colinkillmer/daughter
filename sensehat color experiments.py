from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.set_rotation(180)
sense.clear((100,100,100))
sleep(1)
sense.show_letter("K", text_colour=[255,255,255], back_colour=[20,20,20])
sleep(5)
sense.clear()
