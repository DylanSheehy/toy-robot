"""Class for toy robot that can moved around a table"""

import logging

class Robot():

    def __init__(self, table, movements):
        self.table = table
        self.movements = movements
        self.orientations = list(movements.keys())
        self.orientation_index = None
        self.position = None

    def report(self):
        """
        Report the robots current location and orientation
        """
        if self.position:
            return "I am currently at %s facing %s" % (self.position, self.get_orientation().upper())
    
    def left(self):
        """
        Move the robot 90 degress left by reducing its index by 1 and if it is now below zero
        wrap it around to the last item a.k.a from north -> west
          0        1       2       3
        north <- east <- south <- west <-
        |                               |
        > ----------------------------- ^
        """
        if self.position:
            self.orientation_index -= 1
            if self.orientation_index < 0:
                self.orientation_index = len(self.orientations) - 1
    
    def right(self):
        """
        Move the robot 90 degress right by increaing its index by 1 and if it is now above the
        length of the orientations array wrap it around to the front item 
        a.k.a from west -> north
            0        1       2       3
        -> north -> east -> south -> west
        |                               |
        ^ ----------------------------- <
        """
        if self.position:
            self.orientation_index += 1
            if self.orientation_index > len(self.orientations) - 1:
                self.orientation_index = 0
    
    def move(self):
        """
        Move robot forward one spot in the given direction it is currently facing
        """
        movement = self.movements.get(self.get_orientation())
        self.place(self.position.add(movement), self.get_orientation())

    def place(self, new_position, new_orientation):
        """
        Place robot at a certian position on the table
        :param newPosition:
        :param newOrientation:
        """
        try:    
            if self.table.on_table(new_position) and self.movements.get(new_orientation):
                self.position = new_position
                self.orientation_index = self.orientations.index(new_orientation)
        except Exception as e:
            logging.error("Error occured when placing robot %s" % (str(e)))
    
    def get_orientation(self):
        """
        Helper method to get english representation of current orientation
        """
        return self.orientations[self.orientation_index]
    

            



