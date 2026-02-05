# WRITE YOUR SOLUTION HERE:
import pygame

window_dims = (width, height) = (640, 480)

pygame.init()
window = pygame.display.set_mode(window_dims)
robot = pygame.image.load("robot.png")

black_rgb =  (0, 0, 0)
window.fill(black_rgb)

robot_dims = (robot_w, robot_h) = (robot.get_width(), robot.get_height())

print(robot_dims) # the robot dimensions are (50, 86)

[w,h] = [robot_w, (height - robot_h)/2] # robots right at the middle height of the screen; using robot width will prevent overlapping
# for i in range(1, 11):
#     window.blit(robot, (w * i, h))

# A cool way using list comprehension
[window.blit(robot, (w * i, h)) for i in range(1, 11)]

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
