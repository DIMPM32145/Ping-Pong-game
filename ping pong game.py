from pygame import *


#Setup the Window Dimensions
window = display.set_mode((800, 600))
display.set_caption('Ping-Pong game')


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


class Player(GameSprite):
    def update(self, up_key, down_key):
        keys = key.get_pressed()
        if keys[up_key] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.y < 500: 
            self.rect.y += self.speed


class BallSprite(sprite.Sprite):
    def __init__(self, ball_image, ball_x, ball_y, ball_width, ball_height):
        super().__init__()
        self.image = transform.scale(image.load(ball_image), (ball_width, ball_height))
        self.rect = self.image.get_rect()
        self.rect.x = ball_x
        self.rect.y = ball_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#Variables 
LIGHT_BLUE = (200, 240, 250) # Color for the Background
finish = False
BLACK = (0, 0, 0) # Color for the Paddles


# Font settings
font.init()
style = font.Font(None, 40)

lose_player1 = style.render("PLAYER 1 LOSE!", True, (180, 0, 0))
lose_player2 = style.render("PLAYER 2 LOSE!", True, (180, 0, 0))

# Ball Variables
speed_x = 3
speed_y = 3

score_p1 = 0
score_p2 = 0

paddle_left = Player(BLACK, 30, 250, 8, 20, 100)
paddle_right = Player(BLACK, 750, 250, 8, 20, 100)
ball = BallSprite('ping-pong ball.svg', 385, 285, 50, 50)
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

        # 1. Handle paddle controls
        paddle_left.update(K_w, K_s)
        paddle_right.update(K_UP, K_DOWN)

        # 2. Automatic Ball Movement
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        # 3. Wall Bounce Logic
        if ball.rect.y < 0 or ball.rect.y > 550:
            speed_y *= -1

        # 4. Paddle Collision Logic
        if sprite.collide_rect(paddle_left, ball) or sprite.collide_rect(paddle_right, ball):
            speed_x *= -1

        # 5. Lose Conditions
        if ball.rect.x < 0:
            score_p2 += 1
            if score_p2 >= 5:
                finish = True
                window.blit(lose_player1, (200, 250))
            else:
                ball.rect.x = 385
                ball.rect.y = 285
                speed_x *= -1

        if ball.rect.x > 750:
            score_p1 += 1
            if score_p1 >= 5:
                finish = True
                window.blit(lose_player2, (450, 250))
            else:
                ball.rect.x = 385
                ball.rect.y = 285
                speed_x *= -1

        text_score = style.render(str(score_p1) + " : " + str(score_p2), True, (0, 0, 0))
        window.blit(text_score, (375, 20))

        # 6. Draw all objects onto the screen
        paddle_left.reset()
        paddle_right.reset()
        ball.reset()


    display.update()
    clock.tick(FPS)
