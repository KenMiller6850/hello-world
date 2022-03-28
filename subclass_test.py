from snakeClass import Snake


class Rattlesnake(Snake):
    def __init__(self,name,venomous):
        self.venomous = venomous
        super().__init__(name)
     # Call the parent's query method and add new behavior
    def displayname(self): 
        return super().displayname() + (' my name is: ' + self.name)  



snake2 = Rattlesnake('Bob',True)     
print(snake2.name)   
print(snake2.length)
print(snake2.venomous)

