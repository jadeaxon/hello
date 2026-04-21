#!/usr/bin/env python3

"""
https://docs.python.org/3/library/datetime.html
https://docs.python.org/3/library/datetime.html#format-codes
"""

import datetime

t = datetime.datetime.now()
print(t, type(t))

print(t.year)
print(t.month)
print(t.day)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

day = t.strftime('%A')
print(day)
month = t.strftime('%B')
print(month)

ymd = t.strftime('%Y-%m-%d')
print(ymd)

t = datetime.datetime(2025, 12, 25)
print(t)


