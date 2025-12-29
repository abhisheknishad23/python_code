class Animal:
    def speaks(self): #abstrack method which will be overwritten
        pass


class Dog(Animal):
    def speaks(self):
        print("Barks")

class Cat(Animal):
    def speaks(self):
        print("Meow")

class Cow(Animal):
    def speaks(self):
        print("moo")

dog = Dog()
cat = Cat()
cow = Cow()

dog.speaks()
cat.speaks()
cow.speaks()