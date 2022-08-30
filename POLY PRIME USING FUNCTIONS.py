
#Polyprime number
'''
def Prime(n):
    if n<=1:
        return False
    for x in range(2,n//2+1):
        if n%x==0:
            return False
    return True
num=11
rev=int(str(num)[::-1])
if rev==num and Prime(num):
    print("polyprime")
else:
    print("not polyprime")
'''
def Prime(n):
    if n<=1:
        return False
    for x in range(2,n//2+1):
        if n%x==0:
            return False
    return True
for num in range(20,500):
    rev=int(str(num)[::-1])
    if rev==num and Prime(num):
        print(num)
    
