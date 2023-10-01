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

x = 50
y=  40
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))


    pygame.draw.rect(screen, (255,0,0), (x, y, width, height))

    keys = pygame.key.get_pressed()
    if not(isJump):
        
        if keys[pygame.K_w] and y > 0:
            y -= vel
        if keys[pygame.K_s] and y < 600 - height:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else:
                jumpCount = 10
                isJump = False
                
    if keys[pygame.K_a] and x > 0:
        x -= vel
    if keys[pygame.K_d] and x < screenwidth - width:
        x += vel

    pygame.display.update()
    dt = clock.tick(60) / 1000

pygame.quit()
