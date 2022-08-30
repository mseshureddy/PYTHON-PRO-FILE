#s1='abcdefg'
#s2='xyz'
#s3='12345'

#output: ax1,by2,cz3,d4,e5,f,g

s1='seshureddy'
s2='12345679'
s3='*&^%@#$'
i=j=k=0
while i<len(s1) or j<len(s2) or k<len(s3):
    u=' '
    if i<len(s1):
        u+=s1[i]
        i+=1
    if j<len(s2):
        u+=s2[j]
        j+=1
    if k<len(s3):
        u+=s3[k]
        k+=1
    print(u,end=' ')



def Req(s1,s2,s3):
    i=j=k=0
    while i<len(s1) or j<len(s2) or k<len(s3):
        u=' '
        if i<len(s1):
            u+=s1[i]
            i+=1
        if j<len(s2):
            u+=s2[j]
            j+=1
        if k<len(s3):
            u+=s3[k]
            k+=1
        return u
c=Req('seshureddy','12345679','*&^%@#$')
print(c)


