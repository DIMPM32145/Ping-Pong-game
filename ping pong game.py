from pygame import *


#Setup the Window Dimensions
window = display.set_mode((800, 600))
display.set_caption('Ping-Pong game')


#Variables 
LIGHT_BLUE = (200, 240, 250)
finish = False


# setting fps
clock = time.Clock()
FPS = 60
game = True


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(LIGHT_BLUE)

    display.update()
    clock.tick(FPS)