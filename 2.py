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

    def __str__(self):
        return f'Засыпающий человек: {self.name}'

    def __repr__(self):
        return self.__str__()


person = NotSleeping('Kate')
print(person.__repr__())
