# psychodelic animation 06.11.2016
import pygame, math, time, random, os

#the path of audio file
file1 = os.path.join('D:\Programy\Python3.4.4\PaintItBlack.mp3')
pygame.init()
pygame.mixer.music.load(file1)
pygame.mixer.music.play(loops=0, start=0.0)

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
MIXED = (200,   0,   127)
MIXED2 = (0, 99, 230)
MIXED3 = (123, 32, 180)
MOOD = (200, 200, 200)

pygame.display.init
size = (450, 300)
#size = (1200,500)
surface = pygame.display.set_mode(size)
mouth_area = [185,90,30,10]

def header(pos, rad, depth, color=WHITE):
    global WHITE
    pygame.draw.circle(surface, color, pos, rad, depth)
    pygame.display.flip()
#header((100,100), 30, 5)

for x in range(12500):
    x_ray = random.randrange(0,size[0])
    y_ray = random.randrange(0,size[1])
    x_ray2 = random.randrange(0,size[0])
    y_ray2 = random.randrange(0,size[1])
    x_red = random.randrange(0,255)
    x_g = random.randrange(0,255)
    x_blue = random.randrange(0,255) 
    pygame.draw.line(surface,(x_red,x_g,x_blue),(x_ray,y_ray), (x_ray2,y_ray2), 2)
    time.sleep(1/(x+10))
    pygame.display.flip()
    
for x in range(1755500):
    x_ray = random.randrange(0,size[0])
    y_ray = random.randrange(0,size[1])
    x_ray2 = random.randrange(0,size[0])
    y_ray2 = random.randrange(0,size[1])
    #jeden kolor - walka dobra ze złem
    x_color = random.choice((0,215))
    pygame.draw.line(surface,(x_color,0,0),(x_ray,y_ray),(x_ray2,y_ray2), 3)
    time.sleep(1/(x+10))
    pygame.display.flip()

# DANGER! It can cause psychodelic effects





