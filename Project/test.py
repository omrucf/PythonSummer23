import pygame

pygame.init()

SW = 1200
SH = 700

screen = pygame.display.set_mode((SW, SH))

pygame.display.set_caption("Test")
pygame.display.set_icon(pygame.image.load("icons/mainIcon.png"))

rect = pygame.Rect(570, 325, 50, 50)

run = True
while run:
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0, 255, 0), rect)

    key = pygame.key.get_pressed()

    if key[pygame.K_a] or key[pygame.K_LEFT]:
        rect.x -= 1
    elif key[pygame.K_d] or key[pygame.K_RIGHT]:
        rect.x += 1
    elif key[pygame.K_w] or key[pygame.K_UP]:
        rect.y -= 1
    elif key[pygame.K_s] or key[pygame.K_DOWN]:
        rect.y += 1

    if rect.x < 0:
        pygame.draw.rect(screen, (255, 0, 0), rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
