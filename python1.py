import pygame
fontType = None

pygame.init()
run = True

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Set my name!!")

clock = pygame.time.Clock()

#Piece of Shit
test_font = pygame.font.Font(fontType, 50)
text_surface = test_font.render('My Game', None, 'red')

qr = pygame.mixer.music.load('vtm.mp3')
# End of Shit, loaded music file for main menu.



class Character:

    def __init__(self):
        self.x = 45
        self.y = 45

class Canvas():

    def __init__(self):   
        self.canvas1 = pygame.image.load('WhiteWolfLogo.png')


        
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
