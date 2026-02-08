import pygame
import time
import random


calors = ["green", "red", "yellow", "black", "white", "blue"]
# Инициализация конкретных модулей
pygame.init()  # Модуль для работы с окном

# Создание окна
screen = pygame.display.set_mode((800, 600))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) на весь экран

pygame.display.set_caption("Змейка")  # загаловок в рамке

# загрузка и установка иконки в рамке
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)


# цикл работы программы

raning = True
x, y = 300, 300
speed_x, speed_y = 3, 2

# контроль частоты работы кадров в секунду
FPS = 60
clock = pygame.time.Clock()
clock.tick(FPS)

# Создание объекта шрифта
font = pygame.font.Font(None, 74)  # Размер шрифта: 74

# Создание текстовой поверхности
text_surface = font.render("Hello, Pygame!", True, "black")


while raning:
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raning = False
    # Отображение текста
    screen.blit(text_surface, (200, 200))
    # elif event.type == pygame.MOUSEBUTTONDOWN:
    #     print(f"Клик мыши в позиции {event.pos}")
    # elif event.type == pygame.MOUSEMOTION:
    #     print(f"Движение мыши в позицию {event.pos}")

    # управление FPS
    # elif event.type == pygame.KEYDOWN:
    #     if event.key == pygame.K_UP:
    #         FPS += 5
    #         print(f"ТЕКУЩИЙ FPS = {FPS}")
    #     if event.key == pygame.K_DOWN:
    #         FPS -= 5
    #         print(f"ТЕКУЩИЙ FPS = {FPS}")

    screen.fill("grey")  # Заливка фона

    # отскок прямоугольника
    x += speed_x
    y += speed_y

    if x <= 0 or x >= 800 - 365:
        speed_x = -speed_x
    if y <= 0 or y >= 600 - 50:
        speed_y = -speed_y

    # Рисование прямоугольника
    pygame.draw.rect(screen, "RED", (x, y, 365, 50))

    # # управление прямоуголиником
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     x -= 3
    # if keys[pygame.K_RIGHT]:
    #     x += 3
    # if keys[pygame.K_UP]:
    #     y -= 3
    # if keys[pygame.K_DOWN]:
    #     y += 3

    # elif event.type == pygame.KEYDOWN:
    #     if event.key == pygame.K_LEFT:
    #         print("Нажата стрелка влево")
    #     elif event.key == pygame.K_RIGHT:
    #         print("Нажата стрелка вправо")
    #     elif event.key == pygame.K_UP:
    #         print("Нажата стрелка вверх")
    #     elif event.key == pygame.K_DOWN:
    #         print("Нажата стрелка вниз")
    #     elif event.key == pygame.K_TAB:
    #         print("Нажата стрелка TAB для смены цвета фона")
    #         screen.fill(random.choice(calors))

    # elif event.type == pygame.KEYUP:
    #     if event.key == pygame.K_LEFT:
    #         print("Отпущена стрелка влево")
    #     elif event.key == pygame.K_RIGHT:
    #         print("Отпущена стрелка вправо")
    #     elif event.key == pygame.K_UP:
    #         print("Отпущена стрелка вверх")
    #     elif event.key == pygame.K_DOWN:
    #         print("Отпущена стрелка вниз")
    #     elif event.key == pygame.K_TAB:
    #         print("Отпущена стрелка TAB для смены цвета фона")

    # pygame.draw.rect(surface, color, (x, y, width, height)) # фигура

    # pygame.draw.circle(screen, (0, 0, 255), (320, 240), 50) # Рисование круга

    # pygame.draw.line(screen, (0, 0, 255), (50, 50), (590, 430), 5) # линия

    # Отображение текста
    screen.blit(text_surface, (x, y))

    # Обновление экрана
    pygame.display.flip()

    # Контроль частоты кадров
    clock.tick(FPS)

# time.sleep(2)  # задержка


pygame.quit()
