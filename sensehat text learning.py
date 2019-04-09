from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(180)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)

n=0
while n<3:
    sense.show_message("poop", text_colour=blue, back_colour=(255,0,0))
    n=n+1
sense.clear((0,0,0))
