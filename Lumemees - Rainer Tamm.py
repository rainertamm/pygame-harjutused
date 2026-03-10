import pygame

pygame.init()
aken = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Lumemees - Rainer Tamm")

tootab = True
while tootab:
    for syndmus in pygame.event.get():
        if syndmus.type == pygame.QUIT:
            tootab = False

    aken.fill((0, 0, 0))# Teeme tausta mustaks

    # Joonistame lumemehe 3 ringi (värv: valge, koordinaadid, suurus)
    pygame.draw.circle(aken, (255, 255, 255), (150, 230), 55)
    pygame.draw.circle(aken, (255, 255, 255), (150, 145), 42)
    pygame.draw.circle(aken, (255, 255, 255), (150, 80), 28)

    # Silmad (väikesed mustad ringid)
    pygame.draw.circle(aken, (0, 0, 0), (140, 72), 4)
    pygame.draw.circle(aken, (0, 0, 0), (160, 72), 4)

    # Nina (punane kolmnurk)
    pygame.draw.polygon(aken, (255, 0, 0), [(145, 82), (155, 82), (150, 97)])

    pygame.display.flip()

pygame.quit()