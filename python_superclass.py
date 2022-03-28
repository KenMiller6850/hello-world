class Animal:
     def __init__(self, name,category):
        self.name = name
        self.category = category

     def coldblooded(self):
       if self.category == 'reptile':
         return 'True'
       elif self.category != 'reptile':
         return "False"
       else:
         return "Unknown"

















