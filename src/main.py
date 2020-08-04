"""
    Main module to run the game.
"""
import pygame
from player import Player
from enemy import EnemyFleet, Enemy
from physics import Physics

class Engine:
    """
        Class to initialize, display and run game.
    """
    def __init__(self, config_file=None):
        """
            Method to initialize the Engine class.
        """
        pygame.init()
        self.running = True
        self.icon = pygame.image.load("assets/icon.png")
        self.background = pygame.image.load("assets/background.png")
        
        self.score_value = 0
        self.screen_text = pygame.font.Font('freesansbold.ttf', 32)

        self.screen = pygame.display.set_mode((800, 600))        
        pygame.display.set_caption("Space Invaders")
        pygame.display.set_icon(self.icon)

        self.player = Player()
        self.enemy_fleet = EnemyFleet(16)
        self.enemy_fleet.create_fleet()
        self.game_physics = Physics()

    def display(self):
        """
            Method to display everythinh on the screen.
        """
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        for enemy in self.enemy_fleet.enemy_register:
            self.screen.blit(enemy.image, tuple(enemy.position))
        self.screen.blit(self.player.image, tuple(self.player.position))
        for bullet in self.player.bullets:
            self.screen.blit(bullet.image, tuple(bullet.position))
        score = self.screen_text.render("Score : {}".format(self.score_value), True, (255, 0, 0))
        self.screen.blit(score, (10, 10))

    def update(self):
        """
            Method to update game states.
        """
        self.player.update()
        self.player.position, _ = self.game_physics.hitting_walls(self.player.position.copy())
        updated_bullet_list = []
        for enemy in self.enemy_fleet.enemy_register:
            isHit = self.game_physics.enemy_collision(enemy.position.copy(), 
                                                        self.player.position.copy())
            if isHit:
                self.running = False
                return

        for enemy in self.enemy_fleet.enemy_register:
            for bullet in self.player.bullets:
                isHit = self.game_physics.bullet_collision(enemy.position.copy(), 
                                                           bullet.position.copy())
                if isHit:
                    enemy.respawn()
                    self.score_value += 1
                    break

        for bullet in self.player.bullets:
            _, isHit = self.game_physics.hitting_walls(bullet.position.copy())
            if not isHit:
                bullet.update()
                updated_bullet_list.append(bullet)
        self.player.bullets = updated_bullet_list

        for enemy in self.enemy_fleet.enemy_register:
            enemy.update()
            enemy.position, isHit = self.game_physics.hitting_walls(enemy.position.copy())
            if isHit:
                enemy.velocity[0] *= -1
                enemy.move(1, axis=1)
            else:
                enemy.move(0, axis=1)

    def event_handler(self):
        """
            Method to handle events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False
                elif event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_LEFT:
                    self.player.move(-1)
                elif event.key == pygame.K_RIGHT:
                    self.player.move(1)
                elif event.key == pygame.K_SPACE:
                    self.player.fire()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.move(0)
                elif event.key == pygame.K_RIGHT:
                    self.player.move(0)

    def run(self):
        """
            Method to run the game engine.
        """
        while self.running:
            self.event_handler()
            self.update()
            self.display()
            pygame.display.update()

engine = Engine()
engine.run()