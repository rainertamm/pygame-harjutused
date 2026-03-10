import pygame

pygame.init()

# Ekraani seaded
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Harjutamine")

# 1. Piltide laadimine
bg = pygame.image.load("bg_shop.png")
chat = pygame.image.load("chat.png")
seller = pygame.image.load("seller.png")


# 2. Piltide mõõtmete muutmine (kasutame sinu suuruseid)
seller = pygame.transform.scale(seller, [260, 300])
chat = pygame.transform.scale(chat, [260, 200])

# 3. Teksti lisamine
font = pygame.font.Font(pygame.font.match_font('arial'), 24)
text = font.render("Tere, olen Rainer Tamm", True, [255, 255, 255])

# Mängutsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 4. Graafika kuvamine UUES JÄRJEKORRAS (jutumull eespool)

    # 4.1. Taust kõige alla
    screen.blit(bg, [0, 0])

    # 4.2. Mehike (joonistub esimesena, jääb taha)
    screen.blit(seller, [102, 165])

    # 4.3. Jutumull (joonistub mehikese peale, kuna on nimekirjas hiljem)
    screen.blit(chat, [245, 68])

    # 4.4. Tekst kõige peale, et oleks näha mulli sees
    screen.blit(text, [270, 140])

    pygame.display.flip()

pygame.quit()