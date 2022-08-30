#Highet values in list
'''
l=[10,30,55,47,38,93,8]
m=l[0]
for ind in range(1,len(l)):
    if m<l[ind]:
        m=l[ind]
print(m)

#lowest values in list
l=[10,30,55,47,38,93,8]
m=l[0]
for ind in range(1,len(l)):
    if m>l[ind]:
        m=l[ind]
print(m)
'''
'''
#LCM(least common factor)
a=12
b=15
res= a if a>b else b
while not (res%a==0 and res%b==0):
    res+=1
print(res)
#HCM 
a=4
b=6
res=a if a<b else b
while not (a%res==0 and b%res==0):
    res-=1
print(res)
'''
'''
def Fun(x):
    return 10*x
R=Fun(2)
print(f'R : {R}')

R=Fun(6)
print(f'R : {R}')

R=Fun(7)
print(f'R : {R}')

def Man(name,markes):
    print(f'Name : {name}')
    print(f'Marks: {markes}')
Man('seshu',90)

print('-'*10)
def Man(name,markes):
    print(f'Name : {name}')
    print(f'Marks: {markes}')
Man(name='seshu',markes=90)
print('-'*10)
Man(markes=90,name='seshu')

'''
def Fun(A,B,C):
    print(f'{A}={A}')
    print(f'{B}={B}')
    print(f'{C}={C}')
Fun(A=10,B=30,C)
#ERROR

def Fun(A,B,C):
    print(f'{A}={A}')
    print(f'{B}={B}')
    print(f'{C}={C}')
Fun(20,C=10,B=30)







