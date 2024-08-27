from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y ,radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, self.radius, PLAYER_SHOT_BORDER_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
