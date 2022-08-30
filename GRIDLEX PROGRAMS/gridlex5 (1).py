'''l=[32,32,30,32,14,10,30,30,32,30]
l1=sorted(list(set(l)))
print(l1[3])
'''

l=[1,2,3,4,5,6,7,8,9,10]
l1=sorted(l)
a=len(l1)//2
b=l.index(a)
if 8<l1[b]:
    for i in range(0,b+1):
        if l1[i]==8:
            print('present')
            break
    else:
        print('not present')
else:
    for i in range(b+1,len(l1)):
        if l1[i]==8:
            print('present')
            break
    else:
        print('not present')
