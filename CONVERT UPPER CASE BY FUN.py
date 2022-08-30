'''
def upper(s):
    t=''
    for i in s:
        if i>='a' and i<='z':
            t+=chr(ord(i)-32)
        else:
            t+=i
    return t
x=upper('PyThoN*&f$5seHUreddy')
print(x)
'''
#COVERT UPPER CASE TO LOWER

def lower(s):
    t=''
    for i in s:
        if i>='A' and i<='Z':
            t+=chr(ord(i)+32)
        else:
            t+=i
    return t
x=lower("SEFYHUJInjm*f3#frg")
print(x)

#swapcase

def swapcase(s):
    t=''
    for i in s:
        if i>='a' and i<='z':
            t+=chr(ord(i)-32)
        elif i>='A' and i<='Z':
            t+=chr(ord(i)+32)
        else:
            t+=i
    return t
print(swapcase('SuHI&GTBhujr$#8k8'))
#print(x)
