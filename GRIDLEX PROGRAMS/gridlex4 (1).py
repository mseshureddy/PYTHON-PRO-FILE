a=[10,20,30]#mean
avg=sum(a)/len(a)
l=[]
sub=[]
d1={}
for i in a:
    d1[i]=abs(i-avg)
    l.append(abs(i-avg))
l=sorted(l)

sec=l[1]
for i in d1:
    if d1[i]==sec:
        sub.append(int(i))
print(min(sub))
    
    
    
    
    
