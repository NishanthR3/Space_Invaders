import math
import pygame

class Physics:
    def __init__(self, config_file=None):
        self.boundary = [(0, 0), (736, 536)]
    
    def hitting_walls(self, position):
        """
            Method to increase velocity to move objects.
        """
        isHit = False
        if position[0] <= self.boundary[0][0]:
            isHit = True
            position[0] = self.boundary[0][0]
        elif position[0] >= self.boundary[1][0]:
            isHit = True
            position[0] = self.boundary[1][0]
        if position[1] <= self.boundary[0][1]:
            isHit = True
            position[1] = self.boundary[0][1]
        elif position[1] >= self.boundary[1][1]:
            isHit = True
            position[1] = self.boundary[1][1]
        return position, isHit

    def bullet_collision(self, enemy, bullet):
        distance = math.sqrt((enemy[0]-bullet[0])**2+
                             (enemy[1]-bullet[1])**2)
        return (distance<27)

    def enemy_collision(self, enemy, player):
        distance = math.sqrt((enemy[0]-player[0])**2+
                             (enemy[1]-player[1])**2)
        return (distance<27)