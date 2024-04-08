class User:
    '''
    clas of users
    '''
    def __init__(self, idd, nickname, first_name, last_name=None, middle_name=None, gender=None):
        self.idd = idd
        self.nickname = nickname
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(self, name_atr, new):
        '''
        function that changes an attribute
        :param name_atr: name of the attribute we want to change
        :param new: new value of the attribute
        :return: None
        '''
        if hasattr(self, name_atr):
            setattr(self, name_atr, new)

    def __str__(self):
        info = f'Пользователь: {self.idd} \nПсевдоним: {self.nickname} \nИмя: {self.first_name}'
        if self.last_name is not None:
            info += f'\nФамилия: {self.last_name}'
        if self.middle_name:
            info += f'\nОтчество: {self.middle_name}'
        if self.gender:
            info += f'\nПол: {self.gender}'
        return info


user = User(12, 'lilyblack', 'Lily', 'Black', 'Ana', 'female')
print(user.__str__())
user.update('nickname', 'lilyablack')
print(user.__str__())
