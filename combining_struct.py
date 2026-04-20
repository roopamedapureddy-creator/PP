class employee:
    def __init__(self,name):
        self.name=name
    def work(self):
        print("employee do the work")
class Developers(employee):
    def work(self):
        print(self.name,"Developers develops the code")
class Manager(employee):
    def work(self):
        print(self.name,"Manager manages the team")
def perform_work(emp):
    emp.work()
d=Developers("girls")
m=Manager("boys")
perform_work(d)
perform_work(m)
    
