import pygame
import python2

pygame.init()
run = True

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Set my name!!")

clock = pygame.time.Clock()

from python2 import Canvas, Character

#Piece of Shit
test_font = pygame.font.Font(None, 50)
text_surface = test_font.render('My Game', None, 'red')

qr = pygame.mixer.music.load('vtm.mp3')
# End of Shit, loaded music file for main menu.

bg = Canvas()

screen.blit(bg.canvas1, (100,50))
pygame.display.flip()
pygame.time.wait(2000)
pygame.mixer.music.play()


while run == True:
    #Prelude
    pygame.display.flip()
    screen.fill((0,0,0))
  
    screen.blit(text_surface, (350,250))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
pygame.quit()
exit()
