import pygame
import math
import time
from pygame import mixer

pygame.init()
print_value = True
x, y = 800, 600
start = False

Font = pygame.font.SysFont("Times New Roman", 50)
Font1 = pygame.font.SysFont(None, 40)
Font2 = pygame.font.SysFont(None, 25)

p1win = Font.render("Player1 won", True, (255, 255, 255))
p2win = Font.render("Player2 won", True, (255, 255, 255))

icon = pygame.image.load("ufo.png")
screen = pygame.display.set_mode((x, y))
centered = screen.get_rect(center=(x, y))
background = pygame.image.load("space.png")

pygame.display.set_icon(icon)
pygame.display.set_caption("Space Invader")

player1_img = pygame.image.load("spaceship.png")
player1_x = 370
player1_y = 480

bullet = pygame.image.load("bullet.png")
bullet_reversed = pygame.image.load("bulletreversed.png")
bullet1_x = player1_x
bullet1_y = player1_y
bullet1_state = "ready"

player2_img = pygame.image.load("battleship.png")
reversed_player2 = pygame.image.load("battleshipreversed.png")
player2_x = 370
player2_y = 50

bullet2_x = player2_x
bullet2_y = player2_y
bullet2_state = "ready"

start_text = Font1.render("Start", 1, (0, 0, 0))

p1text = Font.render("p1:", True, (255, 255, 255))
p2text = Font.render("p2:", True, (255, 255, 255))

mixer.music.load("backgroundmusic.wav")
mixer.music.play(-1)

laser_sound = mixer.Sound("laser.wav")
explosion_sound = mixer.Sound("explosion.wav")
run = True
score_player_1 = 0
score_player_2 = 0
player1_shots = 0
player2_shots = 0


def player():
    screen.blit(player1_img, (player1_x, player1_y))


def enemy():
    screen.blit(player2_img, (player2_x, player2_y))


def fire_bullet(x, y):
    global bullet1_state

    bullet1_state = "fire"
    screen.blit(bullet, (player1_x + 16, bullet1_y + 10))


def fire_bullet_1(x, y):
    global bullet2_state

    bullet2_state = "fire"
    screen.blit(bullet_reversed, (player2_x + 16, bullet2_y + 10))


def isCollisionPlayer2(player2_x, player2_y, bullet1_x, bullet1_y):
    distance = (math.sqrt(math.pow(player2_x - bullet1_x, 2))) + (
        math.pow(player2_y - bullet1_y, 2)
    )
    if distance < 27:
        explosion_sound.play()
        return True

    else:
        return False


def isCollisionPlayer1(player1_x, player1_y, bullet2_x, bullet2_y):
    distance1 = (math.sqrt(math.pow(player1_x - bullet2_x, 2))) + (
        math.pow(player1_y - bullet2_y, 2)
    )
    if distance1 < 27:
        explosion_sound.play()
        return True

    else:
        return False


