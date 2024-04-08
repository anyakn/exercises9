class NotSleeping:
    '''
    class of a person, who is trying to sleep
    '''
    def __init__(self, name):
        self.name = name
        self.sheep = 0

    def add_sheep(self):
        '''
        function that add 1 sheep to the count
        :return: number of sheeps counted
        '''
        self.sheep += 1
        return self.sheep

    def lost(self):
        '''
        function that makes person count sheeps from the beginning
        :return:None
        '''
        self.sheep = 0

    def get_count_sheeps(self):
        '''
        function that shows number of counted sheeps
        :return: how many sheeps are counted
        '''
        return self.sheep

    def __str__(self):
        return f'Засыпающий человек: {self.name}'

    def __repr__(self):
        return self.__str__()


person = NotSleeping('Kate')
print(person.__repr__())

for i in range(15):
    person.add_sheep()
person.lost()
for i in range(6):
    person.add_sheep()
print(person.get_count_sheeps())
