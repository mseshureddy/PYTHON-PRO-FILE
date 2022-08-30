#INPUT:seshureddyoie
#OUTPUT:
#E=3
#U=1
#O=1
#I=1

s='seshureddyoie'
SS=s.upper()
s1='AEIOU'
d={}
for ch in SS:
    if ch in s1:
        d[ch]=d.get(ch,0)+1

for k,v in d.items():
    print(f'{k}={v}')
        
print("*"*10)

s='seshuoareio'
A=s.upper()
d={'A','E','I','O','U'}
d1={}
for i in A:
    if i in d:
        d1[i]=d1.get(i,0)+1

for k,v in d1.items():
    print(f'{k}={v}')
    
        

