'''
string='seshu reddy'
print(string[::-1])
'''
'''
strg='welcome'
print(strg[::3])
'''
'''
string='seshu reddy'
var=reversed(string)
for i in var:
    print(i,end='')
'''
'''
string='seshu reddy'
var=reversed(string)
print("".join(var))
'''
'''
string='seshu reddy'
empty_str=' '
i=len(string)-1
while i>=0:
    empty_str+=string[i]
    i-=1
print(empty_str)
'''
'''
string="python is good programming language"
s=string.split()#according to space
print(s)#form of list
print(' '.join(s[::-1]))#empty string contianib
g space


#language programming good is python
'''
'''
string="python is good programming language"
s=string.split()
l=[]
for i in s:
    l.append(i[::-1])
print(' '.join(l))


#nohtyp si doog gnimmargorp egaugnal

'''

'''
string="one two three four five six seven"
s=string.split()
print(s)
print(len(s))

'''
'''
i=0
l=[]
while i<len(s):
    if i%2==0:
        l.append(s[i])#bases on index
    else:
        l.append(s[i][::-1])
    i+=1
print(' '.join(l))

'''
'''
s='seshu'
i=0
while i<len(s):
    print(s[i])
    i=i+2
'''
'''
s='seshu reddy'
s1=s[1::2]
s2=s[0::2]
print(s1)
print(s2)
'''
s='B4A1D3'
alphabat_latters=[]
digits=[]
for ch in s:
    if ch.isalpha():
        alphabat_latters.append(ch)
    else:
        digits.append(ch)
print(''.join(sorted(alphabat_latters)+sorted(digits)))

        

        
        





















