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


open_canvas(1280, 1024)
background = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

running = True
x, y = 640, 512
frame = 0
hide_cursor()

while running:
    clear_canvas()
    background.draw(640, 512)
    cursor.draw(x, y)
    update_canvas()

    cursor_show()

close_canvas()
