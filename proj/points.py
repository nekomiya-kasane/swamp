from objects import Object
from maps import *
import matplotlib.pyplot as plt

class Food(Object):

    def __init__(self, name, pos, quantity):
        super().__init__(name, pos, None)
        self.quantity = quantity

    def draw(self):
        plt.annotate(self.name, self.pos)
        g_map[self.pos[0], self.pos[1]] = Region.FOOD
        super().draw()

    def consume(self, quantity):
        self.quantity -= quantity
        self.quantity = max(0, self.quantity)

    def is_empty(self):
        return self.quantity == 0

class Toy(Object):

    def __init__(self, name, pos, avatar):
        super().__init__(name, pos, avatar)