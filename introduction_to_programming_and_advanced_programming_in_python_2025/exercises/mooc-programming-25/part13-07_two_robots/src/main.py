# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window_dims = (width, height) = (640, 480)
window = pygame.display.set_mode(window_dims)
black_rgb = (0, 0, 0)
robot = pygame.image.load("robot.png")
robot_dims = (robot_w, robot_h) = (robot.get_width(), robot.get_height())
clock = pygame.time.Clock()

x1 = 0
y1 = 100
pos_x1 = 1

x2 = 0
y2 = 300
pos_x2 = 2


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill(black_rgb)
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    x1 += pos_x1
    if x1 + robot_w >= width:
        pos_x1 = - pos_x1
    if x1 <= 0:
        pos_x1 = - pos_x1

    x2 += pos_x2
    if x2 + robot_w >= width:
        pos_x2 = - pos_x2
    if x2 <= 0:
        pos_x2 = - pos_x2


    clock.tick(60)
