 
def Fact(n):
    res=1
    for var in range(1,n+1):
        res*=var
    return res

num=145
temp=0

for n in str(num):
    v=int(n)
    temp+=Fact(v)
if num==temp:
    print("special number")
else:
    print("Not special number")


