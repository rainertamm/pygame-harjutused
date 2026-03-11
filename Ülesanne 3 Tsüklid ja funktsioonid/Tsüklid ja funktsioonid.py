import pygame
import sys

pygame.init()

# 1. Värvid
L_GREEN = [153, 255, 153] # Taustavärv (nagu pildil)
RED = [255, 0, 0]         # Joone värv

# 2. Ekraani seaded
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Harjutamine")
screen.fill(L_GREEN)

# 3. Funktsioon ruudustiku joonistamiseks
def joonista_ruudustik(ruudu_suurus, ridade_arv, veergude_arv, joone_varv):

    joone_paksus = 2 # Pildil tunduvad jooned veidi paksemad kui 1 piksel

    # Joonistame horisontaalsed jooned (read)
    # Alustame 0-st ja lisame ühe rea võrra juurde, et ka alumine joon joonistuks
    for i in range(ridade_arv + 1):
        y = i * ruudu_suurus
        # pygame.draw.line(pind, värv, algus_koordinaat, lõpp_koordinaat, paksus)
        # Horisontaalne joon algab vasakust servast (x=0) ja lõppeb ruudustiku laiusel
        # Lõpp_x arvutatakse: veergude_arv * ruudu_suurus
        pygame.draw.line(screen, joone_varv, [0, y], [veergude_arv * ruudu_suurus, y], joone_paksus)

    # Joonistame vertikaalsed jooned (veerud)
    for j in range(veergude_arv + 1):
        x = j * ruudu_suurus
        # Vertikaalne joon algab ülevalt servast (y=0) ja lõppeb ruudustiku kõrgusel
        # Lõpp_y arvutatakse: ridade_arv * ruudu_suurus
        pygame.draw.line(screen, joone_varv, [x, 0], [x, ridade_arv * ruudu_suurus], joone_paksus)


# 4. Kutsun funktsiooni välja erinevate parameetritega
# Pildil tundub ruudu suurus olevat umbes 20-30 pikslit.
# Nii täidame kogu ekraani.
joonista_ruudustik(20, 24, 32, RED)

pygame.display.flip()

# 5. Mängu tsükkel (võimaldab ristist sulgeda)
gameover = False
while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

pygame.quit()