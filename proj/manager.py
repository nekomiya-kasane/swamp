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
        self.to_destroy = []

    def find_nearest_toy(self, pos):
        return min(self.toys, key=lambda toy: toy.pos[0] - pos[0])
    
    def find_nearest_human(self, pos):
        return min(self.humans, key=lambda human: human.pos[0] - pos[0])
    
    def run(self):
        plt.figure(figsize=(15, 10))
        self.objects = self.humans + self.animals + self.foods + self.toys
        for i in range(100):
            self.plot_terrain()
            get_map().clear_objects()

            step_time()
            for o in self.objects:
                if o.destroy:
                    del o
                    continue
                if i != 0:
                    o.step()
                o.draw()
            self.plot_things()
            plt.title(f"Time: {get_time()}")
            if i != 0:
                plt.pause(1)

            plt.clf()
            

    def plot_terrain(self):
        plt.imshow(get_map().map)# + get_map().things)

    def plot_things(self):
        pass    
    
manager = ObjectManager()

def get_manager():
    global manager
    return manager