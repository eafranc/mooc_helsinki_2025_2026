# WRITE YOUR SOLUTION HERE:
# Reusing the code from last exercise

import pygame

window_dims = (width, height) = (640, 480)

pygame.init()
window = pygame.display.set_mode(window_dims)

black_rgb = (0, 0, 0)
window.fill(black_rgb)

robot = pygame.image.load("robot.png")
robot_dims = (robot_w, robot_h) = (robot.get_width(), robot.get_height())

[w,h] = [robot_w, 160] 

offset = [offset_w, offset_h] = [5, 10]
[[window.blit(robot, (i * w + j * offset_w, h + j * offset_h)) for i in range(1, 11)] for j in range(1, 11)]

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
