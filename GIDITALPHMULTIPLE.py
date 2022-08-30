s='2a3b4c5d'
empt_str=' '
for var in s:
    if var.isdigit():
        valu=var
    else:
        ass=str(var)
        empt_str+=valu*ass
print(empt_str)
        
    
