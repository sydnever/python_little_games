#!/usr/bin/env python3
"""
    Lesson 1.1 A jump ball
"""
# import os
import sys

# exit code
EXIT_NUM_ARGVS = 5
EXIT_INVALID_PARAM = 2
EXIT_NO_PARAM = 1
EXIT_SUCCESS_END = 0

# global value
XY_SCOPE = list(range(1, 100))
O_SCOPE = list(range(1, 5))


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


def no1_1(coordinate_x, coordinate_y):
    """
        1.1 a hold ball
    """
    return


def main():
    """
        main function
    """
    # check the number of argvs
    if len(sys.argv) == 1:
        print_help()
        exit(EXIT_NO_PARAM)
    if len(sys.argv) != 4:
        print("Error: invalid number of argvs")
        print_help()
        exit(EXIT_NUM_ARGVS)
    """
        x: coordinate_x
        y: coordinate_y
        o: option_o
    """
    # declaration for x, y, o
    coordinate_x = 0
    coordinate_y = 0
    option_o = 0
    # get params     
    for tmp_argv in sys.argv[1:]:
        if tmp_argv[0:2] == "o=":
            option_o = int(tmp_argv[2:])
        elif tmp_argv[0:2] == "x=":
            coordinate_x = int(tmp_argv[2:])
        elif tmp_argv[0:2] == "y=":
            coordinate_y = int(tmp_argv[2:])
        else:
            print("Error: invalid argvs")
            print_help()
            exit(EXIT_INVALID_PARAM)
    # check params in valid scopes or not
    x_in_range = coordinate_x in XY_SCOPE
    y_in_range = coordinate_y in XY_SCOPE
    o_in_range = option_o in O_SCOPE
    if x_in_range and y_in_range and o_in_range:
        # begin
        if option_o == 1:
            pass
        exit(EXIT_SUCCESS_END)
    else:
        print("Error: please make x and y in a valid range")
        exit(EXIT_INVALID_PARAM)


if __name__ == "__main__":
    main()
