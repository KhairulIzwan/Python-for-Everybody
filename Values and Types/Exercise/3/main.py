#!/usr/bin/env python3

"""

Assume that we execute the following assignment statements:

width = 17
height = 12.0

For each of the following expressions, write the value of the expression and the type (of the value of the expression).

1. width//2
2. width/2.0
3. height/3
4. 1 + 2 \* 5

"""

#
width = 17
height = 12.0

#
print("width: %.2f" % width)
print("height: %.2f" % height)
print("\n")

#
calc = width // 2
print("width // 2: %.2f" % calc)
print(type(calc))
print("\n")

#
calc = width / 2.0
print("width / 2.0: %.2f" % calc)
print(type(calc))
print("\n")

#
calc = height / 3
print("height / 3: %.2f" % calc)
print(type(calc))
print("\n")

#
calc = 1 + 2 * 5
print("1 + 2 * 5: %.2f" % calc)
print(type(calc))
print("\n")
