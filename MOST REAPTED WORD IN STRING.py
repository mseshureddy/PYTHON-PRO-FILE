
s='we are the are that we we we'
s1=s.split()
d={}
for i in s1:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
m=max(d.values())
for k,v in d.items():
    #print(f'{k}={v}')
    if m==v:
        print(f'{v}')
        
'''
def Higest(s):
    s1=s.split()
    d={}
    for i in s1:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1

    return d
x=Higest('we are the are that we we we')
#print(x)
m=min(x.values())
for k,v in x.items():
    if m==v:
        print(f'{k}={v}')

'''

































