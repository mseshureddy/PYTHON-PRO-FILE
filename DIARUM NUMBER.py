n=int(input("Enter a number:"))#135
c=n
count=len(str(n))
temp=0
while n>0:
    rem=n%10
    temp=temp+rem**count
    count=count-1
    n//=10
if temp==c:
    print("Given number is Disarum number")
else:
    print("Given number is not Disrum number")
