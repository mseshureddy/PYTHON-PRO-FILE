'''
s='a3z2c5'
s1=' '
for ch in s:
    if ch.isalpha():
        x=ch
    else:
        b=int(ch)
        s1+=x*b
l=sorted(s1)
print(''.join(l))
'''

#inpu=aaaabbbccz
#outpur=4a3b2c1z
'''
s='aaaabbbccz'
p=s[0]
out=' '
c=1
i=1
while i<len(s):
    if s[i]==p:
        c+=1
    else:
        out+=str(c)+p
        p=s[i]
        c=1
    if i==len(s)-1:
        out+=str(c)+p
    i+=1
print(out)
        
'''

string='a4k3b2'
s=' '
for i in string:
    if i.isalpha():
        s+=i
        x=i
    else:
        d=int(i)
        new= chr(ord(x)+d)
        s+=new
print(s)
































