#!/usr/bin/env python3

def adder(*args):
    r = args[0]
    for arg in args[1:]:
        r += arg
    return r

def adder3(x=1, y=2, z=3):
    r = x + y + z
    return r

args_list = [
    (1, 2, 3, 4),
    ("one", "two", "three"),
    (1.1, 2.2),
    ([1], [2]),
    (1, 2.3, "three"),
    ([1], 2),
    ((7, 8), (9, 10)),
    ({"a", "b"}, {"c", "d"}),
    ({"k1": "v"}, {"k2": "v"})
]

args3_list = [
    (1, 2, 3),
    (1.1, 2.2, 3.3),
    ("one", "two", "three"),
]

for args in args3_list:
    try:
        r = adder3(*args)
        print(r)
    except Exception as e:
        print(f"Error adding {args}: {e}")

adder3()
adder3(-1, -2)
adder3(-1, -2, -3)
adder3(1, 2, 3, 4)


