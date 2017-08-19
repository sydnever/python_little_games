#!/usr/bin/env python3
"""
    Lesson 1.1 A jump ball
"""
# import os
import sys

# exit code
EXIT_TOO_MANY_ARGVS = 5
EXIT_INVALID_PARAM = 2
EXIT_NO_PARAM = 1
EXIT_SUCCESS_END = 0


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


def main():
    """
        main fuction
    """
    if len(sys.argv) == 1:
        print_help()
        exit(EXIT_NO_PARAM)
    # default value
    coordinate_x = 5
    coordinate_y = 10
    option_o = 1
    if len(sys.argv) > 4:
        print("too many argvs")
        print_help()
        exit(EXIT_TOO_MANY_ARGVS)
    # print(sys.argv[1:])
    for tmp_argv in sys.argv[1:]:
        # print(tmp_argv[0:2])
        if tmp_argv[0:2] == "o=":
            option_o = tmp_argv[2:]
            # print("get o: " + option_o)
        elif tmp_argv[0:2] == "x=":
            coordinate_x = tmp_argv[2:]
            # print("get x: " + coordinate_x)
        elif tmp_argv[0:2] == "y=":
            coordinate_y = tmp_argv[2:]
            # print("get y: " + coordinate_y)
        else:
            # print("invalid param: " + tmp_argv)
            exit(EXIT_INVALID_PARAM)
    print("test: o=" + str(option_o) + \
            " x=" + str(coordinate_x) + \
            " y=" + str(coordinate_y))
    x_in_range = coordinate_x in list(range(1, 100))
    y_in_range = coordinate_y in list(range(1, 100))
    print(x_in_range)
    print(y_in_range)
    if x_in_range and y_in_range:
        exit(EXIT_SUCCESS_END)
    else:
        print("Error: please make x and y in a valid range")
        exit(EXIT_INVALID_PARAM)


if __name__ == "__main__":
    main()
