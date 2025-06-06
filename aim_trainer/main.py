import math
import random
import time
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")


class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR1 = "red"
    COLOR2 = "white"
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True
        
    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False
            
        if self.grow:
            self.size += self.GROWTH_RATE
            
        else:
            self.size -= self.GROWTH_RATE
            
    def draw(self, wind):
        pygame.draw.circle(wind, self.COLOR2, (self.x, self.y), self.size)
        pygame.draw.circle(wind, self.COLOR1, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(wind, self.COLOR2, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(wind, self.COLOR1, (self.x, self.y), self.size * 0.4)
            
        

def main():
    run = True
    targets = []
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
    pygame.quit()



if __name__ == "__main__":
    main()