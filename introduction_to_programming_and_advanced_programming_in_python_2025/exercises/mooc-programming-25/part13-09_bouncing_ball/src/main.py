# WRITE YOUR SOLUTION HERE:
import pygame
import math

screen_dims = (width, height) = (640, 480)
black_rgb = (0, 0, 0)
window = pygame.display.set_mode(screen_dims)
ball = pygame.image.load("ball.png")
ball_dims = (ball_w, ball_h) = (ball.get_width(), ball.get_height()) # ball_dims = (50, 50)

x = (width - ball_w)/2
y = (height - ball_h)/2
# We can change the ball speed by changing the parameters below:
pos_x = 1
pos_y = 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill(black_rgb)

    x += pos_x
    y += pos_y

    if x <= 0 or x >= width - ball_w: # x goes from 0 to 640 - 50 = 590
        pos_x = - pos_x # reflection!

    if y <= 0 or y >= height - ball_h: # y goes from 0 to 480 - 50 = 430
        pos_y = - pos_y # reflection!

    window.blit(ball, (x, y))

    pygame.display.flip()
    clock.tick(60)
    # print (x, y) # this line is useful to understand the ball trajectory when testing only

# NOTICE: in the if-statements we necessarily use <= and >= instead of == because if the pos_x and pos_y were changed (and thus the ball speed),
#         the ball position may trespass the screen limits due to the increments never turning x and y equal to these limits
#         (when the if-statements become True). The case in which pos_x = pos_y = 1 might conceal this situation.
