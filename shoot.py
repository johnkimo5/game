from circleshape import CircleShape
import pygame
from constants import *

class Shot(CircleShape):
  SHOT_RADIUS = 5
  def __init__(self, x, y):
    super().__init__(x, y, self.SHOT_RADIUS)

  def draw(self, screen):
    # surface, color, center, radius, width
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt
  
