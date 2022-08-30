number=[4,2,1,9,5,3,7,1,0,45,30]
if number[0]>number[1]:
    m1=number[0]
    m2=number[1]
else:
    m1=number[1]
    m2=number[0]

for x in number[2:]:
    if x>m2:
        if x>m1:
            m2,m1=m1,x
            
        else:
            m2=x
print(m2)
