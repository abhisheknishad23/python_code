from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(vehicle):
    def start(self):
        print('Car start with a key')

class Bike(vehicle):
    def start(self):
        print('Bike start with a button')

car = Car()
bike = Bike()

car.start()
bike.start()
