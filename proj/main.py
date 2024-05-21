import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import random

from maps import *
from manager import *
from animals import *
from human import *
from points import *
import sys, os

if __name__ == '__main__':
    import json

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open('objects.json' if len(sys.argv) <= 1 else sys.argv[1]) as f:
        data = json.load(f)

    mgr = get_manager()
    for animal in data['animals']:
        if animal['type'] == 'dog':
            mgr.animals.append(Dog(animal['name'], animal['pos'], animal['avatar']))
            mgr.animals[-1].hungary = int(animal['hungary'])

    for human in data['humans']:
        mgr.humans.append(Human(human['name'], human['pos'], human['avatar']))

    # for food in data['foods']:
    #     mgr.humans.append(Food)
    for toy in data['toys']:
        mgr.toys.append(Toy(toy['name'], toy['pos'], toy['avatar']))

    setup_map(data['width'], data['height'])

    manager.run()

    # for food in data['']

    # for toy in data['toys']:
    #     mgr.toys.append(Toy())