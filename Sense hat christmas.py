from sense_hat import SenseHat
sense = SenseHat()
sense.show_message("Merry Christmas Sam", scroll_speed=0.05, text_colour=[250,0,0], back_colour=[0,250,0])
r = [255,0,0]
o = [255,127,0]
y = [255,255,0]
g = [0,255,0]
b = [0,0,255]
i = [75,0,130]
v = [159,0,255]
l = [0,0,0]
w = [255,255,255]

image = [
    l,l,l,l,l,l,l,l,
    l,l,l,r,r,l,l,l,
    l,r,r,o,o,r,r,l,
    r,o,o,y,y,o,o,r,
    o,y,y,g,g,y,y,o,
    y,g,g,b,b,g,g,y,
    b,b,b,i,i,b,b,b,
    b,i,i,v,v,i,i,b
    ]

sense.set_pixels(image)
