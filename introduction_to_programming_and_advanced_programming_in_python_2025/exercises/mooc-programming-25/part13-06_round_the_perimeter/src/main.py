# # WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window_dims = (width, height) = (640, 480)

window = pygame.display.set_mode(window_dims)
black_rgb = (0, 0, 0)
robot = pygame.image.load("robot.png")
robot_dims = (robot_w, robot_h) = (robot.get_width(), robot.get_height())
clock = pygame.time.Clock()

x = 0
y = 0
pos_x = 1
pos_y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill(black_rgb)
    window.blit(robot, (x, y))
    pygame.display.flip()

    x += pos_x
    y += pos_y

    if x + robot_w == width and y == 0:
        pos_x = 0
        pos_y = 1

    if x + robot_w == width and y + robot_h == height:
        pos_x = -1
        pos_y = 0

    if x == 0 and y + robot_h == height:
        pos_x = 0
        pos_y = -1

    if x == 0 and y == 0:
        pos_x = 1
        pos_y = 0

    clock.tick(300) # faster to evaluate the code
