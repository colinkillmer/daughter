from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
def red():
    sense.clear(255,0,0)
def blue():
    sense.clear(0,0,255)
def green()
:
    sense.clear(0,255,0)
def yellow():
    sense.clear(255,255,0)
def blank():
    sense.clear(0,0,0)


sense.stick.direction_up = red
sense.stick.direction_down = blue
sense.stick.direction_left = green
sense.stick.direction_right = yellow
sense.stick.direction_middle = blank

while True:
    pass
    
