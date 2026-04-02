import pygame
import sys

pygame.init()

# --- 1. SEADED JA VÄRVID ---
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ping-Pong")
clock = pygame.time.Clock()

# Hele taustavärv
lBlue = [153, 204, 255]
black = [0, 0, 0]

# --- 2. PILTIDE LAADIMINE JA SKALEERIMINE ---
# Palli seaded (suurus 20x20)
ballImage = pygame.image.load("ball.png")
ballImage = pygame.transform.scale(ballImage, [20, 20])
# Aluse seaded (suurus 120x20)
padImage = pygame.image.load("pad.png")
padImage = pygame.transform.scale(padImage, [120, 20])

# --- 3. RECT OBJEKTID JA ALGSEADED ---
# Palli koordinaadid ja kiirus
ball_x = screenX / 2
ball_y = screenY / 4
ball_speedX = 3
ball_speedY = 4

# Palli Rect
ball = pygame.Rect(ball_x, ball_y, 20, 20)

# Aluse koordinaadid ja kiirus
pad_width = 120
pad_x = (screenX / 2) - (pad_width / 2)
pad_y = screenY / 1.5
pad_speedX = 5  # Alus liigub horisontaalselt

# Aluse Rect
pad = pygame.Rect(pad_x, pad_y, pad_width, 20)

# Skoor
score = 0
font = pygame.font.SysFont("Arial", 36)

# --- 4. PEATSÜKKEL ---
gameover = False
while not gameover:
    clock.tick(60)

    # 4.1. Sündmuste kontroll
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # --- 5. LIIKUMISE LOOGIKA ---

    # 5.1. Palli liigutamine
    ball.x += ball_speedX
    ball.y += ball_speedY

    # Palli põrkamine seintest
    # Vasak/parem sein
    if ball.right > screenX or ball.left < 0:
        ball_speedX = -ball_speedX

    # Ülemine sein
    if ball.top < 0:
        ball_speedY = -ball_speedY

    # Alumine sein (Põrand)
    if ball.bottom > screenY:
        ball_speedY = -ball_speedY
        score -= 1  # NEGATIIVNE PUNKT!

    # 5.2. Aluse liigutamine (automaatne, nagu ülesandes "vahetab suunda, kui puudub seinu")
    pad.x += pad_speedX

    if pad.right > screenX or pad.left < 0:
        pad_speedX = -pad_speedX

    # --- 6. KOKKUPÕRKE TUVASTAMINE ---
    # Kui pall (ball Rect) puutub alust (pad Rect)
    if ball.colliderect(pad) and ball_speedY > 0:
        ball_speedY = -ball_speedY  # Muudame suuna tagasi üles
        score += 1  # POSITIIVNE PUNKT!

    # --- 7. JOONISTAMINE ---
    screen.fill(lBlue)

    # Joonistame pildid vastavalt Rect'ide asukohale
    screen.blit(ballImage, ball)
    screen.blit(padImage, pad)

    # Joonistame skoori
    score_text = font.render(f"Skoor: {score}", True, black)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()