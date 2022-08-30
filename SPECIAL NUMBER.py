n=int(input("Enter a number: "))#145
c=n
temp=0
while n>0:
    rem=n%10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    temp+=fact
    n//=10
if temp==c:
    print("Given number is special number")
else:
    print("Given number is not a special number")
