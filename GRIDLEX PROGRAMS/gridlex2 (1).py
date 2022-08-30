l=[[2,-1,-1],[9,5,-1],[-1,3,8]]
l1=l[0]
l2=l[1]
l3=l[2]
if -1 not in l1:
    a=sum(l1)
elif -1 not in l2:
    a=sum(l2)
elif -1 not in l3:
    a=sum(l3)
elif -1 not in [l1[0],l2[1],l3[2]]:
    a=l1[0]+l2[1]+l3[2]
elif -1 not in [l1[2],l2[1],l3[0]]:
    a=l1[2]+l2[1]+l3[0]
count=0
for i in l:
    for j in i:
        if j==-1:
            count+=1
i=1
while i<=count:
    if l1.count(-1)==1:
        b=l1.index(-1)
        l1[b]=a-sum(l1)-1
    elif l2.count(-1)==1:
        b=l2.index(-1)
        l2[b]=a-sum(l2)-1
    elif l3.count(-1)==1:
        b=l3.index(-1)
        l3[b]=a-sum(l3)-1
    elif l1[0]==-1 and l2[0]!=-1 and l3[0]!=-1:
        l1[0]=a-l2[0]-l3[0]
    elif l1[0]!=-1 and l2[0]==-1 and l3[0]!=-1:
        l2[0]=a-l1[0]-l3[0]
    elif l1[0]!=-1 and l2[0]!=-1 and l3[0]==-1:
        l3[0]=a-l2[0]-l1[0]

        
    elif l1[1]==-1 and l2[1]!=-1 and l3[1]!=-1:
        l1[1]=a-l2[1]-l3[1]
    elif l1[1]!=-1 and l2[1]==-1 and l3[1]!=-1:
        l2[1]=a-l1[1]-l3[1]
    elif l1[1]!=-1 and l2[1]!=-1 and l3[1]==-1:
        l3[1]=a-l2[1]-l1[1]

    elif l1[2]==-1 and l2[2]!=-1 and l3[2]!=-1:
        l1[2]=a-l2[2]-l3[2]
    elif l1[2]!=-1 and l2[2]==-1 and l3[2]!=-1:
        l2[2]=a-l1[2]-l3[2]
    elif l1[2]!=-1 and l2[2]!=-1 and l3[2]==-1:
        l3[2]=a-l2[2]-l1[2]


    elif l1[0]==-1 and l2[1]!=-1 and l3[2]!=-1:
        l1[0]=a-l2[1]-l3[2]
    elif l1[0]!=-1 and l2[1]==-1 and l3[2]!=-1:
        l2[1]=a-l1[0]-l3[2]
    elif l1[0]==-1 and l2[1]==-1 and l3[2]==-1:
        l3[2]=a-l2[1]-l1[0]


    elif l1[2]==-1 and l2[1]!=-1 and l3[0]!=-1:
        l1[2]=a-l2[1]-l3[0]
    elif l1[2]!=-1 and l2[1]==-1 and l3[0]!=-1:
        l2[1]=a-l1[2]-l3[0]
    elif l1[2]==-1 and l2[1]==-1 and l3[0]==-1:
        l3[0]=a-l2[1]-l1[2]
    i+=1


print(l1,l2,l3)
    
