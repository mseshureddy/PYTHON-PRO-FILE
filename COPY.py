#copy
'''
l1=[10,20,30]
l2=l1
print('l1=',l1)
print('l2=',l2)
l2[0]=200
print(l1)
print(l2)

'''
'''
#shollowcopy
l1=[10,20,30]
l2=l1.copy()
print(id(l1))
print(id(l2))
print(l1)
print(l2)
l2[1]=200
print(l2)
print(l1)
'''

#deepcopy
'''
import copy
l1=[[10,20,30],[200,300]]
l2=copy.deepcopy(l1)
print(id(l1))
print(id(l2))

'''
'''
l1=[[10,20,30],[200,300]]
l2=l1.copy()
print(id(l1))
print(id(l2))
print(l1)
print(l2)
l1[1][0]=2000
print(l1)
print(l2)

'''
'''
l1=[[10,20,30],[40,50,60]]
l2=l1.copy()
print(l1)
print(l2)
print(id(l1))
print(id(l2))
l1[1][0]=4000
print(l2)
print(l1)
print(id(l1))
print(id(l2))

'''
 
l1=[10,20,30]
l2=l1.copy()
print(l1)
print(l2)
print(id(l1))
print(id(l2))



