# define and import functions
import math


def sign(n):  # returns 1 if the number is positive, and -1 if the number is negative
    if abs(n) == n:
        return 1
    else:
        return -1


# open the file
file = open("day-3\input.txt", "r")  # open the file
bit_amounts = []  # the amount of each place throughout the input
for i in range(0, len(file[0]) - 1):  # fill the bit_amounts array with 0's
    bit_amounts[i] = 0

# parse the input
for line in file:  # for each line in the input file
    for i in range(0, len(line) - 1):  # for each character in the current line
        # get n
        if line[i] == "0":
            n = -1
        else:
            n = 1

        # add n to the bit amounts array
        bit_amounts[i] += n

# get the gamma and epsilon rate
bin_gamma_rate = ""
bin_epsilon_rate = ""


# convert the binary numbers into decimal

# print the output
