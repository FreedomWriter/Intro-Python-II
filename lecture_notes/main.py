
class Store:
  def __init__(self, name, categories):
    self.name= name
    self.categories = categories

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

my_store = Store("petapalooza", [Category('food'), Category('costumes'), Category('toys')])
print(my_store)
selection = int(input('Please select a category number '))-1
while (selection != len(my_store.categories)):
  print(f"You selected {my_store.categories[selection]}")
  selection = int(input('Please select a category number '))-1

