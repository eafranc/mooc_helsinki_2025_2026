# Complete your game here
import pygame
from random import randint

"""
MineDropper game, 'developed' for advanced python course
Purpose: collect as many coins as possible
Spacebar drops a mine
Mines take 2 seconds to arm. After arming, they will kill both the player and enemies upon touch
Enemies spawn at random and will move towards you in a direct path 
"""

# Workaround for my shitty vscode STILL ignoring working directory settings
root = ""
if False:
    root = "C:\\Users\\danie\\AppData\\Local\\tmc\\vscode\\mooc-programming-25\\part14-01_own_game\\src\\"

# An entity in game which is represented by an image.
class GameRasterEntity: 
    def __init__(self, image: pygame.Surface, x: int = 0, y: int = 0):
        self._image = image
        self._hitbox = image.get_rect()
        self.x = x
        self.y = y
    @property
    def hitbox(self):
        return self._hitbox
    def draw(self, window: pygame.Surface):
        self._hitbox = window.blit(self._image, (self.x, self.y))
    def collides_with(self, other: GameRasterEntity):
        return self._hitbox.colliderect(other.hitbox)
    @property
    def center(self):
        return (
            self.x + 0.5 * self._image.get_width(),
            self.y + 0.5 * self._image.get_height()
        )
    @property
    def proximity_radius(self):
        return (self._image.get_height()**2 + self._image.get_width()**2)**0.5
    def __repr__(self):
        args = [
            self._image,
            self.x,
            self.y
        ]
        return f"Sprite({', '.join(args)})"

