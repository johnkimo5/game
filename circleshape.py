import pygame
# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collisions(self, other):
        # implement checking for a collision
        # distance between the two objects
        distance = self.position.distance_to(other.position)
        total_radii = self.radius + other.radius
        if distance <= total_radii:
            return True
        return False
    