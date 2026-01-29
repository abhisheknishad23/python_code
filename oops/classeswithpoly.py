class bird:
    def sound(self):
        print('Birds make sounds')

class crow(bird):
    def sound(self):
        print('crow sy "cow cow"')
class parrot(bird):
    def sound(self):
        print('parrot sounds, ghop ghop')

bird1 = crow()
bird2 = parrot()

bird1.sound()
bird2.sound()