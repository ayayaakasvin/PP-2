import pygame

class ScreenProperties:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.screen = pygame.display.set_mode((self.x, self.y))

    def returnScreen(self):
        return self.screen
    
class CircleProperties:
    def __init__(self) -> None:
        self.radius = 25
        self.x = self.radius * 2
        self.y = self.radius * 2
        self.color = (255, 0, 0) # red color

    def drawTheCircle(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    

class Input(): # here you can play with settings if you want 
    def __init__(self, circle, screen) -> None:
        self.circle = circle
        self.x_boundary = screen.x
        self.y_boundary = screen.y
        self.MIN_DISTANCE_COEFFICIENT = 1.2 # minimum cf for circle to not go in boundary, but there is still line between circle and boundary due to resolution of window ig :/

    def ArrowPressed (self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT] and self.circle.x > (self.circle.radius * self.MIN_DISTANCE_COEFFICIENT): self.circle.x -= 20
        if pressed[pygame.K_RIGHT] and self.circle.x + (self.circle.radius * self.MIN_DISTANCE_COEFFICIENT) < self.x_boundary: self.circle.x += 20
        if pressed[pygame.K_UP] and self.circle.y > (self.circle.radius * self.MIN_DISTANCE_COEFFICIENT): self.circle.y -= 20
        if pressed[pygame.K_DOWN] and self.circle.y + (self.circle.radius * self.MIN_DISTANCE_COEFFICIENT) < self.y_boundary: self.circle.y += 20