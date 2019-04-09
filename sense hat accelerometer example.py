from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.set_rotation(180)
red = (255,0,0)

#this part says that while the program is running, x,y,and z will be acceleration measurements

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = abs(x)
    y = abs(y)
    z = abs(z)

#this part says that if the acceleration is greater than a certain value, ! will appear
    
    if x>1.5 or y>1.5 or z>1.5:
        sense.show_letter("!", red)
    else:
        sense.clear()

        
