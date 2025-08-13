import pygame
from constants import *
from player import Player
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    
    # set screen and clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # establish groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    #instantiate Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # GAME LOOP
    while True:
        for event in pygame.event.get():
            # exit if close the game window
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        updatable.update(dt)
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        # limit the FPS to 60
        dt = (clock.tick(60)) / 1000



if __name__ == "__main__":
    main()
