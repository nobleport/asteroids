import pygame
from constants import *
from objects.asteroid import Asteroid
from objects.player import Player
from objects.asteroidfield import *
from objects.shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shootable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (shootable, drawable, updateable)
    
    field = AsteroidField()
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for obj in drawable:
            obj.draw(screen)
        for obj in updateable:
            obj.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print('Game over!')
                return
            for shot in shootable:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()
        pygame.display.flip()

        dt = timer.tick(60) / 1000
        
    

if __name__ == "__main__":
    main()