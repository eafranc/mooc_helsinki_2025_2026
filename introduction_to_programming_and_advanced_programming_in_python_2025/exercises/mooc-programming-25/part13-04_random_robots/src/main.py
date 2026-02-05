# WRITE YOUR SOLUTION HERE:
import pygame

from random import randint

pygame.init()

window_dims = (width, height) = (640, 480)

window = pygame.display.set_mode(window_dims)

black_rgb = (0, 0, 0)
window.fill(black_rgb)

robot = pygame.image.load("robot.png")
robot_dims = (robot_w, robot_h) = (robot.get_width(), robot.get_height())

[window.blit(robot, (randint(0, width - robot_w), randint(0, height - robot_h))) for i in range(1000)]


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
