#!/usr/bin/env python3

def adder(x, y):
    return x + y

args = [
    (1, 2),
    ("one", "two"),
    (1.1, 2.2),
    ([1], [2])]
]

for (x, y) in args:
    r = adder(x, y)
    print(r)



