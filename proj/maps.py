import numpy as np

g_map = None
g_time = 0

class Region:
    HOUSE = 0
    BACKYARD = 1
    WALL = 2
    FOOD = 3
    TOY = 4
    ANIMAL = 5
    HUMAN = 6

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = np.zeros((height, width), dtype=int)
        self.things = np.zeros((height, width), dtype=int)

    def set_object(self, pos, region):
        self.things[pos[0], pos[1]] = region

    def clear_objects(self):
        self.things = np.zeros((self.height, self.width), dtype=int)

def setup_map(width, height):
    global g_map
    if g_map is not None:
        return g_map
    
    width, height = int(width), int(height)
    g_map = Map(width, height)

    g_map.map[:,:] = Region.BACKYARD
    g_map.map[0:int(0.25*height),:] = Region.HOUSE
    g_map.map[0:3,:] = g_map.map[height-3:height,:] = Region.WALL
    g_map.map[:,0:3] = g_map.map[:,width-3:width] = Region.WALL

    return g_map

def step_time():
    global g_time
    g_time = (g_time + 0.01) % 24
    return g_time

def get_time():
    global g_time
    return g_time

def get_map():
    global g_map
    return g_map
