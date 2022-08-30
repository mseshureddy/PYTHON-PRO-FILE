# upper
'''
def Upper(string):
    temp=' '
    for var in string:

        if var>='a' and var<='z':
            temp+=chr(ord(var)-32)
        else:
            temp+=var
    return temp
string01=Upper("python98$%is GOOdprimminGG LangguaGE7()^")
print(string01)

'''
#lower
'''

def Lower(string):
    tmp=' '
    for variable in string:
        if variable>='A' and variable<='L':
            tmp+=chr(ord(variable)+32)
        else:
            tmp+=variable
    return tmp
Assing=Lower("DSESHU ID #$HNFJ798hnjukjdjhjh999@#$")
print(Assing)
'''
'''
#swapcase
def Swpcase(s):
    temp=' '
    for i in s:
        if i>='a' and i<='z':
            temp+=chr(ord(i)-32)

        elif i>='A' and i<='Z':
            temp+=chr(ord(i)+32)
        else:
            temp+=i
    return temp
x=Swpcase("SESHUreddy5$%^&MualaNI")
print(x)
'''


'''
def Remove(string01,string02):
    temp=' '
    for var_01 in string01:
        if var_01!=string02:
            temp+=var_01
    return temp
call_function=Remove("we are python developers",'e')
print(call_function)
'''

def Remove(str1,str2):
    temp_var=' '
    for var_01 in str1:
        if var_01 not in str2:
            temp_var+=var_01
    return temp_var
        
call_function=Remove("we are python developers",'e')
print(call_function)




















