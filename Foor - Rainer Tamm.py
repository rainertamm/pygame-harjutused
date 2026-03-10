import pygame

pygame.init()
aken = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Foor - Rainer Tamm")

tootab = True
while tootab:
    for syndmus in pygame.event.get():
        if syndmus.type == pygame.QUIT:
            tootab = False

    aken.fill((0, 0, 0))# Teeme tausta mustaks

    # Foori kast (hall raam)
    pygame.draw.rect(aken, (150, 150, 150), (100, 20, 100, 260), 2)

    # Kolm tuld (punane, kollane, roheline)
    pygame.draw.circle(aken, (255, 0, 0), (150, 65), 39)
    pygame.draw.circle(aken, (255, 255, 0), (150, 150), 39)
    pygame.draw.circle(aken, (0, 255, 0), (150, 235), 39)

    pygame.display.flip()

pygame.quit()