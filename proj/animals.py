from objects import *
from manager import *

class Dog(Object):

    def __init__(self, name, pos, avatar, avatar_zoom=1):
        super().__init__(name, pos, avatar, avatar_zoom)
        self.hungary = 100
        self.bored = 0
        self.age = 1

    def step(self):
        if self.can_see(Region.TOY):
            self.bored = max(0, self.bored - 1)
        else:
            self.bored += 1
            self.hungary -= 1
            if self.bored > 30:
                self.set_target('toy')