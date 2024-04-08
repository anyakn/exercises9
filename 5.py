class Game:
    '''
    class of basketball
    '''
    def __init__(self, dict_command):
        self.dict_command = dict_command

    def ball_thrown(self, command, points):
        '''
        function that adds score to a team
        :param command: number of team
        :param points: number of pointes received
        :return: None
        '''
        if 'command' + str(command) in self.dict_command.keys():
            self.dict_command['command' + str(command)] += points

    def get_score(self):
        '''
        function that returns current game score
        :return: current game score
        '''
        return tuple(self.dict_command.values())

    def get_winner(self):
        '''
        function that shows the winner
        :return: name of a winning team
        '''
        max_point = max(self.dict_command.values())
        k = 0
        winner = ''
        for key, value in self.dict_command.items():
            if value == max_point:
                k += 1
                winner = key
        if k == 1:
            return winner
        return 'Ничья'


game = Game({'command1': 0, 'command2': 0})
game.ball_thrown(1, 9)
game.ball_thrown(2, 9)
print(game.get_score())
print(game.get_winner())
