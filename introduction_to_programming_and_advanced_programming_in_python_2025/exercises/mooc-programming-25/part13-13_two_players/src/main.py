# WRITE YOUR SOLUTION HERE:
# 1 - MY SOLUTION - VERBOSE, UNLIKE THE SOLUTION GIVEN - I WILL RECREATE THE COURSE SOLUTION ON SOLUTION 2
# import pygame

# pygame.init()
# screen_dims = (width, height) = (640, 480)
# black_rgb = (0, 0, 0)
# screen = pygame.display.set_mode(screen_dims)
# robot = pygame.image.load("robot.png")
# robot_dims = (robot_w, robot_h) = (robot.get_width(), robot.get_height())
# clock = pygame.time.Clock()

# x1 = 0
# y1 = height - robot_h

# x2 = width - robot_w
# y2 = height - robot_h

# to_left1 = False
# to_up1 = False
# to_right1 = False
# to_down1 = False

# to_left2 = False
# to_up2 = False
# to_right2 = False
# to_down2 = False

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 to_left1 = True
#             if event.key == pygame.K_UP:
#                 to_up1 = True
#             if event.key == pygame.K_RIGHT:
#                 to_right1 = True
#             if event.key == pygame.K_DOWN:
#                 to_down1 = True

#         if event.type == pygame.KEYUP: 
#             if event.key == pygame.K_LEFT:
#                 to_left1 = False
#             if event.key == pygame.K_UP:
#                 to_up1 = False
#             if event.key == pygame.K_RIGHT:
#                 to_right1 = False
#             if event.key == pygame.K_DOWN:
#                 to_down1 = False

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_a:
#                 to_left2 = True
#             if event.key == pygame.K_w:
#                 to_up2 = True
#             if event.key == pygame.K_d:
#                 to_right2 = True
#             if event.key == pygame.K_s:
#                 to_down2 = True

#         if event.type == pygame.KEYUP: 
#             if event.key == pygame.K_a:
#                 to_left2 = False
#             if event.key == pygame.K_w:
#                 to_up2 = False
#             if event.key == pygame.K_d:
#                 to_right2 = False
#             if event.key == pygame.K_s:
#                 to_down2 = False

#     if to_left1 and x1 >= 0:
#         x1 -= 2
#     if to_up1 and y1 >= 0:
#         y1 -= 2
#     if to_right1 and x1 <= width - robot_w:
#         x1 += 2
#     if to_down1 and y1 <= height - robot_h:
#         y1 += 2

#     if to_left2 and x2 >= 0:
#         x2 -= 2
#     if to_up2 and y2 >= 0:
#         y2 -= 2
#     if to_right2 and x2 <= width - robot_w:
#         x2 += 2
#     if to_down2 and y2 <= height - robot_h:
#         y2 += 2

#     screen.fill(black_rgb)
#     screen.blit(robot, (x1, y1))
#     screen.blit(robot, (x2, y2))
#     pygame.display.flip()
#     clock.tick(60)

# 2 - SOLUTION WITH BETTER AND SHORTER CODE
import pygame

pygame.init()
screen_dims = (width, height) = (640, 480)
screen = pygame.display.set_mode(screen_dims)
black_rgb = (0, 0, 0)
robot = pygame.image.load("robot.png")
robot_dims = (robot_w, robot_h) = (robot.get_width(), robot.get_height())
clock = pygame.time.Clock()

positions = [
    [0, height - robot_h],             # robot 0 position
    [width - robot_w, height -robot_h] # robot 1 position
]

# tuples containing: key, which robot it moves, horizontal movement (X), vertical movement (Y)
controls = [ 
# ====== KEY ===== ROB = X = Y ==
    (pygame.K_LEFT,  0, -2,  0),
    (pygame.K_RIGHT, 0,  2,  0),
    (pygame.K_UP,    0,  0, -2),
    (pygame.K_DOWN,  0,  0,  2),

    (pygame.K_a,     1, -2,  0),
    (pygame.K_d,     1,  2,  0),
    (pygame.K_w,     1,  0, -2),
    (pygame.K_s,     1,  0,  2)
]

key_pressed = {} # A dictionary that will collect the key pressed based on event.key (which has a code for each keyboard key)

while True:
    # INPUT - Generic events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            key_pressed[event.key] = True # catches the event.key, which has a code that identifies the key pressed

        if event.type == pygame.KEYUP:
            del key_pressed[event.key] # deletes the key released from the dictionary (which keeps track of pressed keys)

    # UPDATE - This loop will process all the controls
    for control in controls:
        if control[0] in key_pressed:
                    # control[1] => ROBOT No.
            positions[control[1]][0] += control[2] # X
            positions[control[1]][1] += control[3] # Y

    # CLAMPING - We use the screen dimensions limits and make sure either robot coordinate doesn't trespass these limits
    for position in positions:
        position[0] = max(0, min(width - robot_w, position[0]))  # assures X is always between 0 and (width - robot_w)
        position[1] = max(0, min(height - robot_h, position[1])) # assures Y is always between 0 and (height - robot_h)

    # RENDER
    screen.fill(black_rgb)
    for position in positions: # this loop gives the positions of all robots (if we add or subtract a robot, the loop would still work)
        screen.blit(robot, (position[0], position[1]))

    pygame.display.flip()
    clock.tick(60)
