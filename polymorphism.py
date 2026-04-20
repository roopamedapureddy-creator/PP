class vechicles:
    def move(self):
        print("vechicles move")
class car(vechicles):
    def move(self):
        print("car used to drive")
class boat(vechicles):
    def move(self):
        print("boat sails in the river")
v1=car()
v2=boat()
v1.move()
v2.move()
