# https://adventofcode.com/2021/day/1

# import
file = open("day-1\input", "r")

# convert the data list
data_list = []
for line in file:
    data_list.append(int(line))

# get length
length = len(data_list)


def part_one():
    # count the number of increases
    increased = 0
    for i in range(0, length - 1):
        if i + 1 < length:
            if data_list[i] < data_list[i + 1]:
                increased += 1

    # print the outputs
    print(f"For part one, the data increases {increased} times.")


def part_two():
    # define sums list
    sums = []

    # create a list containing every window
    for i in range(0, length - 1):
        # add the sum of data_list[i - (i + 2)] to the sums list
        sum = 0
        for j in range(i, i + 3):
            if j < length:
                sum += data_list[j]
        sums.append(sum)

    # count increases
    increased = 0
    for i in range(1, len(sums) - 1):
        if sums[i] < sums[i + 1]:
            increased += 1

    # print the outputs
    print(f"For part two, the data increases {increased} times.")


part_one()
part_two()
