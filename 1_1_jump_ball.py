#!/usr/bin/env python3
import os
import sys


# print len(sys.argv)
# print sys.argv

def print_help():
    print ("1.1 jump_ball by syd")
    print ("usage: 1_1_jump_ball.py o=1 x=5 y=10")
    print ("o: ")
    print ("     1. a hold ball")
    print ("x: the x coordinate (5 default)")
    print ("y: the y coordinate (10 default)")


if len(sys.argv) == 1:
    print_help()
    exit(1)

x = 5
y = 10
o = 1

if len(sys.argv) > 4:
    print ("too many argvs")
    print_help()
    exit(5)
