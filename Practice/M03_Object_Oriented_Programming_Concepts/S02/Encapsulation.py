'''
Data hiding:
Access specifiers
public 
protected(_)
private(___)
class A:
    a = 10
    _b = 20 
    __c = 30 

obj = A()
print(obj.a)
print(obj._b)
print(obj._A__c)
'''
class Bank:
    def __init__(self,balance):
        self.__balance = balance
    def credit(self,amount):
        self.__balance += amount
    def debit(self,amount):
        self.__balance -= amount
    def display(self):
        print("Current balance:",self.__balance)
b = Bank(1000)
b.display()
b.credit(1500)
b.display()
b.debit(500)
b.display()