class A:
    def one(self):
        print("This is python")
class B(A):
    def two(self):
        print("this is oops")
class C(B):
    def three(self):
        print("this is multi-level")
obj=C()
obj.one()
obj.two()
obj.three()
