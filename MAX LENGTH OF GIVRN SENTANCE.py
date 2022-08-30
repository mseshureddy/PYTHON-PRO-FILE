'''
s='python is good programming language'
s1=s.split()
d={}
for i in s1:
    if i not in d:
        d[i]=len(i)

m=min(d.values())
print(m)
for k ,v in d.items():
    if v==m:
        print(k)
'''
def Maxword(s):
    s1=s.split()
    d={}
    for i in s1:
        if i not in d:
            d[i]=len(i)
    return d
x=Maxword('python is good programming language')
#print(x)
m=max(x.values())
#print(m)
for k,v in x.items():
    if m==v:
        print(k)


    
