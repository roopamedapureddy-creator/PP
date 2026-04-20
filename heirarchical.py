class vechicles:
    def move(self):
        print("vechicles moved")
class car(vechicles):
    def drive(self):
        print("cars to make a drive")
class bike(vechicles):
    def ride(self):
        print("bike to rides")
c=car()
c.move()
c.drive()
b=bike()
b.move()
b.ride()
