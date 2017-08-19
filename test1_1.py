#!/usr/bin/env python3
import os
import random

PY3 = "python3 "
WORKSPACE = "/Users/syd/PycharmProjects/python_little_games/"
TEST1_1 = "lesson1_1_jump_ball.py"
CMD = PY3 + WORKSPACE + TEST1_1

PARAM_O = " o="
PARAM_X = " x="
PARAM_Y = " y="


def test(xy_l, xy_r, param_o):
    """
        use random value to test something
    """
    rand_x = str(random.randint(xy_l, xy_r))
    rand_y = str(random.randint(xy_l, xy_r))
    test_str = PARAM_O + str(param_o) + PARAM_X + rand_x + PARAM_Y + rand_y
    print("#" + test_str)
    test_str = CMD + test_str
    os.system(test_str)
    print("#")


def main():
    """
        main function
    """
    print("#********** test begin **********")
    print("#1_1_jump_ball no params")
    os.system(CMD)
    print("#")
    print("#--------------------------------")
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
    # TODO
    print("#--------------------------------")
    print("#1_1_jump_ball 1. a hold ball")
    print("#in range test")
    for i in range(5):
        test(1, 99, 1)
    print("#")
    print("#out range test")
    for i in range(10):
        test(-50, 150, 1)


if __name__ == "__main__":
    main()
