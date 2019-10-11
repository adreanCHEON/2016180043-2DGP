from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def curve_move(p1, p2, p3, p4):
    global x, y

    # draw p1-p2
    for i in range(0, 50, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]

    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2

    # draw p3-p4
    for i in range(50, 100, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p2[0] + (-4 * t ** 2 + 4 * t) * p3[0] + (2 * t ** 2 - t) * p4[0]
        y = (2 * t ** 2 - 3 * t + 1) * p2[1] + (-4 * t ** 2 + 4 * t) * p3[1] + (2 * t ** 2 - t) * p4[1]

    # draw p4-p1
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p1[0] + (t ** 3 - t ** 2) * p2[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p1[1] + (t ** 3 - t ** 2) * p2[1]) / 2

    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = 0, 0
frame = 0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    curve_move((random.randint(0, 1280 - 1), random.randint(0, 1024 - 1)),
               (random.randint(0, 1280 - 1), random.randint(0, 1024 - 1)),
               (random.randint(0, 1280 - 1), random.randint(0, 1024 - 1)),
               (random.randint(0, 1280 - 1), random.randint(0, 1024 - 1)))
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()
