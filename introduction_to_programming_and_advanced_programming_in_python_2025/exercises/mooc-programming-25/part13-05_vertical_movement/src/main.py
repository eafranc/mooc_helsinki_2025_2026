# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window_dims = (width, height) = (640, 480)
window = pygame.display.set_mode(window_dims)
black_rgb = (0, 0, 0)
robot = pygame.image.load("robot.png")
robot_dims = (robot_w, robot_h) = (robot.get_width(), robot.get_height())

x = 0
y = 0
position = 1

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill(black_rgb)
    window.blit(robot, (x, y))
    pygame.display.flip()

    y += position
    if y + robot_h >= height:
        position = - position
    elif y <= 0:
        position = - position

    clock.tick(60)
