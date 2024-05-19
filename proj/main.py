import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import random

from proj.maps import *
import sys

if __name__ == '__main__':
    import json

    with open('objects.json' if len(sys.argv) > 1 else sys.argv[1]) as f:
        data = json.load(f)

    for animal in data['animals']:
        if animal['type'] == 'dog':
            object