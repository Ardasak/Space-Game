import pygame
import math
import time
from pygame import mixer

pygame.init()
yazdır = True
x, y = 800, 600
start = False
Font = pygame.font.SysFont("Times New Roman", 50)
Font1 = pygame.font.SysFont(None, 40)
Font2 = pygame.font.SysFont(None, 25)
p1win = Font.render("Player1 won", True, (255, 255, 255))
p2win = Font.render("Player2 won", True, (255, 255, 255))
icon = pygame.image.load("ufo.png")
ekran = pygame.display.set_mode((x, y))
centered = ekran.get_rect(center=(x, y))
background = pygame.image.load("space.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Invader")
player1Img = pygame.image.load("spaceship.png")
player1x = 370
player1y = 480
bullet = pygame.image.load("bullet.png")
bullet1 = pygame.image.load("bulletreversed.png")
bullet1x = player1x
bullet1y = player1y
bullet1_state = "ready"
player2Img = pygame.image.load("battleship.png")
reversedplayer2 = pygame.image.load("battleshipreversed.png")
player2x = 370
player2y = 50
bullet2x = player2x
bullet2y = player2y
bullet2_state = "ready"
starttext = Font1.render("Start", 1, (0, 0, 0))
Yazı = Font.render("p1:", True, (255, 255, 255))
Yazı1 = Font.render("p2:", True, (255, 255, 255))
mixer.music.load("backgroundmusic.wav")
mixer.music.play(-1)
lasersound = mixer.Sound("laser.wav")
explosionsound = mixer.Sound("explosion.wav")
run = True
score = 0
score1 = 0
player1_shots = 0
player2_shots = 0


def player():
    ekran.blit(player1Img, (player1x, player1y))


def enemy():
    ekran.blit(player2Img, (player2x, player2y))


def fire_bullet(x, y):
    global bullet1_state

    bullet1_state = "fire"
    ekran.blit(bullet, (player1x + 16, bullet1y + 10))


def fire_bullet_1(x, y):
    global bullet2_state

    bullet2_state = "fire"
    ekran.blit(bullet1, (player2x + 16, bullet2y + 10))


def isCollision(player2x, player2y, bullet1x, bullet1y):
    distance = (math.sqrt(math.pow(player2x - bullet1x, 2))) + (
        math.pow(player2y - bullet1y, 2)
    )
    if distance < 27:
        explosionsound.play()
        return True

    else:
        return False


def isCollision1(player1x, player1y, bullet2x, bullet2y):
    distance1 = (math.sqrt(math.pow(player1x - bullet2x, 2))) + (
        math.pow(player1y - bullet2y, 2)
    )
    if distance1 < 27:
        explosionsound.play()
        return True

    else:
        return False


while run:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    ekran.blit(background, (0, 0))
    ellipse = pygame.draw.ellipse(ekran, (255, 255, 255), (333, 260, 100, 50))
    ekran.blit(starttext, (350, 270))
    if event.type == pygame.MOUSEBUTTONDOWN and ellipse.collidepoint(event.pos):
        start = True
    if start:
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            player1x -= 0.5
            bullet1x -= 0.5
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            player1x += 0.5
            bullet1x += 0.5
        ekran.fill((0, 0, 0))

        if player1x <= 0:
            player1x = 0
        elif player1x >= 736:
            player1x = 736
        if player1y <= 0:
            player1y = 0
        elif player1y >= 536:
            player1y = 536
        if pygame.key.get_pressed()[pygame.K_a]:
            player2x -= 0.5
            bullet2x -= 0.5
        if pygame.key.get_pressed()[pygame.K_d]:
            player2x += 0.5
            bullet2x += 0.5

        if player2x <= 0:
            player2x = 0
        elif player2x >= 736:
            player2x = 736
        if player2y <= 0:
            player2y = 0
        elif player2y >= 536:
            player2y = 536
        if pygame.key.get_pressed()[pygame.K_UP]:
            if bullet1_state == "ready":
                bullet1x = player1x
                lasersound.play()
                fire_bullet(bullet1x, bullet1y)
         
                player1_shots += 1
        if pygame.key.get_pressed()[pygame.K_w]:
            if bullet2_state == "ready":
                bullet2x = player2x
                lasersound.play()
                fire_bullet_1(bullet2x, bullet2y)
                player2_shots += 1
        collusion = isCollision(player2x, player2y, bullet1x, bullet1y)
        collusion1 = isCollision1(player1x, player1y, bullet2x, bullet2y)

        ekran.blit(background, (0, 0))
        player()
        enemy()
        if bullet1y <= 0:

            bullet1y = 480
            bullet1_state = "ready"
        if bullet1_state == "fire":

            fire_bullet(player1x, bullet1y)
            bullet1y -= 1
        if bullet2y >= 600:

            bullet2y = 50
            bullet2_state = "ready"
        if bullet2_state == "fire":

            fire_bullet_1(player2x, bullet2y)
            bullet2y += 1
        if collusion:
            bullet1y = 480
            bullet1_state = "ready"
            score += 1
        if score >= 3 or score1 >= 3:

            yazdır = False
            mixer.music.stop()
            explosionsound.stop()
            lasersound.stop()
            ekran.fill((0, 0, 0))
            pygame.draw.rect(ekran, (255, 255, 255), (390, 350, 100, 50))
            pygame.draw.rect(ekran, (255, 255, 255), (390, 290, 100, 50))
            yazı = Font1.render("Leave", 1, (0, 0, 0))
            yazı1 = Font1.render("Play", 1, (0, 0, 0))
            ekran.blit(yazı, centered)
            ekran.blit(yazı1, (400, 360))
            winner = Font1.render("Winner", 1, (255, 255, 255))
            loser = Font1.render("Loser", 1, (255, 255, 255))
            if score >= 3:
                score1 = -999
                ekran.blit(p1win, (300, 200))
                ekran.blit(winner, (70, 300))
                ekran.blit(player1Img, (80, 400))
                ekran.blit(loser, (640, 300))
                ekran.blit(reversedplayer2, (650, 400))
            elif score1 >= 3:
                score = -999
                ekran.blit(p2win, (300, 200))
                ekran.blit(loser, (70, 300))
                ekran.blit(player1Img, (80, 400))
                ekran.blit(winner, (640, 300))
                ekran.blit(reversedplayer2, (650, 400))

            player1_infos = Font2.render(
                f"Wasted bullets: {player1_shots}", 1, (255, 255, 255)
            )
            player2_infos = Font2.render(
                f"Wasted bullets: {player2_shots}", 1, (255, 255, 255)
            )
            ekran.blit(player1_infos, (60, 120))
            ekran.blit(player2_infos,(630,120))
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and 390 < mouse[0] < 490
                and 290 < mouse[1] < 340
            ):
                pygame.quit()
                quit()
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and 390 < mouse[0] < 490
                and 350 < mouse[1] < 400
            ):
                mixer.music.play(-1)
                score = 0
                score1 = 0
                player2x = 370
                player2y = 50
                player1x = 370
                player1y = 480
                player1_shots=0
                player2_shots=0
                yazdır = True

        if collusion1:
            bullet2y = 50
            bullet2_state = "ready"
            score1 += 1

        if yazdır:
            score2 = str(score)
            score3 = str(score1)
            score4 = Font.render(score2, True, (255, 255, 255))
            score5 = Font.render(score3, True, (255, 255, 255))
            ekran.blit(score4, (750, 50))
            ekran.blit(score5, (750, 0))
            ekran.blit(Yazı, (670, 50))
            ekran.blit(Yazı1, (670, 0))
            

    pygame.display.update()

pygame.quit()
