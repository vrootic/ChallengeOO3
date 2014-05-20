#! /usr/bin/python
# -*-coding: utf-8 -*-

# Please test under python2.7 :)
import sys

data_set_num = raw_input()

def square(x):
    return x * x

def non_negative(x):
    return x > 0

def kernel(b, e):
    n = raw_input()
    print sum(map(square, filter(non_negative, map(int, sys.stdin.readline().split(" "))) ))

reduce(kernel, range(int(data_set_num)+1))

