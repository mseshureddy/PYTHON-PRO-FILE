n=5
star=1
space=n-1
for i in range(n):
    for j in range(space):
        print(' ',end=' ')
    for k in range(star):
        print('*',end=' ')
    print()
    star+=2
    space-=1

print('-'*20)

n=5
star=2*n-1
space=0
for i in range(n):
    for j in range(space):
        print(' ',end=' ')
    for k in range(star):
        print('*',end=' ')

    print()
    star-=2
    space+=1
