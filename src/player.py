import pygame
from bullet import Bullet

class Player:
    def __init__(self, config_file=None):
        self.image = pygame.image.load("assets/player.png")
        self.position = [370, 480]
        self.velocity = [0, 0]
        self.step = [4, 4]
        self.bullets = []
    
    def move(self, speed, axis=0):
        """
            Method to increase velocity to move objects.
        """
        self.velocity[axis] = speed

    def update(self):
        """
            Method to update position.
        """
        self.position[0] += self.velocity[0]*self.step[0]
        self.position[1] += self.velocity[1]*self.step[1]
    
    def fire(self):
        """
            Method to fire bullets.
        """
        self.bullets.append(Bullet(self.position[0]))