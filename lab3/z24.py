# Napisz klasę Rectangle, która ma atrybuty width i height oraz metodę area(), zwracającą 
# pole prostokąta

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
print(Rectangle(10,20).area())