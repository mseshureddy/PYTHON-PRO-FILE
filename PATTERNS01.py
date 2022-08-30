n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i>=j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

print('*'*10)


n=5
star=1
for i in range(n):#rows
    for j in range(star):
        print('*',end=' ')
    star+=1
    print()
