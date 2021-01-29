# a method this is declared but doesn't have implementation.
# it require subclass to provide implementation.

from abc import ABC,abstractmethod

class Animal(ABC):

    @abstractmethod
    def eat(self):
        pass

class Tiger(Animal):
    def eat(self):
        print("Non veg")

obj = Tiger()
obj.eat()

#obj1 = Animal()
#obj1.eat()     #it will give error
