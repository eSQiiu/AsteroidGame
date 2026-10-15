import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
from player import Player
from logger import log_event   
import sys
from shot import Shot



def main():
    pygame.init()
    dt = 0.0
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}\n"
    f"Screen width: {SCREEN_WIDTH}\n"
    f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    Asteroid.containers = (asteroids, updatable, drawable,)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    points = 0
    game_over = False
    font = pygame.font.Font(None, 28)

    
    
    
    while True:
        
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        if not game_over:
            updatable.update(dt)
            for asteroid in asteroids:
                if player.collides_with(asteroid):
                    log_event("player_hit")
                    game_over = True
                    print("Game over!")
                for shot in shots:
                    if shot.collides_with(asteroid):
                        log_event("asteroid_shot")
                        points += 10
                        asteroid.split()
                        shot.kill()
                    
        for sprite in drawable:
            sprite.draw(screen)
        score_text = font.render(f"Points: {points}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        if game_over:
            game_over_text = font.render("Game Over!", True, (255, 0, 0))
            screen.blit(game_over_text, (SCREEN_WIDTH / 2 - game_over_text.get_width() / 2,
                                         SCREEN_HEIGHT / 2 - game_over_text.get_height() / 2))
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    
       
        
        
       


if __name__ == "__main__":
    main()
