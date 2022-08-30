'''
n=7
check=0
if n<=1:
    check=1
for num in range(2,n):
        if n%num==0:
            check=1
            break
if check==0:
    print("prime")
else:
    print("not prime")
'''
'''
for i in range(20,31):
    check=0
    if i<=1:
        check=1
    for num in range(2,i):
        if i%num==0:
            check=1
            break
    else:
        if check==0:
            
            print(i)
'''
'''
n=12345
temp=0
x=str(n)
for i in x:
    number=int(i)
    temp+=number
print(temp)
        
'''
'''
n=123456
even=0
odd=1
s=str(n)
for string in s:
    number=int(string)
    if number%2==0:
        even+=number
    else:
        odd*=number
print(even,odd)

'''
'''
N=73164
x=str(N)
for num in x:
    number=int(num)
    check=0
    if number<=1:
        check=1
    for i in range(2,number):
            if number%i==0:
                check=1
                break
    if check==0:
        print(number)
'''
'''
number=2357

s=str(number)
temp=0
for char in s:
    num=int(char)
    check=0
    if num<=1:
        check=1
    for var in range(2,num):
        if num%var==0:
            check==1
            break
    if check==0:
        temp+=num
print(temp)

'''
'''
n=8
for i in range(2,n//2+1):
    if n%i==0:
        print("Given number is Not prime")
        break
else:
    print("Given number is prime")


'''




'''
n=1
if n>1:
    if n%2==0:
        print("Not prime")
    else:
        print("prime")

else:
    print("invalid")
    '''
'''
n=4
for i in range(2,n//2+1):
    if n%i==0:
        print("not prime")
        break
else:print("prime")

'''
'''
n=7
check=0
if n<=1:
    check=1
    for num in range(2,n):
        if n%num==0:
            check=1
            break
if check==1:
    print("prime")
else:
    print("not prime")

'''
'''
n=9
b=True
if n>1:
    for var in range(2,n//2+1):
        if n%var==0:
            b=False
            break
    if b:
        print("Prime")
    else:
        print("not prime")
else:
    print("not prime")
    print("not prime")
        
'''
'''
s=20
end=70
for var in  range(s,end+1):
    if var>1:
        for var2 in range(2,var//2+1):
            if var%var2==0:
                break
        else:
            print(var)
'''
'''
s=1
e=20

t=0
for _ in range(s,e+1):
    if _>1:
        b=True
        for var in range(2,_//2+1):
            if _%var==0:
                b=False
                break
        if b:
            if t%2!=0:
                print(_)
            t+=1
'''

#print a prime number by using functions

def prime(n):
    if n==1:
        return False
    for var in range(2,n+1):
        if n%var==0:
            return False
    return True
x=7
if prime(x):
    prime("prime")
else:
    print("Not prime")



