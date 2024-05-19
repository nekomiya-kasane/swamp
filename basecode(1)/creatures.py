"""
creatures.py - class definitions for the creatures in FOP Assignment, Sem 1 2024

Written by : 
Student ID :

Includes:
    Puppy
    Person
    Friend (child class of Person)
    Stranger (child class of Person)
    Squirrel
    Animal

Versions:
    - initial version supplied 1/4/24
"""
import random
import matplotlib.pyplot as plt
import matplotlib.patches as pat

def flip_coords(pos, LIMITS):
    return((pos[1],pos[0]))

class Puppy():
    """
    Holds information and behaviour of puppy creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

    def step_change(self):
        validmoves = [(-1,0),(0,1),(1,1)]
        print(validmoves)
        move = random.choice(validmoves)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self ,ax, LIMITS):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0]-0.5, fpos[1]-0.5), radius=0.4, color=self.colour2)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0]+0.5, fpos[1]-0.5), radius=0.4, color=self.colour2)
        ax.add_patch(patch)

class Squirrel():
    """
    Holds information and behaviour of squirrel creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

    def step_change(self):
        validmoves = [(-1,0),(0,1),(1,1)]
        print(validmoves)
        move = random.choice(validmoves)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self ,ax, LIMITS):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0]-0.5, fpos[1]-0.5), radius=0.4, color=self.colour2)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0]+0.5, fpos[1]-0.5), radius=0.4, color=self.colour2)
        ax.add_patch(patch)

class Toy():
    """
    Multiple types of toys for puppy simulation
    """
    def __init__(self, name, colour, pos, vis):
        self.name = name
        self.colour = colour
        self.pos = pos
        self.visible = vis

    def get_pos(self):
        return self.pos

    def plot_me(self,ax, LIMITS):
        if self.visible:
            fpos = flip_coords(self.pos, LIMITS)
            patch = pat.Circle(fpos, radius=0.5, color=self.colour)
            ax.add_patch(patch)
        else:
            ax.annotate("X", self.pos, color=self.colour)

