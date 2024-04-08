import math


class Point:
    '''
    class of point on a plane
    '''
    def __init__(self, coordinates=None):
        '''

        :param coordinates: coordinates of a startinf point
        '''
        if coordinates is None:
            coordinates = tuple([0, 0])
        self.coordinates = coordinates

    def get_x(self):
        '''
        function of getting x coordinate
        :return: x coordinate
        '''
        return self.coordinates[0]

    def get_y(self):
        '''
        function of getting y coordinate
        :return: y coordinate
        '''
        return self.coordinates[1]

    def distance(self, other):
        '''
        function that count distance between 2 points
        :param other: coordinates of other point
        :return: distance
        '''
        x1 = self.get_x()
        y1 = self.get_y()
        point_2 = Point(other)
        x2 = point_2.get_x()
        y2 = point_2.get_y()
        distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        return distance

    def sum(self, other):
        '''
        function that sums up x and y coordinates of 2 points
        :param other: coordinates of other point
        :return: sum of the coordinates
        '''
        x1 = self.get_x()
        y1 = self.get_y()
        point_2 = Point(other)
        x2 = point_2.get_x()
        y2 = point_2.get_y()
        x3 = x1 + x2
        y3 = y1 + y2
        return tuple([x3, y3])

    def __str__(self):
        return f'Point ({self.get_x()}, {self.get_y()})'

    def __repr__(self):
        return self.__str__()
