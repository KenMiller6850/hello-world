from python_superclass import Animal

class specimen(Animal):
    def __init__(self, name, category, color): #instantiates the specimen class - with the "color" attribute
       self.color = color
       super().__init__(name, category) #calls the constructor for the parent class so we can access those methods
	
    def invisible(self): #This method exists only in the child subclass
       if self.color == 'green':
         return 'True'
       elif self.category != 'green':
         return "False"
       else:
         return "Unknown"


d = specimen('Bill','reptile','purple')


print(d.name)
print(d.category)
print(d.coldblooded())
print(d.invisible())
