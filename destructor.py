class destex:
    def __init__(self,name):
        self.name=name
        print("constructor called the",name)
    def __del__(self):
        print("Destructor called",self.name)
d1=destex("Ram")
del d1
