import pygame

pygame.init()
screen = pygame.display.set_mode((900, 900))

clock = pygame.time.Clock()

x, y = 30, 30
radius = 25

running = True

while running:
    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, 'Red', (x, y), radius)
    
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_UP] and y - radius > 0:
        y -= 25
    if pressed[pygame.K_DOWN] and y + radius < 900:
        y += 25
    if pressed[pygame.K_RIGHT] and x + radius < 900:
        x += 25
    if pressed[pygame.K_LEFT] and x - radius > 0:
        x -= 20
    
    pygame.display.update()
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()