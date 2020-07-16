from product import Product

class Crate(Product):
    def __init__(self, name, description, price, size, material):
        super().__init__(name,description, price )
        self.size = size
        self.material = material

    def __str__(self):
        #return f'{self.name} is ${self.price} and is made of {self.material}'
        return super().__str__() + f' and is made of {self.material}'

c = Crate('crate', 'not gonna last', 99, 'too small', 'plastic')

# # overide the string method assigned to the child class to default to parent string method
# print(super(Crate, c).__str__())

print(c)