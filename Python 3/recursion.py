#!/usr/bin/env python3

# You can have a function call itself. This is recursion.
def factorial(n):
    # Base case.
    if n == 0: return 1
    if n == 1: return 1
    # Recursive case.
    return n * factorial(n - 1)

r = factorial(5) # 5 * 4 * 3 * 2 * 1
print(r)

# Find the nth Fibonacci number.
def fibonacci(n):
    if n == 1: return 0
    if n == 2: return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
for i in range(1, 10):
    r = fibonacci(i)
    print(r)

# Python limits how deep a recursion can go to protect against infinite recursion.
import sys
print(sys.getrecursionlimit())

def infinite():
    return 1 + infinite()

try:
    r = infinite()
    print(r)
except RecursionError as e:
    print(e)



