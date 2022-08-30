'''

s='AAABBBCCCDD'
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for k,v in d.items():
    print(f'{k}={v}')
'''
#input: 'AAABBBCCCDDD'
#output:A =3
#B =3
#C =3
#D =3
''' 
s='AAABBBCCCDDD'
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
print(d)
for k,v in d.items():
    print('{} ={}'.format(k,v))
'''
#input: ABAABBCA
#output:4A3bB1c
'''
s='ABAABBCA'
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
temp=' '
for k,v in d.items():
    temp=temp+str(v)+k
print(temp)

'''
#input:ABAABBCA
#output:4A3B1C
'''
def Alp(s):
    d={}
    for ch in s:
        if ch not in d:
            d[ch]=1
        else:
            d[ch]+=1
        temp=' '
        for k,v in d.items():
            temp+=str(v)+k
    return temp
x=Alp('ABAABBCA')
print(x)
        
'''
def Alp(s):
    d={}
    for ch in s:
        d[ch]=d.get(ch,0)+1
        temp=''
        for k,v in sorted(d.items()):
            temp+=k+str(v)
    return temp

x=Alp('KKFFABAABBCA')
print(x)
        



















