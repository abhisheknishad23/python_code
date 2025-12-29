#create a bus child classs that inherits from the vechile claaa. the default fare charge of any vechile is seating capacity*100. if vechicle is bus instance, we need to add an extra 10% on full fare as a maintenance charge. so total fare for bus instance will become the final amount = total fare + 10% of the total fare.

class Vechicle:

    def __init__(self, seating_capecity):
        self.seating_capecity = seating_capecity

    def get_fare(self):
        return self.seating_capecity * 100
    
class Bus(Vechicle):

    def __init__(self, seating_capecity):
        super().__init__(seating_capecity)

    def get_fare(self):
        Vechicle_fare = super().get_fare()
        maintenance_fare = 0.1*Vechicle_fare
        total_fare = Vechicle_fare + maintenance_fare
        return total_fare
    
Vechicle = Vechicle(50)
print("vechicle fare", Vechicle.get_fare())

bus1 = Bus(50)
print("bus fare:", bus1.get_fare())