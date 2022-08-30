N=1256
s=str(N)
temp=0
for i in range(len(s)):
    temp+=int(s[i])
print(temp)
print('-'*20)


n=124679
temp=0
while n>0:
    rem=n%10
    temp+=rem
    n//=10
print(temp)


#adding all even digits in given number 3467
n=346784
count=0
while n>0:
    rem=n%10
    if rem%2==0:
        count+=rem

print(count)
    
