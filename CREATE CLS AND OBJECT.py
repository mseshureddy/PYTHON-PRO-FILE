class Dog:
    
    #class attribute
    attribute="mammal"
    
    #instance atrribute
    def __init__(self,name):
        self.name=name

    def speak(self):
        print(self.name)

#Driver code
#Object instantition
Rorder=Dog("Rorder")
Tommy=Dog("Tommy")

Rorder.speak()
Tommy.speak()
        
