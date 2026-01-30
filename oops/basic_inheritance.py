class Animal:
    def speak(self):
        print('animal make sounds')

class dog(Animal):
    def bark(self):
        print('dogs bark')

dogs= dog()
dogs.speak()
dogs.bark()