while run:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(background, (0, 0))
    ellipse = pygame.draw.ellipse(screen, (255, 255, 255), (333, 260, 100, 50))
    screen.blit(start_text, (350, 270))

    if event.type == pygame.MOUSEBUTTONDOWN and ellipse.collidepoint(event.pos):
        start = True

    if start:
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            player1_x -= 0.5
            bullet1_x -= 0.5
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            player1_x += 0.5
            bullet1_x += 0.5

        screen.fill((0, 0, 0))

        if player1_x <= 0:
            player1_x = 0
        elif player1_x >= 736:
            player1_x = 736
        if player1_y <= 0:
            player1_y = 0
        elif player1_y >= 536:
            player1_y = 536

        if pygame.key.get_pressed()[pygame.K_a]:
            player2_x -= 0.5
            bullet2_x -= 0.5
        if pygame.key.get_pressed()[pygame.K_d]:
            player2_x += 0.5
            bullet2_x += 0.5

        if player2_x <= 0:
            player2_x = 0
        elif player2_x >= 736:
            player2_x = 736
        if player2_y <= 0:
            player2_y = 0
        elif player2_y >= 536:
            player2_y = 536

        if pygame.key.get_pressed()[pygame.K_UP]:
            if bullet1_state == "ready":
                bullet1_x = player1_x
                laser_sound.play()
                fire_bullet(bullet1_x, bullet1_y)
                player1_shots += 1

        if pygame.key.get_pressed()[pygame.K_w]:
            if bullet2_state == "ready":
                bullet2_x = player2_x
                laser_sound.play()
                fire_bullet_1(bullet2_x, bullet2_y)
                player2_shots += 1

        collusion_player_2 = isCollisionPlayer2(player2_x, player2_y, bullet1_x, bullet1_y)
        collusion_player_1 = isCollisionPlayer1(player1_x, player1_y, bullet2_x, bullet2_y)

        screen.blit(background, (0, 0))
        player()
        enemy()

        if bullet1_y <= 0:
            bullet1_y = 480
            bullet1_state = "ready"

        if bullet1_state == "fire":
            fire_bullet(player1_x, bullet1_y)
            bullet1_y -= 1

        if bullet2_y >= 600:
            bullet2_y = 50
            bullet2_state = "ready"

        if bullet2_state == "fire":
            fire_bullet_1(player2_x, bullet2_y)
            bullet2_y += 1

        if collusion_player_2:
            bullet1_y = 480
            bullet1_state = "ready"
            score_player_1 += 1

        if score_player_1 >= 3 or score_player_2 >= 3:
            print_value = False
            mixer.music.stop()
            explosion_sound.stop()
            laser_sound.stop()
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (255, 255, 255), (390, 350, 100, 50))
            pygame.draw.rect(screen, (255, 255, 255), (390, 290, 100, 50))
            leave_text = Font1.render("Leave", 1, (0, 0, 0))
            play_text = Font1.render("Play", 1, (0, 0, 0))
            screen.blit(leave_text, centered)
            screen.blit(play_text, (400, 360))
            winner = Font1.render("Winner", 1, (255, 255, 255))
            loser = Font1.render("Loser", 1, (255, 255, 255))

            if score_player_1 >= 3:
                score_player_2 = -999
                screen.blit(p1win, (300, 200))
                screen.blit(winner, (70, 300))
                screen.blit(player1_img, (80, 400))
                screen.blit(loser, (640, 300))
                screen.blit(reversed_player2, (650, 400))

            elif score_player_2 >= 3:
                score_player_1 = -999
                screen.blit(p2win, (300, 200))
                screen.blit(loser, (70, 300))
                screen.blit(player1_img, (80, 400))
                screen.blit(winner, (640, 300))
                screen.blit(reversed_player2, (650, 400))

            player1_infos = Font2.render(
                f"Wasted bullets: {player1_shots}", 1, (255, 255, 255)
            )

            player2_infos = Font2.render(
                f"Wasted bullets: {player2_shots}", 1, (255, 255, 255)
            )

            screen.blit(player1_infos, (60, 120))
            screen.blit(player2_infos,(630,120))

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
                score_player_1 = 0
                score_player_2 = 0
                player2_x = 370
                player2_y = 50
                player1_x = 370
                player1_y = 480
                player1_shots=0
                player2_shots=0
                print_value = True

        if collusion_player_1:
            bullet2_y = 50
            bullet2_state = "ready"
            score_player_2 += 1

        if print_value:
            p1scorestr = Font.render(str(score_player_1), True, (255, 255, 255))
            p2scorestr = Font.render(str(score_player_2), True, (255, 255, 255))
            screen.blit(p1scorestr, (750, 50))
            screen.blit(p2scorestr, (750, 0))
            screen.blit(p1text, (670, 50))
            screen.blit(p2text, (670, 0))
            
    pygame.display.update()

pygame.quit()
