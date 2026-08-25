'''
acquring the properties from one class to another class 

types:
single 
multi-level 
hierarchical 
multiple 
Hybrid


class A:
    def display1(self):
        print("This is class A display method")
class B(A):
    def display2(self):
        print("This is class B display method")
b = B()
b.display1()
b.display2()
'''
class A:
    def display1(self):
        print("This is class A display method")
class B(A):
    def display2(self):
        print("This is class B display method")
class C(B):
    def display3(self):
        print("This is class C display method")
b = C()
b.display1()
b.display2()
b.display3()