import pygame
import random
import math

# initialize pygame
pygame.init()

# SCREEN CUSTOMIZATION
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('background.png')
pygame.display.set_caption("Monster Truck Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# PLAYER PROFILE
playerImage = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# ENEMY PROFILE
enemyImage = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy =6
for i in range (num_of_enemy):
    enemyImage.append(pygame.image.load('enemy.png'))
    enemyX.append( random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = ("ready")
score_val = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY=10
def show_score(x,y) :
    score = font.render("Score :" + str(score_val),True, (255,255,255))
    screen.blit(score ,(x, y))


def player(x, y):
    screen.blit(playerImage, (x, y))


def enemy(x, y,i):
    screen.blit(enemyImage[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = ("fire")
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# GAME LOOP INFINITE
running = True
while running:

    screen.fill((110, 10, 202))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if a keystroke is pressed check weather its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = + 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checking for boundaries for spaceship

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    for i in range(num_of_enemy):
        enemyX[i] += enemyX_change[i]
        if enemyX[i]<= 0:
            enemyX_change[i] = +3
            enemyY[i]+= enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_val += 1

            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)
    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    #collision


    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()
