#prime number by using function
'''
def prime(n):
    if 1>=n:
        return False
    for x in range(2,n):
        if n%x==0:
            return False
    return True
num=7
if prime(num):
    print("prime")
else:
    print('not prime')
'''
#prime number by using bu normal way
'''
num=8
if 1<=num:
    check=0
    for x in range(2,num//2+1):
        if num%x==0:
            check=0
            break
    else:
        check=1
if check==1:
    print("prime")
else:
    print("not prime")
'''
#prime number in onther way
'''
n=1
if 0>=n:
    
    for i in range(2,n//2+1):
        if n%i==0:
            print("not prime")
            break
    else:
        print("prime")
else:
    print("not prime becauese it is less then one")


'''

#fibnosice number series in function
'''
def fib(n):
    f=0
    s=1
    if n==1 or n==2:
        return n-1
    for num in range(n-2):
        t=f+s
        f=s
        s=t
    return t
for x in range(1,10):
    v=fib(x)
    print(v,end=' ')

'''
#fibnosice number nth number
'''
n=9
f=0
s=1
for num in range(n-2):
    t=f+s
    f=s
    s=t
print(t)
'''
#fibnosice with recrsion
'''
def fib(n):
    if n==1 or n==2:
        return n-1
    return fib(n-1)+fib(n-2)
x=fib(3)
print(x)
'''
#factorial number
'''
n=5
fact=1
for i in range(1,n):
    fact+=fact*i
print(fact)
'''
'''

#factorail in function
'''
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
x=fact(7.9)
print(x)

'''

#factorial by math module
'''
import math
number=math.factorial(3)
print(number)
'''













































