'''--- Part Two ---

Now that you've helpfully marked up their design documents,
it occurs to you that triangles are specified in groups of
three vertically. Each set of three numbers in a column
specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with
the same hundreds digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
In your puzzle input, and instead reading by columns, how many
of the listed triangles are possible?'''

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
stride = 3


print(possible_triangles)