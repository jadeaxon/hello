#!/usr/bin/env python3

# In its simplest form, match the value of an expression against some literal values.
match 3 * 2:
    case 1:
        pass
    case 5:
        pass
    case 6:
        print("matched")

day = 1
name = ""
match day:
    case 0:
        name = "Sunday"
    case 1:
        name = "Monday"
print(name)


# match doesn't have an else clause: it has a case _.
s = "something"
match s:
    case "nothing":
        pass
    case _:
        print("default case")

# You can use | to handle multiple cases with same block.
x = 5
match x:
    case 1 | 2 | 3:
        pass
    case 4 | 5:
        print("matched 4 or 5")

# You can add a bonus condition (guard) to each case statement.
ignore = True
x = 6
match x:
    case 6 if not ignore:
        print("matched 6")
    # NO: case 3 + 2 + 1:
    # Looks like the case value can't be an expression?
    case 6: # Yup, you can use the same value twice.
        print("matched 2nd 6")

# It can do some other convoluted stuff where it does partial
# tuple assignments and object matching.
# Just going to stick with matches to literal values in these examples for now.



