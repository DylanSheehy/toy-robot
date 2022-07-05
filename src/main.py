"""Main simulation file and the entry point for the simulation itself for the user"""

import logging
import argparse
import sys

from table import Table
from robot import Robot
from point import Point
from pathlib import Path

def run(args):
    """
    Entry point for simulation
    """
    # Setup logging
    logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')
    logging.propagate = True

    # Create point movement values to match point to a move based on the orientation i.e north would be adding one to y axis so point(0,1)
    # Dicitonaries are ordered in python 3.6 allowing for orientation tracking to be done using the index of each item in movements.keys()
    movements = {
        "north": Point(0,1),
        "east": Point(1,0),
        "south": Point(0,-1),
        "west": Point(-1,0),
    }
    
    # Creating 5,5 table
    table = Table(Point(0,0), Point(4,4))
    robot = Robot(table, movements)

    # If no input file is passed run against user command prompt input
    while not args.file:
            userInput = input()
            __run_input_data(userInput, robot)
    
    # Run against file
    if args.file:
        path = Path(args.file)
        with open(path, "r") as dataFile:
            for line in dataFile.readlines():
                __run_input_data(line.strip("\n"), robot)

def __run_input_data(data, robot):
    """
    Helper method to decide what commands to issue to the robot if any
    :param data:
    :para robot:
    """
    commandData = [x.lower() for x in data.split(" ")]
    match commandData[0]:
        case "place":
            #Ensure inconsistent spacing in input is handled
            placementData = ''.join(commandData[1:]).split(",")
            point = Point(placementData[0], placementData[1])
            robot.place(point, placementData[2])
        case "left":
            robot.left()
        case "right":
            robot.right()
        case "move":
            robot.move()
        case "report":
            print(robot.report())
        case "exit":
            sys.exit()
        case _:
            return
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Simulation of a toy robot moving on a square tabletop, of dimensions 5 units x 5 units'
    )
    parser.add_argument(
        '--file', dest='file', action='store',
        help='Run with input file',
    )
    args = parser.parse_args()
    run(args)