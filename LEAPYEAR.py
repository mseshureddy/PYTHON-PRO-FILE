'''
N=2024
if (N%100!=0 and N%4==0) or N%400==0:
    print("leap")
else:
    print("not leap")
'''
s1='python'
temp=0
for i in s1:
    temp+=1
s2=' '
for j in range(-1,-temp-1,-1):
    s2+=s1[j]
print(s2)
