

import pygame
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape
import random   
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, ("white"), self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            a1 = self.velocity.rotate(angle)
            a2 = self.velocity.rotate(-angle)
            newN = self.radius - ASTEROID_MIN_RADIUS
            Asteroid.containers = self.containers
            asteroid1 = Asteroid(self.position.x, self.position.y, newN)
            asteroid1.velocity = a1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, newN)
            asteroid2.velocity = a2 * 1.2