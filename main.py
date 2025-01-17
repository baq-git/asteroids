import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import *
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        for update_object in updatable:
            update_object.update(dt)

        for asteroid_object in asteroids:
            if asteroid_object.collision(player):
                print("Game over!")
                return

            for bullet in shots:
                if asteroid_object.collision(bullet):
                    bullet.kill()
                    asteroid_object.split()

        for draw_object in drawable:
            draw_object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
