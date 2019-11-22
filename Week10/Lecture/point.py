from math import sqrt


class Point(object):
    def __init__(self, x_param = 0.0, y_param = 0.0):
        self.x = x_param
        self.y = y_param

    def distance(self, point):
        x_diff = self.x - point.x
        y_diff = self.y - point.y
        return sqrt(x_diff**2 + y_diff**2)

    def sum(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __str__(self):
        print('Called the str method')
        return "({0.2f},{0.2f})".format(self.x, self.y)
)