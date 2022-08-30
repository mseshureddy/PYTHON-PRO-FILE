n=11
star=1
space=n-1
for i in range(n):
    for j in range(space):
        print(' ',end=' ')
    for k in range(star):
        if k==0 or k+1==star or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    star+=1
    space-=1
print('--'*20)

n=11
star=n
space=0
for i in range(n):
    for j in range(space):
        print(' ',end=' ')
    for k in range(star):
        if k==0 or k+1==star or i==0:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    star-=1
    space+=1
