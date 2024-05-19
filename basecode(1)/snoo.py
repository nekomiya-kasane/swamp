"""
snoo.py - base simulation for the FOP Assignment, Sem 1 2024

Written by : 
Student ID :

Usage:

Versions:
    - initial version supplied 1/4/24
"""
import numpy as np
import matplotlib.pyplot as plt

from creatures import Puppy, Squirrel, Toy

def plot_yard(ax, p):
    ax.imshow(p)


def build_yard(dims):
    
    plan = np.zeros(dims)
    plan[0:110,:] = 6
    plan[80,:] = 0
    plan[20:90,20:70] = 10
    return plan
   
def update_smells(smells, toys, creatures):
    np.where(smells>0, smells-1, 0)
    for t in toys:
        pos = t.get_pos()
        smells[pos[0], pos[1]] += 2
        smells[pos[0]-1:pos[0]+2,pos[1]-1:pos[1]+2] +=1
    for c in creatures:
        pos = c.get_pos()
        smells[pos[0], pos[1]] += 5

def main():
    size = (120,100)
    yard = build_yard(size)
    smells = np.zeros(size)
    
    snoopy = Puppy("Snoopy", "white/black", (5,15))
    rocky = Squirrel("RockY", "brown", (15,5))
    cast = [snoopy, rocky]

    toy1 = Toy("Ball1", "green", (15,5), True)
    toy2 = Toy("Ball2", "green", (10,5), False)
    toys = [toy1, toy2]

    for t in range(5):
        for c in cast:
            c.step_change()
        update_smells(smells, toys, cast)

        fig, axs = plt.subplots(1, 2, figsize=(30,15))
        plot_yard(axs[0], yard)
        for c in cast:
            c.plot_me(axs[0], size)
        axs[1].imshow(smells)
        plt.pause(4)
        plt.clf()

if __name__ == "__main__":
    main()
