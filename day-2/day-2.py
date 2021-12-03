depth = 0  # depth
position = 0  # horizontal position
aim = 0  # aim variable

# import and parse the inputs
file = open("day-2\input.txt", "r")
for line in file:
    length = len(line)
    amount = int(line[length - 2])  # get the last character excluding \n

    if line[0] == "f":  # if it's a move forward command
        position += amount
        depth += aim * amount
    elif line[0] == "u":  # if it's a move up command
        aim -= amount
    elif line[0] == "d":  # if it's a move down command
        aim += amount

# print x and y
print(f"the horizontal position is: {position}")
print(f"the depth is: {depth}")
print(f"depth * position is: {depth * position}")
