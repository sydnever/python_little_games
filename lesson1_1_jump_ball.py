#!/usr/bin/env python3
"""
    Lesson 1.1 A jump ball
"""
# import os
import sys


# print len(sys.argv)
# print sys.argv

def print_help():
    """
        help
    """
    print("1.1 jump_ball by syd")
    print("usage: lessson1_1_jump_ball.py o=1 x=5 y=10")
    print("o: ")
    print("     1. a hold ball")
    print("x: the x coordinate (5 default, 0 < x < 100, int)")
    print("y: the y coordinate (10 default, 0 < y < 100, int)")


if len(sys.argv) == 1:
    print_help()
    exit(1)

# exit code
EXIT_TOO_MANY_ARGVS = 5
EXIT_INVALID_PARAM = 2
EXIT_SUCCESS_END = 0

# default value
coordinate_x = 5
coordinate_y = 10
option_o = 1


if len(sys.argv) > 4:
    print("too many argvs")
    print_help()
    exit(EXIT_TOO_MANY_ARGVS)

print(sys.argv)
for tmp_argv in sys.argv[1:]:
    print(tmp_argv[0:2])
    if tmp_argv[0:2] == "o=":
        option_o = tmp_argv[2:]
    elif tmp_argv[0:2] == "x=":
        coordinate_x = tmp_argv[2:]
    elif tmp_argv[0:2] == "y=":
        coordinate_y = tmp_argv[2:]
    else:
        print("invalid param: " + tmp_argv)
        exit(EXIT_INVALID_PARAM)


if coordinate_x not in range(1, 100) or coordinate_y not in range(1, 100):
    print("___________________________________________")
    print("Error: please make x and y in a valid range")
    print("*******************************************")    
    print("test: o=" + option_o + " x=" + coordinate_x + " y=" + coordinate_x)    
    exit(EXIT_INVALID_PARAM)
else:
    print("test: o=" + option_o + " x=" + coordinate_x + " y=" + coordinate_x)
    


exit(EXIT_SUCCESS_END)
