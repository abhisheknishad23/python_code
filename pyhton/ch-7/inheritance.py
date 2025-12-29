class parent:
    def __init__(self):
        self.super_attribut = True
        print("This is the parent class")

class Child(parent):
    def __init__(self):
        super().__init__()
        print("This is a child class")
        print(self.super_attribut)

child1 = Child()