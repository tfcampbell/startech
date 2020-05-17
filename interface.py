import pygame
screen = pygame.display.set_mode((640, 400))
running = True
#https://pygame.readthedocs.io/en/latest/1_intro/intro.html
#set background colour
RED =(255, 0, 0)



#start the event loop
while running :
    for event in pygame.event.get():
        #quit event
        if event.type == pygame.QUIT:
            running = False

    #fill background colour
    screen.fill(RED)
    pygame.display.update()
pygame.quit()


