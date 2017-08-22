#!/usr/bin/env python3
"""
    test for lesson 1.1
"""

import os
import random

PY3 = "python3 "
WORKSPACE = "/Users/syd/PycharmProjects/python_little_games/"
TEST1_1 = "lesson1_1_jump_ball.py"
CMD = PY3 + WORKSPACE + TEST1_1

PARAM_O = " o="
PARAM_X = " x="
PARAM_Y = " y="


def test(xy_l, xy_r, o_l, o_r):
    """
        use random value to test something
    """
    rand_x = str(random.randint(xy_l, xy_r))
    rand_y = str(random.randint(xy_l, xy_r))
    rand_o = str(random.randint(o_l, o_r))
    test_str = PARAM_O + rand_o + PARAM_X + rand_x + PARAM_Y + rand_y
    print("#" + test_str)
    test_str = CMD + test_str
    os.system(test_str)
    print("#")


def test_params():
    """
        no params
        too many/less params
        invalid/null params
        out-of-range params
    """
    print("#1_1_jump_ball no params")
    os.system(CMD)
    print("#")
    print("#1_1_jump_ball too many params")
    os.system(CMD + " 1 2 3 4 5")
    print("#")
    print("#1_1_jump_ball too less params")
    os.system(CMD + " 1 2 ")
    print("#")
    print("#1_1_jump_ball invalid params")
    os.system(CMD + " 1 2 3")
    print("#")
    print("#1_1_jump_ball null params")
    os.system(CMD + " o= x= y=")
    os.system(CMD + " o=1 x= y=")
    os.system(CMD + " o= x=1 y=")
    os.system(CMD + " o= x= y=1")
    os.system(CMD + " o=1 x=1 y=")
    os.system(CMD + " o=1 x= y=1")
    os.system(CMD + " o= x=1 y=1")
    print("#1_1_jump_ball params out of range")
    for i in range(10):
        test(-50, 150, -5, 10)
    print("#--------------------------------")


def main():
    """
        main function
    """
    print("#********** test begin **********")
    # for i in range(5):
    #     test(1, 99, 1, 1)
    test(5, 10, 4, 4)


if __name__ == "__main__":
    main()
