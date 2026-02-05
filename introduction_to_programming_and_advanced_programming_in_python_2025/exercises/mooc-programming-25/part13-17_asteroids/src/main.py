# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
screen_dims = (width, height) = (640, 480)
window = pygame.display.set_mode(screen_dims)

# COLORS
black = (0,   0, 0)
red   = (255, 0, 0)

clock = pygame.time.Clock()

# ROBOTS
robot = pygame.image.load("robot.png")
robot_dims = (robot_w, robot_h) = (robot.get_width(), robot.get_height())
robot_position = [0, height - robot_h] # robot initial position

# ROCKS
rock = pygame.image.load("rock.png")
rock_dims = (rock_w, rock_h) = (rock.get_width(), rock.get_height())
number_of_rocks = 10
rock_positions = []
for i in range(number_of_rocks):
    x = randint(0, width - rock_w)
    y = randint(-200, 0)
    rock_positions.append([x, y])

# FUNCTION FOR COLLISION BETWEEN ROCK AND ROBOT
def collision(robot_x, robot_y, rock_x, rock_y):
    overlap_x = (robot_x < rock_x + rock_w) and (robot_x + robot_w > rock_x) # rock is just behind or just in front of the robot - 2 expressions for X-axis
    overlap_y = (robot_y < rock_y + rock_h) # since the rocks can only come from above the robot, there's only one expression for Y-axis

    return overlap_x and overlap_y

# CONTROLS
controls = [ 
    (pygame.K_LEFT , -2),
    (pygame.K_RIGHT,  2)
]
key_pressed = {}

# GAME STATUS
points = 0
game_over = False
font = pygame.font.SysFont("Arial", 24)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            key_pressed[event.key] = True

        if event.type == pygame.KEYUP:
            del key_pressed[event.key]

    if not game_over:
        for control in controls:
            if control[0] in key_pressed:
                robot_position[0] += control[1] # X

        robot_position[0] = max(0, min(width - robot_w, robot_position[0]))  # CLAMPING: assures X is always between 0 and (width - robot_w) (screen X limit)

        # UPDATE: 
        for i in range(number_of_rocks):
            rock_positions[i][1] += 1
            # if the rock touches the ground, the game freezes - GAME OVER
            if rock_positions[i][1] >= height - rock_h:
                game_over = True

            # checks collision
            if collision(robot_position[0], robot_position[1], rock_positions[i][0], rock_positions[i][1]):
                # if there's collision, the rocks are "respawned", i.e., they restart from above to fall again (we're recycling them)
                rock_positions[i][0] = randint(0, width - rock_w) 
                rock_positions[i][1] = randint(-100, 0)
                points += 1 # in collision, the robot collects the rock and the player scores 1

    # RENDER
    window.fill(black)
    for position in rock_positions:
        window.blit(rock, (position[0], position[1]))
    window.blit(robot, (robot_position[0], robot_position[1]))
    text = font.render(f"Points: {points}", True, red)
    window.blit(text, (width - 100, 10))
    pygame.display.flip()
    clock.tick(120)
