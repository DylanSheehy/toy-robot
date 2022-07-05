"""Class for x,y points allowing"""

class Point():

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
    def greater_than(self, point):
        """
        Method to decide if either x and y of a given point are greater than this one
        :param point:
        """
        return self.x >= point.x and self.y >= point.y
    
    def less_than(self, point):
        """
        Method to decide if either x and y of a given point are less than this one
        :param point:
        """
        return self.x <= point.x and self.y <= point.y
        
    def add(self, point):
        """
        Add two points together
        :param point:
        """
        return Point(self.x + point.x, self.y + point.y)

    def __str__(self):
        """
        String representation of Point object
        """
        return "(%s,%s)" % (self.x, self.y)