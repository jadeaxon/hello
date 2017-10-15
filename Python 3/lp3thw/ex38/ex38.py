#!/usr/bin/env python3

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait, there are not 10 things in that list.  Let's fix that.")

# Turn a string into a list with split().
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # Last
print(stuff.pop())
# Use join() to turn a list into a single string.
print(' '.join(stuff)) # What?  Cool!
# Uses list slices.  We have not seen them yet.
# The 2nd index is not inclusive.
print('#'.join(stuff[3:5])) # Super stellar!

