import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import main_state
import world_build_state

from boy import Boy
from zombie import Zombie

name = "RankingState"


def enter():
    hide_cursor()
    hide_lattice()


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and SDLK_ESCAPE:
            game_framework.change_state(world_build_state)


def update():
    pass


def draw():
    global font
    font = load_font('ENCR10B.TTF')
    font.draw()
