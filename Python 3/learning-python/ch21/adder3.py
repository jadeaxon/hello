#!/usr/bin/env python3

def adder(*args):
    r = args[0]
    for arg in args[1:]:
        r += arg
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

for args in args_list:
    try:
        r = adder(*args)
        print(r)
    except Exception as e:
        print(f"Error adding {args}: {e}")


