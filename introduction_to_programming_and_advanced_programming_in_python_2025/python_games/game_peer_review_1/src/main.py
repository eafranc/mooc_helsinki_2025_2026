# Complete your game here

# Coin Snatcher is a game about avoiding ghosts and collecting 20 coins.
# 'a' and 'd' keys move the robot horizontaly, and space allows the robot to jump
# The walls can be wall jumped on as to allow escaping from the many ghosts
# This game is not particularly balanced or easey, and because of the randomness of the game, certain combinations of ghosts can make winning imposible.
# Because of this, the backspace key cuts to the end animation, otherwise, collecting 20 coins wins the game

# TIP: Resting on the left wall is dangerous, because that is where ghosts spawn, the right wall is safer

# Thanks, good luck, and enjoy!


import pygame
import random
pygame.display.set_caption("Coin Snatcher")

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        self.robot = pygame.image.load("robot.png")
        self.monster = pygame.image.load("monster.png")
        self.coin_art = pygame.image.load("coin.png")
        self.door = pygame.image.load("door.png")

        self.window.fill((0, 0, 51))
        pygame.display.flip()

        self.x = 320 - self.robot.get_width()/2
        self.y = 400 - self.robot.get_height()

        self.left = False
        self.right = False
        self.velocity = 0
        self.points = 0

        self.game_font = pygame.font.SysFont("Arial", 32)

        self.coin = self.define_coin()
        self.ghost = self.define_ghost()
        self.coins = [self.coin()]
        self.ghosts = []

        self.win_circle = 0 # This is the ending animation and serves as a indicator for a game end

        self.main_loop()

    def define_coin(self):
        class Coin:

            def __init__(self):

                self.y = random.randint(1, 1000) * -1
                self.x = random.randint(20, 600)

            def move(self):

                self.y += 1

        return Coin

    def define_ghost(self):
        class Ghost:

            def __init__(self):

                self.y = random.randint(20, 330)
                self.x = random.randint(1, 1000) * -1

            def move(self):
                self.x += 1

        return Ghost

    def random_spawns(self):
        if random.randint(1, 120) == 1:
                self.coins.append(self.coin())

        if random.randint(1, 250) == 1:
            self.ghosts.append(self.ghost())

    def events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.right = True

                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.left = True

                    if event.key == pygame.K_SPACE:
                        if self.y == 400-self.robot.get_height() or self.x <= 1 or self.x >= 639 - self.robot.get_width():
                            self.velocity = 5

                    if event.key == pygame.K_BACKSPACE:
                        self.win_circle += 1

                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.right = False

                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.left = False

    def move_robot(self):
        if self.right and self.x + self.robot.get_width() < 640:
            self.x += 3

        if self.left and self.x > 0:
            self.x -= 3

    def proscess_jumping(self):
        if self.velocity > 0 or self.velocity < 0:
            self.y -= self.velocity
            self.velocity -= 0.1
        elif self.velocity == 0 and self.y != 400-self.robot.get_height():
            self.velocity == -5

        if self.y >= 400-self.robot.get_height():
            self.velocity = 0
            self.y = 400-self.robot.get_height()

        if self.y < 0:
            self.y = 0
            self.velocity *= -0.3


    def proscess_coins(self):
        for coin in self.coins:
            self.window.blit(self.coin_art, (coin.x, coin.y))
            coin.move()
            if coin.y >= 400-self.coin_art.get_height():
                self.coins.remove(coin)

            if self.x + self.robot.get_width() >= coin.x and self.x <= coin.x + self.coin_art.get_width() and self.y + self.robot.get_height() >= coin.y and self.y <= coin.y + self.coin_art.get_height():
                self.coins.remove(coin)

                self.points += 1

    def proscess_ghosts(self):
        for ghost in self.ghosts:
            self.window.blit(self.monster, (ghost.x, ghost.y))
            ghost.move()

            if self.x + self.robot.get_width() >= ghost.x and self.x <= ghost.x + self.monster.get_width() and self.y + self.robot.get_height() >= ghost.y and self.y <= ghost.y + self.monster.get_height():
                self.ghosts.remove(ghost)

                exit()

    def scoreboard(self):
        points_text = self.game_font.render(f"Points: {self.points}", True, (0, 255, 255))
        self.window.blit(points_text, (500, 410))

    def main_loop(self):
        while True:

            self.window.fill((0, 0, 51))
            self.events() # Checks and runs code for events like quit and movement

            if self.win_circle < 1:

                self.random_spawns()
                self.move_robot()


                pygame.draw.rect(self.window, (0, 0, 0), (0, 400, 640, 480)) # Draw ground

                self.window.blit(self.robot, (self.x, self.y))

                self.proscess_jumping()

                self.proscess_ghosts()
                self.proscess_coins()

                self.scoreboard()

                if self.points >= 20:
                    self.win_circle += 1

            else:
                self.window.blit(self.robot, (self.x, self.y))
                pygame.draw.circle(self.window, (0, 255, 255), (self.x + self.robot.get_width()/2, self.y + self.robot.get_height()/2), self.win_circle)
                self.win_circle += 5
                if self.win_circle >= 640:
                    self.window.blit(self.game_font.render("You Win! Thanks for playing!", True, (0, 0, 0)), (160, 200))

                if self.win_circle >= 1500:
                    exit()

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    Game()






