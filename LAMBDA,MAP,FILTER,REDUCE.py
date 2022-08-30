'''
l=['i','be','i','program']
l1=['am','st','n','ming']
print([i+j for i,j in zip(l,l1)])
#emp=list(map(lambda(i,j):i+j, zip(l,l1)))
#res = list(map(lambda(i, j): i + j, zip(l, l1)
'''



add=lambda a,b,c:a+b+c
print(add(2,3,5))

print('*'*20)

full_name=lambda fn,ln:fn+ln
print(full_name('seshu',' ''reddy'))
print('*'*20)

def multiple(n):
    return n-10
l=[10,20,30,40]
s=list(map(multiple,l))
print(s)
print('*'*20)

l=[10,20,30,40,50,50,40]
s=list(map(lambda n: n//10,l))
print(s)
set_form=set(s)
print(set_form)
print('*'*20)




def odd(n):
    return n%2==0
l=[2,4,6,9,4,7,3,9]
c=list(filter(odd,l))
print(c)

print('*'*20)

l=[2,4,6,9,4,7,3,9]
#s=list(filter(lambda i: i%2==0,l))
#s=list(filter(lambda v: v>4,l))
s=list(map(lambda x:x*10,filter(lambda x:x%2==0,l)))
print(s)

print('*'*20)

from functools import reduce
l=[4,5,6,1,2]
x=reduce(lambda q,y:q-y,l)
print(x)



















