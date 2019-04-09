from picamera import PiCamera
from time import sleep
from datetime import datetime
camera = PiCamera()
now = datetime.now()
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(180)
camera.rotation = 90
camera.start_preview()
sense.clear((100,100,100))
sleep(1)
sense.show_letter("3", text_colour=[255,255,255],back_colour=[20,20,20])
sleep(1)
sense.show_letter("2", text_colour=[255,255,255],back_colour=[20,20,20])
sleep(1)
sense.show_letter("1", text_colour=[255,255,255],back_colour=[20,20,20])
sleep(1)
sense.clear()

filename = "{0:%Y}-{0:%m}-{0:%d}-{0:%H}-{0:%M}-{0:%S}.jpg".format(now)
camera.capture('/home/pi/Desktop/weddingtrialpics/{0}'.format(filename))
camera.stop_preview()
