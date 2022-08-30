'''
l=[1,2,3,4]
l2=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        t=l[i]+l[j]
        t2=0
        for k in range(len(l)):
            if k!=i and k!=j:
                t2+=l[k]
        nl=[t,t2]
        if nl not in l2: 
            l2.append(nl)
print(l2)#[[3, 7], [4, 6], [5, 5], [6, 4], [7, 3]]
res=l2[0]
mini=l2[0][1]-l2[0][0]
for i in range(1,len(l2)):
    if abs(l2[i][1]-l2[i][0])<mini:
        mini=abs(l2[i][1]-l2[i][0])
        res=l2[i]
print(res)
'''

: l=[[4,-1,2],[3,5,-1],[-1,1,6]]
diag=0
for i in range(len(l)):
    for j in range(len(l[i])):
        if i==j:
            diag+=l[i][j]
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j]==-1 and sum(l[i])!=15:
            l[i][j]=diag-sum(l[i])-1
print(l)






















