class Room():
    def __init__(self, name='', description='', n_to='', s_to='', e_to='', w_to='', items=[]):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items

    # def __str__(self):
    #     output = self.name
    #     i = 1
    #     for item in self.items:
    #         output += f'\n{i}. {item} '
    #         i +=1
    #     return output

class List(Room):
    def __init__(self, items, name):
        super().__init__(items, name)
    # def __str__(self):
    #     output = self.name
    #     i = 0
    #     for item in self.items:
    #         i +=1
    #         return f'\n{i}. {item}'
    #     return output

    def __repr__(self):
        return f'{self.name} has {len(self.items)} items'
        



    