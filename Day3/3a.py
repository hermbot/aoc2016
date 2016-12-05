'''--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth
of hallways and office furniture that makes up this part of Easter
Bunny HQ. This must be a graphic design department; the walls are
covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it
describes, but... 5 10 25? Some of these aren't triangles. You
can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than
the remaining side. For example, the "triangle" given above is
impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?'''

import numpy as np

data = np.loadtxt("input3.txt")

def is_triangle(sides):
    triangle = True
    if sides[0] + sides[1] <= sides[2]:
        triangle = False
        return
    elif sides[1] + sides[2] <= sides[0]:
        triangle = False
        return
    elif sides[0] + sides[2] <= sides[1]:
        triangle = False
        return

    return triangle

possible_triangles = 0
for row in data:
    if is_triangle(row):
        possible_triangles += 1

print(possible_triangles)
