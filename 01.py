from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, color, breed):
        self.color = color
        self.breed = breed

    @abstractmethod
    def call(self):
        pass

    def jump(self):
        return 'jumping'

    def run(self):
        return 'running'

    def walk(self):
        return 'walking'

    def sleep(self):
        return 'sleeping'
    
    @abstractmethod
    def generate(self):
        pass

class Cat(Animal):
    def clean(self):
        pass

    def call(self):
        return 'miew'

    @classmethod
    def generate(cls, dad, mom):
        return cls(
            color=dad.color + ' & ' + mom.color,
            breed=dad.breed + '-' + mom.breed
        )

class Dog(Animal):
    pass

mom_cat = Cat(color='black', breed='persian')
dad_cat = Cat(color='white', breed='scottish')

child_cat = Cat.generate(dad_cat, mom_cat)
print(child_cat.color, child_cat.breed)