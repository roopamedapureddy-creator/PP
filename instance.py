class numbers:
    def __inti__(self):
        self.x=100
    def display(self):
        y=40
        print("instance varaible",self.x)
        print("normal variable is",y)
n=numbers()
n.display()
print("outside method the value is",n.x)
print(y)
