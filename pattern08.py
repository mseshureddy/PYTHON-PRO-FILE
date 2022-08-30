n=11
star=1
space=n//2
for i in range(n):
    for j in range(space):
        print(' ',end=' ')
    for k in range(star):
        if k==0 or k+1==star:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    if i<n//2:
        star+=2
        space-=1
    else:
        star-=2
        space+=1
