import pygame
import sys
import random

pygame.init()

# 1. SEADED JA PILTIDE LAADIMINE
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Autode animatsioon ja skoor")
clock = pygame.time.Clock()

MUST = [0, 0, 0]

taust = pygame.image.load("bg_rally.jpg")
punane_auto = pygame.image.load("f1_red.png")
sinine_auto = pygame.image.load("f1_blue.png")

# 2. MUUTUJAD JA ALGSEADED
punane_laius = punane_auto.get_rect().width
sinine_laius = sinine_auto.get_rect().width

tee_vasak_serv = 140
tee_parem_serv = 500

# Radade arvutamine
tee_laius = tee_parem_serv - tee_vasak_serv
raja_laius = tee_laius / 3

rada1_x = tee_vasak_serv + (raja_laius / 2) - (sinine_laius / 2)  # Vasak
rada2_x = tee_vasak_serv + raja_laius + (raja_laius / 2) - (sinine_laius / 2)  # Keskmine
rada3_x = tee_vasak_serv + (raja_laius * 2) + (raja_laius / 2) - (sinine_laius / 2)  # Parem

# Määrame punase auto täpselt keskmisele rajale!
punane_x = rada2_x
punane_y = 380

# Teeme nimekirja ainult vasakust ja paremast rajast siniste autode jaoks
rajad_sinistele = [rada1_x, rada3_x]

skoor = 0
font = pygame.font.SysFont("Arial", 36)

sinised_autod = []

#Loome 2 sinist autot (üks vasakule, teine paremale)
for i in range(2):
    x = rajad_sinistele[i]  # Esimene auto saab raja1_x, teine saab rada3_x
    y = random.randint(-600, -100)
    kiirus = random.randint(2, 5)
    sinised_autod.append([x, y, kiirus])

#3. PEATSÜKKEL
gameover = False
while not gameover:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #4. GRAAFIKA JOONISTAMINE JA LOOGIKA
    screen.blit(taust, (0, 0))
    screen.blit(punane_auto, (punane_x, punane_y))

    for i in range(len(sinised_autod)):
        screen.blit(sinine_auto, (sinised_autod[i][0], sinised_autod[i][1]))
        sinised_autod[i][1] += sinised_autod[i][2]

        # Kui sinine auto jõuab ekraani alla
        if sinised_autod[i][1] > screenY:
            skoor += 1

            # Saadame auto uuesti üles
            sinised_autod[i][1] = random.randint(-300, -50)

            # Hoiame auto endiselt tema isiklikul rajal (ainult äärmised rajad)
            sinised_autod[i][0] = rajad_sinistele[i]
            sinised_autod[i][2] = random.randint(2, 5)

    # Skoori kuvamine
    skoor_tekst = font.render("Skoor: " + str(skoor), True, MUST)
    screen.blit(skoor_tekst, (10, 10))

    # 5. EKRAANI UUENDAMINE
    pygame.display.flip()

pygame.quit()