import pygame as pg
from random import choice
import os

pg.init()  # инициализация всех модулей pygame

# РАБОЧЕЕ ОКНО
screen = pg.display.set_mode((1200, 900))
pg.display.set_caption("Snake by Afonin")
screen.fill("grey")

# ИКОНКА 
icon = pg.image.load("icon.png")
pg.display.set_icon(icon)

# ЧАСЫ / FPS
clock = pg.time.Clock()

#  ШРИФТЫ 
title_font = pg.font.Font(None, 77)       # заголовок игры
menu_font = pg.font.Font(None, 80)        # меню / пауза
gameover_font = pg.font.Font(None, 70)    # конец игры
score_font = pg.font.Font(None, 40)       # счёт

#  СОСТОЯНИЯ ИГРЫ 
MENU = "menu"
GAME = "game"
PAUSE = "pause"
GAMEOVER = "gameover"
state = MENU  # текущее состояние игры

#  УРОВНИ СЛОЖНОСТИ 
levels = {"Лёгкий": 5, "Средний": 10, "Сложный": 15}  # FPS для уровней
level_names = list(levels.keys())
level_index = 0
FPS = levels[level_names[level_index]]

# РЕКОРД 
record_file = "record.txt"

# проверяем, есть ли файл с рекордом
if os.path.exists(record_file):
    with open(record_file, "r") as f:
        try:
            record = int(f.read())
        except:
            record = 0
else:
    record = 0

# СЧЁТ 
count = 0  # текущий счёт

#  ЕДА 
x_l = list(range(30, 1200 - 30, 30))
y_l = list(range(30, 900 - 30, 30))
x_e = choice(x_l)
y_e = choice(y_l)

#  ЗМЕЙКА 
x = 1200 // 2
y = 900 // 2
speed_x = 0
speed_y = 0
snake_body = []

# БОНУС УСКОРЕНИЯ 
bonus_active = False
bonus_timer = 0
BONUS_TIME = 3000  # миллисекунды

# ФУНКЦИЯ СБРОСА ИГРЫ 
def reset_game():
    global x, y, speed_x, speed_y, snake_body, count, x_e, y_e, bonus_active
    x, y = 1200 // 2, 900 // 2
    speed_x = speed_y = 0
    snake_body = [(x, y)]
    count = 0
    x_e, y_e = choice(x_l), choice(y_l)
    bonus_active = False

reset_game()
running = True

# ГЛАВНЫЙ ЦИКЛ 
while running:

    screen.fill("grey")  # фон

    # МЕНЮ 
    if state == MENU:
        title = title_font.render("ЗМЕЙКА", True, "black")
        screen.blit(title, (500, 150))

        start = menu_font.render("ENTER — играть", True, "black")
        level_text = menu_font.render(f"Сложность (UP/DOWN): {level_names[level_index]}", True, "black")
        record_text = menu_font.render(f"Рекорд: {record}", True, "black")
        exit_text = menu_font.render("ESC — выход", True, "black")

        screen.blit(start, (400, 350))
        screen.blit(level_text, (220, 450))
        screen.blit(record_text, (480, 520))
        screen.blit(exit_text, (420, 600))

    #ИГРА 
    elif state == GAME:
        # движение змейки
        x += speed_x
        y += speed_y
        snake_body.append((x, y))

        # съела ли еду
        if (x, y) == (x_e, y_e):
            count += 1  # увеличиваем счёт
            x_e, y_e = choice(x_l), choice(y_l)

            # каждые 5 очков → бонус ускорения
            if count % 5 == 0:
                bonus_active = True
                bonus_timer = pg.time.get_ticks()
        else:
            snake_body.pop(0)  # если не съела — удаляем хвост

        # проверка столкновений
        if x < 30 or x > 1170 or y < 30 or y > 870 or (x, y) in snake_body[:-1]:
            state = GAMEOVER
            # проверка на рекорд
            if count > record:
                record = count
                with open(record_file, "w") as f:
                    f.write(str(record))

        # бонус времени
        if bonus_active:
            if pg.time.get_ticks() - bonus_timer > BONUS_TIME:
                bonus_active = False

        # рисуем змейку
        for s in snake_body:
            pg.draw.circle(screen, (0, 100, 0), s, 15)

        # рисуем еду
        pg.draw.circle(screen, "red", (x_e, y_e), 15)

        # отображаем счёт
        score_text = score_font.render(f"Счёт: {count}", True, "black")
        screen.blit(score_text, (20, 20))

        # отображаем бонус
        if bonus_active:
            bonus_text = score_font.render("УСКОРЕНИЕ!", True, "blue")
            screen.blit(bonus_text, (500, 20))

    # ПАУЗА 
    elif state == PAUSE:
        pause_text = menu_font.render("ПАУЗА (P — продолжить)", True, "black")
        screen.blit(pause_text, (300, 400))

    #GAME OVER 
    elif state == GAMEOVER:
        over_text = gameover_font.render("Игра окончена", True, "black")
        score_final = score_font.render(f"Финальный счёт: {count}", True, "black")
        restart_text = score_font.render("R — заново | ESC — меню", True, "black")
        record_text = score_font.render(f"Рекорд: {record}", True, "black")

        screen.blit(over_text, (430, 300))
        screen.blit(score_final, (470, 380))
        screen.blit(restart_text, (420, 450))
        screen.blit(record_text, (530, 520))

    # СОБЫТИЯ 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN:

            # МЕНЮ 
            if state == MENU:
                if event.key == pg.K_RETURN:  # начать игру
                    FPS = levels[level_names[level_index]]
                    reset_game()
                    state = GAME
                elif event.key == pg.K_ESCAPE:  # выйти
                    running = False
                elif event.key == pg.K_UP:  # выбрать уровень выше
                    level_index = (level_index - 1) % len(level_names)
                elif event.key == pg.K_DOWN:  # выбрать уровень ниже
                    level_index = (level_index + 1) % len(level_names)

            # ИГРА
            elif state == GAME:
                if event.key == pg.K_p:  # пауза
                    state = PAUSE
                elif event.key == pg.K_RIGHT and speed_x >= 0:
                    speed_x, speed_y = 30, 0
                elif event.key == pg.K_LEFT and speed_x <= 0:
                    speed_x, speed_y = -30, 0
                elif event.key == pg.K_DOWN and speed_y >= 0:
                    speed_x, speed_y = 0, 30
                elif event.key == pg.K_UP and speed_y <= 0:
                    speed_x, speed_y = 0, -30

            # ПАУЗА
            elif state == PAUSE:
                if event.key == pg.K_p:  # продолжить
                    state = GAME

            # GAME OVER
            elif state == GAMEOVER:
                if event.key == pg.K_r:  # перезапуск игры
                    reset_game()
                    state = GAME
                elif event.key == pg.K_ESCAPE:  # вернуться в меню
                    state = MENU

    # КОНТРОЛЬ FPS С УЧЁТОМ БОНУСА 
    if state == GAME:
        if bonus_active:
            clock.tick(FPS + 5)  # ускорение
        else:
            clock.tick(FPS)
    else:
        clock.tick(10)  # меню / пауза / game over

    pg.display.flip()  # обновление экрана

pg.quit()
