from product import Product
class Store:
  def __init__(self, name, categories, employees):
    self.name= name
    self.categories = categories
    self.products = products

  def __str__(self):
    output = self.name
    i = 1
    for cat in self.categories:
      output += f'\n{i}. {cat} '
      i +=1
    return output

  def __repr__(self):
    return f'{self.name} has {len(self.categories)} categories'

from category import Category
cats =  [Category('food'), Category('costumes'), Category('toys')]
my_store = Store("petapalooza",  [Product('toy', 'squeak squirrel'), Product('something', 'some other description'), Product('another', 'another description')]cats, 10)
print(my_store)
selection = int(input('Please select a category number '))-1
while (selection != len(my_store.categories)):
  print(f"You selected {my_store.categories[selection]}")
  selection = int(input('Please select a category number '))-1

