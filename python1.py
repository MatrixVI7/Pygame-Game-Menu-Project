import pygame
#############################
#                                                     #
#############################

pygame.init()

screenwidth = 800
screenheight = 600

screen = pygame.display.set_mode((screenwidth, screenheight))
clock = pygame.time.Clock()
running = True


pygame.display.set_caption("TEST PROJECT")

walkRight = [pygame.image.load('PythonProject/R1.png'), pygame.image.load('PythonProject/R2.png'), pygame.image.load('PythonProject/R3.png'), pygame.image.load('PythonProject/R4.png'), pygame.image.load('PythonProject/R5.png'), pygame.image.load('PythonProject/R6.png'), pygame.image.load('PythonProject/R7.png'), pygame.image.load('PythonProject/R8.png'), pygame.image.load('PythonProject/R9.png')]
walkLeft = [pygame.image.load('PythonProject/L1.png'), pygame.image.load('PythonProject/L2.png'), pygame.image.load('PythonProject/L3.png'), pygame.image.load('PythonProject/L4.png'), pygame.image.load('PythonProject/L5.png'), pygame.image.load('PythonProject/L6.png'), pygame.image.load('PythonProject/L7.png'), pygame.image.load('PythonProject/L8.png'), pygame.image.load('PythonProject/L9.png')]
bg = pygame.image.load('PythonProject/bg.jpg')
char = pygame.image.load('PythonProject/standing.png')

x = 40
y=  400
width = 64
height = 64
vel = 5

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount

    screen.blit(bg, (0,0))

    if walkCount +1 >= 27:
        walkCount = 0
        
    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        screen.blit(char, (x,y))
        
    pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
    else:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
                right = False
                left = False
            else:
                jumpCount = 10
                isJump = False
                
    if keys[pygame.K_a] and x > 0:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_d] and x < screenwidth - width:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    redrawGameWindow()
    pygame.display.update()
    dt = clock.tick(60) / 1000

pygame.quit()
