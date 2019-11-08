from pico2d import *
import game_framework

# Bird Run Speed
PIXEL_PER_METER = (10.0 / 0.1) # 10pixel 10cm
RUN_SPEED_KMPH = 2.0 # Km/hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Bird:
    def __init__(self):
        self.frame = 0
        self.x, self.y = 1600 // 2, 500
        self.dir = 0
        self.act = 2
        self.image = load_image('bird_animation.png')

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        if self.dir == 0:
            self.x += 5
        elif self.dir == 1:
            self.x -= 5

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, self.act, 100, 100, self.x, self.y)
        if self.x == 1600:
            self.dir = 1
        elif self.x == 0:
            self.dir = 0
