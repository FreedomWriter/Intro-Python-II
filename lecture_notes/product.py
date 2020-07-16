class Product:
    def __init__(self, name, description, category, price = 0):
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def __str__(self):
        return f'{self.name} is ${self.price}'