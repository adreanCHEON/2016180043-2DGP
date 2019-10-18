import game_framework
import main_state

from pico2d import *

name = "PauseState"
image = None
blip = 0

def enter():
    global image
    image = load_image('pause.png')
    pass


def exit():
    global image
    del image
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()
    pass


def update():
    pass


def draw():
    global blip
    clear_canvas()
    main_state.draw()
    if blip == 0:
        image.draw(400, 300, 100, 100)
        delay(1)
        blip = 1
    else:
        blip = 0

    update_canvas()
    pass


