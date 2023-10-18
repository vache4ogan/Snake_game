import pygame
import random

pygame.init()

clock = pygame.time.Clock()
# Main Settings

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Змейка by Ваче')

ikon = pygame.image.load('ikon/free-icon-assasin-3426321.png')

pygame.display.set_icon(ikon)

sound = pygame.mixer.Sound('INTERWORLD_-_METAMORPHOSIS_73761657.mp3')

sound.play(loops = -1)
GREEn = (0, 128, 0)
RED = (255, 0, 0)
run = True

fps = 60

snake_x = 250
snake_y = 200

a_x = random.randint(10, 1270)
a_y = random.randint(10, 710)

x_change = 0
y_change = 0

snake = [(snake_x, snake_y)]
len_snake = 1

score = pygame.font.Font('ofont.ru_Cygre.ttf', 36)

while run:
    screen.fill((0, 0, 0))
    scoreTXT = score.render('Счет: ' + str(len_snake), False, (255, 255, 255))

    apple = pygame.draw.rect(screen, RED, [a_x, a_y, 20, 20])

    # snakeH = pygame.draw.rect(screen, GREEn, [snake_x, snake_y, 20, 20])
    [pygame.draw.rect(screen, GREEn, [x, y, 20, 20]) for x, y in snake]
    snake = snake[-len_snake:]

    if snake_x <= 0:
        snake_x = 1280
    elif snake_x >= 1280:
        snake_x = 0
    elif snake_y >= 720:
        snake_y = 0
    elif snake_y <= 0:
        snake_y = 720

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if x_change == -5:
                    continue
                x_change = 5
                y_change = 0
            elif event.key == pygame.K_LEFT:
                if x_change == 5:
                    continue
                x_change = -5
                y_change = 0
            elif event.key == pygame.K_DOWN:
                if y_change == -5:
                    continue
                x_change = 0
                y_change = 5
            elif event.key == pygame.K_UP:
                if y_change == 5:
                    continue
                x_change = 0
                y_change = -5

    snake_x += x_change
    snake_y += y_change

    if (pygame.draw.rect(screen, GREEn, [snake[-1][0], snake[-1][1], 20, 20])).colliderect(apple):
        del apple
        a_x = round(random.randint(20, 1260))
        a_y = round(random.randint(20, 700))
        len_snake += 1
        fps += 1
        print(len_snake)

    snake.append((snake_x, snake_y))
    snake[0] = (snake_x, snake_y)

    screen.blit(scoreTXT, (600, 20))

    pygame.display.update()

    clock.tick(fps)
