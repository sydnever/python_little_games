#!/usr/bin/env python3
"""
    Lesson 1.1 A jump ball
"""
import os
import sys


# print len(sys.argv)
# print sys.argv

def print_help():
    """
        help
    """
    print("1.1 jump_ball by syd")
    print("usage: 1_1_jump_ball.py o=1 x=5 y=10")
    print("o: ")
    print("     1. a hold ball")
    print("x: the x coordinate (5 default)")
    print("y: the y coordinate (10 default)")


if len(sys.argv) == 1:
    print_help()
    exit(1)

coordinate_x = 5
coordinate_y = 10
option_o = 1

if len(sys.argv) > 4:
    print("too many argvs")
    print_help()
    exit(5)

for tmp_argv in sys.argv:
    if tmp_argv[0:1] == "o=":
        option_o = tmp_argv[2:]
    elif tmp_argv[0:1] == "x=":
        coordinate_x = tmp_argv[2:]
    elif tmp_argv[0:1] == "y=":
        coordinate_y = tmp_argv[2:]
    else:
        print("invalid param: " + tmp_argv)
        exit(2)

print("test: o=" + option_o + " x=" + coordinate_x + " y=" + coordinate_x)
