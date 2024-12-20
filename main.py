import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shot

def main():
  # Initialize pygame object
  pygame.init()


  # Groups 
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  

  # Containers
  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  Shot.containers = (shots, updatable, drawable)

  # Instantiation
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  field = AsteroidField()
  dt = 0
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  # Game loop
  while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    black = (0, 0 ,0)
    screen.fill(color=black)
    for obj in drawable:
       obj.draw(screen)
    # Update step
    for obj in updatable:
       obj.update(dt)
    for obj in asteroids:
       if obj.collisions(player):
          print("Game over!")
          sys.exit()
       for shot in shots:
          if shot.collisions(obj):
             shot.kill()
             obj.split()
       
       
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    


if __name__ == "__main__":
  main()
