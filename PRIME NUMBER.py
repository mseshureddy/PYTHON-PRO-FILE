'''
n=7
c=0
if n<=1:
    c=1
for i in range(2,n):
    if n%i==0:
        c=1
        break
if c==0:
    print("prime") 
else:
    print("not prime")
 
'''
'''
for num in range(20,31):
    c=0
    if num<=1:
        c=1
    for i in range(2,num):
        if num%i==0:
            c=1
            break
    else:
        if c==0:
            
            print(num)
'''
'''
n=1234
t=1
x=str(n)
for i in x:
    c=int(i)
    t=t*c
print(t)
'''
'''
n=23165
even=0
odd=1
x=str(n)
for i in x:
    number=int(i)
    if number%2==0:
        even+=number
    else:
        #odd=odd*number
        odd*=number
print("It is adding of even number: ",even)
print("It is multiple of odd numbers: ",odd)

'''
'''
n=23165
x=str(n)
l=list()
for i in x:
    number=int(i)
    if number>1:
        if (number%2)!=0:
            #print(number,end=' ')
            l.append(number)
print(l)
'''
'''
n=73165
x=str(n)
temp=0
for i in x:
    num=int(i)
    check=0
    if num<=1:
        check=1
    for var in range(2,num):
        if num%var==0:
            check=1
            break
    if check==0:
        temp+=num
print(temp)

'''
'''
n=73165
x=str(n)
for i in x:
    num=int(i)
    check=0
    if num<=1:
        check=1
    for var in range(2,num):
        if num%var==0:
            check=1
            break
    if check==0:
        print(num)
'''
'''
n=8
if 1<=n:
    check=0
    for i in range(2,n):
        if n%i==0:
            check=0
            break
    else:
        check=1
if check==1:
    print('prime')
else:
    print("not prime")


'''
#buy using funcion
def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
num=8
if prime(num):
    print("prime")
else:
    print("not prime")



































    


























