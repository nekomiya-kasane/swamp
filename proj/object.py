import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import random

from proj.maps import *

g_directions8 = [(-1,0),(0,1),(0,1),(0,-1),(-1,1),(1,1),(1,-1),(-1,-1)]

class State:
    IDLE = 0
    MOVING = 1
    WANDERING = 2

class Object:
    def __init__(self, name, pos, avatar, avatar_zoom=1):
        self.name = name
        self.pos = pos
        self.state = State.IDLE
        self.velocity = 0
        self.target = None
        self.path = None
        self.avatar = OffsetImage(plt.imread(avatar), zoom=avatar_zoom)
        self.available_tiles = []

    def draw(self):
        plt.annotate(self.name, self.pos)
        box = AnnotationBbox(self.avatar, self.pos, frameon=False)
        plt.gca().add_artist(box)

    def set_target(self, target, velocity=1, callback=None):
        self.target = target
        self.velocity = velocity
        self.path = self.get_path()
        self.state = State.MOVING
        self.callback = callback

    def step(self):
        if self.target is None:
            return
        if self.state == State.MOVING:
            for i in range(self.velocity):
                self.pos = self.path.pop(0)
                if self.pos == self.target:
                    self.state = State.IDLE
                    if self.callback is not None:
                        self.callback()
                    return
            if type(self.target) == str:
                self.path = self.get_path()
        elif self.state == State.WANDERING:
            rmoved, cmoved = None, None
            while (rmoved is not None and cmoved is not None) or g_map.map[rmoved, cmoved] not in self.available_tiles:
                rmoved = self.pos[0] + random.choice([-1,0,1])
                cmoved = self.pos[1] + random.choice([-1,0,1])
            self.pos[0], self.pos[1] = [rmoved, cmoved]

            

