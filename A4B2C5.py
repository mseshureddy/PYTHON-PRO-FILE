string='A4B2C5'
s=' '
for var in string:
    if var.isalpha():
        s+=var
        v=var
    else:
        d=int(var)
        s+=chr(ord(v)+d)
        
print(s)
    
