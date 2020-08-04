import random
import pygame
from player import Player

class EnemyFleet:
    def __init__(self, number_enemies, config_file=None):
        self.enemy_register = []
        self.number_enemies = number_enemies

    def create_fleet(self):
        for _ in range(self.number_enemies):
            self.enemy_register.append(Enemy([random.randint(0, 736), random.randint(50, 150)]))

class Enemy(Player):
    def __init__(self, position, config_file=None):
        super(Enemy, self).__init__(config_file=config_file)
        self.image = pygame.image.load("assets/enemy.png")
        self.position = position
        self.velocity = [-1, 1]
        self.step = [3, 40]

    def reverse_motion(self):
        self.velocity[0] *= -1
    
    def respawn(self):
        self.position = [random.randint(0, 736), random.randint(50, 150)]