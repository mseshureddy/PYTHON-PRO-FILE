#Prime number
'''
def Prime(n):
    if n<=1:
        return False
    for var in range(2,n//2+1):
        if n%var==0:
            return False
    return True
num=8
if Prime(num):
    print("prime")
else:
    print("Not Prime")

'''
#Prime number range
def Prime(n):
    if n<=1:
        return False
    for var in range(2,n):
        if n%var==0:
            return False
    return True


for num in range(1,100):
    
    if Prime(num):
        print(num)
