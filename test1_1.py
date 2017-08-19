#!/usr/bin/env python3
import os
import random


def test(xy_l, xy_r, o_l, o_r):
    RAND_O = str(random.randint(o_l, o_r))
    RAND_X = str(random.randint(xy_l, xy_r))
    RAND_Y = str(random.randint(xy_l, xy_r))
    TEST_STR = CMD + PARAM_O + RAND_O + PARAM_X + RAND_X + PARAM_Y + RAND_Y

    print(PARAM_O + RAND_O + PARAM_X + RAND_X + PARAM_Y + RAND_Y)
    os.system(TEST_STR)
    print("")


PY3 = "python3 "
WORKSPACE = "/Users/syd/PycharmProjects/python_little_games/"
TEST1_1 = "lesson1_1_jump_ball.py"
CMD = PY3 + WORKSPACE + TEST1_1

print("********** test begin **********")

print("1_1_jump_ball no params")
os.system(CMD)

print("--------------------------------")
print("1_1_jump_ball too many params")
os.system(CMD + " 1 2 3 4 5")

PARAM_O = " o="
PARAM_X = " x="
PARAM_Y = " y="
print("--------------------------------")
print("1_1_jump_ball 1. a hold ball")

for i in range(5):
    test(1, 100, 1, 10)

for i in range(10):
    test(-50, 150, -5, 15)
