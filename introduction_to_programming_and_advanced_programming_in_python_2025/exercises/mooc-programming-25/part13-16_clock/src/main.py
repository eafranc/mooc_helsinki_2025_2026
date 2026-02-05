# WRITE YOUR SOLUTION HERE:
import pygame
import math
from datetime import datetime, timedelta

pygame.init()
pygame.display.set_caption("Clock")
screen_dims = (width, height) = (640, 480)
screen = pygame.display.set_mode(screen_dims)

# RGB COLORS USED FOR THE SHAPES
black = (0  , 0,   0)
red   = (255, 0,   0)
blue  = (0  , 0, 255)

# CLOCK FRAME - CENTER AND RADIUS
center = (width / 2, height / 2)
radius = 200

# FUNCTIONS TO CREATE DYNAMIC CLOCK HANDS - They use datetime and timedelta objects to move them (so we don't need Clock() object)
def clock_hand(clock_hand_size: int, thickness: int, clock_hand_type: str):
    [frequency, real_clock_hand_time] = which_clock_hand(clock_hand_type)
    initial_angle = 3 * math.pi / 2 # initial_angle makes all the clock hands start from the same position, pointing to number 12 on the clock
    angular_speed = 2 * math.pi * frequency
    angle = initial_angle + angular_speed * real_clock_hand_time    # real_clock_hand_time must be in seconds
                                                                    # (this is properly arranged in function which_clock_hand)

    x = center[0] + clock_hand_size * math.cos(angle)
    y = center[1] + clock_hand_size * math.sin(angle)

            # Line: (surface, color, A(x1, y1), B(x2, y2), thickness)
    return  pygame.draw.line(screen, blue, center, (x, y), thickness)

def which_clock_hand(clock_hand_type: str):
    time_now = datetime.now()
    # time_now = datetime(2026, 1, 21, 18, 45) # >>> only a test value to check a time greater than 12 hours (18:45)
    if clock_hand_type == "seconds":
        frequency = 1 / 60 
        real_clock_hand_time = timedelta(seconds= time_now.second).total_seconds()
    elif clock_hand_type == "minutes":
        frequency = 1 / (60 * 60) 
        real_clock_hand_time = timedelta(minutes= time_now.minute).total_seconds()
    elif clock_hand_type == "hours":
        frequency = 1 / (60 * 60 * 12) 
        real_clock_hand_time = timedelta(hours= time_now.hour).total_seconds()
    return [frequency, real_clock_hand_time]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill(black)

    # Drawing the clock frame
    # Circle: (surface, color, (center_x, center_y), radius)
    pygame.draw.circle(screen, red, center, radius)
    pygame.draw.circle(screen, black, center, radius - 5)
    pygame.draw.circle(screen, red, center, 10)

    # Declaring all the clock hands
    seconds = clock_hand(180, 2, "seconds")
    minutes = clock_hand(150, 4, "minutes")
    hours   = clock_hand(100, 6, "hours")

    pygame.display.flip()
    print(datetime.now().strftime("%H:%M:%S")) # to check the system time with the clock

# I really enjoyed this exercise. The coolest one!
