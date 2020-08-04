import pygame

class Bullet:
    def __init__(self, position, config_file=None):
        self.image = pygame.image.load("assets/bullet.png")
        self.position = [position+16, 470]
        self.velocity = [0, -1]
        self.step = [0, 4]

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
    