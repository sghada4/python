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
        
class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet("Tom","cat",['On Your Mat & Stay','Gentel'],"mio mio")
    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("Empty")
        return self

    def bathe(self):
        self.pet.noise()

my_treats = ['Pizza',"Humburger"]
my_pet_food = ['Cat Chow','Fancy Feast']
Asma = Ninja("Asma","Neji",my_treats,my_pet_food, Pet)
Asma.feed();
Asma.pet.play().noise().sleep()

    
        #  - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method
