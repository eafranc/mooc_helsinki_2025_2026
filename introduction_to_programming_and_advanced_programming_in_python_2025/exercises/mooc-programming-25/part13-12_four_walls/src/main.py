# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
screen_dims = (width, height) = (640, 480)
black_rgb = (0, 0, 0)
screen = pygame.display.set_mode(screen_dims)
robot = pygame.image.load("robot.png")
robot_dims = (robot_w, robot_h) = (robot.get_width(), robot.get_height())
clock = pygame.time.Clock()

x = 0
y = height - robot_h

to_left = False
to_up = False
to_right = False
to_down = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_DOWN:
                to_down = True

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_DOWN:
                to_down = False

    if to_left and x >= 0:
        x -= 2
    if to_up and y >= 0:
        y -= 2
    if to_right and x <= width - robot_w:
        x += 2
    if to_down and y <= height - robot_h:
        y += 2

    screen.fill(black_rgb)
    screen.blit(robot, (x, y))
    pygame.display.flip()
    clock.tick(60)
