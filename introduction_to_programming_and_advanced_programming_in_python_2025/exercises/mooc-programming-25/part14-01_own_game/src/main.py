# Complete your game here
import pygame
from random import randint

class CoinGuardian:
    def __init__(self):
        """
        COIN GUARDIAN
        
        - The goal of the game is to capture all the monsters before they capture all the coins.
        - You win the game if you manage to capture all the monsters and there is still at least one coin on the screen.
        - You lose the game if the monsters have captured all the coins.
        - Before the game starts, the player can select values for the number of monsters, the number of coins, and the speed of the monsters.
        """
        pygame.init()

        self.configure_game() # this function works by user input and sets the number of coins, monsters, and the speed of the monsters
        # if the setup above is somehow inconvenient, the alternative is commenting the line above and uncommenting the following attributes:

        # self.num_coins = 10
        # self.num_monsters = 4
        # self.monster_speed = 1

        self.load_images()

        # Game general attributes
        self.width = 640
        self.height = 480
        self.window = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont("Arial", 24)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Coin Guardian")

        # useful dimensions for clamping and for the collision calculations
        self.robot_w = self.images["robot"].get_width()
        self.robot_h = self.images["robot"].get_height()
        self.monster_w = self.images["monster"].get_width()
        self.monster_h = self.images["monster"].get_height()
        self.coin_w = self.images["coin"].get_width()
        self.coin_h = self.images["coin"].get_height()

        self.new_game()
        self.main_loop()

    def configure_game(self):
        print("=== COIN GUARDIAN ===")
        print()

        try:
            coins_input = input("Number of coins (default 10): ")
            self.num_coins = int(coins_input) if coins_input else 10

            monsters_input = input("Number of monsters (default 4): ")
            self.num_monsters = int(monsters_input) if monsters_input else 4

            speed_input = input("Monster speed 1-3 (default 1): ")
            self.monster_speed = int(speed_input) if speed_input else 1
            self.monster_speed = max(1, min(3, self.monster_speed)) # clamp between 1 and 3

        except ValueError:
            print("Invalid input, using defaults...")
            self.num_coins = 10
            self.num_monsters = 4
            self.monster_speed = 1

        print()
        input("Press ENTER to start")

    def load_images(self):
        self.images = {
            "robot": pygame.image.load("robot.png"),
            "coin": pygame.image.load("coin.png"),
            "monster": pygame.image.load("monster.png")
        }

    def new_game(self):
        # robot begins in the center
        self.robot = {
            "x": self.width // 2,
            "y": self.height // 2 
        }

        # coins appear in random positions
        self.coins = []
        for i in range(self.num_coins):
            self.coins.append({
                "x": randint(0, self.width - self.coin_w), # coin dimensions (w x h in pixels) = 40 x 40
                "y": randint(0, self.height - self.coin_h)
            })

        # monsters appear in random position, but away from the robot
        self.monsters = []
        min_distance = 150 # minimum distance from the robot
        for i in range(self.num_monsters):
            while True:
                x = randint(0, self.width - self.monster_w) # monster dimensions (w x h in pixels) = 50 x 70
                y = randint(0, self.height - self.monster_h)

                # calculates the distance from the robot
                dx = x - self.robot["x"]
                dy = y - self.robot["y"]
                distance = (dx ** 2 + dy ** 2) ** 0.5

                if distance >= min_distance: # if the distance is valid, it quits the while loop
                    break
            self.monsters.append({"x": x, "y": y})

        self.robot_speed = 3
        # self.monster_speed = 1 # monster speed is set on function configure_game()
        self.game_over = False
        self.victory = False # if True = WIN, False = LOSE
        self.waiting_to_start = True # the game needs the user to press ENTER in order to start

    def main_loop(self):
        while True:
            self.check_events()

            if not self.game_over and not self.waiting_to_start:
                self.move_monsters()
                self.check_collisions()

            self.draw_window()
            self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.waiting_to_start: # on the game screen, the user must press ENTER to start the game
                    self.waiting_to_start = False
                if event.key == pygame.K_F2:
                    self.new_game()
                if event.key == pygame.K_ESCAPE:
                    exit()

        if self.waiting_to_start:
            return

        # continuous movement of the robot
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.robot["x"] -= self.robot_speed
        if keys[pygame.K_RIGHT]:
            self.robot["x"] += self.robot_speed
        if keys[pygame.K_UP]:
            self.robot["y"] -= self.robot_speed
        if keys[pygame.K_DOWN]:
            self.robot["y"] += self.robot_speed

        # clamping - keep the robot within the screen limits
        self.robot["x"] = max(0, min(self.width - self.robot_w, self.robot["x"])) # robot dimensions (w x h in pixels) = 50 x 86
        self.robot["y"] = max(0, min(self.height - self.robot_h, self.robot["y"]))

    def move_monsters(self):
        for monster in self.monsters:
            # if there are no coins, the monsters stay still
            if len(self.coins) == 0:
                continue

            # finds the closest coin
            closest_coin = None
            closest_distance = 9999 

            for coin in self.coins:
                dx = coin["x"] - monster["x"]
                dy = coin["y"] - monster["y"]
                distance = (dx ** 2 + dy ** 2) ** 0.5

                if distance < closest_distance:
                    closest_distance = distance
                    closest_coin = coin

            # move towards the closest coin
            if closest_coin:
                dx = closest_coin["x"] - monster["x"]
                dy = closest_coin["y"] - monster["y"]

                # adjust the movement
                if abs(dx) > 0:
                    monster["x"] += self.monster_speed if dx > 0 else - self.monster_speed
                if abs(dy) > 0:
                    monster["y"] += self.monster_speed if dy > 0 else - self.monster_speed

    def check_collisions(self):
        # 1. robot captures monster
        for monster in self.monsters[:]:
            if (self.robot["x"] < monster["x"] + self.monster_w and
                self.robot["x"] + self.robot_w > monster["x"] and
                self.robot["y"] < monster["y"] + self.monster_h and
                self.robot["y"] + self.robot_h > monster["y"]):
                self.monsters.remove(monster)

        # 2. monster captures coin
        for monster in self.monsters:
            for coin in self.coins[:]:
                if (monster["x"] < coin["x"] + self.coin_w and
                    monster["x"] + self.monster_w > coin["x"] and
                    monster["y"] < coin["y"] + self.coin_h and
                    monster["y"] + self.monster_h > coin["y"]):
                    self.coins.remove(coin)

        # 3. checks if all monsters were captured
        if len(self.monsters) == 0:
            self.game_over = True
            self.victory = True # Capture all the monsters = WIN
        elif len(self.coins) == 0:
            self.game_over = True
            self.victory = False # Monsters capture all the coins = LOSE

    def draw_window(self):
        self.window.fill((30, 30, 30)) # dark gray

        # draw coins
        for coin in self.coins:
            self.window.blit(self.images["coin"], (coin["x"], coin["y"]))

        # draw monsters
        for monster in self.monsters:
            self.window.blit(self.images["monster"], (monster["x"], monster["y"]))

        # draw robot
        self.window.blit(self.images["robot"], (self.robot["x"], self.robot["y"]))

        # draw score
        coins_saved = len(self.coins)
        monsters_left = len(self.monsters)
        yellow_rgb = (255, 255, 0)
        text = self.font.render(f"Coins: {coins_saved} | Monsters: {monsters_left}", True, yellow_rgb)
        self.window.blit(text, (10, 10))

        # instructions
        orange_rgb = (255, 130, 0)
        instructions = self.font.render("F2 = New Game | ESC = Quit", True, orange_rgb)
        self.window.blit(instructions, (10, self.height - 30))

        # start screen
        if self.waiting_to_start:
            message = "Press ENTER to start!"
            message_color = (255, 255, 255) # white
            text = self.font.render(message, True, message_color)
            text_x = self.width // 2 - text.get_width() // 2
            text_y = self.height // 2 - text.get_height() // 2
            pygame.draw.rect(self.window, (0, 0, 0), (text_x - 10, text_y - 10, text.get_width() + 20, text.get_height() + 20))
            self.window.blit(text, (text_x, text_y))

        # messages for the end of the game
        if self.game_over:
            if self.victory:
                message = f"VICTORY! Coins saved: {len(self.coins)}"
                message_color = (0, 255, 0) # green
            else:
                message = "GAME OVER! The monsters got all the coins!"
                message_color = (255, 0, 0) # red

            text = self.font.render(message, True, message_color)
            text_x = self.width // 2 - text.get_width() // 2
            text_y = self.height // 2 - text.get_height() // 2
            pygame.draw.rect(self.window, (0, 0, 0), (text_x - 10, text_y - 10, text.get_width() + 20, text.get_height() + 20))
            self.window.blit(text, (text_x, text_y))

        pygame.display.flip() # updates the screen

if __name__ == "__main__":
    CoinGuardian()
