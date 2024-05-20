from maps import *
from objects import *

import matplotlib.pyplot as plt

class ObjectManager:

    def __init__(self):
        self.objects : list[Object] = []
        self.humans = []
        self.animals = []
        self.foods = []
        self.toys = []

    def find_nearest_toy(self, pos):
        return min(self.toys, key=lambda toy: toy.pos[0] - pos[0])
    
    def find_nearest_human(self, pos):
        return min(self.humans, key=lambda human: human.pos[0] - pos[0])
    
    def run(self):
        for i in range(10):
            self.plot_terrain()
            for o in self.objects:
                o.step()
                o.draw()
            self.plot_things()
            plt.pause(1)
            plt.clf()

    def plot_terrain(self):
        plt.imshow(get_map().map)

    def plot_things(self):
        pass            
    
manager = ObjectManager()

def get_manager():
    global manager
    return manager