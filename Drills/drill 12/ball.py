import game_framework
from pico2d import *
import game_world
import random


class Ball:
    def __init__(self):
        self.image = load_image('ball21x21.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw()
