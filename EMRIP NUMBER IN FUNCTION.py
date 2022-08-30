'''
def prime(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True


num=13
rev=int(str(num)[::-1])
if prime(num) and rev!=num and prime(rev):
    print('emrip numer')
else:
    print('not emrip')
            
'''
'''
print("*"*20)

def primt(n):
    if n<=1:
        return False
    for i in range(1,n):
        if n%i==0:
            return False
    return True

num=12
rev=int(str(num)[::-1])
if rev==num and prime(num) and prime(rev):
    print("poly prime")
else:
    print('not poly prime')
'''
