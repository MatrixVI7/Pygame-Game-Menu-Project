import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0

pygame.display.set_caption("TEST PROJECT")

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height()/2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))


    pygame.draw.circle(screen, (255,0,0), player_pos, 40)

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.display.update()
    dt = clock.tick(60) / 1000

pygame.quit()
