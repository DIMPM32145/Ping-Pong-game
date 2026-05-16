from pygame import *


#Setup the Window Dimensions
window = display.set_mode((800, 600))
display.set_caption('Ping-Pong game')

#Classes
# CLASSES
class GameSprite(sprite.Sprite):
    def __init__(self, color, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = Surface((player_width, player_height))
        self.image.fill(color)
        
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#Variables 
LIGHT_BLUE = (200, 240, 250) # Color for the Background
finish = False
BLACK = (0, 0, 0) # Color for the Paddles

paddle_left = GameSprite(BLACK, 30, 250, 8, 20, 100)
paddle_right = GameSprite(BLACK, 750, 250, 8, 20, 100)



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


        paddle_left.reset()
        paddle_right.reset()
        
    display.update()
    clock.tick(FPS)
