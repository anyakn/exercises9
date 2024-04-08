class StrandsDNA:
    '''
    class of strands of DNA
    '''
    def __init__(self):
        self.all_strands = []

    def add_strands(self, strands):
        '''
        function that adds strands of DNA
        :param strands: strands we want to add
        :return: None
        '''
        new_strands = strands.split()
        self.all_strands.extend(new_strands)
        self.all_strands.sort()

    def get_max_strands(self):
        '''
        function to get strands of maximum length
        :return: string of these strands split by a space
        '''
        max_strands = []
        max_len = len(max(self.all_strands, key=len))
        for strand in self.all_strands:
            if len(strand) == max_len and strand not in max_strands:
                max_strands.append(strand)
        return ' '.join(max_strands)
