s='B4A1D3'
alphabat_latters=[]
digits=[]
for ch in s:
    if ch.isalpha():
        alphabat_latters.append(ch)
    else:
        digits.append(ch)
#print(''.join(sorted(alphabat_latters)+sorted(digits)))
print(''.join(sorted(digits)+sorted(alphabat_latters)))
