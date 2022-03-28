from python_superclass import Animal

class specimen(Animal):
    def __init__(self, name, category, color):
       self.color = color
       super().__init__(name, category)
	
    def invisible(self):
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
