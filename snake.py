import random
import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Game")
icon = pygame.image.load("snake_icon.png")
pygame.display.set_icon(icon)
snake_img = pygame.image.load("snake_image.png")
snakeX = 10
snakeY = 270
snakeX_change = 0
snakeY_change = 0
snake_angle = 0
apple_img = pygame.image.load("apple.png")
appleX = random.randint(0, 670)
appleY = random.randint(0, 528)
current_img = snake_img
game_over = pygame.font.Font("freesansbold.ttf", 64)
score_value = pygame.font.Font("freesansbold.ttf", 32)
count_score = 0
bg_img = pygame.image.load("bg_image.jpg")


def snake(x, y, angle):
    rotated_img = pygame.transform.rotate(current_img, angle)
    screen.blit(rotated_img, (x, y))


def apple(x, y):
    screen.blit(apple_img, (x, y))


running = True
while running:
    screen.blit(bg_img, (0, 0))
    score = score_value.render("Score: " + str(count_score), True, (255, 255, 255))
    screen.blit(score, (10, 10))
    snake(snakeX, snakeY, snake_angle)
    apple(appleX, appleY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snakeY_change = -0.2
                snakeX_change = 0
                snake_angle = 90
                current_img = snake_img
            if event.key == pygame.K_DOWN:
                snakeY_change = 0.2
                snakeX_change = 0
                snake_angle = -90
                current_img = snake_img
            if event.key == pygame.K_LEFT:
                snakeX_change = -0.2
                snakeY_change = 0
                snake_angle = 0
                current_img = pygame.transform.flip(snake_img, True, False)
            if event.key == pygame.K_RIGHT:
                snakeX_change = 0.2
                snakeY_change = 0
                snake_angle = 0
                current_img = snake_img
    snakeX += snakeX_change
    snakeY += snakeY_change
    if snakeX <= 0 or snakeX >= 670 or snakeY <= -60 or snakeY >= 528:
        snakeX = 1000
        over_text = game_over.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, (200, 250))
    distance = math.sqrt(
        (math.pow(appleX - snakeX, 2)) + (math.pow(appleY - snakeY, 2))
    )
    if distance < 50:
        count_score += 1
        appleX = random.randint(0, 670)
        appleY = random.randint(0, 528)
        apple(appleX, appleY)
    pygame.display.update()
