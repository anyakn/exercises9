import math


class Point:
    '''
      class of point on a plane
      '''
    def __init__(self, coordinates=None):
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


class Segment:
    '''
    class of segments
    '''
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def one_intersection(self):
        '''
        function that shows weather the segment has one intersection with coordinate axes or no
        :return: true if yes, false if no
        '''
        if self.point_1.get_x * self.point_2.get_x <= 0 and self.point_1.get_y * self.point_2.get_y <= 0:
            return False
        elif self.point_1.get_x * self.point_2.get_x > 0 and self.point_1.get_y * self.point_2.get_y > 0:
            return False
        return True


class CoordinateSystem:
    '''
    class of coordinate systems
    '''
    def __init__(self):
        self.segments = []

    def add_segment(self, segment):
        '''
        function that adds the segment to coordinate system
        :param segment: segment we want to add
        :return: None
        '''
        self.segments.append(segment)

    def axis_intersection(self):
        '''
        function that shows how many segments have one intersection with coordinate axes
        :return: number of segments
        '''
        k = 0
        for s in self.segments:
            if s.one_intersection is True:
                k += 1
        return k
