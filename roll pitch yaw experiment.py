from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

r = (255,0,0)
b = (0,0,0)
g = (0,255,0)
x = 1
y = 1

maze =[[r,r,r,r,r,r,r,r],
       [r,b,b,b,b,b,b,r],
       [r,b,b,b,b,b,b,r],
       [r,b,b,b,b,b,b,r],
       [r,b,b,b,b,b,b,r],
       [r,b,b,b,b,b,b,r],
       [r,b,b,b,b,b,b,r],
       [r,r,r,r,r,r,r,r]]
def move_marble(pitch, roll, x, y):
    new_x = x
    new_y = y
    if 1 < pitch < 179 and x !=0:
        new_x -=1
    elif 359 > pitch > 179 and x !=7:
        new_x +=1
    if 1 < roll < 179 and y !=7:
        new_y +=1
    elif 359 > roll > 179 and y !=0:
        new_y -=1
    return new_x,new_y
game_over = False
while game_over ==False:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    x,y = move_marble(pitch,roll,x,y)
    maze[y][x] = g
    sense.set_pixels(sum(maze,[]))
    sleep(.05)
    maze[y][x] = b
       
