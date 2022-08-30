'''
s='malayalam'
s1=''
for i in s:
    if i not in s1:
        s1+=s[::-1]
if s==s1:
    print("palindrome")
else:
    print("not palindrome")
'''
'''
def palin(s):
    return s==s[::-1]

    
x=palin('malayalam')
if x:
    print('yes')
else:
    print('no')

'''
