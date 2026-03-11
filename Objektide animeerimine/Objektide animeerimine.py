import pygame
import sys
import random

pygame.init()

# --- 1. SEADED JA PILTIDE LAADIMINE ---
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Autode animatsioon ja skoor")
clock = pygame.time.Clock()

# Värv teksti jaoks
MUST = [0, 0, 0]

# Piltide laadimine
taust = pygame.image.load("bg_rally.jpg")
punane_auto = pygame.image.load("f1_red.png")
sinine_auto = pygame.image.load("f1_blue.png")

# --- 2. MUUTUJAD JA ALGSEADED ---
# Punase auto asukoht (alla keskele)
punane_laius = punane_auto.get_rect().width
punane_x = (screenX / 2) - (punane_laius / 2)  # Keskel
punane_y = 380

# Skoori muutuja
skoor = 0
# Fondi seadistamine skoori jaoks
font = pygame.font.SysFont("Arial", 36)

# Siniste autode massiivi loomine (hoiame koordinaate ja kiirust)
# Õppematerjali eeskujul: coords = [[x, y, kiirus], [x, y, kiirus], ...]
sinised_autod = []

# Loome alguses näiteks 3 sinist autot suvalistesse kohtadesse
for i in range(3):
    # Autod jäävad tee vahemikku (tee x on umbes 150 kuni 450 vahel, sõltub pildist)
    x = random.randint(150, 450)
    # Alustavad erinevatelt kõrgustelt (isegi ekraanist kõrgemal, et kohe kõik korraga ei tuleks)
    y = random.randint(-400, -50)
    # Suvaline kiirus
    kiirus = random.randint(2, 5)

    # Lisame auto andmed listi
    sinised_autod.append([x, y, kiirus])

# --- 3. PEATSÜKKEL ---
gameover = False
while not gameover:
    clock.tick(60)  # 60 kaadrit sekundis

    # Ristist sulgemise kontroll
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # --- 4. GRAAFIKA JOONISTAMINE JA LOOGIKA ---

    # 4.1. Tausta joonistamine (see kustutab eelmise kaadri)
    screen.blit(taust, (0, 0))

    # 4.2. Punase auto joonistamine
    screen.blit(punane_auto, (punane_x, punane_y))

    # 4.3. Siniste autode animatsioon ja loogika
    for i in range(len(sinised_autod)):
        # Joonistame sinise auto tema [x, y] koordinaatidele
        screen.blit(sinine_auto, (sinised_autod[i][0], sinised_autod[i][1]))

        # Liigutame autot allapoole vastavalt tema kiirusele
        # sinised_autod[i][1] on y-koordinaat, sinised_autod[i][2] on kiirus
        sinised_autod[i][1] += sinised_autod[i][2]

        # Kui sinine auto jõuab ekraani alla
        if sinised_autod[i][1] > screenY:
            skoor += 1  # Lisame skoori!

            # Saadame auto uuesti üles ja muudame x-asukohta
            sinised_autod[i][1] = random.randint(-200, -50)  # y-asukoht üleval
            sinised_autod[i][0] = random.randint(150, 450)  # Uus x-asukoht teel
            sinised_autod[i][2] = random.randint(2, 5)  # Uus suvaline kiirus

    # 4.4. Skoori kuvamine
    # Teisendame arvu tekstiks: str(skoor)
    skoor_tekst = font.render("Skoor: " + str(skoor), True, MUST)
    # Joonistame teksti ekraanile (üles vasakule nurka)
    screen.blit(skoor_tekst, (10, 10))

    # --- 5. EKRAANI UUENDAMINE ---
    pygame.display.flip()

pygame.quit()