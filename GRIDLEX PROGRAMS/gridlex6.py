

def calculations(func):
    def inner(*args):
        sub=args
        for i in sub:
            if i<0:
                return None
        return func(*args)
    return inner
            
       
@calculations
def operations(num1,num2):
    print(num1+num2)
    print(num1-num2)
    print(num1*num2)
operations(10,20)
@calculations
def division(n1,n2,n3):
    print(n1,n2,n3)
division(-10,20,30)


    
