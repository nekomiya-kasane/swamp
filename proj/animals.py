from objects import *
from manager import *

class DogState(State):
    EATING = 3

class Dog(Object):

    def __init__(self, name, pos, avatar, avatar_zoom=1):
        super().__init__(name, pos, avatar, avatar_zoom)
        self.hungary = 100
        self.bored = 0
        self.age = 1
        self.state = State.WANDERING
        self.available_tiles = [Region.BACKYARD, Region.DOG_HOUSE]

    def step(self):
        if self.state != State.IDLE:
            if self.can_see(Region.TOY):
                self.bored = max(0, self.bored - 1)
            else:
                self.bored += 1
            if self.bored > 30:
                self.set_target('toy')

        # Not sleeping and near food
        if self.state == DogState.EATING and self.can_see(Region.FOOD):
            if self.hungary <= 100:
                self.hungary += 1
            else:
                self.state = State.WANDERING
        elif self.state != State.IDLE and self.can_see(Region.FOOD) and self.hungary <= 10:
            self.state == DogState.EATING
        else:
            self.state = State.WANDERING
            self.hungary -= 1
        
        if self.hungary < 0:
            self.set_destroy()
            return

        self.age += 1

        if get_time() > 16 and self.target is not None:
            self.set_target("Dog House")
        
        if self.can_see(Region.DOG_HOUSE, 0):
            self.state = State.IDLE

        if get_time() >= 0 and get_time() <= 16 and self.state == State.IDLE:
            self.state = State.WANDERING
        
        super().step()

    def draw(self):
        super().draw()
        plt.annotate(f"({self.hungary}, {self.bored}, {self.age})", (self.pos[1], self.pos[0] + 2))
