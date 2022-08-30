'''
def Fun(n):
    if n==11:
        return
    print(n)
    Fun(n+1)
n=1
Fun(n)
'''
'''
def Fun(n):
    if n==0:
        return
    print(n)
    Fun(n-1)
n=10
Fun(n)
'''
'''
def Fun(n):
    if n==-11:
        return
    print(n)
    Fun(n-1)
n=-1
Fun(n)
'''
'''

def Fun(n):
    if n==-1:
        return
    print(n)
    Fun(n+1)
n=-10
Fun(n)
'''
'''
def add(n):
    if n==0:
        return 0

    
    return (n%10)+(n//10)




x=add(123)
print(x)
'''

'''
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
x=fact(5)
print(x)

'''


def fib(n):
    f=0
    s=1
    if n==1 or n==2:
        return n-1
    for x in range(n-2):
        t=f+s
        f,s=s,t
    return t
for num in range(1,6):
    x=fib(num)
    print(x)




def fib(n):
    f=0
    s=1
    if n==1 or n==2:
        return n-1
    for x in range(n-2):
        t=f+s
        f,s=s,t
    return t
num=5
print(fib(num)

























































