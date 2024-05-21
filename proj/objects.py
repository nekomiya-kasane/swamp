import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import random

from maps import *

g_directions8 = [(-1,0),(0,1),(0,1),(0,-1),(-1,1),(1,1),(1,-1),(-1,-1)]

class State:
    IDLE = 0
    MOVING = 1
    WANDERING = 2

class Object:
    def __init__(self, name, pos, avatar, avatar_zoom=0.025):
        self.name = name
        self.pos = pos
        self.state = State.IDLE
        self.velocity = 0
        self.target = None
        self.path = None
        self.avatar = OffsetImage(plt.imread(avatar), zoom=0.075) if avatar else None
        self.available_tiles = []
        self.enabled = True
        self.type = Region.ANIMAL
        self.destroy = False

    def draw(self):
        plt.annotate(self.name, (self.pos[1], self.pos[0]))
        box = AnnotationBbox(self.avatar, (self.pos[1], self.pos[0]), frameon=False)
        plt.gca().add_artist(box)

        get_map().things[self.pos[0], self.pos[1]] = self.type

    def set_target(self, target, velocity=1, callback=None):
        self.target = target
        self.velocity = velocity
        self.path = self.get_path()
        self.state = State.MOVING
        self.callback = callback

    def step(self):
        if self.state == State.MOVING:
            if self.target is None:
                return
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
            rmoved = self.pos[0] + random.choice([-1,0,1])
            cmoved = self.pos[1] + random.choice([-1,0,1])
            if get_map().map[rmoved, cmoved] in self.available_tiles:
                self.pos[0], self.pos[1] = [rmoved, cmoved]

    def can_see(self, what, rang=1):
        neighbor = get_map().map[
            self.pos[0] - rang : self.pos[0] + rang + 1, 
            self.pos[1] - rang : self.pos[1] + rang + 1
        ]
        for i in range(rang * 2 + 1):
            for j in range(rang * 2 + 1):
                if what == neighbor[i, j]:
                    return True
        return False
    
    def set_destroy(self):
        self.destroy = True
