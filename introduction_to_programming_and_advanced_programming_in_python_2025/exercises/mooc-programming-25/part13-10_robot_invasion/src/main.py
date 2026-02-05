# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
screen_dims = (width, height) = (640, 480)
window = pygame.display.set_mode(screen_dims)
black_rgb = (0, 0, 0)
robot = pygame.image.load("robot.png")
robot_dims = (robot_w, robot_h) = (robot.get_width(), robot.get_height())
clock = pygame.time.Clock()

number_of_robots = 16

# I need to generate the robots positions before the while-loop, so I can keep their x-positions
positions = []
for i in range(number_of_robots):
    x = randint(0, width - robot_w) # x must be a random position were the robots are all visible on the screen
    y = randint(-200, 0) # the y position is given above the screen so we can see them in random y-position when they "fall" on the screen
    positions.append([x, y]) # I'll put the coordinates of the robots in a list because I want to change them on the while-loop (no tuples then!)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill(black_rgb)

    for i in range(number_of_robots):
        positions[i][1] += 1 # this will change the y-position on every robot so they can "fall"
        x = positions[i][0]
        y = positions[i][1]

        if y >= height - robot_h:
            positions[i][1] = height - robot_h # when the robots touch the floor, y doesn't change anymore (they stay on the floor)
            if x <= width/2: # now that the robots are on the floor, the ones on the left side run to the left, the other ones to the right
                positions[i][0] -= 1 # Notice that I change directly the positions list
            else:
                positions[i][0] += 1
            # when all the robots went off the screen, we can make they fall again ("respawn")
            if x < - robot_w or x > width:
                positions[i][0] = randint(0, width - robot_w) # we use the same expressions used to give the initial random positions before while loop
                positions[i][1] = randint(-1000, -100)

        window.blit(robot, (x, y)) # this is giving the final position of each robot on each frame

    pygame.display.flip()
    clock.tick(120)
