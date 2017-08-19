#!/usr/bin/env python3
import os

test1_1 = "/Users/syd/PycharmProjects/python_little_games/1_1_jump_ball.py"
print ("********** test begin **********")

print ("1_1_jump_ball no params")
os.system("python3 " + test1_1)

print ("--------------------------------")
print ("1_1_jump_ball too many params")
os.system("python3 " + test1_1 + " 1 2 3 4 5")

o = " o="
x = " x="
y = " y="
print ("--------------------------------")
print ("1_1_jump_ball 1. a hold ball")
