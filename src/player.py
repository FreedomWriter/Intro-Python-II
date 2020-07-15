# Write a class to hold player information, e.g. 
    # name
    # current_room

# 



class Player():
    def __init__(self, name="", current_room="", items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def get_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)
    # def __str__(self):
    #     return '{self.name} is currently in {self.current_room}'.format(self=self)
