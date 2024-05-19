class ObjectManager:

    def __init__(self):
        self.objects = []
        self.humans = []
        self.animals = []
        self.foods = []
        self.toys = []

    def find_nearest_toy(self, pos):
        return min(self.toys, key=lambda toy: toy.pos[0] - pos[0])
    
    def find_nearest_human(self, pos):
        return min(self.humans, key=lambda human: human.pos[0] - pos[0])