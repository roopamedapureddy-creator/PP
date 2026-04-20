class Bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        self.balance=self.balance-amount
    def display(self):
        print(self.name,"balance is",self.balance)
acc=Bankaccount("python",10000)
acc.deposit(666)
acc.withdraw(500)
acc.display()
