from proj.object import Object

class HumanState:
    IDLE = 0

class Human(Object):
    def __init__(self, name, pos, avatar, avatar_zoom=1, type='owner'):
        super().__init__(name, pos, avatar, avatar_zoom)
        self.human_state = HumanState.IDLE
        self.emotion = 100
        self.dogfood = 0

    def 