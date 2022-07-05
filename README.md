# Toy Robot

A python program that simulates a toy robot moving on a square tabletop, of dimensions 5 units x 5 units
# Usage

* Requires python 3.6+ and pipenv

### Installation
```sh
$ cd toy-robot
$ pipenv install 
```

### Running robot
```sh
$ cd toy-robot
$ pipenv shell
$ python src/main.py
$ PLACE 1,2,North
$ MOVE
$ LEFT
$ MOVE
$ REPORT
> I am currently at (0,3) facing WEST
```

* --file allows you to pass the input data in using a text file

#### 
```sh
$ cd toy-robot
$ pipenv shell
$ python src/main.py --file "<path_to_file>"
> I am currently at (3,3) facing NORTH
```
sample_file.txt
```plain
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
```

### Running tests
```sh
$ cd toy-robot/src
$ pipenv shell
$ python -m pytest ../test/ -vv
```