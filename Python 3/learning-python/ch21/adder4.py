#!/usr/bin/env python3

def adder(**kwargs):
    item = kwargs.popitem()
    r = item[1]
    for (k, v) in kwargs.items():
        r += v
    return r

args_list = [
    {'a': 1, 'b': 2, 'c': 3, 'd': 4},
    {'a': "one", 'b': "two", 'c': "three"},
    {'x': 1.1, 'y': 2.2},
    {'L1': [1], 'L2': [2]},
    {'d1': {"k1": "v"}, 'd2': {"k2": "v"}}
]

for args in args_list:
    try:
        r = adder(**args)
        print(r)
    except Exception as e:
        print(f"Error adding {args}: {e}")



