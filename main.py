import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    dt = 0

    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    while True:
        screen.fill("white")

        for elem in updatable:
            elem.update(dt)

        for elem in drawable:
            elem.draw(screen)

        for elem in asteroids:
            player_collision = player.check_collision(elem)
            if player_collision:
                print("Game over!")
                return
            for shot in shots:
                shot_collision = shot.check_collision(elem)
                if shot_collision:
                    shot.kill()
                    elem.split()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()