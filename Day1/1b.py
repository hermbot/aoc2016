'''--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting
Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location
you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
'''

f = open('input1.txt', 'r')
lines = f.read().split(',')


def get_number(direction):
    a = direction.replace(" ", "")
    a = a[1:]
    return int(a)


def change_direction(current_dir, new_dir):
    if current_dir == "north":
        if "R" in new_dir:
            return "east"
        else:
            return "west"
    elif current_dir == "east":
        if "R" in new_dir:
            return "south"
        else:
            return "north"
    elif current_dir == "south":
        if "R" in new_dir:
            return "west"
        else:
            return "east"
    elif current_dir == "west":
        if "R" in new_dir:
            return "north"
        else:
            return "south"


x_pos = 0
y_pos = 0
direction = "north"
distance_list = []

for i in lines:
    new_direction = change_direction(direction, i)
    if new_direction == "north":
        y_pos += get_number(i)
    elif new_direction == "east":
        x_pos += get_number(i)
    elif new_direction == "south":
        y_pos -= get_number(i)
    elif new_direction == "west":
        x_pos -= get_number(i)
    direction = new_direction
    dist_from_origin = abs(x_pos) + abs(y_pos)
    if dist_from_origin in distance_list:
        print("First spot visited twice: " + str(dist_from_origin))
        break
    else:
        distance_list.append(dist_from_origin)

#print(abs(x_pos) + abs(y_pos))
