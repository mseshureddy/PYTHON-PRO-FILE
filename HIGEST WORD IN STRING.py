'''
string='pytho is good programming language'
result=max(string.split(),key=len)
print(result)
print("longest word length:" , len(result))

'''
'''
string="seshu reddy"
d={}
for i in string:
    if not i in d:
        d[i]=1
    else:
        d[i]+=1
for k,v in d.items():
    print(f'{k}={v}')
'''
#write program to print no.of times each word is repeating a string?
'''
string='we are python we developers'
x=string.split()
d={}
for var in x:
    if var not in d:
        d[var]=1
    else:
        d[var]+=1
for keys,values in d.items():
    print(f'{keys}={values}')
'''

'''
string='we are python we developers'
x=string.split()
d={}
for var in x:
    if var not in d:
        d[var]=len(var)
    
for keys,values in d.items():
    print(f'{keys}={values}')
'''


string='we are python we developers'
x=string.split()
d={}
for var in x:
    if var not in d:
        d[var]=1
    else:
        d[var]+=1
m=max(d.items())
for keys,values in d.items():
    if m==values:
print(m)
































