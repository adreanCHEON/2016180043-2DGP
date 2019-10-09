from pico2d import *


def cursor_show():
    global running
    global x, y
    ev = get_events()

    for event in ev:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, (1024 - 1) - event.y


def character_move():
    global direction
    global flag
    global a, b

    evnts = get_events()

    for event in evnts:
        if event.type == SDL_MOUSEBUTTONDOWN:
            for i in range(0, 100 + 1, 2):
                t = i/100
                p = (1 - t) * a + t * x
                q = (1 - t) * b + t * y
                character.clip_draw(frame * 100, 100 * 1, 100, 100, p, q)



open_canvas(1280, 1024)
background = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

running = True
x, y = 640, 512
frame = 0
direction = 0
flag=0
a, b = 640, 512
hide_cursor()

while running:
    clear_canvas()
    background.draw(640, 512)
    cursor.draw(x, y)
    if direction == 0:
        if flag == 0:
            character.clip_draw(frame * 100, 100 * 3, 100, 100, a, b)
        elif flag == 1:
            character.clip_draw(frame * 100, 100 * 2, 100, 100, a, b)
    update_canvas()
    frame = (frame + 1) % 8

    cursor_show()
    character_move()

close_canvas()
