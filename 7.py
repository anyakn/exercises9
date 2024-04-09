class TrafficLight:
    '''
    class of traffic light
    '''
    def __init__(self):
        self.current_signal = 'зеленый'
        self.permissible_values = ['зеленый', 'желтый', 'красный']
        self.chain = ['зеленый']

    def next_signal(self):
        '''
        function that changes the color of traffic light to the next one
        :return: None
        '''
        index_current = self.permissible_values.index(self.current_signal)
        if index_current == 0 or index_current == 2:
            index_next = 1
            self.chain.append(self.permissible_values[index_next])
        else:
            if self.chain[-2] == self.permissible_values[0]:
                index_next = 2
                self.chain.append(self.permissible_values[index_next])
            else:
                index_next = 0
                self.chain.append(self.permissible_values[index_next])
        if len(self.chain) > 2:
            self.chain = self.chain[-2:]
        self.current_signal = self.permissible_values[index_next]


traffic = TrafficLight()
traffic.next_signal()
print(traffic.current_signal)

traffic.next_signal()
print(traffic.current_signal)

traffic.next_signal()
print(traffic.current_signal)

traffic.next_signal()
print(traffic.current_signal)

traffic.next_signal()
print(traffic.current_signal)

traffic.next_signal()
print(traffic.current_signal)
