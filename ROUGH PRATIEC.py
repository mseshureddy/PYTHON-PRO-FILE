'''
s={'s','e','s','h','u'}
print(s)
l=list(s)
l.append('R')
print(l)
   
'''
'''
n=2021
if (n%4==0 or n%400==0) and (n%100)!=0:
    print("leap")
else:
    print("not leap")
'''
n=7
star=1
space=n//2
for i in range(n):
    for j in range(space):
        print(' ',end=' ')
    for k in range(star):
        if k==0 or k+1==star:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    if i<n//2:
        star+=2
        space-=1
    else:
        star-=2
        space+=1
