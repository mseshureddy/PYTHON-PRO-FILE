n=int(input("Enter a number"))#135
c=n
temp=0
while n>0:
    rem=n%10
    temp=temp+rem
    n//=10
if c%temp==0:
    print("Given nuber is Harsad Number")
else:
    print("Given number is not a Hasrad number")
