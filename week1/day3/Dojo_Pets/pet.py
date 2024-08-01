class Pet:
    def __init__(self, name , type , tricks, pet_noise  ):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.healh = 100
        self.energy = 100
        self.pet_noise= pet_noise
    def sleep(self):
        self.energy+=25
        return self
    def eat(self):
        self.energy+=5
        self.healh+=10
        return self

    def play(self):
        self.healh+=5
        return self
    def noise(self):
        print(self.pet_noise)
        return self
        

