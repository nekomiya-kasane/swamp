import cv2
import numpy as np

g_map = None

class Region:
    HOUSE = 0
    BACKYARD = 1
    WALL = 2

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = np.zeros((height, width), dtype=int)

def setup_map(width, height):
    global g_map
    if g_map is not None:
        return g_map
    g_map = Map(width, height)

    g_map.map[:,:] = Region.BACKYARD
    g_map.map[0:int(0.25*height),:] = Region.HOUSE
    g_map.map[0:3,:] = g_map.map[height-3:height,:] = Region.WALL
    g_map.map[:,0:3] = g_map.map[:,width-3:width] = Region.WALL

    return g_map



