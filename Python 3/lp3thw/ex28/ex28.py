#!/usr/bin/env python3

r = True and True 
e = True
print(r == e)
r = False and True 
e = False
print(r == e)
r = 1 == 1 and 2 == 1 
e = False
print(r == e)
r = "test" == "test" 
e = True
print(r == e)
r = 1 == 1 or 2 != 1 
e = True
print(r == e)
r = True and 1 == 1 
e = True
print(r == e)
r = False and 0 != 0 
e = False
print(r == e)
r = True or 1 == 1 
e = True
print(r == e)
r = "test" == "testing" 
e = False
print(r == e)
r = 1 != 0 and 2 == 1 
e = False
print(r == e)
r = "test" != "testing" 
e = True
print(r == e)
r = "test" == 1 
e = False
print(r == e)
r = not (True and False) 
e = True
print(r == e)
r = not (1 == 1 and 0 != 1) 
e = False
print(r == e)
r = not (10 == 1 or 1000 == 1000) 
e = False
print(r == e)
r = not (1 != 10 or 3 == 4) 
e = False
print(r == e)
r = not ("testing" == "testing" and "Zed" == "Cool Guy")
e = True
print(r == e)
r = 1 == 1 and (not ("testing" == 1 or 1 == 0)) 
e = True
print(r == e)
r = "chunky" == "bacon" and (not 3 == 4 or 3 == 3) 
e = False
print(r == e)
r = 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")) 
e = False
print(r == e)


