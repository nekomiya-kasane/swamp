"""
testToy.py - Toy test code for FOP Assignment


Written by : 
Student ID :

Usage:

Versions:
    - initial version supplied 1/4/24
"""
import numpy as np
import matplotlib.pyplot as plt

from creatures import Toy

def main():
    size = (20,20)
    yard = np.zeros(size)
    
    toy1 = Toy("Ball1", "green", (15,5), True)
    toy2 = Toy("Ball2", "green", (10,5), False)
    
    fig = plt.figure(figsize=(15,15))

    
    plt.imshow(yard, cmap="Blues_r")
    ax = plt.axes()
    toy1.plot_me(ax, size)
    toy2.plot_me(ax, size)
    plt.show()

if __name__ == "__main__":
    main()
