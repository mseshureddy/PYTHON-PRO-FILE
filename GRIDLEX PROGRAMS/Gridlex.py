

s=input()
l=s.split()
count=[]
print(len(l))
d={}
for i in l:
    if i.lower() not in d:
        d[i.lower()]=1
    else:
        d[i.lower()]+=1
for i in d:
    count.append(d[i])
a=max(count)
for i in d:
    if d[i]==a:
        print(i,d[i])
a1=len(l[0])
for i in range(1,len(l)):
    if a1<len(l[i]):
        a1=len(l[i])
        long=l[i]
print(long)


        
        

    



























    
    
























