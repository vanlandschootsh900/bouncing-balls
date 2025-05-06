#Shay VanLandschoot
#--DATE--#
# Pygame game template

import pygame
import sys
import config
import random

def init_game ():

    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) 
   
    
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True
class Circle:

    def __init__(self,rad,color):
        self.rad = rad
        self.color = color

        buffer=10

        self.x = random.randint(self.rad +buffer,config.WINDOW_HEIGHT- self.rad-buffer)
        self.y = random.randint(self.rad +buffer,config.WINDOW_HEIGHT- self.rad-buffer)
        self.change_x = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        self.change_y = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    def move(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x <= self.rad or self.x >= config.WINDOW_WIDTH - self.rad:
            self.change_x *= -1

        if self.y <= self.rad or self.y >= config.WINDOW_HEIGHT - self.rad:
            self.change_y *= -1

    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.rad)


def main():
    
    screen = init_game()
    clock = pygame.time.Clock()

    circles = [
        Circle(25, config.RED),
        Circle(30, config.GREEN),
        Circle(35, config.BLUE),
        Circle(40, config.PURPLE)
        ]
    airal = pygame.font.SysFont('airal',55)


    running = True
    while running:
        running = handle_events()

        for circle in circles:
            circle.move()

        screen.fill(config.WHITE) # Use color from config

        for circle in circles:
            circle.draw(screen)

        # Add code to draw stuff (for example) below this comment
  








        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
