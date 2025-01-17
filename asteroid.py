import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        velocity_vec_1 = self.velocity.rotate(random_angle)
        velocity_vec_2 = self.velocity.rotate(-random_angle)

        smaller_new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, smaller_new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, smaller_new_radius)

        asteroid_1.velocity = velocity_vec_1 * 1.2
        asteroid_2.velocity = velocity_vec_2 * 1.2
