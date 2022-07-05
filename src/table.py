"""Table class for robot to move across"""

class Table():

    # Treating table like a grid drawn between two points blc (x, y) trc (x, y)
    def __init__(self, bottom_left_corner, top_right_corner):
        self.bottom_left_corner = bottom_left_corner
        self.top_right_corner = top_right_corner
    
    def on_table(self, position):
        """ 
        Check if point(position) provided would place robot on table
        :param position:
        """
        return self.top_right_corner.greater_than(position) and self.bottom_left_corner.less_than(position)