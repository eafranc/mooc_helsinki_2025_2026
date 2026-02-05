# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
screen_dims = (width, height) = (640, 480)
screen = pygame.display.set_mode(screen_dims)
black_rgb = (0, 0, 0)
robot = pygame.image.load("robot.png")
robot_dims = (robot_w, robot_h) = (robot.get_width(), robot.get_height())
clock = pygame.time.Clock()

# the robot will be at the top left corner of the screen before being "attached" to the mouse cursor at the moment the latter appears
robot_x = 0
robot_y = 0

while True:
    # INPUT - Generic events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEMOTION:
            # bear in mind that the robot coordinates are related to its top left vertex
            robot_x = event.pos[0] - robot_w/2
            robot_y = event.pos[1] - robot_h/2

    screen.fill(black_rgb)
    screen.blit(robot, (robot_x, robot_y))
    pygame.display.flip()
    clock.tick(60)
