import pygame

pygame.init()
run = True

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Main Menu Project")

clock = pygame.time.Clock()

from Secondary_functions import Canvas, Character


# TEST.
test_font = pygame.font.Font(None, 30)
text_s1 = test_font.render('My Game', None, 'red')
text_s2 = test_font.render('Start The Game', None, 'red')
text_s3 = test_font.render('End The Game', None, 'red')
text_s4 = test_font.render('Name Your Character', None, 'red')

pygame.mixer.music.load('vtm.mp3')
# 

bg = Canvas()

screen.blit(bg.canvas1, (225,125))
pygame.display.flip()
pygame.time.wait(2000)
qr = pygame.mixer.music.play()


while run == True:
    #Prelude
    pygame.display.flip()
    screen.fill((0,0,0))
    screen.blit(bg.canvas2, (0,0))
  
    screen.blit(text_s1, (75,50))
    screen.blit(text_s2, (75,270))
    screen.blit(text_s3, (75,480))
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                screen = pygame.display.flip()
                qr = pygame.mixer.music.load('Lx.mp3')
                screen.fill((0,0,0))
                screen.blit(bg.canvas3, (0,0))
                screen.blit(text_s4, (250,150))
        elif event.type == pygame.QUIT:
            pygame.quit()
            run = False
exit()
