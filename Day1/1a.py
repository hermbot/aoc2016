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

print(x_pos)
print(y_pos)
