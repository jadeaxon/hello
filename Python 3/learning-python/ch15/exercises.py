#!/usr/bin/env python3

s = 'chapter 15 exercises'
L = [ord(c) for c in s]
print(L)
L = list(map(ord, s))
print(L)

L = []
sum = 0
for c in s:
    code_point = ord(c)
    L.append(code_point)
    sum += code_point
print(L)
print(sum)

m = 1
if m == 1:
    print("January")
elif m == 2:
    print("February")
elif m == 3:
    print("March")
else:
    print("unknown month")

match m:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case _:
        print("unknown month")

months = {
    1: "January",
    2: "February",
    3: "March"
}
print(months[m])


for k in sorted(months.keys()):
    print(k, months[k])


# L = [1, 2, 4, 8, 16, 32, 64]
L = [2 ** x for x in range(7)]
print(L)
L = list(map(lambda x: 2 ** x, range(7)))
print(L)
x = 5
i = 0
while i < len(L):
    if 2 ** x == L[i]:
        print('at index', i)
        break
    i += 1
else:
    print(x, 'not found')

for i, e in enumerate(L):
    if e == 2 ** x:
        print('at index', i)
        break
else:
    print(x, 'not found')

if 2 ** x in L:
    print("found")
else:
    print("not found")




