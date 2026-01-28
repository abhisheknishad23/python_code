class car:
    def details(self, brand, color):
        self.brand = brand
        self.color = color

    def show(self):
        print(f'This car is a {self.color} {self.brand}')

car1=car()
car1.details('Tata','yellow')

car2=car()
car2.details('BMW','black')

car1.show()
car2.show()