
'''
string='AAABBCCDDEEt'
s1=' '
for i in string:
    if i not in s1:
        s1+=i
print(s1)

'''
#2nd way
'''
string='AAAABBBBCCCDDD'
l=[]
for i in string:
    if i not in l:
        l.append(i)
v=''.join(l)
print(v)
'''
#3rd way

string='AAABBBCCCDDEEE'
s=set(string)
print(s)
v=''.join(s)
v1=sorted(v)
print(''.join(v1))
