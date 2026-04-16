class animals:
    def make_sound(self):
        print("Animals make sound")
class mammal(animals):
    def do_sound(self):
        print("Mammals do the sounds")
class cat(animals):
    def sound(self):
        print("Cats do the sound meow")
class Bat(mammal,cat):
    pass
b=Bat()
b.make_sound()
b.do_sound()
b.sound()
