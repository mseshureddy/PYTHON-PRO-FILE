#Prime number
'''
def Prime(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
num=8
if Prime(num):
    print("prime")
else:
    print("Not Prime")
'''
#write a programm to print prime number range
'''
def prime(number):
    if number<=1:
        return False
    for num in range(2,number):
        if number%num==0:
            return False
    return True
for i in range(1,100):
    if prime(i):
        print(i)
'''
#write a programm poly prime number or not
'''
def prime(digit):
    if digit<=1:
        return False
    for i in range(2,n//2+1):
        if digit%i==0:
            return False
    return True
n=13
rev=int(str(n)[::-1])
if rev!=n and prime(n) and prime(rev):
    print('pp')
else:
    print('not pp')

'''
#write a programm to range of poly prime numbers
'''
def prime(integer):
    if integer<=1:
        return False
    for var in range(2,integer//2+1):
        if integer%var==0:
            return False
    return True
for num in range(1,100):
    rev=(str(num)[::-1])
    if rev!=num and prime(num):
        print(num)
'''

#write a programm to given number is emrip or not?
'''
def prime(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
num=11
rev=int(str(num)[::-1])
if rev!=num and prime(num) and prime(rev):
    print("emrip")
else:
    print('not emrip')

'''
#range of emrip numbers
'''
def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
for num in range(1,500):
    rev=int(str(num)[::-1])
    if rev==num and prime(num) and prime(rev):
        print(num)
'''
#given number is factorial or not
'''
def fact(n):
    fact=1
    for i in range(1,n):
        fact=fact*i
    return fact
num=5
x=fact(num)
print(x)

'''
#given number is special number or not


'''
def fact(n):
    fact=1
    for i in range(1,n):
        fact+=fact*i
    return fact

num=146
temp=0
for var in str(num):
    c=int(var)
    v=fact(c)
    temp+=v
if temp==num:
    print('sp')
else:
    print("not sp")

'''
#range of special numbers
'''
def fact(number):
    fact=1
    for num in range(1,number):
        fact+=fact*num
    return fact

for i in range(1,150):
    temp=0
    while i>0:
        var=i%10
        v=fact(var)
        temp+=v
        var//=10
if temp==i:
    print(i)
    
'''
#Difference between higest  and lowest prime numbers

#find prime
#empty list
'''
def prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

l=[]
for var in range(1,100):
    if prime(var):
        l.append(var)
print(l[-1]-l[0])


'''
#poly prime

#rev==numer
#prime
'''
n=131
rev=int(str(n)[::-1])
if n>1 and rev==n:
    for i in range(2,n//2+1):
        if n%i==0:
            print("not pp")
            break
    else:
        print("pp")
else:
    print("not pp")

'''
#emrip number

#rev!=number
#prim(num)
#prim(rev)
'''
num=16
rev=int(str(num)[::-1])
if num>1 and rev!=num:
    for i in range(2,num):
        if num%i==0:
            print("not emrip")
            break
    else:
        print('emrip')
else:
    print('not emrip')
    
'''
'''
for num in range(1,100):
    rev=int(str(num)[::-1])
    if num>1 and rev!=num:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
'''
'''
s='Ab^&GVBrfh786$%&'
x=s.swapcase()
print(x)
'''
'''
string='seh09hu678hynu'
number=''
s=''
for ch in string:
    if ch.isalpha():
        s+=ch
    else:
        number+=str(ch)
print(number)
'''
#prime numbers in given string

#prime
#exract numbers

def prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

def exract(s):
    for i in s:
        if i>'0' and i<='9':
            if prime(int(i)):
                print(int(i))



exract('2njm7ngn5m9m4mj7mgb9jm3')








   
    




















        








    

































        








