class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        self.price -= self.price * (percent / 100)

# Test
p = Product("Laptop", 2000)
p.apply_discount(10)
print(p.name)
print(p.price)
