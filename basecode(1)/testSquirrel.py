"""
testSquirrel.py - Squirrel test code for FOP Assignment

Written by : 
Student ID :

Usage:

Versions:
    - initial version supplied 1/4/24
"""
import numpy as np
import matplotlib.pyplot as plt

from creatures import Squirrel

def main():
    size = (20,20)
    yard = np.zeros(size)
    
    rocky = Squirrel("RockY", "brown", (15,5))
    
    fig = plt.figure(figsize=(15,15))

    for t in range(5):
        rocky.step_change()
        plt.imshow(yard, cmap="Blues_r")
        ax = plt.axes()
        rocky.plot_me(ax)
        plt.pause(1)
        plt.clf()

if __name__ == "__main__":
    main()
