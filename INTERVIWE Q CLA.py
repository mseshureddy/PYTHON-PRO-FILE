'''
n=12
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
print(l)

print('-'*10)

#remove duplicates in string
string='ENGINEERING'
emp_str=' '
for ch in string:
    if ch not in emp_str:
        emp_str+=ch
print(emp_str)

#Remove duplicates in list

list01=[10,30,20,10,40,50,20]
empty_list=[]
for i in list01:
    if i not in empty_list:
        empty_list.append(i)
print(empty_list)


#count of characters in given string withoutun

string='ENGINEERING'
y=string.split()
d={}
for i in string:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)

for k,v in d.items():
    print(f'{k}={v}')
'''

'''
string='we are what we are'
s=string.split()
d={}
for var in s:
    if var not in d:
        d[var]=1
    else:
        d[var]+=1
for keys, values in d.items():
    print(f'{keys}={values}')

'''
'''
string01="we are what we are"
string02=string01.split()
empty_dict={}
for var in string02:
    if var not in empty_dict:
        empty_dict[var]=len(var)
for k,v in empty_dict.items():
    print(f'{k}={v}')


'''

'''
string='we are what we are'
s=string.split()
d={}
for var in s:
    if var not in d:
        d[var]=1
    else:
        d[var]+=1

m=max(d.values())
for k,v in d.items():
    if m==v:
        print(m)
'''


'''
string='ENGINNERING'
d={}
for var in string:
    if var not in d:
        d[var]=len(var)
    else:
        d[var]+=1

m=max(d.values())
for k,v in d.items():
    if v==m:
        print(k)

'''
'''
S="we are in class"
L=S.split()[::-1]
print(' '.join(L))
'''

'''
s="we are in class"
s1=s.split()
print(s1)
for i in s1:
    print(i[::-1],end=' ')
'''
'''
l='seshu m'
for i in range(0,len(l)):
    print(i,end=' ')

l='seshu m'
for i in range(0,len(l)):
    print(l[i],end=' ')
'''
#find the second largest number in given list
number=[4,2,1,9,5,3,7,1,0,45]
if number[0]>number[1]:
    m,m2=number[0],number[1]
else:
    m,m2=number[1],number[0]

for x in number[2:]:
    if x>m2:
        if x>m:
            m2=m
            m=x
        else:
            m2=x
print(m2)










































