#higest values in given list

l=[2,5,7,9,46,45,34]
h=l[0]
for i in l:
    if i>h:
        h=i
print(h)

print('-'*20)
#lowest value in given list

l=[2,5,7,9,46,45,34]
h=l[0]
for x in l:
    if i<h:
        h=i
print(h)
print('-'*20)
'''
l=[234,67,95,78,980]
h=l[0]
for i in l:
    if i>h:
        h=i
print(h)

l=[45,78,345,934,56,4]
h=l[0]
for i in l:
    if i<h:
        h=i
print(i)
'''
print('-'*20)
#higest values  in given list by using reduce,lambda functions
from functools import reduce
l=[5,6,3,8,29,7,8]
r=reduce(lambda x,y: x if x>y else y,l)
print(r)

print('-'*20)
#lowest value in given list by using reduce,lambda functions

from functools import reduce
l=[78,45,3,78,92,1]
r=reduce(lambda x,y: x if x<y else y,l)
print(r)

print('-'*20)

l=[78,45,3,78,92,1]
h=l[0]
for i in l:
    if i>h:
        h=i
print(h)

print('-'*20)
l=[78,45,3,78,92,1]
r=reduce(lambda x,y: x if x>y else y,l)
print(r)
print('-'*20)

l=[78,45,3,78,92,1]
x=max(l)
print(x)




    





































