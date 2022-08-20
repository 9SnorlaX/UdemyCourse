#Example

class Animal:
    def die(self):
        print("bye")
        self.health = 0

class Carnivour:
    def hunt(self):
        print("eating")
        self.satiety = 100

class Dog(Animal, Carnivour):
    def bark(self):
        print("woof-woof")

dog = Dog()
dog.bark()
dog.hunt()
dog.die()

class Animal:
    def set_health(self, health):
        print("set in animal")

class Carnivour(Animal):
    def set_health(self, health):
        print("set in carnivour")

class Mammal(Animal):
    def set_health(self, health):
        print("set in mammal")

class Dog(Mammal, Carnivour):
    pass


class Animal:
    def set_health(self, health):
        print("set in animal")

class Carnivour(Animal):
    def set_health(self, health):
        print("set in carnivour")

class Mammal(Animal):
    def set_health(self, health):
        print("set in mammal")

class Dog(Mammal, Carnivour):
    def set_health(self, health):
        Mammal.set_health(self, health)
        Carnivour.set_health(self, health)
        Animal.set_health(self, health)

        print("set in dog")

dog = Dog()
dog.set_health(10)

class Animal:
    def set_health(self, health):
        print("set in animal")

class Carnivour(Animal):
    def set_health(self, health):
        super().set_health(health)
        #Animal.set_health(self, health)
        print("set in carnivour")

class Mammal(Animal):
    def set_health(self, health):
        super().set_health(health)
        #Animal.set_health(self, health)
        print("set in mammal")

class Dog(Mammal, Carnivour):
    def set_health(self, health):
        super().set_health(health)
        #Mammal.set_health(self, health)
        #Carnivour.set_health(self, health)

        print("set in dog")

dog = Dog()
dog.set_health(10)

