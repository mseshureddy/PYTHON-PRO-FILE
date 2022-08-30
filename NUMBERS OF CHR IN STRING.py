s='ABBACBAABCDEDEFGFGFGA'
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
m=max(d.items())
for k,v in d.items():
    if v==m:
        v=m
print(v)
