import pygame
from pygame.locals import *

#set up font for labels
fonts = pygame.font.get_fonts()

#set up colour
RED = (255, 0, 0)
GRAY = (150, 150, 150)

#define 4 rectangles
#left, top, width, height
rect_study= Rect(40, 40, 300, 120)
rect_ballroom = Rect(40, 180, 300, 120)
rect_kitchen = Rect(370, 40, 300, 120)
rect_dining_hall = Rect(370, 180,300, 120)

#set up screen size
pygame.init()
w, h = 740, 380
screen = pygame.display.set_mode((w, h))
running = True

#load image
img = pygame.image.load('bird.png')
img.convert()
#resize the image
img = pygame.transform.scale(img, (60,60))
rect = img.get_rect()
#place in the Kitchen
rect.center=(w//1.4, h//2.9)

#event loop that creates an interface
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        screen.fill(GRAY)            
        pygame.draw.rect(screen, RED, rect_study)
        pygame.draw.rect(screen, RED, rect_kitchen)
        pygame.draw.rect(screen, RED, rect_dining_hall)
        pygame.draw.rect(screen, RED, rect_ballroom)
        screen.blit(img, rect)  
        pygame.display.update()

pygame.quit()