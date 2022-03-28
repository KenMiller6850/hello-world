class Snake(object):

     def __init__(self, name, length):
       self.name = name
       self.length = length

     def change_name(self, new_name): # note that the first argument is self
         self.name = new_name # access the class attribute with the self keyword

     def displayName(self):
         print(self.name)      




d = Snake('Bob',6)         

print(d.displayName)

