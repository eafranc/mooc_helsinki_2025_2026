# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()

window_dims = (width, height) = (640, 480)
window = pygame.display.set_mode(window_dims)
robot = pygame.image.load("robot.png")
robot_dims = (robot_w, robot_h) = (robot.get_width(), robot.get_height())
clock = pygame.time.Clock()
black_rgb = (0, 0, 0)

angle = 0
radius = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill(black_rgb)

    # we need to create 10 robots and distribute them equidistantly around the circle
    for i in range(10): 
        # every robot will have a first angle related to their initial position (a phase): initial_angle =  2*PI*k/10, k = 0, 1, ..., 9 
        x = (width - robot_w)/2 + radius * math.cos(angle + 2 * i * math.pi /10)
        y = (height - robot_h)/2 + radius * math.sin(angle + 2 * i * math.pi /10)
        window.blit(robot, (x, y))
    pygame.display.flip()

    angle += 0.01
    clock.tick(60)
