import pygame
import sys

pygame.init()

# --- 1. SEADED JA VÄRVID ---
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ping-Pong - Ülesanne 6")
clock = pygame.time.Clock()

lBlue = [153, 204, 255]
black = [0, 0, 0]

# --- 2. MUUSIKA LAADIMINE ---
# Laeme taustamuusika ja paneme selle korduvalt mängima (-1)
try:
    pygame.mixer.music.load('taustamuusika.mp3')
    pygame.mixer.music.play(-1)
except pygame.error:
    print("Hoiatus: Muusikafaili 'taustamuusika.mp3' ei leitud!")

# --- 3. PILTIDE LAADIMINE JA SKALEERIMINE ---
ballImage = pygame.image.load("ball.png")
ballImage = pygame.transform.scale(ballImage, [20, 20])

padImage = pygame.image.load("pad.png")
padImage = pygame.transform.scale(padImage, [120, 20])

# --- 4. RECT OBJEKTID JA ALGSEADED ---
ball_speedX = 3
ball_speedY = 4
ball = pygame.Rect(screenX / 2, screenY / 4, 20, 20)

pad_width = 120
pad_speedX = 0  # Alus alguses seisab
pad = pygame.Rect((screenX / 2) - (pad_width / 2), screenY / 1.5, pad_width, 20)

score = 0
font = pygame.font.SysFont("Arial", 36)

# --- 5. PEATSÜKKEL ---
gameover = False
while not gameover:
    clock.tick(60)

    # 5.1. Sündmuste kontroll
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

        # Klahvi allavajutamine (määrame liikumise kiiruse)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pad_speedX = 6
            elif event.key == pygame.K_LEFT:
                pad_speedX = -6

        # Klahvi vabastamine (peatame aluse liikumise)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                pad_speedX = 0

    # --- 6. LIIKUMISE LOOGIKA ---

    # Aluse liigutamine
    pad.x += pad_speedX

    # Aluse piirid (ei lase ekraanilt välja)
    if pad.left < 0:
        pad.left = 0
    if pad.right > screenX:
        pad.right = screenX

    # Palli liigutamine
    ball.x += ball_speedX
    ball.y += ball_speedY

    # Palli põrkamine seintest (vasak, parem, üleval)
    if ball.right > screenX or ball.left < 0:
        ball_speedX = -ball_speedX
    if ball.top < 0:
        ball_speedY = -ball_speedY

    # Palli kukkumine alumisest äärest välja -> MÄNG LÄBI
    if ball.bottom >= screenY:
        print(f"Mäng läbi! Sinu lõppskoor: {score}")
        gameover = True  # Murrame tsüklist välja ja sulgeme akna

    # Kokkupõrge alusega
    if ball.colliderect(pad) and ball_speedY > 0:
        ball_speedY = -ball_speedY
        score += 1

        # --- 7. JOONISTAMINE ---
    screen.fill(lBlue)
    screen.blit(ballImage, ball)
    screen.blit(padImage, pad)

    score_text = font.render(f"Skoor: {score}", True, black)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()