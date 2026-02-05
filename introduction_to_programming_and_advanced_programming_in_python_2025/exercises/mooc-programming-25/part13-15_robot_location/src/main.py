# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
screen_dims = (width, height) = (640, 480)
screen = pygame.display.set_mode(screen_dims)
black_rgb = (0, 0, 0)
robot = pygame.image.load("robot.png")
robot_dims = (robot_w, robot_h) = (robot.get_width(), robot.get_height())
clock = pygame.time.Clock()

# the robot will be at the top left corner of the screen before being "attached" to the mouse cursor at the moment the latter appears
robot_x = randint(0, width - robot_w)
robot_y = randint(0, height - robot_h)

while True:
    # INPUT - Generic events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # bear in mind that the robot coordinates are related to its top left vertex
            if robot_x <= event.pos[0] <= robot_x + robot_w and robot_y <= event.pos[1] <= robot_y + robot_h:
                robot_x = randint(0, width - robot_w)
                robot_y = randint(0, height - robot_h)

    screen.fill(black_rgb)
    screen.blit(robot, (robot_x, robot_y))
    pygame.display.flip()
    clock.tick(60)
