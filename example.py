class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("name is :",self.name)
        print("marks :",self.marks)
s=student("Roopa",90)
s.display()
