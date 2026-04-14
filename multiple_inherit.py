class parent:
    def mother(self):
        print("This is mother class")
class parent1:
    def father(self):
        print("This is father class")
class parents(parent,parent1):
    def child(self):
        print("This is the child class from mother and father")
p1=parents()
p1.mother()
p1.father()
p1.child()
