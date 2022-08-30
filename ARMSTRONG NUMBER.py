n=int(input("Enter a number:"))#153
c=n
temp=0
count=len(str(n))
while n>0:
    rem=n%10
    temp=temp+rem**count
    n//=10
if temp==c:
    print("Given number is Disarumen number")
else:
    print("Given number is not disarum number")
    
            

            
