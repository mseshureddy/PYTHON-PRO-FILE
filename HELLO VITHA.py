'''
s='Hello visa'
n=100
for i in range(1,1000):
    if i==n:
        print(f'{n}={s}')
        for i in range(2,10):
            m=n*i
            m1=s
            print(f'{m}={m1}')
        

'''
'''

from functools import reduce
def prime(num):
    if num<1:
        return "not prime number"
    for i in range(2,num//2+1):
        if num%i==0:
            return "not prime number"
    return "prime number"
print(prime(7))
l=[]
for i in range(1,100):
    if prime(i):
        l.append(i)
print(l)
print(2*"\n")
r=reduce(lambda x,y: x if x>y else y,l)
print("higest number:",r)
print(f'This is {r} higest value in my list')
'''

class TicketMixin:
    
    """ Mixin to calculate ticket price based on age """
    def calculate_ticket_price(self, age):
        
        ticket_price = 0
        price = ticket_price
        
        if self.age < 12:
            price = ticket_price + 0
        elif self.age < 18:
            price = ticket_price + 15
        elif self.age < 60:
            price = ticket_price + 20
        elif self.age >= 60:
            price = ticket_price + 10
        return price

class Customer(TicketMixin):
    """ Create instance of Customer """
    def __init__(self, name, age,):
        self.name = name
        self.age = age
    
    def describe(self):
        #return f"{self.name} age {self.age} ticket price is {self.calculate_ticket_price(self.age)}"
        return f"{self.name} age {self.age} tick price is {self.calculate_ticket_price(self.age)}"
        
customer = Customer("Ryan Phillips", 10)
print(customer.describe())





























