# Player entity, based on GameRasterEntity. Processes user input.
class Sprite(GameRasterEntity):
    def __init__(self, image: pygame.Surface, screen_width: int, screen_height: int, velocity: int = 2):
        super().__init__(image)
        self.velocity = velocity
        self.upkey = pygame.K_UP
        self.downkey = pygame.K_DOWN
        self.leftkey = pygame.K_LEFT
        self.rightkey = pygame.K_RIGHT
        self.toup = False
        self.todown = False
        self.toleft = False
        self.toright = False
        self.x_max = screen_width - self._image.get_width()
        self.y_max = screen_height - self._image.get_height()
        self.x_min = 0
        self.y_min = 0

    def process_events(self, event: pygame.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.leftkey:
                self.toleft = True
            if event.key == self.rightkey:
                self.toright = True
            if event.key == self.downkey:
                self.todown = True
            if event.key == self.upkey:
                self.toup = True

        if event.type == pygame.KEYUP:
            if event.key == self.leftkey:
                self.toleft = False
            if event.key == self.rightkey:
                self.toright = False
            if event.key == self.downkey:
                self.todown = False
            if event.key == self.upkey:
                self.toup = False

    def move(self):
        if self.toright and self.x < self.x_max:
            self.x += self.velocity
        if self.toleft and self.x > self.x_min:
            self.x -= self.velocity
        if self.toup and self.y > self.y_min:
            self.y -= self.velocity
        if self.todown and self.y < self.y_max:
            self.y += self.velocity

    def __str__(self):
        return f"Sprite"
    def __repr__(self):
        args = [
            self._image,
            self.x_max + self._image.get_width(),
            self.y_max + self._image.get_height(),
            self.velocity
        ]
        return f"Sprite({', '.join(args)})"

# Enemy entity, based on GameRasterEntity. Moves towards given GameRasterEntity.
class Hostile(GameRasterEntity):
    velocity = 1
    def __init__(self, image, x = 0, y = 0):
        super().__init__(image, x, y)
        self.hitpoints = 100
    def move_towards(self, target: GameRasterEntity):
        if self.center[0] < target.center[0]:
            self.x += self.velocity
        else:
            self.x -= self.velocity
        if self.center[1] < target.center[1]:
            self.y += self.velocity
        else:
            self.y -= self.velocity
    def hit(self, damage: int = 100):
        self.hitpoints -= damage
    @property
    def is_dead(self):
        return self.hitpoints <= 0

# Mine entity, based on GameRasterEntity. Takes 120 frames to arm.
class Mine(GameRasterEntity):
    def __init__(self, image, x = 0, y = 0):
        super().__init__(image, x, y)
        self.frames_to_armed = 120
    @property
    def is_armed(self):
        return self.frames_to_armed <= 0
    
    # Progress the arming timer one frame
    def move_timer(self):
        if self.frames_to_armed > 0:
            self.frames_to_armed -= 1

class MineDropper:
    def __init__(self):
        pygame.init()
        
        self.load_images()
        
        self.framerate = 60
        self.window = pygame.display.set_mode((1680, 1050))
        self.medium_font = pygame.font.SysFont("Arial", 24)
        self.small_font = pygame.font.SysFont("Arial", 12)
        self.big_font = pygame.font.SysFont("Arial", 60)
        pygame.display.set_caption("m00")

        self.new_game()
        self.clock = pygame.time.Clock()
        self.main_loop()

    # Creates a list of all drawables
    @property
    def all_drawables(self):
        return self.enemies + self.mines + self.coins
    
    # Restarts the game
    def new_game(self):
        self.time_elapsed = 0
        self.is_defeated = False
        self.score = 0
        self.enemies = []
        self.mines = []
        self.coins = []
        self.player = Sprite(self.images["robot"], self.window.get_width(), self.window.get_height(), 3)
        self.player.x = self.window.get_width() / 2
        self.player.y = self.window.get_height() / 2

    # Load images to self.images dict
    def load_images(self):
        self.images = {}
        for name in ["coin", "door", "monster", "robot"]:
            self.images[name] = pygame.image.load(root + name + ".png")
        
        #Generate mine image in memory, because we can't use any additional file resources :) 
        mine_radius = 15
        circle_surface = pygame.Surface((mine_radius*2, mine_radius*2), pygame.SRCALPHA)
        pygame.draw.circle(circle_surface, (255, 0, 0), (mine_radius, mine_radius), mine_radius, 3)
        pygame.draw.circle(circle_surface, (0, 0, 0), (mine_radius, mine_radius), mine_radius-3)
        self.images["mine"] = circle_surface

    # Main loop of the game
    def main_loop(self):
        while True:
            self.check_events()
            if not self.is_defeated:
                self.process_events()
                self.draw_window()
                self.clock.tick(self.framerate)

    # Process user input
    def check_events(self):
        for event in pygame.event.get():
            self.player.process_events(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F2:
                    self.new_game()
                if event.key == pygame.K_SPACE:
                    self.drop_mine()
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.QUIT:
                exit()

    # Deliver result of user input and let moving entities process time
    def process_events(self):
        self.possibly_spawn_enemy()
        self.possibly_spawn_coin()
        self.player.move()
        for eny in self.enemies:
            eny.move_towards(self.player)
            for mine in self.mines:
                if eny.collides_with(mine) and mine.is_armed:
                    #Both enemy and mine get destroyed
                    #TODO: multiple enemies and also player get destroyed by blast radius
                    #TODO: sympathic detonation of nearby mines in blast radius
                    self.mines.remove(mine)
                    eny.hit()
                    if eny.is_dead and eny in self.enemies:
                        self.enemies.remove(eny)
            if eny.collides_with(self.player):
                self.defeat()

        for mine in self.mines:
            if self.player.collides_with(mine) and mine.is_armed:
                self.defeat()
            mine.move_timer()
            
        for coin in self.coins:
            if self.player.collides_with(coin):
                self.score += 1
                self.coins.remove(coin)

    # Get a random spawn location which is not TOO close to the player
    def get_valid_spawn_location(self, imagename: str) -> tuple:
        def get_random_point(target: GameRasterEntity) -> tuple:
            return (
                randint(0, self.window.get_width() - target.hitbox.width),
                randint(0, self.window.get_height() - target.hitbox.height)
            )
        
        target = GameRasterEntity(self.images[imagename])
        total_radius = (self.player.proximity_radius + target.proximity_radius)*2
        #pick random coordinate, keep doing so until radius to player is sufficient
        loc = get_random_point(target)
        while pygame.math.Vector2(self.player.x, self.player.y).distance_to(loc) < total_radius:
            loc = get_random_point(target)
        return loc

    # Spawn a mine
    def drop_mine(self):
        self.mines.append(
            Mine(
                self.images["mine"], 
                self.player.center[0], 
                self.player.center[1]
            )
        )

    # 1:100 Spawn an enemy
    def possibly_spawn_enemy(self):
        if randint(0, 100) == 1:
            loc = self.get_valid_spawn_location("monster")
            self.enemies.append(Hostile(self.images["monster"], loc[0], loc[1]))

    # 1:200 Spawn a coin
    def possibly_spawn_coin(self):
        if randint(0, 200) == 1:
            loc = self.get_valid_spawn_location("coin")
            self.coins.append(GameRasterEntity(self.images["coin"], loc[0], loc[1]))

    # Draws game
    def draw_window(self):
        self.window.fill((120, 120, 120))
        self.player.draw(self.window)
        for ent in self.all_drawables:
            ent.draw(self.window)
        # Drawing this in Mine.draw() def override would be problematic due to 
        # transfer of font and framerate 
        for mine in self.mines:
            timer = self.small_font.render(f"{mine.frames_to_armed / self.framerate:.0f}", True, (255, 255, 255))
            self.window.blit(timer, 
                            (
                                 mine.center[0] - 0.5 * timer.get_width(), 
                                 mine.center[1] - 0.5 * timer.get_height()
                            )
                        )
            
        self.print_static_text()

        if self.is_defeated:
            game_text = self.big_font.render(f"Defeated! {self.score} coins collected", True, (255, 0, 0), (0, 0, 0))
            self.window.blit(game_text, (
                self.window.get_width() / 2 - 0.5 * game_text.get_width(),
                self.window.get_height() / 2 - 0.5 * game_text.get_height()
            ))

        pygame.display.flip()

    # Prints static texts in game screen
    def print_static_text(self):
        game_text = self.medium_font.render("Score: " + str(self.score), True, (255, 0, 0))
        self.window.blit(game_text, (25, 10))

        game_text = self.medium_font.render("F2 = new game", True, (255, 0, 0))
        self.window.blit(game_text, (200, 10))

        game_text = self.medium_font.render("Esc = exit game", True, (255, 0, 0))
        self.window.blit(game_text, (400, 10))

        game_text = self.medium_font.render("Spacebar = drop mine", True, (255, 0, 0))
        self.window.blit(game_text, (600, 10))

    # Set player to defeated
    def defeat(self):
        self.is_defeated = True

if __name__ == "__main__":
    MineDropper()