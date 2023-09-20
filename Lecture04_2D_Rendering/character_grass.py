from pico2d import *
import math

check = False

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90

p = 270
r = 210
while (True):
    clear_canvas_now()
    
    if check == True:
        if x < 750 and y == 90:
            if x == 399:
                check = False
            x = x+1
        elif x==750 and y < 550:
            y = y+1
        elif y==550 and x > 50:
            x = x-1
        elif x==50 and y>90:
            y = y-1        
    elif check == False:
        p = p+1
        x = 400 + r*math.cos(p/360 *2*math.pi)
        y = 300 + r*math.sin(p/360 *2*math.pi)
        if p%360 == 270:
            check = True
            x = 400
            y = 90
    character.draw_now(x,y)     
    grass.draw_now(400,30) 
    delay(0.01)
  
close_canvas()






