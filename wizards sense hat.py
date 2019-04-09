from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

r = (255,0,0)
g = (0,255,0)
w = (255,255,255)
l = (20,20,20)
b = (150,42,42)
u = (0,0,255)
o = (255,165,0)
y = (255,255,0)

#candy cane
candycane_pixels = [
    l,l,l,l,l,l,l,l,
    l,l,r,r,w,w,r,l,
    l,l,w,w,l,r,r,l,
    l,l,r,r,l,w,w,l,
    l,l,w,w,l,l,l,l,
    l,l,r,r,l,l,l,l,
    l,l,w,w,l,l,l,l,
    l,l,r,r,l,l,l,l
]
#Hot cocoa
hotcocoa_pixels = [
    l,l,l,l,l,l,l,l,
    l,l,w,w,w,w,l,l,
    l,w,b,b,b,b,w,l,
    l,w,w,w,w,w,w,w,
    l,w,w,w,w,w,w,l,
    l,w,w,w,w,w,w,l,
    l,w,w,w,w,w,w,w,
    l,w,w,w,w,w,w,l
]
#snow man
snowman_pixels = [
    l,u,u,u,u,u,u,u,
    l,l,w,w,w,w,w,l,
    l,l,w,l,w,l,w,l,
    l,l,w,w,o,o,o,l,
    l,l,w,w,l,l,w,l,
    l,g,w,w,w,w,y,g,
    l,g,y,g,y,g,y,g,
    l,g,y,g,y,g,y,g
]
sense.set_pixels(candycane_pixels)
sleep(3)
sense.set_pixels(hotcocoa_pixels)
sleep(3)
sense.set_pixels(snowman_pixels)
sleep(3)
sense.clear()


