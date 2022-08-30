import re
def string(n):
    numbers = re.findall('\d+',n)
    numbers=map(int,numbers)
    return max(numbers)

x=string('100jyjg6768gjht45')
print(x)
    
 
