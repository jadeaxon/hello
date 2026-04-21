#!/usr/bin/env python3

# lambda <args>: <expression>
# returns a function that returns <expression>
f = lambda: 1
r = f()
print(r) # 1

f = lambda x: x + 1
r = f(2)
print(r) # 3

f = lambda x, y: x + y
r = f(2, 3)
print(r) # 5

# Sort some strings by their 2nd character.
L = ["foo", "bar", "biz"]
L.sort(key=lambda s: s[1])
print(L)

L = list(map(lambda s: s + "y", L))
print(L)

L = ["foo", "fe", "bar", "be", "zap", "ze"]
L = list(filter(lambda s: len(s) == 3, L))
print(L)

D = {
    "add": lambda x, y: x + y,
    "sub": lambda x, y: x - y,
    "mul": lambda x, y: x * y,
    "pow": lambda x, y: x ** y,
    "div": lambda x, y: x / y
}
r = D["pow"](2, 3)
print(r) # 8


